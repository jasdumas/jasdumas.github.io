---
layout: post
title: Best Practices for Shiny Development
subtitle: debugging, reactivity, and designing for the user
tags: [rstats, r, r-bloggers, shiny]
---

### Introduction

> As a programmer you read more code than you write. Keep it readable, commented, consistent and explicit. –Sindre Sorhus, Web Developer & Creator of Pageras

*Shiny* is a powerful and popular web framework for R programmers to elevate the way people consume analytics for both technical and non-technical decision makers. Shiny is used in many organizations from start-ups to top-trafficked web sites like [Wikipedia](http://Wikipedia.org). Now that Statisticians and researchers are armed with the skills to build these advanced web applications there are many opportunities to produce agile and user friendly software. This best practice guide outlines some areas (that I have grown to personally use as I've developed Shiny applications) that make for an enjoyable coding experience and successful deployment of applications that will actively engage users to use the application the right way.

### Be kind to your future self with version control & helpful comments

![](http://i.giphy.com/SfMfMAgvL6G1W.gif)

* Use *any* type of version control you feel comfortable with. This is a software development practice and in general a good idea if you don't want to anger your future self. I use Git and Github and recommend them as the go-to collaborative interface as the the R community is vibrant on github.

* It also helps to document your process with comments that are insightful and describe why you choose a certain process over another. If I find a helpful method from the ever omniscient [Stackoverflow](http://stackoverflow.com/search?q=shiny) I always include the link of the answer in the code as a comment as a reminder of where the idea originated. R and Shiny are open source but it's always nice to give credit where credit is due.

### Finding the bug in debugging and knowing what part of your code went awry

* `cat()`: This is useful for producing and printing output within reactives, to inform *you* the developer of which reactive has ran, especially if you are concerned about order. As practice I like to include a line similar to this: `cat('In plot_reactive...\n')`.

* `print()`: Print statements are a good way of producing output that has been created by the reactives or output render* functions. Even printing the intermediary steps of a process that are populating a visualization is a useful verification of correct calculations for your desired outcome.

* `traceback()`: This prints the call stack of the last uncaught error, i.e., the sequence of calls that lead to the error. This is useful when an error occurs with an unidentifiable (or cryptic) error message. Since your Shiny application will have **inputs with lead to reactives which lead to render* outputs**, the source of errors in code can be challenging to pin-point. The traceback helps guide you through the potential mistakes in the scripts.

### "Know the difference between telling Shiny to do something, and telling Shiny how to do something with reactive functions" - Joe Cheng CTO at RStudio

* Render* output objects: Just as you specify `output$foo <- renderText({ print("hi")})` keep these function free of computation and only use them as a way to return the "side effect" or the recipe to build the output. It is preferable in using reactive expressions to model calculations, over using observers to set (reactive) variables. See Joe Cheng's slide deck from the Shiny Developer Conference:  [Slides](https://cdn.rawgit.com/rstudio/reactivity-tutorial/master/slides.html#/warm-up-side-effects)

* Naming conventions: Its a good idea to adhere to a style guide about file structure and R programming but it can be dutifully useful to develop a coding style in variable naming to assist with collaborators and to prevent constant scrolling up to the top of the script when you forget what you named that reactive value. For example add `_reactive` to the end of the names of my reactive functions or `_plot` if that reactive creates data to be plotted in a `render*()` function. Those simple changes improves readability of your script. I also use lowercase names rather than uppercase in the ui.R file.

### Try not to drag down your server

* Scope: Make sure to understand the potential usage of the Shiny application and how it loads and interacts with data. If you have a large dataset that you don't want loaded or read each time a new user visits the app put it outside (above) of the `shinyServer()` function (i.e. save on RAM computation by having the object available across all or multiple sessions). Read this article for additional wise words from the Rstudio team. <http://shiny.rstudio.com/articles/scoping.html>

### UX design concepts for Statisticians

> You don’t have to change who you are, you have to be more of who you are. – Sally Hogshead, New York Times bestselling author

The Statistical community revels in big data and analytics and are now skilled in approaches to developing web applications on top of your models to generate digestible insights to business partners and customers. I'm not suggesting that everyone be an expert on user experience design (because trust me I'm not), but a little goes a long way.

Here are some quick tips that will be 'easy' wins that can transform a statistical tool into a software tool.

* Always include [progress bars](http://shiny.rstudio.com/articles/progress.html): Imagine waiting up to a minute for a page on Twitter to load without any prompt - I would probably leave the application and tell everyone that Twitter sucks (obviously this is just an example and Twitter is fabulous!). With Shiny potentially loading large datasets, its critical to inform the user of background processes so that they don't leave the application with a negative experience.

* Always include a landing or home page: Inform your users to the usage of the application (i.e. an explanation of the equation or method be used) & details on data quality (i.e. last data refresh date), legal or proprietary messages. The page will be the first impression the user will get and it should exude professionalism, and hospitality. I'm personally make great use of the `HTML()` function to include additional [Bootstrap components](http://getbootstrap.com/components/) such as the [Jumbotron](http://getbootstrap.com/components/#jumbotron) to include a bold welcome message and in the 'Learn More' button, a link to a instructional video (that feature works only on Google Chrome once the application has been deployed).

* Appearance: If you didn't know that Shiny uses the Bootstrap Framework (from the above bullet point) for its UI, here is your message: **SHINY uses Bootstrap for its underlying UI**. So feel free to get creative with color by using setting the `theme = 'http://bootswatch.com/readable/bootstrap.css'` or any of the templates from <http://bootswatch.com/> in the `shinyUI()` function. For the true front-end nerds, you can also set up your own **CSS** file and mock up any theme you like, just as long as its included in the /www folder of your application.

![](http://i.giphy.com/yYSSBtDgbbRzq.gif)

* Always include an about page: Be proud of your work and include a small biography of the application developers and also a way for users to contact (or blame) the application maintainers with an email address.

* ...and I recommend reading this article [Signifiers, not affordances](http://jnd.org/dn.mss/signifiers_not_affordances.html) and this book [The Design of Everyday Things](http://jnd.org/books.html#doet) from Don Norman, if you want to better equip yourself with the tools and thought-process to design things for people. Also there is a [udacity course](https://www.udacity.com/course/intro-to-the-design-of-everyday-things--design101) for it as well

Happy Coding!
