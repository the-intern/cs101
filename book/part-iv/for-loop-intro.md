# Python's `for` Loop

You've seen the `while` loop but, with the introduction of another `iterable`, i.e., the `list` (the `string` being the first), it's time to learn the `for` loop, a means of repeating code blocks for the extent of an iterable's length.

The while loop typically is designed to repeat a specific block of code an _unknown_ number of times until a condition is met. In some cases, it is intended to repeat without end.

But if the number of loops can be known ahead of time, you typically will use the `for loop`.

When we say the number of loops "can be known ahead of time," that doesn't necessarily mean a specific number. Rather, it means the number of repetitions can be known with respect to something else. Thus, when you know you need to iterate over a string or list, you know that the repetitions will be **_no more_** than the size of the string or list or whatever other iterable you are moving through.

## Syntax

The most basic and common for loop contains two keywords (`for` and `in`) and two variable names:

```python

for var in some_iterable:
    # code block

```

In the for loop above, the `var` is simply the variable name you provide and `some_iterable` is just that -- a string or list or some other iterable over which you loop. `var` could be any variable name upon which you decide -- following all the same rules for variable naming -- and upon each iteration through the loop, the `var` will be assigned to the next item in the iteratable.

Thus:

```python

names = ['George', 'John', 'James', 'Benjamin']

for name in names:
    print(name)

# George
# John
# James
# Benjamin

```

## Use of `range` in `for` Loop

Python's `range()` function creates a series of integers on the fly ...

```python

for i in range(10):
    #
    print(n)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

```

... and it works quite well with for loops because the integers generated can be used to index into sequences like lists and strings.

```python

names = ['George', 'John', 'James', 'Benjamin']

for i in range(len(names)):
    print(i, names[i])

# 0 George
# 1 John
# 2 James
# 3 Benjamin

```
