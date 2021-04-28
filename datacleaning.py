import sklearn.neighbors._base
import sys
sys.modules['sklearn.neighbors.base'] = sklearn.neighbors._base
import pandas as pd
from sklearn.base import TransformerMixin
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer
from missingpy import MissForest

class prepross(TransformerMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def fit(self, X, y=None):
        self.fill = pd.Series([X[c].value_counts().index[0]
                               if X[c].dtype == np.dtype('O') else X[c].mean() for c in X], index=X.columns)
        return self

    def transform(self, X, y=None):
        return X.fillna(self.fill)


def rm_rows_cols(df, row_thresh=0.8, col_thresh=0.8):
    if "Index" in df.columns:
      df.drop("Index", axis=1, inplace=True)
    df.columns = [col.strip() for col in df.columns]
    df = df.drop_duplicates()
    df = df.dropna(axis=0,how='all').dropna(axis=1,how='all').dropna(axis=1,how='all').dropna(axis=0,thresh= int(len(df.columns)*0.8)).dropna(axis=1,thresh=int(len(df)*0.8))
    df = df.infer_objects()
    return df


def replace_special_character(df,usr_char=None,do=None, ignore_col=None):
    spec_chars = ["!", '"', "#", "%", "&", "'", "(", ")",
                  "*", "+", ",", "-", ".", "/", ":", ";", "<",
                  "=", ">", "?", "@", "[", "\\", "]", "^", "_",
                  "`", "{", "|", "}", "~", "–", "//", "%*", ":/", ".;", "Ø", "§",'$',"£"]
    if do== 'remove':
      for chactr in usr_char:
        spec_chars.remove(chactr)
    elif do=='add':
      for chactr in usr_char:
        spec_chars.append(chactr)
    if len(ignore_col)>0:
        df_to_concat = df[ignore_col]
        df = df[list(set(df.columns)-set(ignore_col))]
    else:
        df_to_concat = pd.DataFrame()
    for c in spec_chars:
        df = df.replace("\\"+c, '', regex=True)
    df = pd.concat([df,df_to_concat], axis=1)
    return df


def custom_imputation(df, imputation_type="RDF"):
    categorical_columns = []
    numeric_columns = []
    for c in df.columns:
        if df[c].map(type).eq(str).any():  # check if there are any strings in column
            categorical_columns.append(c)
        else:
            numeric_columns.append(c)
    # create two DataFrames, one for each data type
    data_numeric = df[numeric_columns]  # Numerical List.
    data_categorical = df[categorical_columns]  # Categorical List.
    # Imputation of Categorical Values by Mean
    data_categorical = pd.DataFrame(prepross().fit_transform(data_categorical),
                                    columns=data_categorical.columns)
    data_numeric.reset_index(drop=True, inplace=True)
    data_categorical.reset_index(drop=True, inplace=True)
    if imputation_type=="KNN":
        if len(data_numeric.columns) >= 1:
            imp = KNNImputer(n_neighbors=5, weights="uniform")
            data_numeric_final = pd.DataFrame(imp.fit_transform(data_numeric), columns=data_numeric.columns)
            data_numeric_final.reset_index(drop=True, inplace=True)
            final_df = pd.concat([data_numeric_final, data_categorical], axis=1)
        else:
            final_df = data_categorical
    if imputation_type=="RDF":
        if len(data_numeric.columns) >= 1:
            imp = MissForest(max_iter=10, decreasing=False, missing_values=np.nan,
                             copy=True, n_estimators=100, criterion=('mse', 'gini'),
                             max_depth=None, min_samples_split=2, min_samples_leaf=1,
                             min_weight_fraction_leaf=0.0, max_features='auto',
                             max_leaf_nodes=None, min_impurity_decrease=0.0,
                             bootstrap=True, oob_score=False, n_jobs=-1, random_state=None,
                             verbose=0, warm_start=False, class_weight=None)
            data_numeric_final = pd.DataFrame(imp.fit_transform(data_numeric), columns=data_numeric.columns)
            data_numeric_final.reset_index(drop=True, inplace=True)
            final_df = pd.concat([data_numeric_final, data_categorical], axis=1)
        else:
            final_df = data_categorical
    if imputation_type == "mean" or \
            imputation_type == "median" or \
            imputation_type == "most_frequent" or \
            imputation_type == "constant":
        if len(data_numeric.columns) >= 1:
            imp = SimpleImputer(missing_values=np.nan, strategy=imputation_type)
            data_numeric_final = pd.DataFrame(imp.fit_transform(data_numeric), columns=data_numeric.columns)
            data_numeric_final.reset_index(drop=True, inplace=True)
            final_df = pd.concat([data_numeric_final, data_categorical], axis=1)
        else:
            final_df = data_categorical
    return final_df


class DataCleaning():
    def __init__(self, file_upload=None, separator=",", row_threshold=None, col_threshold=None, special_character = None, action = None, ignore_columns=[], imputation_type="RDF"):
        if file_upload == None:
            print("Kindly upload a file")
        else:
            self.df = pd.read_csv(file_upload, sep=separator, error_bad_lines=False)
        self.row_threshold = row_threshold
        self.col_threshold = col_threshold
        self.special_character = special_character
        self.action = action
        self.ignore_columns = ignore_columns
        self.imputation_type = imputation_type

    def start_cleaning(self):
        df1 = rm_rows_cols(self.df, row_thresh=0.8, col_thresh=0.8)
        df2 = replace_special_character(df1, self.special_character, self.action, self.ignore_columns)
        df3 = custom_imputation(df2, self.imputation_type)
        return df3
















