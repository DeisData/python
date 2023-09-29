# Introduction to Python (2) 
# Conditionals and Loops Questions

\

## Question 1: Boolean expressions
Does the following code evaluate as `True` or `False`?

```python
n1 = 45
n2 = -23
n3 = 0
s1 = 'hello'
s2 = 'goodbye'

not (n2 < n3 and s1 == s2 or n1 >= n3)
```

\

## Question 2: Boolean types
What happens when you compare different data types with `==`? What about `>`, `<`, `<=`, or `>=`?

\

## Question 3: if-else

Create a variable called `num` and assign it the value of some number. Create an if-else statement that checks to see if `num` negative is negative or not.

If `num` is negative, multiply `num` by `-1` to make it positive, then print the new value.

If `num` is positive, multiply the number by itself (square it), and print this new value. 

Try your code with different values for `num`.

\
\
\

## Question 4: if-elif-else

Consider this code:

```python
if 4 > 5:
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')
```

Which of the following would be printed if you were to run this code? Why did you pick this answer?

1. A
2. B
3. C
4. B and C

\

## Question 5: Conditionals

Write code that will prints the square root of `x` if x is larger than 20 and `0` if x is less than `0`.

**Bonus**: Print an error message if x is a string or a boolean. 

\

## Question 6: More conditionals 

Create a list called `my_list` with the numbers 0 through 3 in it. Create a variable called `x` with some value.

Create a series of conditionals that check to see if the value in `x` is in `my_list`. 

If this is the case, print out different text depending on what index the item is at in the list.

0. "From zero to hero"
1. "One is the loneliest number."
2. "Two's company."
3. "Three's a crowd."

\

## Question 7: Squaring

Create a blank list as a variable.

Using a for loop, append that list with `.append()` with the square of all integers from 5 to 15. 

\

## Question 8: Looping over a string

Given the following loop:

```python
word = 'oxygen'
for letter in word:
    print(letter)

```
How many times is the body of the loop executed?

- 3 times
- 4 times
- 5 times
- 6 times

\

## Question 9: `for` loops

Iterate over all integers from 0 to 1000 and print all multiples of 41 (numbers that can be divided by 41 with no remainder). How many multiples are there?

Hint: We can use `%` to get remainders.

For instance, `5 % 2` gives us 1.

\

## Question 10
Below are four lists: `x1`, `x2`, `y1`, and `y2`.

Using a single for loop, subtract the values of x1 and x2 at each index, and take the square of the difference. Do the same for `y1` and `y2`. Add the two squares together. Store all 4 squares in a list in the same order.

\

## Question 11: Comprehensions

Using a list comprehension and range() to make a list containing integers 10 - 1000.

\

---

\

# Challenge questions

## 1) Conditionals and loops

\

Below is a tongue twister:

Peter Piper picked a peck of pickled peppers.
A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers,
Where’s the peck of pickled peppers Peter Piper picked?

Turn the tongue twister into a string. Feel free to remove line breaks to make it easier.

Using a for loop and conditionals, count how many times the letter "P" is used, either lower case or upper case.

\

### 2) Nested for loops

On the next page is a nested dictionary structure called `environment_data` containing temperature, humidity, and pressure values for different months in 2021 and 2022. Copy and paste it into a Python cell.

For each year, use for loops to store the months with temperature above 20 degrees and humidity between 50 and 60 in their own lists.

\
\
\
\
\
\
\


```python
environment_data = {
    '2021': {
        'January': {'temperature': 12.3, 'humidity': 40.2, 'pressure': 1012},
        'February': {'temperature': 11.1, 'humidity': 42.7, 'pressure': 1008},
        'March': {'temperature': 13.2, 'humidity': 44.5, 'pressure': 1006},
        'April': {'temperature': 15.8, 'humidity': 50.1, 'pressure': 1010},
        'May': {'temperature': 18.5, 'humidity': 52.3, 'pressure': 1005},
        'June': {'temperature': 21.2, 'humidity': 55.8, 'pressure': 1000},
        'July': {'temperature': 23.8, 'humidity': 57.2, 'pressure': 1001},
        'August': {'temperature': 25.6, 'humidity': 60.1, 'pressure': 1005},
        'September': {'temperature': 22.5, 'humidity': 58.2, 'pressure': 1009},
        'October': {'temperature': 19.4, 'humidity': 51.7, 'pressure': 1011},
        'November': {'temperature': 16.3, 'humidity': 47.2, 'pressure': 1010},
        'December': {'temperature': 13.4, 'humidity': 43.8, 'pressure': 1008}
    },
    '2022': {
        'January': {'temperature': 9.8, 'humidity': 38.1, 'pressure': 1015},
        'February': {'temperature': 10.5, 'humidity': 43.2, 'pressure': 1010},
        'March': {'temperature': 12.9, 'humidity': 47.0, 'pressure': 1004},
        'April': {'temperature': 16.0, 'humidity': 50.6, 'pressure': 1011},
        'May': {'temperature': 18.9, 'humidity': 53.5, 'pressure': 1006},
        'June': {'temperature': 21.6, 'humidity': 57.1, 'pressure': 1001},
        'July': {'temperature': 24.2, 'humidity': 59.4, 'pressure': 1002},
        'August': {'temperature': 26.0, 'humidity': 62.3, 'pressure': 1006},
        'September': {'temperature': 22.9, 'humidity': 59.8, 'pressure': 1010},
        'October': {'temperature': 19.8, 'humidity': 54.5, 'pressure': 1012},
        'November': {'temperature': 16.7, 'humidity': 49.1, 'pressure': 1011},
        'December': {'temperature': 13.8, 'humidity': 45.5, 'pressure': 1009}
    }
}
```