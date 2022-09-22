# Try It Yourself

Applying the same methodology for extracting a hextet, we can extract the url from an html anchor tag. The steps can be enumerated:

- use `find()` to identify the index location of the first tag on the page - using as an argument to `find()` the string `<a href=`
- by the same method, find the quote `"` mark's index position
- then the second quote mark
- extract the url from between those two quote marks.

```python

# our data
page = """
    <h1>Lorem ipsum dolor sit amet.</h1>
    <ul>
      <li>
        <a href="https://brave.com">Search</a>
      </li>
      <li><a href="https://docs.python.org/3">Python docs</a></li>
    </ul>
"""

# find the first import index value
start_link = None
# find the first quote mark
start_quote = None
# find the final quote mark that comes just before the end of the url
end_quote = None

# now we use string slicing for extraction
url = None

```

You can try it here:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/caterinadiacomo/caterina-man-made-code/part-ii-strings?labpath=src%2Fpart-ii-strings%2F07-try-it-yourself.ipynb)
