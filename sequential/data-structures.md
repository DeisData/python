# Python Data Structures

Going over the fundmentals, we learned how to store numbers and sets of characters as variables. Python also has built-in ways to store multiple strings and numbers, namely **lists**, **tuples**, **dictionaries**, and **sets**. These all allow you to groups of ints, floats, and strings in different arrangements. Here, we created a `list` of 5 ints called `x`.


```python
x = [ 1, 2, 3, 4, 5 ] # integers 1 - 5
```

Here are brief descriptions of the four structures.

- Lists: store data in a **specific order**
- Dictionaries: store combinations of **keys** and **values** without any order
- Tuples: store data in a specific order and **cannot** be altered
- Sets: store unordered data

We will dive into these in more detail below, focusing primarily on lists and dictionaries.

## Lists

Lists are very common tools in Python. They allow us to store large amounts of data with an order. They come with very handy tools to reference different objects stored in them. We can also easily add items to them.

### Initialize a list
There are two ways of initializing an empty list: `list()` and ` [] `. 


```python
# these do the same thing
my_list = list() 
your_list = []
```

To make a list with pre-populated with items, we can fill the brackets with comma-separated values.


```python
number_list = [ 0.1, 0.2, 0.3, 0.4 ] # lists can hold numbers
string_list = [ 'cat', 'dog', 'rabbit' ] # can also hold strings
```

### Referencing to items in a list

Each item in a list has an **index**. If your list has 3 items, it has 3 indexes (or indicies, depending on who you ask). 

In Python, indexes starts at 0. To reference the first item in `number_list`, we use `number_list[0]`.


```python
number_list[0] # get the first item from number_list
```




    0.1



We can reference the rest of the numbers in the list with indexes 1 through 3. Note that even though there are 4 items in the list, the index goes from 0 to 3. 

We also can use the items in a list the same way we can use variables to do math or other operations.


```python
print( number_list[1] - number_list[3] ) # 0.2 - 0.4 
print( 'my favorite kind of animal is', string_list[2] ) # prints rabbit
```

    -0.2
    my favorite kind of animal is rabbit


If we try to reference an index that does not exist in a list, we get an error.


```python
number_list[4]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    /Users/fordfishman/GitHub/python/data-structures.ipynb Cell 15' in <cell line: 1>()
    ----> <a href='vscode-notebook-cell:/Users/fordfishman/GitHub/python/data-structures.ipynb#ch0000027?line=0'>1</a> number_list[4]


    IndexError: list index out of range


If we want to reference the last item in a list, we can do it two ways. We can use the length of list and subtract 1. Alternatively, we can also use `[-1]` as a shorthand for the last item.


```python
print( number_list[ len(number_list) - 1 ] )
print( number_list[-1])
```

    0.4
    0.4


### Appending to a list

If we want to add an item to the end of `string_list`, we can use `string_list.append()`.


```python
string_list.append('bear')
print(string_list)
```

    ['cat', 'dog', 'rabbit', 'bear']


### Reassigning an item in a list

We can also alter any item currently in a list.


```python
number_list[0] = 2096
print(number_list)
```

    [2096, 0.2, 0.3, 0.4]


### Question 1: Lists
Create a list of numbers. Add the first number in the list to the last number of the list. Append this value to the list.


```python
### Your code here:

```

## Dictionaries
Like lists, dictionaries are powerful ways to store items. However, the two structures are quite different from each other. Instead of storing items in a specific order, like a list, dictionaries store them as **keys** and **values**. For example, you might have a key `giraffes` paired with the value `25`, and the key `kangaroos` paired with the value `32`. We can do this with using brackets (`{ }`) and colons (`:`) with the format of `{ KEY1: VALUE1, KEY2: VALUE2, ... }`.


```python
animals_dict = { 'giraffes': 25, 'kangaroos': 32 }
```

Notice that our keys are strings and our values here are ints. Keys and values can be any data types, though it tends to be best practice for keys to be strings. 

We can also write this vertically, putting key-value pairs on their own lines for visual clarity. You will still need to separate entries with a comma, however.


```python
animals_dict = { 
    'giraffes': 25, 
    'kangaroos': 32 
}
```

Once we create a dictionary with keys and values, we can use the key to return the corresponding value. We do this by using `DICT[KEY]`:


```python
animals_dict['giraffes']
```




    25



Similarly to lists, if we try to reference a key that is not present in the dictionary, we will get an error.


```python
animals_dict['beaver']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    /Users/fordfishman/GitHub/python/data-structures.ipynb Cell 33' in <cell line: 1>()
    ----> <a href='vscode-notebook-cell:/Users/fordfishman/GitHub/python/data-structures.ipynb#ch0000041?line=0'>1</a> animals_dict['beaver']


    KeyError: 'beaver'


However, dictionaries have a way around this. We can use the `.get()` function to either return a value for a key or a default value that we specify. We run it with `DICT.get(KEY, DEFAULT_VALUE)`.


```python
animals_dict.get('beaver', 0) # will return 0 because beaver is not a key in this dictionary
```




    0



Making an empty dictionary is similar to making an empty list. We can either use `dict()` or `{}`.


```python
# these do the same thing
my_dict = dict()
your_dict = {}
```

### Adding to a dictionary
It is very simple to add a new item to a dictionary. Instead of using the colon notation, we can simply run `DICT[KEY] = VALUE`. 


```python
animals_dict['moose'] = 43 # new key-value pair - moose: 43
print(animals_dict)
```

    {'giraffes': 25, 'kangaroos': 32, 'moose': 43}


### Give a key a new value
Giving a key a new value works just like reassigning an item in a list. Note that this means that you cannot have two identical keys in the same dictionary.


```python
animals_dict['giraffes'] = 85 # key giraffes assigned the value of 85
print(animals_dict)
```

    {'giraffes': 85, 'kangaroos': 32, 'moose': 43}


### Question 2: Dictionaries
Assign the value of `giraffes` in `animal_dict` to a new key `rabbit` in the same dictionary.


```python
### your code here: 

```

## Tuples
Tuples are a lot like lists. They are ordered collections of items that can be referenced with number indexing. However, they are **immutable**, meaning that once you create one, you cannot change it by adding to it or editing items in it. They are a somewhat more efficient to use, so they are situationally useful.

You can create a new tuple with parentheses. Note that creating an empty tuple has little use, since it cannot be altered.


```python
my_tuple = ( 0, 1, 2, 4, 8 ) 
```

## Sets

Sets are unordered collections of items. You can think about about them like dictionaries that only consist of keys. Like tuples, they are more situationally useful than lists or dictionaries. Like dictionaries, they also use `{}` but they do not use colons. 


```python
my_set = set() # the only way to initialize an empty set

new_set = { 'lions', 'tigers', 'bears' } # without colons, NOT a dictionary
```

We can add items to a list using `.add()`. However, if the item is already present in the set, only one copy will be kept in it. Therefore, sets keep a unique group of items.


```python
new_set.add('oh my') # oh my will now be a string in the set
print(new_set)

new_set.add('bears') # won't have two beats in the set
print(new_set)
```

    {'oh my', 'tigers', 'lions', 'bears'}
    {'oh my', 'tigers', 'lions', 'bears'}


### Question 3: Structures

For each of the following examples, should you use a list, dictionary, tuple, or set?

1. A group of employees and their IDs.
2. All 12 months in order.
3. Your favorite foods ranked.
4. All of the foods you have tried.

## Bonus: Nested structures

We can place data structures within other data structures as well. These new structures are referred to as **nested data structures**, and they are powerful.

We have lists containing lists, dictionaries containing dictionaries, dictionaries containing lists, and much more.

```python
# list of lists
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f', 'f']
list3 = ['h', 'i', 'j']
large_list = [list1, list2, list3]
print(large_list)
# dictionary of dictionaries

sample1 = {
    'co2': [10.2, 3.4, 10.1],
    'n': 4,
    'city': 'Waltham'
}

sample2 = {
    'co2': [4.2, 2.3, 3.5, 23],
    'a': 23,
    'city': 'Watertown'
}

samples = {'s1': sample1, 's2':sample2}
samples2 = dict()

samples = {'s1': sample1, 's2':sample2}
print(samples)
```


Indexing and referencing items in these nested structures can get quite complicated. It's important to know the full nested structure when doing these references.

```python
print(large_list[0][2])

print(samples['s1']['city'])

print(samples['s2']['co2'][0])
```

### Bonus Question 1: Nested structures pt. 1
Create a list that contains an empty list, an empty dictionary, an empty tuple, and an empty set.

Then, add any new item to the nested list and the set, and add a key-item pair to the dictionary.

```python
# your code here
```


### Bonus Question 2: Nested structures pt. 2

We want to store information regarding the ecological community in the local area.

In Rivertown, there are 12 species of frogs, 2 species of snakes, and 20 species of birds. 

In Spring Valley, there are 4 species of frogs, 1 species of snake, 2 species of birds, and 13 species of rodents.

In Ice Town, there are 4 species of birds, 6 species of rodents, and 1 species of bear.

Store this information in one nested data structure.

```python
# your code here
```