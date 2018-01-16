---
layout: post
title: "Extracting data from Twitter for @hrbrmstr's #nom foodie images"
output: 
  html_document: 
    self_contained: no
tags: [rstats, r, r-bloggers, tutorial, food]
---





[Bob Rudis](https://rud.is/) (@hrbrmstr) is a famed expert, author and developer in Data Security and the Chief Security Data Scientist at Rapid7. Bob also creates the most deliciously vivid images of his meals documented by the #nom hashtag. I'm going to use a similar method used in my previous projects ([Hipster Veggies](https://github.com/jasdumas/hipster-veggies) & [Machine Learning Flashcards](https://jasdumas.github.io/2017-05-02-twitter-ml-flashcards/)) to wrangle all those images into a nice collection - mostly for me to look at for inspiration in recipe planning.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Yum! Have you ever thought about collecting all these recipes &amp; images into a cookbook?!</p>&mdash; Jasmine Dumas (@jasdumas) <a href="https://twitter.com/jasdumas/status/952971103990898689?ref_src=twsrc%5Etfw">January 15, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Source Repository: [jasdumas/bobs-noms](https://github.com/jasdumas/bobs-noms)

## Analysis


```r
library(rtweet) # devtools::install_github("mkearney/rtweet")
library(tidyverse)
library(dplyr)
library(stringr)
library(magick)
library(knitr)
library(kableExtra)
```



```r
# get all of bob's recent tweets
bobs_tweets <- get_timeline(user = "hrbrmstr", n = 3200)

#filter noms with images only
bobs_noms <- 
  bobs_tweets %>% dplyr::filter(str_detect(hashtags, "nom"), !is.na(media_url))
```



```r
bobs_noms$clean_text <- bobs_noms$text
bobs_noms$clean_text <- str_replace(bobs_noms$clean_text,"#[a-zA-Z0-9]{1,}", "") # remove the hashtag
bobs_noms$clean_text <- str_replace(bobs_noms$clean_text, " ?(f|ht)(tp)(s?)(://)(.*)[.|/](.*)", "") # remove the url link
bobs_noms$clean_text <- str_replace(bobs_noms$clean_text, "[[:punct:]]", "") # remove punctuation
```



```r
# let's look at these images in a smaller data set
bobs_noms_small <- bobs_noms %>% select(created_at, clean_text, media_url)

bobs_noms_small$img_md <- paste0("<img src='",bobs_noms_small$media_url, "' alt='",bobs_noms_small$clean_text ,"' width='600' height='400'>")
```


```r
data.frame(images = bobs_noms_small$img_md)
```

```
##                                                                                                                                                                                               images
## 1             <img src='http://pbs.twimg.com/media/DTmdeptVoAAZYpp.jpg' alt='Moroccaninspired lamb meatballs prepped. Naan dough is kneading. Going to be a  sup tonight.' width='600' height='400'>
## 2                                                                               <img src='http://pbs.twimg.com/media/DTTF55oX0AMyyVL.jpg' alt='Tsukune with tare tonight ' width='600' height='400'>
## 3                                                                       <img src='http://pbs.twimg.com/media/DS4_fRFU0AA3LVL.jpg' alt='Lamb roast isnt too shabby either ' width='600' height='400'>
## 4                                                                <img src='http://pbs.twimg.com/media/DS48BemVAAAN38J.jpg' alt='The pain de mie thankfully came out well ' width='600' height='400'>
## 5  <img src='http://pbs.twimg.com/media/DR7j-HMV4AAzXpH.jpg' alt='Sage rosemary &amp; espresso infused salt rubbed roast lamb. Goose fat roasted potatoes _almost _ done ' width='600' height='400'>
## 6                                                                                                         <img src='http://pbs.twimg.com/media/DQDDt9qXcAAg_Hb.jpg' alt='' width='600' height='400'>
## 7                                                                          <img src='http://pbs.twimg.com/media/DPfXiVBXkAAkKAK.jpg' alt='Ham amp; turkey frittata time! ' width='600' height='400'>
## 8                                                                                              <img src='http://pbs.twimg.com/media/DO34I4oXkAEvmDS.jpg' alt='Postconfit ' width='600' height='400'>
## 9                                                                                                 <img src='http://pbs.twimg.com/media/DO32TmIX0AAmkT7.jpg' alt='PostPBC ' width='600' height='400'>
## 10                                                                                                        <img src='http://pbs.twimg.com/media/DO2xnqcXcAAGBZO.jpg' alt='' width='600' height='400'>
## 11                          <img src='http://pbs.twimg.com/media/DO2D1HQVwAEZQzk.jpg' alt=' is home\n#2's Wedding Sunday.\n20 ppl over tonight for \U0001f983\n#joy\n#nom' width='600' height='400'>
## 12                                                    <img src='http://pbs.twimg.com/media/DNVuMHWWkAI4biV.jpg' alt='Definitely an Indonesian spring rolls kind of night ' width='600' height='400'>
## 13                                      <img src='http://pbs.twimg.com/media/DNBMw2NWAAEwGft.jpg' alt='Homemade breadsticks for the homemade pasta and meatballs tonight ' width='600' height='400'>
## 14                                                                                                        <img src='http://pbs.twimg.com/media/DM8GWXYXcAEAFkJ.jpg' alt='' width='600' height='400'>
## 15                                                                           <img src='http://pbs.twimg.com/media/DMniz1TX0AAboZw.jpg' alt='Bonein PBC smoked pork roast ' width='600' height='400'>
## 16                                <img src='http://pbs.twimg.com/media/DMlFfC0X0AAPuVf.jpg' alt='Prosciutto de Parma Cacio di Bosco &amp; spinach omelettes this morning ' width='600' height='400'>
## 17                                                 <img src='http://pbs.twimg.com/media/DMDWHUdX4AEJF5r.jpg' alt='Our Friday night is shaping up well How’s yours going? ' width='600' height='400'>
## 18                                                                     <img src='http://pbs.twimg.com/media/DLz-HotX4AEVVY1.jpg' alt='Pork tenderloin on the PBC tonight ' width='600' height='400'>
## 19   <img src='http://pbs.twimg.com/media/DK-fDgRWkAAGuhe.jpg' alt='Overnight nutmeg-infused yeast waffles with sautéd local picked Maine apples &amp; Maine maple syrup ' width='600' height='400'>
```


```r
# create a function to save these images!
save_image <- function(df){
  for (i in c(1:nrow(df))){
    image <- try(image_read(df$media_url[[i]]), silent = F)
  if(class(image)[1] != "try-error"){
    image %>%
      image_scale("1200x700") %>%
      image_write(paste0("../post_data/data/", bobs_noms$clean_text[i],".jpg"))
  }
 
  }
   cat("saved images...\n")
}

save_image(bobs_noms)
```

```
## saved images...
```
