# Background and Instructions

> The Challenge to Naming Variables

---

## But first a comment on `comments` ...

When in your source code --- i.e., in a python file or `module` (any file that ends in `.py`), you'll often need to put in comments.  In fact, if you look at any professional code, developers and engineers use a <u>lot</u> of comments.

That is because, a day or two or a month later they will forget why they used that variable.  Also, someone else will often have to use their code.

Trust me, you'll want to and should __use comments__.

Comments consist of text that is not processed by the Python interpreter.

Python has two types of comments: __single line__ and __multi-line__.

A single-line comment starts with a `#` or hashtag (also known as a number symbol or octothorp[e]).  For example:

`somefile.py`

```python
# This is a comment and will not be processed

# patient's initial age
age = 99

```

Multi-line comments are triple quotes and must come before and after comment (either `'''` or `"""`) and appear like so:

`otherfile.py`:

```python

'''
This is multi-line
And can continue for a while
or just have one line
'''
```

I introduce comments here because you will start to see them and you shouldn't wonder what or how they are doing what they are doing.

---

### Variables

Almost always you will name the values or data used in your program.  A variable is the name that you attach to a particular object or value.

To declare a variable / name an object, you `assign` it a value with a <u>single</u> equals sign `=`.

For example:

`file_with_a_lot_of_numbers.py`
```python
age = 187
weight = 600
x = 2.34556
```


## Variable Rules

Python gives you a __lot__ of leeway for names, but some things are simply required and some forbidden by the immovable Python interpreter:

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)

## A Fairly Easy Challenge

In the accompanying `main.py` file, a number of variables throw errors.  Hit `Run` and look at the output in the console.  Your job is to correct these so that the program properly prints out all the values:

```python
# how old
 age    =   19

# body fat
w@ight =   499

# some fraction
0_ratio = 3/4

# bmi
bo dy_mass index = 345/3 * 5

# iq
intelli,gence quotient = 129



```


