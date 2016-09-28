---
layout: post
title: Adding Tags to your beautiful-jekyll site
tags: [website, design, beautiful-jekyll]
---


There are a lot of [inquires](http://pavdmyt.com/how-to-implement-tags-at-jekyll-website/) and [posts](http://charliepark.org/tags-in-jekyll/) to add tags to jekyll-powered blogs on GitHub. Here is a step-by-side guide on how to add a tag in order to creates a designated XML feed, necessary if you want to list your blog aggregators and sites such as [R-bloggers](https://www.r-bloggers.com/). Some features are extra to add social share buttons the the bottom of the page.

* Create a file called [**share-section.html**](https://github.com/jasdumas/jasdumas.github.io/commit/ed3a57afefade4f4f9cb3b5a07131d7c242115ab) in the "includes" folder.

* Edit the css file [**main.css**](https://github.com/jasdumas/jasdumas.github.io/commit/0ca9565367b599b2dab52063330589b317eaecfa) with the following code above the /*--- Pager ---*/ section label.

* Edit the existing [**feed.xml**](https://github.com/jasdumas/jasdumas.github.io/commit/83e0f736fce52aae3579d80bb538a1069d206c29) file which lives in the root folder of the GitHub repo.

* Create a file called [**r-bloggers-feed.xml**](https://github.com/jasdumas/jasdumas.github.io/commit/e87046a8b50ce06850b44ecf7273fa5d8b95d9cd) in the root folder of the GitHub repo.

* Edit your [**existing posts**](https://github.com/jasdumas/jasdumas.github.io/commit/a5f94ab9118b3af1bde8d01fc331b9445c2ce08a) and add the tags line in the **yaml** header.

* Congrats! - check out your newly rendered blog posts with the social share buttons at the bottom and the new tags created. Visit your new XML feed by going to the page, for example: [jasdumas.github.io/r-bloggers-feed.xml](http://jasdumas.github.io/r-bloggers-feed.xml) - it will have a collection of your tagged post ready to submit to a blog roll.
