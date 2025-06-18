# Introduction to Python (4): Figures
# Practice questions


### Question 1: Scatter plot

We can make a scatter plot very similarly to a line plot with `ax.scatter()` instead of `ax.plot()`. Try recreating the life expectancy line plots with scatter plots, instead. 

<details>

<summary>Solution</summary>

Swapping out plot types in matplotlib can be simple if both take the same number of inputs. Here we can just replace `ax.plot()` instead of `ax.scatter()`.

```python
figure, ax = plt.subplots()
# instead of ax.plot(), use ax.scatter()
ax.scatter(df_jm['year'], df_jm['life_expectancy'], color='#333', label='Jamaica') 
ax.scatter(df_cb['year'], df_cb['life_expectancy'], color='blue', label='Cuba') 
ax.set_xlabel('Year')
ax.set_ylabel('Life expectancy')
ax.set_title('Life expectancy over time in Jamaica and Cuba')
ax.legend() 
plt.show()
```

</details>

## Question 2: Histograms

Plot histograms of `gdp_per_day` for 4 different countries in the `gapminder.csv` data set. You can do this in one or multiple panels.

<details>
<summary>Solution</summary>

Here's how you would do this in one panel in seaborn.

```python
# import log function
from numpy import log10
# subset
df_2000 = df[df['year']==2000].copy() # .copy() removes some warnings pandas will throw
# log transform
df_2000['population_log10'] = log10(df.population)
sns.histplot(df_2000, x='population_log10', multiple='stack', hue='region')
plt.show()
```

And here's how to do in multiple panels in matplotlib.

```python
# import log function and array
from numpy import log10
# subset
df_2000 = df[df['year']==2000].copy() # .copy() removes some warnings pandas will throw
# log transform
df_2000['population_log10'] = log10(df.population)

nrow = 2
ncol = 2

# draw axes
figure, ax = plt.subplots(nrow,ncol, sharey=True, figsize=(10,10))


# creates a pandas 2x2 object of region names
regions = pd.unique(df_2000.region).reshape((2,2))

for i in range(nrow): # i goes from 0 - 1

   for j in range(ncol): # j goes from 0 - 1

      region = regions[i][j]
      df_sub = df_2000[ df_2000['region']==region]

      ax[i,j].hist(df_sub['population_log10'], bins=15)
      ax[i,j].set_xlabel('Population (log10)')
      ax[i,j].set_xlim((4.5,9.5)) # make them have the same x range
      ax[i,j].set_ylabel('Number of countries')
      ax[i,j].set_title(region)

plt.show()
```

</details>

## Question 3: Plots from the gallery
Take a look at the some of [the plot types in matplotlib](https://matplotlib.org/stable/plot_types/index.html) and [the Seaborn Gallery](https://seaborn.pydata.org/examples/index.html). Using the `gapminder` data, recreate some of these plot types in matplotlib and/or Seaborn. 