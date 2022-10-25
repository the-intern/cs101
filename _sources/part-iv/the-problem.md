# The Problem

We've already used one data structure, the string.

But as data structures go, it's a bit difficult to deal with. For example, you cannot insert new characters or sub-strings into an existing string; you can't update a character in a string; and it holds but one data `type` --- a single-character string.

```{note}

That sounds odd, but that's an accident arising from how Python defines a string. Other, statically-typed languages have a `char` data type in addition to an array of `chars` called `strings`. But more on that maybe later.

```

That's all to say that strings are a bit unwieldy for more advanced application of data structures. That's not to say strings aren't ubiquitous and important; just that, as data structures, they can be quite limiting.

## Enter Python's `list`

The workhorse of data structures in Python is the `list`. It's quite versatile and, when compared to other data structures, quite easy to use. It does have limits, but for many, if not most, use cases, the list is all you need.

By definition `lists` are mutable sequences can store any data type --- integers, floats, booleans, strings, etc. In fact, they can hold other lists.

The Python docs maintain that lists are "used to store collections of homogeneous items," but, within any given list, you can put all data types.

## Syntax ... 👉
