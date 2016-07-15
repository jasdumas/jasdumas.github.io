---
layout: post
title: Day Drinking with R
subtitle: My first R package on CRAN, ttbbeer
---

After attending the [useR! 2016 R Conference](http://user2016.org/), I felt supercharged and armed with new insights and ideas about how to further contribute to the R community. I met wonderful people in real life (IRL) from twitter and heard interesting case studies about using R for large data analysis. I already have two R packages on Github but wanted to expereince the detailed (yet rewarding) process of submitting a package to CRAN (Comprehensive Archive R Network). For my first package I had looked to what my interest were and what was needed in the community, which turns out to be *more* analysis-ready datasets about beer. 

**Yes, BEER!** 

Beer analytics is the use and analysis of data to gain insight about breweries, production, operations and its impact. The U.S. Department of Treasury has a voluminous collection of historical data and reports about beer statisitcs as reported by breweries at the National level. In my previous analysis project, about [web scraping craft brewery data in Connecticiut](http://trendct.org/2016/03/18/tutorial-web-scraping-and-mapping-breweries-with-import-io-and-r/), I noticed the minimal amount of data that was available for beer-centric analyses and more interestingly the data that was publicly available on the [data.gov](data.gov) was locked in PDF's or static HTML tables. This problem presented the perfect opportunity for me to contribute a dataset package and learn more about package development.

The process for creating the R package was fairly well documented in the [R Packages book](http://r-pkgs.had.co.nz/) by Hadley Wickham. I also looked for guidance by exaiming existing R dataset packages, like [`janeaustenr`](https://github.com/juliasilge/janeaustenr) by Julia Silge. 

My first submission for review, I made a silly mistake and did not upload my package to [win-builder](http://win-builder.r-project.org/) for checking the source code on a Windows machine - *I will never make that mistake again*. My reviewer, Kurt, was prompt and courteous in informing me that an error arose from a faulty site certificate in a supplied url in my documentation from [https://www.ttb.gov/beer/beer-stats.shtml](https://www.ttb.gov/beer/beer-stats.shtml). After I fixed this error, I re-submitted and was waiting by my email with schoolchild-like wonderment until my acceptance into the nearly 8000 R package community was confirmed. I'm really honored to have taken this important step from just being a consumer of R packages, to a R package developer. The R community has been really great in their feedback via Twitter:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">My first <a href="https://twitter.com/hashtag/rstats?src=hash">#rstats</a> package is now on CRAN - a data set on US Beer Statistics from <a href="https://twitter.com/usdatagov">@usdatagov</a> ! <a href="https://t.co/AnNKqNXYRz">https://t.co/AnNKqNXYRz</a> 😎</p>&mdash; Jasmine Dumas (@jasdumas) <a href="https://twitter.com/jasdumas/status/749636903217995776">July 3, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

______

Here is my first package available on CRAN: [`ttbbeer`](http://cran.us.r-project.org/web/packages/ttbbeer/index.html), which I will continue to update with new "liberated" datasets and use this as an opportunity to increase education and advocate for analysis-ready datasets on open government data portals. Here is the [wiki](https://github.com/jasdumas/ttbbeer/wiki) to follow along on the journey to more Open Beer Data. Cheers :beers:

To install the package type the following:

```r
install.packages("ttbbeer")
library("ttbbeer")
```

Or you can install the development version from Github:

```r
library(devtools)
install_github("jasdumas/ttbbeer")
library(ttbbeer)
```
