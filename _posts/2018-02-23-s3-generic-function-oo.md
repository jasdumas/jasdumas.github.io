---
title: "R's S3 generic-function object-oriented system"
subtitle: "Just like your mom's chippity chipper recipe"
layout: post
tags: [r, rstats, python, programming]
social-share: true
bigimg: /post_data/cookies.jpg
---


In Data Science, there are numerous instances where different techniques call for the use of different tools. For me, this means hopping between R and python on a weekly basis. I've been fortunate enough to have taken formal courses in python & R in the last few years and just by circumstances have chosen R as my primary language in my data science toolkit. This usually equates to a real mental struggle when jumping into a Jupyter Notebook and making trivial mistakes in the first 15 minutes, like below.

![](/post_data/python-mess.jpeg)


I don't have any tricks yet, aside from a set of data analysis starter notebooks to quell the initial confusion, but I have noticed when I mentor other Data Scientists (those who have R skills and are now learning python or vice versa) and participate in pair-programming, I often drift to explaining the differences between R's generic-function OO and python (and a many other languages) message-passing OO as a means of remembering how to structure functions. I'm only knowledgeable about explaining this differences from printing out and bookmarking Hadley Wickham's [OO Field Guide chapter](http://adv-r.had.co.nz/OO-essentials.html) in the [Advanced R](http://adv-r.had.co.nz/) book! Don't be worried by the title of being too 'Advanced', if you are interested in learning more about the _why_ of certain things in R, it's a great resource.

With the first few paragraphs of the field guide outlining some examples of the different systems, I wanted to dig in a bit further and learn more about the **generic-function object-oriented system** that I could use to explain to others and hopefully help me remember.

### What is a generic function?

According to Wikipedia:
> a [generic function](https://en.wikipedia.org/wiki/Generic_function) is a function defined for [polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))  which is the provision of a single interface to entities of different types.


Wow, that's a mouthful but essentially meaning that the function decides which method to call on different types of classes. Imagine the generic function as a recipe for cookies and the common steps include mixing, baking, and cooling and some different methods for specific types! 🍪 Ultimately the cookies you make are dictated by what type of ingredients you include.

| Generic Function (recipe)                                                                                                                                      | Method (finishing)                     | Class (ingredient)   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|----------------------|
| [Cookies](http://allrecipes.com/recipe/10275/classic-peanut-butter-cookies/)                                                                                   | Make criss-cross pattern               | smooth peanut butter |
| [Cookies](https://www.tasteofhome.com/recipes/buttery-almond-cookies)                                                                                          | Roll in remaining confectioners' sugar | chopped almonds      |
| [Cookies](http://allrecipes.com/recipe/9668/gingerbread-men/?internalSource=streams&referringId=14712&referringContentType=recipe%20hub&clickId=st_trending_s) | Decorate with frosting                 | ground ginger        |


### Further Reading

- [genericFunction-class {methods}](https://stat.ethz.ch/R-manual/R-devel/library/methods/html/genericFunction-class.html)
- [Generic functions and methods](http://www.hep.by/gnu/r-patched/r-exts/R-exts_152.html)
- [Methods](https://www.rdocumentation.org/packages/methods/versions/3.3.1/topics/Methods)
- [Developments in Class Inheritance and Method Selection](https://statweb.stanford.edu/~jmc4/classInheritance.pdf)
- [History of S & R](https://www.r-project.org/conferences/useR-2006/Slides/Chambers.pdf)
- [Tidbits from the Books that Defined S (and R)](https://www.r-bloggers.com/tidbits-from-the-books-that-defined-s-and-r/)
- [Chippity Chippers Recipe](http://www.kraftrecipes.com/member-recipe/chippity-chippers-87857.aspx)
