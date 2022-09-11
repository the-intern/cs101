# Strings - Continued

## Definition

A string is a sequence (ordered) of characters surrounded by either single or double quotes.

```python
'I am a string!'
# or
"I am a string!"

```

Just remember, however, whatever kind of quotation mark **starts** the string must also **end** the string.

When you use which is not always important, but sometimes it determines what you might do within it.

For example, double quotes `""` allows you to include apostrophes (e.g., for contractions or possessives) inside of quotes as a character in the string.

```python
"I'm glad to know ya."

```

In the case of that contraction above, were you to have started the string with single quotes, you would have had to `escape` the apostrophe:

```python
'I\'m glad to know ya.`
```

The backslash `\` just before the apostrophe 'escapes' it, i.e., it is read literally and not interpreted as the end of the string.

## Variables Are Not Strings

Using the interpreter, notice how the color of the input changes before and after you put quotes on
both sides of the string.
What happens when you do not include any quotes:
print Hello
Without the quotes, Python reads Hello as a variable that is undefined:
NameError: name 'Hello' is not defined
As we saw above, Python will not print an undefined variable, which is why we get the name error.
Quiz (Video: Valid Strings)
Which of the following are valid strings in Python?
a. "Ada" b. 'Ada" c. "Ada d. Ada
e. '"Ada'
