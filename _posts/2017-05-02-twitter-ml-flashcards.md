---
title: 'Extracting data from Twitter for #machinelearningflashcards'
subtitle: 'A tutorial for machine learning - learning'
layout: post
tags: [rstats, r, image-processing, ml, tutorial, data-science, data-analysis]
output: 
  html_document: 
    self_contained: no
bigimg: /post_data/data/ConfusionMatrix.jpg
---



I'm a fan of [Chris Albon](https://chrisalbon.com/)'s recent project [#machinelearningflashcards](https://twitter.com/hashtag/machinelearningflashcards?src=hash) on Twitter where generalized topics and methodologies are drawn out with key takeaways. It's a great approach to sharing concepts about machine learning for everyone and a timely refresher for those of us who frequently forget algorithm basics.

I leveraged [Maëlle Salmon](https://github.com/maelle)'s recent blog post on the [*Faces of #rstats Twitter*](http://www.masalmon.eu/2017/03/19/facesofr/) heavily as a tutorial for this attempt at extracting data from Twitter to download the #machinelearningflashcards.

Source Repo for this work: [jasdumas/ml-flashcards](https://github.com/jasdumas/ml-flashcards)

___

## Directions

#### 1. Load libraries:

For this project I used `rtweet` to connect the Twitter API to search for relevant tweets by the hash tag, `dplyr` to filter and pipe things, `stringr` to clean up the tweet description, and `magick` to process the images. 

*Note*: I previously ran into trouble when downloading [*ImageMagick*](https://www.imagemagick.org/script/index.php) and detailed the errors and approaches, if you fall into the same trap I did: [How to install imagemagick on MacOS](https://gist.github.com/jasdumas/29caf5a9ce0104aa6bf14183ee1e3cd8)

```r
library(rtweet)
library(dplyr)
library(magick)
library(stringr)
library(kableExtra)
library(knitr)
```

#### 2. Get tweets for the hash tag and only curated tweets for Chris Albon's work: 

```r
ml_tweets <- search_tweets("#machinelearningflashcards", n = 500, include_rts = FALSE) %>% filter(screen_name == 'chrisalbon')
```


```r
mt <- ml_tweets[1:3, 1:5]

kable(mt, format = "html") %>%
  kable_styling(bootstrap_options = "striped", 
                full_width = F) 
```

<?xml version="1.0" encoding="UTF-8"?>
<table class="table table-striped" style="width: auto !important; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> screen_name </th>
   <th style="text-align:left;"> user_id </th>
   <th style="text-align:left;"> created_at </th>
   <th style="text-align:left;"> status_id </th>
   <th style="text-align:left;"> text </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> chrisalbon </td>
   <td style="text-align:left;"> 11518572 </td>
   <td style="text-align:left;"> 2017-05-09 22:51:43 </td>
   <td style="text-align:left;"> 862077650772164608 </td>
   <td style="text-align:left;"> Mean Squared Error #machinelearningflashcards https://t.co/K1iDqLV5DD </td>
  </tr>
  <tr>
   <td style="text-align:left;"> chrisalbon </td>
   <td style="text-align:left;"> 11518572 </td>
   <td style="text-align:left;"> 2017-05-09 18:15:39 </td>
   <td style="text-align:left;"> 862008178527031296 </td>
   <td style="text-align:left;"> R-Squared #machinelearningflashcards https://t.co/73gR8tb5PA </td>
  </tr>
  <tr>
   <td style="text-align:left;"> chrisalbon </td>
   <td style="text-align:left;"> 11518572 </td>
   <td style="text-align:left;"> 2017-05-09 16:23:04 </td>
   <td style="text-align:left;"> 861979845563105280 </td>
   <td style="text-align:left;"> Motivation For Kernel PCA #machinelearningflashcards https://t.co/AhLB91gHBh </td>
  </tr>
</tbody>
</table>

#### 3. Get the text within the tweet to add to the file name by removing the hash tag and URL link with some light [regex](https://en.wikipedia.org/wiki/Regular_expression): 

```r
ml_tweets$clean_text <- ml_tweets$text
ml_tweets$clean_text <- str_replace(ml_tweets$clean_text,"#[a-zA-Z0-9]{1,}", "") # remove the hashtag
ml_tweets$clean_text <- str_replace(ml_tweets$clean_text, " ?(f|ht)(tp)(s?)(://)(.*)[.|/](.*)", "") # remove the url link
ml_tweets$clean_text <- str_replace(ml_tweets$clean_text, "[[:punct:]]", "") # remove punctuation
```

#### 4. Write a function to download images of the flashcards from the media_url column and append the file name from the cleaned tweet text description and save into a folder:


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



#### 5. Apply the function:

```r
save_image(ml_tweets)
```

```
## Function complete...
```

At the end of this process you can view all of the **#machinelearningflashcards** in one [location](https://github.com/jasdumas/ml-flashcards/tree/master/data)! Thanks to Chris Albon for his work on this, and I'm looking forward to re-running this script to gain additional knowledge from new **#machinelearningflashcards** that are developed in the future! 


