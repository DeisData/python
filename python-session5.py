# Load standard libraries for data analysis
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp


# Import data
gapminder = pd.read_csv('gapminder.csv')
gapminder.info()


############################################
# PYTHON SYNTAX AND STRUCTURE
# How do we make sense of all these periods?
############################################

# ENDING A STATEMENT

# end-of-line
x = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9

# continuation marker \
x = 1 + 2 + 3 + 4 +\
5 + 6 + 7 + 8 + 9

# continuation with () [] ""
x = (1 + 2 + 3 + 4 +
         5 + 6 + 7 + 8 + 9)

# early end of statement ;
x = 1 + 2 + 3; print(x)

# In a program like excel, we structure our functions like this:
# we have data in x
x = [2, 3, 5]

# We are used to calling an operation on x with f(x)
max(x)

# In python, everything is treated as an object
# We have data in a numpy array x
# we call an operation on x with x.f(x)
x = np.array([2, 3, 5])
x.max()

# If we have pandas dataframes, we get plotting functions
x = pd.DataFrame(x)
x.plot(kind='box')

#  . . . and with data loaded into a dataframe
gapminder.max()

gapminder.population.max()

gapminder.age5_surviving.plot(kind='box')

############################################
# FOR LOOPS
# How can I make a program do many things?
############################################


# for each thing in this group, do these operations
for number in [2, 3, 5]:
    print(number)

# This for loop is equivalent to:
print(2)
print(3)
print(5)

# for loop vocabulary:
#  - The collection is what the loop is being run on
#  - The body is the operations done for each value in the collection
#  - The loop variable is what changes in each iteration of the loop

# CHAT Challenge!
# QUESTION 1: What is our collection?
# QUESTION 2: What is our body?
# QUESTION 3: What is our loop variable?


# INDENTATION is always meaningful in Python
firstName = "Claire"
    lastName="Pontbriand"
    
#    The loop variable can be called anything.
for kitten in [2, 3, 5]:
    print(kitten)

    
#    The body of a loop can contain many statements
primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed   = p ** 3
    print(p, squared, cubed)

#    Use range to iterate over a sequence of numbers
print('a range is a build in function: range(0,3)')
for number in range(0,3):
    print(number)


#    The Accumulator pattern turns many values into one
#  A common pattern:
#  1. Initialize an accumulator variable to 0, an empty string, or empty list
#  2. Update the variable with values from a collection

# Sum the first 10 integers.
total = 0
for number in range(10):
    total = total + (number + 1)
    print(total)
# what happens if we change indention?





###########################################################
# CONDITIONALS
# How can programs do different things for different data?
###########################################################

#   Use if statements to control whether or not
#  a block of code is executed

mass = 3.5
if mass > 3.0:
    print(mass, 'is large')

mass = 2.0
if mass > 3.0:
    print(mass, 'is large')


#   Conditionals can be used inside loops
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')


# Use else to execute a block of code with if condition is not met
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 9.0:
        print(m, 'is huge')
    elif m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')


masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')

        
# Use elif (short for else if) to specify additional tests
# Conditions are tested once, in order, so order matters!
#
# QUESTION 4: What will this give us?
grade = 85
if grade >= 70:
    print('grade is C')
elif grade >= 80:
    print('grade is B')
elif grade >= 90:
    print('grade is A')


# We can evolve the values of variables too
velocity = 10.0
for i in range(5): # execute the loop 5 times
    print(i, ':', velocity)
    if velocity > 20.0:
        print('moving too fast')
        velocity = velocity - 5.0
    else:
        print('moving too slow')
        velocity = velocity + 10.0
print('final velocity:', velocity)


#   Compounding relations using and, or, and parentheses
mass     = [ 3.54,  2.07,  9.22,  1.86,  1.71]
velocity = [10.00, 20.00, 30.00, 25.00, 20.00]

i = 0
for i in range(5):
    if mass[i] > 5 and velocity[i] > 20:
        print("Fast heavy object.  Duck!")
    elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
        print("Normal traffic")
    elif mass[i] <= 2 and velocity[i] <= 20:
        print("Slow light object.  Ignore it")
    else:
        print("Whoa!  Something is up with the data.  Check it")

# Make use of parentheses just like in mathematics
# if (mass[i] <= 2 or mass[i] >= 5) and velocity[i] > 20:
# if mass[i] <= 2 or (mass[i] >= 5 and velocity[i] > 20):


# QUESTION 5.  What does this program print?
pressure = 71.9
if pressure > 50.0:
    pressure = 25.0
elif pressure <= 50.0:
    pressure = 0.0
print(pressure)


# QUESTION 6.  FILL IN THE BLANK using len() so that this program only processes
#   files with fewer than 50 records.
import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    ____:
        print(filename, len(contents))

# (We're not going to run this code.  We don't have these data files ready)




############################################
# PUTTING IT TOGETHER
#   An example of loops and conditionals
#   working with data
############################################
gapminder.info()

gdata_1995 = gapminder[gapminder.year == 1995]
print(gdata_1995)

countries  = gdata_1995.country
print(countries)

# Question: 
# Which countries have gdp per capita above average
# in 1995?

mean_gdp = gdata_1995.gdp_per_capita.mean()
print(mean_gdp)


# Let's loop through the countries
# and print years where who is above 
# the global average

for place in countries:
    place_data = gdata_1995[gdata_1995.country==place]
#    print(place)
#    print(place_data)
    place_gdp = np.array(place_data.gdp_per_capita)        
    if place_gdp > mean_gdp:
        print(place, 'is above average gpd per capita')
    else:
        print(place, 'is below average gdp per capita')




