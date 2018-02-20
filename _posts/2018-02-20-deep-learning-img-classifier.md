---
title: 'Deep Learning Image Classification with Keras and Shiny'
layout: post
tags: [r, rstats, machine-learning, deep-learning, shiny]
social-share: true
---

I have to admit my initial thoughts of deep learning were pessimistic and in order to not succumb to impostor syndrome, I put off learning any new techniques in the growing sub field of machine learning, until recently. After attending & speaking at [Data Day Texas](http://datadaytexas.com/) and listening to Lukas Biewald's Keynote titled: [Deep Learning in the Real World](https://www.slideshare.net/lbiewald/deep-learning-in-the-real-world), I began to see through the complexities of Deep Learning and understand the real world applications. My favorite example from the keynote was [Coca Cola deploying a deep learning model](https://developers.googleblog.com/2017/09/how-machine-learning-with-tensorflow.html) to easily capture under the cap promotional codes. I left the conference with some initial ideas about detecting deer in my backyard using a web cam and running a image classification algorithm as my first step into _learning by doing_. 

For this image classification project I leveraged a pre-trained model from the `R` interface to [Keras](https://keras.rstudio.com/index.html), that had been previously trained on a similar task. This enabled me to prototype something quickly and cheaply in a weekend and wrap the code as an interactive web app with a `shiny` flexdashboard.  Here is the link to the `shiny` app which enables you to upload a image and return the top 3 predicted classes for that image: [https://jasminedumas.shinyapps.io/image_clf/](https://jasminedumas.shinyapps.io/image_clf/) and a preview of the app in action below.


<img src="/post_data/img_clf_app.jpeg" alt="alt text" width="900px" height="600px">




