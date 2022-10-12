# Challenge - 05 - `while` Loops

## 1. Write a `while` loop such that you print out the first 10 natural numbers:

1

2

3

4

5

6

7

8

9

10

```python
# variable declarations?

# while



```

## 2. Write a `while` loop that prints the following even numbers:

2

4

6

8

10

12

14

16

18

20

```python
# variables?

# while ...
```

## 3. Write a `while` loop that processes all the lower-case letters and prints out a letter if it is a vowel

### Preliminaries to writing the loop

A handy operator in Python is `in` which returns a `boolean` answering whether some item is present in an interable such as a string. For example:

```python
some_characters = 'abcdefg'
# use 'in' to see if an 'e' is present

print('x' in some_characters) # will return and print 'False'
print('e' in some_characters) # will return and print 'True'
```

    False
    True

Use `in` to write the loop.

Additional hints:

1.  use an `if` statement in the loop

2.  The `if` statement should check if a character is `in` the string `vowels`.

3.  If it is, use a print statement to output it.

Note: Make sure to **remove** the `pass` keyword

```python
letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

count = 0
while count < len(letters):
    # do something here
    count += 1
```

## 4. Write a `while` loop that generates a random integer from 1000 to 1100 and only breaks out if the integer is equal to 1050 **but not before printing out the 1050**!

```python
from random import randint

while True:
    pass
```

## 5. Countdown

- Write a procedure named `countdown()`
- It should take in an integer and prints backward from that integer down to 0 and then prints "Blastoff!"
- Call it with the integer 10

```python

def countdown(i):

    while i >= 0:
        pass

countdown(10)
```
