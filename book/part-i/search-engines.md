```{admonition} You Are Here

I want to know what good is a web search engine that returns 324,909,188 ‘matches’ to my keyword.  That’s like saying, _Good news, we’ve located the product you’re looking for. It’s on Earth._

> __W. Bruce Cameron__

```

# Building a Search Engine

We all know the basic purpose and use of an internet search engine.  But can we build our own, even if rudimentary?

We can.  It won't compete with Google's or DuckDuckGo.  But we can, with some Python, build out an engine that uses the first implementation of the Google search engine circa 1998.

We'll roughly follow the recipe laid out by Larry Page and Sergey Brin in their 1998 paper [The PageRank Citation Ranking: Bringing Order to the Web](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf)

Using a simple form of _PageRank_, we'll:

- build a crawler, i.e., a program that, using a _starter page_ will go from page to page following anchor tags (a.k.a., links) to find related pages
- build an index, i.e., creating a database of the documents or pages found and mapping content to their _urls_
- use that index, find pages - ranked by relevance - to any given search query

```{figure} ../images/part-i/searchengine.png
:height: 250px
:name: SEParts

The 3 steps to building a search engine
```
