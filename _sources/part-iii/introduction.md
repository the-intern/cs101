# Introduction

In the prior section we wrote some code to extract a single link from a web page.

Some things to note about what we did:

1.  It was a simple number of steps, three or four at most.
2.  We used but two processes given us by Python itself, i.e., the string's `find()` method and the string's `slicing` operation.
3.  We assumed a link was on the page.
4.  The page was really just a snippet.
5.  We were only looking for the very first link on the 'page' and ignored anything beyond it.
6.  Perhaps most importantly, however, **_this is how you begin any project, no matter its ultimate complexity_**. That is, simply and taking but _one_ step at a time.

```{danger} Don't be fooled into thinking vast software projects and their programs are achieved in any other way but __one simple step__ at a time.

```

## We are on to our next single step towards building a search engine

In this unit we will extract **all** links from a full web page and, perhaps, from a various number of like pages.

But, in order to accomplish that, we have some prerequisites:

1. Be able to write (i.e., **_implement_**) and call on our very own custom **_procedures_**; and
2. Be able to **_control_** our program in such a way that, depending on the data (e.g., how many links on a page), the program will operate appropriately

Procedures will package code so it can be reused with different inputs.

Control will allow us to manage the program's _state_, instead of just executing instructions one after the other.
