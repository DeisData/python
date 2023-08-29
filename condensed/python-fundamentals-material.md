# Introduction to Python (1): Questions

\

## Question 1. Do it yourself! Coding

```python

# INSTRUCTIONS: Write a message in the quotes.
# type Shift+Enter to run the cell.
message = ''


print(message)
```

\

## Question 2: Math calculations

Calculate the following value in Python: $\frac{25}{(35 - 3)^3}$

\

## Question 3. Swapping Values
Given the code below, what is the value of the variable `swap` by the end of the block?

```python
x = 1.0
y = 3.0
swap = x
x = y
y = swap
```

\

## Question 4: Assigning variables


`a` has been initialized to be 25. Assign variable `b` to be 5 less than `a` without using `b = 20`. Print the value of b.

```python
a = 25
# write your code here:
```

\


## Question 5: Errors


What will happen if you run this code?

```python
last_name = Montoya
print(last_name)
```

\

## Question 6: Variable type
Choose a type (int, float, str) that each of these descriptions should be:
- Time elapsed from the start of the year until now in days.
- Serial code of a piece of lab equipment
- A lab specimen's age

\

## Question 7: Variable conversion

```python
first = 1.0
second = "1"
third = "1.1"
```

Which of the following will return the floating point number `2.0`?

```python
# first + float(second) # choice a
# float(second) + float(third) # choice b
# first + int(third) # choice c
# first + int(float(third)) # choice d
# int(first) + int(float(third)) # choice e
# 2.0 * second # choice f
```

\

## Question 8: Making a list


Create a small grocery list as a Python list of strings. Using indexing, print the third item in the list.

\

## Question 9: Appending
Create a list of numbers. Add the first number in the list to the last number of the list. Append this value to the list.

\


## Question 10: Grocery dictionary


Make a dictionary where the keys are the names of the items in your grocery list, and the values are the expected cost of the item.

\

## Question 11: Dictionary modification
Assign the value of `giraffes` in `animal_dict` to a new key `rabbit` in the same dictionary.

\

---

\

# **Challenge questions**

\

## 1) Quadratic formula


A quadratic equation has the following form:


$$0 = ax^2 + bx + c$$


We can use the quadratic formula (below) to find the roots of a quadratic equation.


$$x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}$$


Create variables $a$, $b$, and $c$ with the value of $4$, $-25$, and $20$, respectively.


Calculate the values of $x$ for a quadratic equation with $a=4$, $b=-25$, and $c = 20$. Remember to calculate the values for both plus and minus ($\pm$).

\

## 2) Nested structures


We want to store information regarding the ecological community in the local area.


In Rivertown, there are 12 species of frogs, 2 species of snakes, and 20 species of birds.


In Spring Valley, there are 4 species of frogs, 1 species of snake, 2 species of birds, and 13 species of rodents.


In Ice Town, there are 4 species of birds, 6 species of rodents, and 1 species of bear.


Store this information in one nested data structure.

