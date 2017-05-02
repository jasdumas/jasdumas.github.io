---
title: 'Extracting data from Twitter for #machinelearningflashcards'
layout: post
tags: [rstats, r, image-processing, machine-learning]
output: 
  html_document: 
    self_contained: no
---



I'm a fan of [Chris Albon](https://chrisalbon.com/)'s recent project [#machinelearningflashcards](https://twitter.com/hashtag/machinelearningflashcards?src=hash) on Twitter where generalized topics and methodologies are drawn out with key takeaways. It's a great approach to sharing concepts about machine learning for everyone and a timely refresher for those of us who frequently forget algorithm basics.

I leveraged [Maëlle Salmon](https://github.com/maelle)'s recent blog post on the [*Faces of #rstats Twitter*](http://www.masalmon.eu/2017/03/19/facesofr/) heavily as a tutorial for this attempt at extracting data from Twitter to download the #Machinelearningflashcards.

Source Repo for this work: [jasdumas/ml-flashcards](https://github.com/jasdumas/ml-flashcards)


## Directions

- Load libraries:

For this project I used `rtweet` to connect the Twitter API to search for relevant tweets by the hash tag, `dplyr` to filter and pipe things, `stringr` to clean up the tweet description, and `magick` to process the images. 

Note: I previously ran into trouble when downloading [*ImageMagick*](https://www.imagemagick.org/script/index.php) and detailed the errors and approaches, if you fall into the same trap I did: [https://gist.github.com/jasdumas/29caf5a9ce0104aa6bf14183ee1e3cd8](https://gist.github.com/jasdumas/29caf5a9ce0104aa6bf14183ee1e3cd8)

```r
library(rtweet)
library(dplyr)
library(magick)
library(stringr)
```

- Get tweets for the hash tag and only curated tweets for Chris Albon's work: 

```r
ml_tweets <- search_tweets("#machinelearningflashcards", n = 500, include_rts = FALSE) %>% filter(screen_name == 'chrisalbon')
```


```r
head(ml_tweets)
```

```
##   screen_name  user_id          created_at          status_id
## 1  chrisalbon 11518572 2017-05-02 16:32:20 859445463316963328
## 2  chrisalbon 11518572 2017-05-01 22:19:26 859170425921650689
## 3  chrisalbon 11518572 2017-05-01 22:11:26 859168412555132928
## 4  chrisalbon 11518572 2017-05-01 20:23:49 859141329879580672
## 5  chrisalbon 11518572 2017-04-28 21:07:10 858065073167777792
## 6  chrisalbon 11518572 2017-04-28 15:33:57 857981218754764800
##                                                                                   text
## 1 Chi-squared For Feature Selection #machinelearningflashcards https://t.co/Pxxa7NDYUS
## 2   Fundamental Theorem Of Calculus #machinelearningflashcards https://t.co/0aOJMYqVFM
## 3      Why is nearest neighbor lazy #machinelearningflashcards https://t.co/vvqX39oGks
## 4         Precision Recall Tradeoff #machinelearningflashcards https://t.co/rKT1d3gD1V
## 5      Singular Value Decomposition #machinelearningflashcards https://t.co/Sahq7AWqQR
## 6         How to avoid overfitting. #machinelearningflashcards https://t.co/uUnUG7Xljv
##   retweet_count favorite_count is_quote_status quote_status_id is_retweet
## 1             1             11           FALSE            <NA>      FALSE
## 2             3              6           FALSE            <NA>      FALSE
## 3             3             10           FALSE            <NA>      FALSE
## 4             6             25           FALSE            <NA>      FALSE
## 5             4             20           FALSE            <NA>      FALSE
## 6            45             83           FALSE            <NA>      FALSE
##   retweet_status_id in_reply_to_status_status_id
## 1              <NA>                         <NA>
## 2              <NA>                         <NA>
## 3              <NA>                         <NA>
## 4              <NA>                         <NA>
## 5              <NA>                         <NA>
## 6              <NA>                         <NA>
##   in_reply_to_status_user_id in_reply_to_status_screen_name lang
## 1                       <NA>                           <NA>   en
## 2                       <NA>                           <NA>   en
## 3                       <NA>                           <NA>   en
## 4                       <NA>                           <NA>   en
## 5                       <NA>                           <NA>   es
## 6                       <NA>                           <NA>   en
##                        source           media_id
## 1 Machine Learning Flashcards 859445461152800768
## 2 Machine Learning Flashcards 859170424256512000
## 3 Machine Learning Flashcards 859168410713808896
## 4 Machine Learning Flashcards 859141327270821888
## 5             Twitter for Mac 858065067903823872
## 6             Twitter for Mac 857981212857516032
##                                        media_url
## 1 http://pbs.twimg.com/media/C-1dF-fVoAAAHR0.jpg
## 2 http://pbs.twimg.com/media/C-xi8uNUwAAKBFx.jpg
## 3 http://pbs.twimg.com/media/C-xhHhLVYAAXUBP.jpg
## 4 http://pbs.twimg.com/media/C-xIfDfVwAA4xmm.jpg
## 5 http://pbs.twimg.com/media/C-h1og6UMAA7oCY.jpg
## 6 http://pbs.twimg.com/media/C-gpXghUwAAXB19.jpg
##                                                 media_url_expanded urls
## 1 https://twitter.com/chrisalbon/status/859445463316963328/photo/1 <NA>
## 2 https://twitter.com/chrisalbon/status/859170425921650689/photo/1 <NA>
## 3 https://twitter.com/chrisalbon/status/859168412555132928/photo/1 <NA>
## 4 https://twitter.com/chrisalbon/status/859141329879580672/photo/1 <NA>
## 5 https://twitter.com/chrisalbon/status/858065073167777792/photo/1 <NA>
## 6 https://twitter.com/chrisalbon/status/857981218754764800/photo/1 <NA>
##   urls_display urls_expanded mentions_screen_name mentions_user_id symbols
## 1         <NA>          <NA>                 <NA>             <NA>      NA
## 2         <NA>          <NA>                 <NA>             <NA>      NA
## 3         <NA>          <NA>                 <NA>             <NA>      NA
## 4         <NA>          <NA>                 <NA>             <NA>      NA
## 5         <NA>          <NA>                 <NA>             <NA>      NA
## 6         <NA>          <NA>                 <NA>             <NA>      NA
##                    hashtags coordinates place_id place_type place_name
## 1 machinelearningflashcards          NA       NA         NA         NA
## 2 machinelearningflashcards          NA       NA         NA         NA
## 3 machinelearningflashcards          NA       NA         NA         NA
## 4 machinelearningflashcards          NA       NA         NA         NA
## 5 machinelearningflashcards          NA       NA         NA         NA
## 6 machinelearningflashcards          NA       NA         NA         NA
##   place_full_name country_code country bounding_box_coordinates
## 1              NA           NA      NA                       NA
## 2              NA           NA      NA                       NA
## 3              NA           NA      NA                       NA
## 4              NA           NA      NA                       NA
## 5              NA           NA      NA                       NA
## 6              NA           NA      NA                       NA
##   bounding_box_type
## 1                NA
## 2                NA
## 3                NA
## 4                NA
## 5                NA
## 6                NA
```

- Get text within the tweet to add to the file name by removing the hash tag and URL link: 

```r
ml_tweets$clean_text <- ml_tweets$text
ml_tweets$clean_text <- str_replace(ml_tweets$clean_text,"#[a-zA-Z0-9]{1,}", "") # remove the hashtag
ml_tweets$clean_text <- str_replace(ml_tweets$clean_text, " ?(f|ht)(tp)(s?)(://)(.*)[.|/](.*)", "") # remove the url link
ml_tweets$clean_text <- str_replace(ml_tweets$clean_text, "[[:punct:]]", "") # remove punctuation
```

- Download images of the flashcards from the `media_url` column and append the file name from the cleaned tweet text description and save into a folder:

```r
save_image <- function(df){
  for (i in c(1:nrow(df))){
    image <- try(image_read(df$media_url[i]), silent = F)
  if(class(image)[1] != "try-error"){
    image %>%
      image_scale("1200x700") %>%
      image_write(paste0("data/", ml_tweets$clean_text[i],".jpg"))
  }
 
  }
   cat("Function complete...\n")
}
```

- Apply the function:

```r
save_image(ml_tweets)
```


At the end of this process you can view all of the #machinelearningflashcards in one place! Thanks to Chris Albon for his work on this, and I'm looking forward to re-running this script to gain additional knowledge from new #machinelearningflashcards that are developed in the future! 


