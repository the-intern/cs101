---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# Quiz III

A hidden cell

```{code-cell} ipython
:tags: ["hide-input"]
print("This is a test.")
```


Now for a quiz

```{code-cell} ipython
:tags: ["hide-input"]

import requests
import json
import base64
from jupyterquiz import display_quiz

git_path = "https://raw.githubusercontent.com/the-intern/cs101-questions/main/questions/01/have-you-created-a-replit-account"
data = requests.get(git_path).text
data = bytes(data, 'utf-8')
decoded_contents = base64.b64decode(data)
json_object_from_strings = json.loads(decoded_contents)
display_quiz(json_object_from_strings)

```

Try to hide cell completely:

```{code-cell} ipython
:tags: ["hide-cell"]
print("This is a test.")
```