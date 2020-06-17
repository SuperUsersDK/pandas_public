# Tuberculosis - data science cleaning

In this exercise must a dataset be cleaned. The data set is data about tuberculosis from WHO (World Health Organization).
The file `datasets/tb.csv` contains reported cases of tuberculosis.

1. Read the file into a dataframe named _tb_. How many observations is present per row?
2. Rename column `iso2` to `_country_`.
3. Remove the prefix `new_sp_` from all columns.
4. Remove the columns `new_sp`, `m04`, `m514`, `f04` and `f514`. Why are there columns not needed?
5. The data from WHO is in wide-format. Which two columns are ID for observations?
6. Change the dataframe to long format such that there only one observation per row.
   There should be ?? rows and ?? columns.
7. Create a new column called `sex` which contains `f` for female and `m` for male. Base the data on the first letter in the age column.
8. Remove `m` and `f` from the age column.

