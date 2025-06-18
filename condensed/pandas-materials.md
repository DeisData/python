# Introduction to Python (3): Pandas
# Practice questions


## Question 1: Columns as variables

Try saving a column as a variable. Print the new variable you've saved. 

<details>
<summary>Solution</summary>

We can save columns as variables the same way we've saved other Python data types as variables.

```python
region = df['region']
```
</details>


## Question 2: Unique years
We can sometimes consider the year to be a categorical variable. How many unique years are there in the data set?

If you're forgetting what the column names are, remember to use `.columns`!

<details>
<summary>Solution</summary>

We can use `.nunique()` for numerical columns too. 

```python
df['year'].nunique()
```
</details>


## Question 3: Summarizing data
Select the columns `age5_surviving`, `gdp_per_day`, and `gdp_per_capita`, and print out summary statistics for these columns.

<details>
<summary>Solution</summary>

```python
df[['age5_surviving', 'gdp_per_day', 'gdp_per_capita']].describe()
```

</details>


## Question 4: Subsetting

Create a subset of data set including only samples from the region `'Asia'`. What is the mean of the `'life_expectancy'` column of this subset?

<details>
<summary>Solution</summary>

`df[df['region']=='Asia']` will get us the desired subset. We can next use `.mean()` to get the mean of a single column.

```python
df_asia = df[df['region']=='Asia']
df_asia['life_expectancy'].mean()
```

</details>


## Question 5: Multiple subsets

Take a subset of df_hungary where the `life_expectancy` column is below 70.

What is the mean of `population` for this subset? Is it different than the mean population of `df_hungary`?

How many data points are remaining? (hint: use `.shape`)

<details>
<summary>Solution</summary>

Taking subsets can be an important way to explore data, but it also can drastically reduce sample size. 

```python
df_hungary_70 = df_hungary[df_hungary['life_expectancy']<70]
print('population:',df_hungary_70['population'].mean())
print('subset rows:', df_hungary_70.shape[0])
```

</details>

## Question 6: Shape after merge

Using `.shape` to compare the size of `merged_left` and `merged_inner`. Are the numbers of rows the same? What about the number of columns? If there is a difference, why is there a difference?

<details>
<summary>Solution</summary>

The `merged_left` has more rows than `merged_inner`, as left joins are more inclusive than inner joins. 

```python
print('merged left:', merged_left.shape)
print('merged inner:', merged_inner.shape)
```

</details>



## Question 7: Comparing merges

Compare the two types of joins. Which type of join results in more rows with missing data? Can you think of situations where one type of join might be more useful than the other?

<details>
<summary>Solution</summary>

Left joins will have more instances of missing data than inner joins, as there will be identifiers from the left data frame that are not present in the left data frame, while inner joins require that identifiers are present in both data frames.

Both types of joins are helpful in different situations. For instance, a left join will be helpful in situations where you want to add additional context to data and missing data is acceptable, while inner joins will be helpful when you want all rows to have data from the incoming data frame. 

</details>

---

# Challenge Questions

## 1) Putting it together

Some data was collected by 5 different researchers on deer population sizes. Below, this data was recorded with accompanying temperature data and dates in three lists. In each list, one researcher is associated with the same index.

0. Haley McCann
1. Siena Welch
2. Jaylin Mercado
3. Ismael Hayden
4. Nina Bright

Transfer these data into a Pandas dataframe. Display the data frame, and export it as a .csv file.

As a reminder, each list is in the same order as the researchers name -> all of Haley McCann's data is at index `0`.


```python
researchers = ['Haley McCann', 'Siena Welch', 
    'Jaylin Mercado', 'Ismael Hayden', 'Nina Bright']

temperatures = [29.75, 12.63, 31.58, 7.16, 32.51]

populations = [442, 336, 505, 913, 933]

dates = ['5/25/2022','3/18/2022','6/28/2022','11/11/2022','7/6/2023']
```


## 2) Planets.csv

Upload the Planets.csv to Google Colab, and load it into Python. Use `.head()` to display the first rows of the DataFrame. What columns are present? How many rows are there? Use `.describe()` to summarize your data.

## 3) Your own data

Upload your own .csv file onto Google Colab. Make sure you have a single row for column names. Try manipulating it and summarizing your data.