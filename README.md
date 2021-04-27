<p align="center"><img src="https://github.com/DataPreprocessing/DataPrep/blob/main/img/DataPrep.png"></p>

<h1 align="center">DATA PREP</h1>

## Description
<p>In any Machine Learning process, Data Preprocessing is the primary step wherein the information gets changed
or Encoded, to bring it to such a state that now the machine can easily parse it. At the end of the day, the features
of the information would now be able to be effectively deciphered by the calculation.</p>

## DataPrep

<p>Data prep is a python package that is going to encounter all your data cleansing problems like removing unwanted 
columns and rows to imputing all categorical and numerical values in a dataframe and delivers you a  <b>cleaned dataframe</b>  for your modeling purpose.</p>

## Parameters

````python
from data_prep import DataPrep

DataPrep(file_uploaded='filename.csv', separator=",", row_threshold=None, col_threshold=None,
         special_character=None, action=None, ignore_columns=None, imputation_type="RDF")
````

| Parameter | Default Value | Limit | Example |
| ------ | ------ | ------ | ------ |
| file_uploaded | ***none*** | Have to provide a CSV file. | filename.csv |
| separator | ***,*** | Have to provide the separator a csv file | ****;****
| row_threshold Drive | ***none*** | 0 to 100 | 80 | 
| col_threshold | ***none*** | 0 to 100 | 80 | 
| special_character | check the list below | Any special characters | [ '$' , '?' ] | 
| action | ***none*** | ***add*** or ***remove*** | add | 
| ignore_columns | ***none*** | Have to provide list of column names <br> to ignoring the special characters operation. | [ 'column1', 'column2' ] | 
| imputation_type | ***RDF*** | Have to select required imputation <br> ***RDF***, ***KNN***, ***mean***, ***median***, ***most_frequent***, ***constant*** . | KNN | 

###  Data Cleaning and Imputation using Default Parameters

````python
from data_prep import DataPrep

dp = DataPrep(file_uploaded='filename.csv')
cleaned_df = dp.start_cleaning()
````

## User optional parameters

### - Appending extra special characters to the existing default_list

DEFAULT SPECIAL CHARACTERS

````python
default_list = ["!", '"', "#", "%", "&", "'", "(", ")",
                  "*", "+", ",", "-", ".", "/", ":", ";", "<",
                  "=", ">", "?", "@", "[", "\\", "]", "^", "_",
                  "`", "{", "|", "}", "~", "–", "//", "%*", ":/", ".;", "Ø", "§",'$',"£"]
````

````python
# ADDING EXTRA SPECIAL CHARACTERS
special_character =['?', '%']
````

<i>Note:- Do not forget to give <b> action = 'add' </b></i>

````python
from data_prep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', special_character =['?', '%'], action='add')
cleaned_df = dp.start_cleaning()
````

### - Removing special characters from existing default_list

````python
# REMOVING SPECIAL CHARACTERS FROM DEFAULT LIST
special_character =['?', '%']
````

<p>Note:- Do not forget to give  action = 'remove' </p>

````python
from data_prep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', special_character =['?', '%'], action='remove')
cleaned_df = dp.start_cleaning()
````

### - Ignoring columns, for not to perform removing special character operation 

````python
from data_prep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', special_character =['?', '%'],
              action='add', ignore_columns=['timestamp', 'date'])
cleaned_df = dp.start_cleaning()
````

### - Changing threshold for removing null rows and columns 

````python
from data_prep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', row_threshold=50, col_threshold=90)
cleaned_df = dp.start_cleaning()
````    

### - Numerical Columns available imputation methods

  - Available Imputation methods
  - RDF (RandomForest) -> (DEFAULT)
  - KNN (k-nearest neighbors)
  - mean
  - median
  - most_frequent
  - constant
  
````python
# Example for KNN imputation.
from data_prep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', imputation_type='KNN')
cleaned_df = dp.start_cleaning()
````

### - ALL AVAILABLE CUSTOM CHANGES

````python
from data_prep import DataPrep

dp = DataPrep(file_uploaded='filename.csv', special_character =['?', '%'], action='add',
              special_character =['?', '%'], action='remove', ignore_columns=['timestamp', 'date'],
              row_threshold=50, col_threshold=90, imputation_type='KNN')
cleaned_df = dp.start_cleaning()
````

<h2 align="center"> THANK YOU </h2>
