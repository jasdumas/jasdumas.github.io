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
___

## Directions

1. Load libraries:

For this project I used `rtweet` to connect the Twitter API to search for relevant tweets by the hash tag, `dplyr` to filter and pipe things, `stringr` to clean up the tweet description, and `magick` to process the images. 

Note: I previously ran into trouble when downloading [*ImageMagick*](https://www.imagemagick.org/script/index.php) and detailed the errors and approaches, if you fall into the same trap I did: [https://gist.github.com/jasdumas/29caf5a9ce0104aa6bf14183ee1e3cd8](https://gist.github.com/jasdumas/29caf5a9ce0104aa6bf14183ee1e3cd8)

```r
library(rtweet)
library(dplyr)
library(magick)
library(stringr)
library(kableExtra)
library(knitr)
```

2. Get tweets for the hash tag and only curated tweets for Chris Albon's work: 

```r
ml_tweets <- search_tweets("#machinelearningflashcards", n = 500, include_rts = FALSE) %>% filter(screen_name == 'chrisalbon')
```


```r
mt <- ml_tweets[1:3,]

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
   <th style="text-align:right;"> retweet_count </th>
   <th style="text-align:right;"> favorite_count </th>
   <th style="text-align:left;"> is_quote_status </th>
   <th style="text-align:left;"> quote_status_id </th>
   <th style="text-align:left;"> is_retweet </th>
   <th style="text-align:left;"> retweet_status_id </th>
   <th style="text-align:left;"> in_reply_to_status_status_id </th>
   <th style="text-align:left;"> in_reply_to_status_user_id </th>
   <th style="text-align:left;"> in_reply_to_status_screen_name </th>
   <th style="text-align:left;"> lang </th>
   <th style="text-align:left;"> source </th>
   <th style="text-align:left;"> media_id </th>
   <th style="text-align:left;"> media_url </th>
   <th style="text-align:left;"> media_url_expanded </th>
   <th style="text-align:left;"> urls </th>
   <th style="text-align:left;"> urls_display </th>
   <th style="text-align:left;"> urls_expanded </th>
   <th style="text-align:left;"> mentions_screen_name </th>
   <th style="text-align:left;"> mentions_user_id </th>
   <th style="text-align:left;"> symbols </th>
   <th style="text-align:left;"> hashtags </th>
   <th style="text-align:left;"> coordinates </th>
   <th style="text-align:left;"> place_id </th>
   <th style="text-align:left;"> place_type </th>
   <th style="text-align:left;"> place_name </th>
   <th style="text-align:left;"> place_full_name </th>
   <th style="text-align:left;"> country_code </th>
   <th style="text-align:left;"> country </th>
   <th style="text-align:left;"> bounding_box_coordinates </th>
   <th style="text-align:left;"> bounding_box_type </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> chrisalbon </td>
   <td style="text-align:left;"> 11518572 </td>
   <td style="text-align:left;"> 2017-05-08 22:16:26 </td>
   <td style="text-align:left;"> 861706382877147136 </td>
   <td style="text-align:left;"> Ridge Regression #machinelearningflashcards https://t.co/yEuyM7TkaT </td>
   <td style="text-align:right;"> 2 </td>
   <td style="text-align:right;"> 5 </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> en </td>
   <td style="text-align:left;"> Machine Learning Flashcards </td>
   <td style="text-align:left;"> 861706380352249857 </td>
   <td style="text-align:left;"> http://pbs.twimg.com/media/C_VlYy2VYAEctP6.jpg </td>
   <td style="text-align:left;"> https://twitter.com/chrisalbon/status/861706382877147136/photo/1 </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> machinelearningflashcards </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
  </tr>
  <tr>
   <td style="text-align:left;"> chrisalbon </td>
   <td style="text-align:left;"> 11518572 </td>
   <td style="text-align:left;"> 2017-05-08 18:36:52 </td>
   <td style="text-align:left;"> 861651129251135488 </td>
   <td style="text-align:left;"> Euclidean Norm #machinelearningflashcards https://t.co/gCCCw9ZswA </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 6 </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> en </td>
   <td style="text-align:left;"> Machine Learning Flashcards </td>
   <td style="text-align:left;"> 861651127187554304 </td>
   <td style="text-align:left;"> http://pbs.twimg.com/media/C_UzIoxUQAA2VHH.jpg </td>
   <td style="text-align:left;"> https://twitter.com/chrisalbon/status/861651129251135488/photo/1 </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> machinelearningflashcards </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
  </tr>
  <tr>
   <td style="text-align:left;"> chrisalbon </td>
   <td style="text-align:left;"> 11518572 </td>
   <td style="text-align:left;"> 2017-05-08 16:35:43 </td>
   <td style="text-align:left;"> 861620640297631744 </td>
   <td style="text-align:left;"> What Are Principal Components #machinelearningflashcards https://t.co/bpagWQb7ev </td>
   <td style="text-align:right;"> 5 </td>
   <td style="text-align:right;"> 18 </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> en </td>
   <td style="text-align:left;"> Machine Learning Flashcards </td>
   <td style="text-align:left;"> 861620637982314496 </td>
   <td style="text-align:left;"> http://pbs.twimg.com/media/C_UXZ7oU0AAHKfS.jpg </td>
   <td style="text-align:left;"> https://twitter.com/chrisalbon/status/861620640297631744/photo/1 </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> machinelearningflashcards </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:left;"> NA </td>
  </tr>
</tbody>
</table>

3. Get text within the tweet to add to the file name by removing the hash tag and URL link: 

```r
ml_tweets$clean_text <- ml_tweets$text
ml_tweets$clean_text <- str_replace(ml_tweets$clean_text,"#[a-zA-Z0-9]{1,}", "") # remove the hashtag
ml_tweets$clean_text <- str_replace(ml_tweets$clean_text, " ?(f|ht)(tp)(s?)(://)(.*)[.|/](.*)", "") # remove the url link
ml_tweets$clean_text <- str_replace(ml_tweets$clean_text, "[[:punct:]]", "") # remove punctuation
```

4. Download images of the flashcards from the `media_url` column and append the file name from the cleaned tweet text description and save into a folder:

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

5. Apply the function:

```r
save_image(ml_tweets)
```


At the end of this process you can view all of the #machinelearningflashcards in one place! Thanks to Chris Albon for his work on this, and I'm looking forward to re-running this script to gain additional knowledge from new #machinelearningflashcards that are developed in the future! 


