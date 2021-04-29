![data-cleaning](https://github.com/DataPreprocessing/DataPrep/blob/main/img/datacleaning.png | width=100%)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/data-cleaning)
![PyPI - License](https://img.shields.io/pypi/l/data-cleaning)
![PyPI](https://img.shields.io/pypi/v/data-cleaning)
![GitHub repo size](https://img.shields.io/github/repo-size/DataPreprocessing/DataCleaning)

<h1 align="center">DATA CLEANING</h1>
## Description
<p>In any Machine Learning process, Data Preprocessing is the primary step wherein the raw/unclean data are transformed 
into cleaned data, So that in the later stage, machine learning algorithms can be applied. This python paackage make the 
data preprocessing very easy in just 2 lines of code. All you have to do is just input a raw data(CSV file), this library
will clean your data and return you the cleaned dataframe on which further you can apply feature engineering, 
feature selection and modeling.

- What this does?
    * Cleans special character
    * Removes duplicates
    * Fixes abnormality in column names 
    * Imputes the data (categorical & numerical)
    
</p>

## Data Cleaning

<p>Data prep is a python package for data preprocessing. This cleans the CSV file and returns the <b>cleaned data frame</b>. 
It does the work of imputation, removing duplicates, replacing special characters, and many more.</p>

## How to use:

Step 1:
  Install the libaray

````python
pip install data-cleaning
````
Step 2:

  Import the library, and specify the path of the csv file. 
````python
from dataprep import DataPrep

dp = DataPrep(file_uploaded='filename.csv')
cleaned_df = dp.start_cleaning()
````

There are some optional parameters that you can specify as listed below,

## Usage:

````python
from dataprep import DataPrep

DataPrep(file_uploaded='filename.csv', separator=",", row_threshold=None, col_threshold=None,
         special_character=None, action=None, ignore_columns=None, imputation_type="RDF")
````

## Parameters

------

| Parameter | Default Value | Limit | Example |
| ------ | ------ | ------ | ------ |
| file_uploaded | ***none*** | Provide a CSV file. | filename.csv |
| separator | ***,*** | Separator used in csv file | ****;****
| row_threshold | ***none*** | 0 to 100 | 80 | 
| col_threshold | ***none*** | 0 to 100 | 80 | 
| special_character | Check the list below |Sspecify the character <br> that is not listed in default_list (see below) | [ '$' , '?' ] | 
| action | ***none*** | ***add*** or ***remove*** | add | 
| ignore_columns | ***none*** | Provide list of column names <br> to ignoring the special characters operation. | [ 'column1', 'column2' ] | 
| imputation_type | ***RDF*** | Select your preferred imputation <br> ***RDF***, ***KNN***, ***mean***, ***median***, ***most_frequent***, ***constant*** . | KNN | 


## Examples of using parameters

### - Appending extra special characters to the existing default_list

The DEFAULT SPECIAL CHARACTERS included in the package are shown below,

````python
default_list = ["!", '"', "#", "%", "&", "'", "(", ")",
                  "*", "+", ",", "-", ".", "/", ":", ";", "<",
                  "=", ">", "?", "@", "[", "\\", "]", "^", "_",
                  "`", "{", "|", "}", "~", "–", "//", "%*", ":/", ".;", "Ø", "§",'$',"£"]
````
How to remove a special character, say for example if you want to remove "?" and "%".

<i>Note:- Do not forget to give <b> action = 'remove' </b></i>

````python
from dataprep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', special_character =['?', '%'], action='remove')
cleaned_df = dp.start_cleaning()
````
How to add a special character, say for example if you want to add "é" that is not in the default_list given above.

<i>Note:- Do not forget to give <b> action = 'add' </b></i>

````python
from dataprep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', special_character =['é'], action='add')
cleaned_df = dp.start_cleaning()
````

### - Ignoring a particular columns and adding a special character
Say for example, column named "timestamp" and "date" needs to be removed and a special character needs to be added 'é'

````python
from dataprep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', special_character =['é'],
              action='add', ignore_columns=['timestamp', 'date'])
cleaned_df = dp.start_cleaning()
````

### - Changing threshold to remove null rows/columns above this given threshold value

````python
from dataprep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', row_threshold=50, col_threshold=90)
cleaned_df = dp.start_cleaning()
````    

### - Imputation methods available

  - RDF (RandomForest) -> (DEFAULT)
  - KNN (k-nearest neighbors)
  - mean
  - median
  - most_frequent
  - constant
  
````python
# Example for KNN imputation.
from dataprep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', imputation_type='KNN')
cleaned_df = dp.start_cleaning()
````

<h2 align="center"> --- THANK YOU, CHEERS --- </h2>
