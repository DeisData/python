#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:23:26 2020

@author: Claire Pontbriand
"""


# # # # # # # # # # # # # # # #  
#                             #
# Built-in Functions and Help #
#                             #
# # # # # # # # # # # # # # # # 
#
#  How can I use built-in functions?
#  How can I find out what they do?
#  What kind of errors can occur in programs?


#  Use comments to add documentation to programs.
# This sentence isn't executed by python
adjustment = 0.5 # Neither is this - anything after # is ignored
print(adjustment)


#  A FUNCTION may take zero or more arguments
#  A function must always use parentheses
print('before')
print()
print('after')


# Commonly-used built-in functions include max, min, 
#  and round.
print(max(1,2,3))
print(min('a','A','0')) # Pythong users (0-9,A-Z,a-z) to compare letters
round(3.712)
round(3.71215,2) # second argument specifies number of decimal places

# Use the built-in function help to get help for a function.
help(round)

# Python reports syntax errors
# when it can’t understand the source of a program.
name='Feng  #forgot to close the quotation marks


# Python reports a runtime error 
# when something goes wrong while a program is executing.
age = 53
remaining = 100 - aege  #mispelled age




# # # # # # # # # # # # # # # #  
#                             #
# Libraries                   #
#                             #
# # # # # # # # # # # # # # # # 
#
#  How can I use software that other people have written?
#
#
# Most of the power of a programming language is in its libraries.
# A library is a collection of files (called modules) 
# that contains functions for use by other programs.
# May also contain data values 
# PyPI is the Python Package Index
#
#
# A program must import a library module before using it.
#



# Refer to things from the module as module_name.thing_name
# Using math, one of the modules in the standard library:
import math

print('pi is', math.pi)
print('cos(pi) is', math.cos(math.pi))


# Use help to learn about the contents of a library module.
help(math)

# Import specific items from a library to shorten program, save memory
from math import cos, pi

print('cos(pi) is', cos(pi))


# Create an alias for a library module when importing 
# it to shorten programs.
import math as m

print('cos(pi) is', m.cos(m.pi))




# # # # # # # # # # # # # # # #  
#                             #
# Reading in Data with Pandas #
#                             #
# # # # # # # # # # # # # # # # 
#
# How can I read tabular data?
#

# Import the Pandas library.
# Pandas is a widely-used Python library 
# for statistics, particularly on tabular data.

# Use Pandas to load a simple CSV data set.
# Get some basic information about a Pandas DataFrame.
# Use the Pandas library to do statistics on tabular data.

data = pd.read_csv('gapminder_data/gapminder_gdp_oceania.csv')
print(data)


# Use index_col to specify that a column's 
# values should be used as row headings

data = pd.read_csv('gapminder_data/gapminder_gdp_oceania.csv', index_col = 'country')
print(data)


# Use DataFrame.info to find out more about a dataframe
data.info()

# Use DataFrame.T to transpose a dataframe
data.T

# Use DataFrame.describe to get summary statistics 
# about data.
print(data.describe())

# You can also writing Data with to_csv


# # # # #
# Selecting Values in a Pandas DataFrame
# # # # # 

# What makes Pandas so attractive is the powerful interface 
# to access individual records of the table, proper handling 
# of missing values, and relational-databases operations 
# between DataFrames.

df = pd.read_csv('gapminder_data/gapminder_gdp_europe.csv', index_col='country')


# Use DataFrame.iloc[..., ...] to select values by their (entry) position
# Can specify location by numerical index 
print(df.iloc[0,0])

# Use DataFrame.loc[..., ...] to select values by their (entry) label.
print(df.loc["Serbia","gdpPercap_2007"])



# Use : on its own to mean all columns or all rows.
print(df.loc[:,"gdpPercap_2007"])



# and apply functions to subsets of data, for example, here
# we find the maximum value of gdp in 2007 from European countries
# (it is Norway)
print(df.loc[:,"gdpPercap_2007"].max())



# # That's it for today!  On to the challenge questions and survey





