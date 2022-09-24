# Modules in Python

Before getting too far afield, it's import to understand Python modules. They really quite simple: they are Python files --- files that end in `.py` and available to your program.

In fact, any time you create a new Python (`.py`) file alongside your `main.py` file, you've created a `module` from which you can `import` procedures or variables or whatever. Take a quick look [at the Python docs](https://docs.python.org/3/tutorial/modules.html#modules) for more. Note this excerpt:

```{admonition} Modules in Python

Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

```

Best to see an simple example. Below are two files: the `main.py` file and some Python module called `myhelpers.py`.

`main.py` makes use of what is in the other file by importing it as a module, e.g.,

![modules](images/modules.png)

`````{note}

1. The file into which you are importing a module ___need not be named `main.py`___

2. The import example above assumes the files are in the same directory or folder --- i.e., alongside each other --- like so:

````bash

some-directory/
├── main.py
└── myhelpers.py

````

`````
