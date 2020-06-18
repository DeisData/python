# Python Programming Session 2 Instructions

[Zoom Classroom Link](https://docs.google.com/document/d/18TwHdTBUU34PNF8Vz2YYWbmME4tS3NS7Ugu5NjaMmBo/edit?usp=sharing)


To prepare for today, please download 2 gapminder datasets to a gapminder_data folder on your Desktop. 
To download an individual file from github, open it, click the [RAW] button, and right-click "Save Link As."
- [gapminder_gdp_oceania.csv](https://github.com/DeisData/python/blob/master/gapminder_gdp_oceania.csv)
- [gapminder_gdp_europe.csv](https://github.com/DeisData/python/blob/master/gapminder_gdp_europe.csv)
 
This week we will be coding in Spyder launched through Anaconda Navigator, instead of working in a Jupyter Notebook.

Code and comments will be shared after the session!

## Questions of the Day:
- How can I use built-in functions?
- How can I find out what they do?
- How can I use software that other people have written?  Answer: Libraries are powerful!
- How can I read in and start getting statistics on tabular data?

## Key Points of the Day:
### Built-In Functions and Help
- Use comments `#` to add documentation to programs.
- A function may take zero or more arguments and uses parentheses
  - Common functions are `max()`, `min()`, and `round()`
  - `help()` will get help for a function
  
### Libraries
- The power of a programming language is in ints libaries.
- `import` a library module to use it
- Use `help` to learn about the contents of a library module
- Import specific iteams from a library to shorten programs. For example, `from math import cos, pi`
- Use an alias for a library when importing it to shorten programs. For example, `import math as m`

### Reading in Data with Pandas DataFrames
- `import pandas` library to get basic statistics out of tabular data
- `index_col` specities a column's values as the row headings
- `DataFrame.info` will tell you more about a dataframe
- `DataFrame.columns` variable stores information about the dataframe's columns
- `DataFrame.T transponses a dataframe
` `DataFrame.describe gets summary statistics
- Use `DataFrame.iloc[...,...]` to select values by integer location
- Use `:` on its own to mean all columns or all rows if selecting a subset of a dataframe



## Challenge Questions
1. Functions
What is wrong?
`print("hello world"`
- a. Syntax Error
- b. Runtime error
- c. Nothing

<details><summary>Solution</summary>
Syntax Error - we forget to close the parentheses for the `print()` function.
</details>

2.  Match the print statement with the appropriate library call.
`print("sin(pi/2) =", sin(pi/2))`
- a. `from math import sin, pi`
- b. `import math`
- c. `import math as m`
- d. `from math import *`

<details><summary>Solution</summary>
Library calls a and d. 
In order to directly refer to sin and pi without the library name as prefix, you need to use the from ... import ... statement. 
Whereas library call a. specifically imports the two functions sin and pi, library call d. imports all functions in the math module.
</details>

3.  Match the print statement with the appropriate library call.
`print("sin(pi/2) =", m.sin(m.pi/2))`
a. `from math import sin, pi`
b. `import math`
c. `import math as m`
d. `from math import *`

<details><summary>Solution</summary>
Library call c. 
Here sin and pi are referred to with a shortened library name m instead of math. 
Library call c. does exactly that using the import ... as ... syntax - 
it creates an alias for math in the form of the shortened name m.
</details>


4. Assume Pandas has been imported into your program and you have the Gapminder GDP data for Europe loaded.
```import pandas as pd
df = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
```
Write an expression to find the Per Capita GDP of Serbia in 2007.

<details>
<summary>Solution</summary>

print(df.loc['Serbia', 'gdpPercap_2007'])

</details>



 
