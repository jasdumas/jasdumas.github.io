My Experience at the 2017 rOpenSci Unconference
================

### Networking & Connecting

This was my first time at the annual rOpenSci Unconference event held in Los Angeles, CA and incidentally my first time in the city. I was excited at the onset, from getting the invite email, to closely watching the project proposals pitched during the lead up to the event. I had felt slightly anxious to meet so many useRs that I had only really engaged with on Twitter, but a far cry from the how nervous I felt when attending the international useR conference in Stanford, CA last Summer. My nerves were calmed after the interesting icebreaker on the first day where I got to group up with the attendees based on animal preference (*\#rdogladies & \#rpuppies obviously!*), learning styles, and thoughts on my personal role within R community (**tl;dr: I'm [one of many folks](link%20to%20oliver's%20tweet) suffering from imposter syndrome regardless of my participation as Co-organizer of R-Ladies CT, and Core Member & Survey Lead of [Forwards]()**).

In the beginning, I did not feel as productive and was really bogged down with the notion of other groups bountiful commits and producing a full-fledged R package in less than 20 hours. I got some sage advice form the community manager, Stephanie Butland about taking mental breaks and developing a smaller my project scope. I also appreciated the breaks to de-stress from the social interaction during dinner on the first night which enabled me to achieve some progress on my project in a secluded setting that I was familiar with 🎧.

Overall, I had a fantastic time getting out of my comfort zone and meeting new people and felt really connected by the end of the event, which culminated in **rounds of hugs, handshakes and beers!** 🍺.

### New Learnings

I learned some new things from working alongside all the other attendees about new packages (`V8`), old packages (`htmlwidgets`), [RStudio Git workflows](), and [Travis CI Cron jobs]() that will indefinitely improve my R programming. I was also grateful to be surrounded by more experienced R programmers to ask questions of and get feedback on approaches.

A great example of this collaboration was when I encountered roadblocks in generating an [htmlwidget]() which I have unsuccessfully tried before. My question was answered by posting on the \#unconf17 slack group and being pointed to several folks in attendance at the event who gave me advice on not using `htmlwidgets` to wrap a non-data visualization JavaScript library as it's only for JS libraries that need to draw a square on a screen as [Joe Cheng]() explained and then referred to [Jeron Ooms's]() new package called `V8` which bundles npm JS libraries for standalone use in R packages. A question and answer feedback cycle like this would have taken days and I probably would have gotten discouraged enough to not complete the project had I been at home developing R packages as usual.

### Collaboration

I initially grouped up with the quantified city group which consisted of [Ben Best](), [Chelsea Ursaner](), [Reka Solymosi]() and [Tim Phan]() and decided on creating a template framework for open data from the web and social media as a variable health index to be extended to other cities. We chatted alot during the event and used our time together for knowledge sharing however I began to pivot to the original project I proposed as I believed it would help me out with enhanced authoring of [Knowledge](link%20to%20airbnb%20knowledge%20repo) posts in RMarkdown at work 😄.

I worked with two remote participants [Ben Marwick]() & [Gordon Shotwell]() on **The Grammar of Grammar: [`gramr`](https://ropenscilabs.github.io/gramr/) package**, which is aimed at **helping R programmers who can't write good but still want to learn how to do other stuff good by checking for grammatical errors (and style choices like cliches and weasel words) in RMarkdown documents**. We developed three functions by wrapping the *native linter for english prose*, [`write-good`](https://github.com/btford/write-good) which aligned with common writing workflows for writing in RMarkdown:

1.  **In-progress work** (A RStudio Addin^ button for unsaved `Untitled` files)

2.  **Existing Rmd Documents** (A function that takes the file path as the argument)

3.  **Interactively editing a document** (A Shiny application which steps through sentences and replaces grammatical error suggestions)

**More about the development process and function usage can be read in the [Blog post](https://ropenscilabs.github.io/gramr/BLOG.Rmd)**
