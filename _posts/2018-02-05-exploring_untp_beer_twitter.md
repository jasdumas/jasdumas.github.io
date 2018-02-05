---
title: "Exploratory & sentiment analysis of beer tweets from Untappd on Twitter"
layout: post
tags: [r, rstats, beer-analytics]
output: 
  html_document: 
  self_contained: no
bigimg: /post_data/beer_flights.JPG
share-img: /post_data/untp-sentiment-1.png
social-share: true
---


```r
knitr::opts_chunk$set(
  fig.path = "{{ site.url }}/post_data/untp-",
	echo = TRUE,
	message = FALSE,
	warning = FALSE
)
```


## Project Objective

Untappd has some usage restrictions for their [API](https://untappd.com/api/register) namely not allowing any exploratory of analytics uses, so [I'm](https://untappd.com/user/jasdumas) going to explore tweets of beer and brewery check-ins from the Untappd app to find some implicit trends in how users share their activity.

## Exploratory Analysis




```r
library(tidyverse)
library(rtweet)
library(stringr)
library(wesanderson)
library(maps)
library(tidytext)
library(dumas) # http://jasdumas.github.io/dumas/
library(wordcloud)
```

All social media shares from the Untappd app include their own short URL **'untp.beer'**, which makes the search query criteria identifiable using the [`search_tweets()`](http://rtweet.info/) function. 

```r
untp <- search_tweets(q = "untp.beer", 
                      n = 18000, 
                      include_rts = FALSE, 
                      retryonratelimit = TRUE,  
                      geocode = lookup_coords("usa"), 
                      lang = "en"
)
```

Let's take a peek at the text of the tweet! 

```r
head(untp$text)
```

```
## [1] "Drinking a Nelson’s Revenge by @evergrainbeer @ Ever Grain Brewing Co. — https://t.co/zZH9LsFpxC #photo"                                                                                                                                          
## [2] "Drinking a Stone Tangerine Express IPA by @StoneBrewing at @stonebrewingco — https://t.co/Od9O87c3Z9 #photo"                                                                                                                                      
## [3] "Meetings - Drinking a Big Cat IPA by @collisionbrew at @pintroomdublin  — https://t.co/xwCDDFo8Fq #photo"                                                                                                                                         
## [4] "I just earned the 'Photogenic Brew  (Level 46)' badge on @untappd! https://t.co/klUlFEPKJ6"                                                                                                                                                       
## [5] "I just earned the '2X (Level 63)' badge on @untappd! https://t.co/eArP2NrWSG"                                                                                                                                                                     
## [6] "Incredibly smooth stout. Chocolate, confectioner’s sugar and bready malt in a flavor profile that is not overly sweet and nicely balanced. - Drinking a Donut Quote Me On This by @HiddenSpringAle @ Casa Girón  — https://t.co/nOE8zNPlwY #photo"
```

From this sample, its apparent that there a few type of default tweets that are available.

#### Let's explore some descriptive stats about the 18,000 tweets that were extracted

How many unique users are in the data set?

```r
length(unique(untp$user_id))
```

```
## [1] 5902
```


```r
paste(min(untp$created_at), max(untp$created_at), sep = " to " )
```

```
## [1] "2018-02-04 19:15:08 to 2018-02-05 22:58:21"
```

My initial assumptions were that all the tweets would be posted from the app, but it seems there is a little bit cross-posting going on from Facebook and some nerds who have set up [IFTTT](https://ifttt.com/discover) applet recipes.

```r
count(untp, source)
```

```
## # A tibble: 3 x 2
##     source     n
##      <chr> <int>
## 1 Facebook     8
## 2    IFTTT     6
## 3  Untappd 17986
```

#### How many types of these check-ins are shared?

There a few different types of tweet structures that can be shared from the Untappd app as notices from the text sample above. They include:

1. Earning Badges (i.e. tweets that contain 'I just earned the...' or even the word 'badge')
2. Added review text (i.e. text which ends in a '-' before the default template of 'Drinking a')
3. Default check-ins (i.e. tweets that begin with 'Drinking ' _a|an|the_)
4. Brewery offering updates (i.e. tweets that begin with 'Just added ...' for new beers added)

There are granular account social settings available that enable the ease of sharing check-in info to certain linked social media accounts.

I'm going to detect the string patterns and create a new column in the data set to house them.

```r
untp$structure_type <- NA

# earning badges
untp$structure_type[untp$text %>% str_detect("I just earned the")] <- "badge achievement"
# default checkin
untp$structure_type[untp$text %>% str_detect("^Drinking ")] <- "default check-in"
# brewery updates
untp$structure_type[untp$text %>% str_detect("^Just added")] <- "brewery update"
# any NA's left should be tweets that users have added additional text/descriptions
untp$structure_type[is.na(untp$structure_type)] <- "additional review"
```


Given that a single check-in can result in multiple badges and multiple social shares, this makes sense to have more tweets associated with the type of beer check-in.

```r
untp %>% group_by(structure_type) %>% 
         summarise(n = n()) %>% 
         mutate(structure_type = fct_reorder(structure_type, n)) %>%
    ggplot(., aes(x = structure_type, y = n)) +
      geom_bar(stat = "identity", fill = wes_palette("BottleRocket1", 1)) +
      theme_minimal() +
      labs(title = "Count of Tweet Types for Untappd Twitter Shares", 
           subtitle = "Most users have shared their badge acheivements", y = "Count of Tweets", x = "")
```

![plot of chunk unnamed-chunk-9]({{ site.url }}/post_data/untp-unnamed-chunk-9-1.png)


#### What kind of badges are users earning?

The 'Brew Bowl LII' badge is the most popular earned badge available during this Superbowl weekend. Consequently, I visited a brewery this weekend and earned this badge as well. 

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Drinking a Golden Messenger by <a href="https://twitter.com/HogRiverBrewing?ref_src=twsrc%5Etfw">@HogRiverBrewing</a> at <a href="https://twitter.com/HogRiverBrewing?ref_src=twsrc%5Etfw">@hogriverbrewing</a> — <a href="https://t.co/70GqltpVXP">https://t.co/70GqltpVXP</a> <a href="https://twitter.com/hashtag/photo?src=hash&amp;ref_src=twsrc%5Etfw">#photo</a></p>&mdash; Jasmine Dumas (@jasdumas) <a href="https://twitter.com/jasdumas/status/959878581936586753?ref_src=twsrc%5Etfw">February 3, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



```r
untp$badge_type <- NA
untp$badge_type <- str_extract(untp$text, "(?<=').*?(?=')")
```

There were numerous 'Middle of the Road' badges awarded of various levels. The description of the Level 5 of that badge is:

> Looking for more kick than a session beer, but want to be able to stay for a few rounds? You have to keep it in the middle. That's 25 beers with an ABV greater than 5% and less than 10%.

So, it would appear that is a popular range of ABV that users are trying, which supports the notion of it'd generally easier to consume more moderate-alcohol content beers rather than heavier beers (Ales vs Stouts).

```r
untp %>% group_by(badge_type) %>% 
         summarise(n = n()) %>% 
         dplyr::filter(!is.na(badge_type)) %>% 
         arrange(desc(n)) %>% 
         top_n(25) %>% 
         mutate(badge_type = fct_reorder(badge_type, n)) %>%
    ggplot(., aes(x = badge_type, y = n)) +
      geom_bar(stat = "identity", fill = wes_palette("GrandBudapest1", 1)) +
      theme_minimal() +
      coord_flip() +
      labs(title = "Count of Badge Types for Untappd Twitter Shares", 
           subtitle = "Brew Bowl LII was the most awarded badge this weekend", y = "Count of Tweets", x = "")
```

![plot of chunk badges]({{ site.url }}/post_data/untp-badges-1.png)


#### Where do people check-in from?

Lot's of activity on the [east coast](https://www.thrillist.com/drink/nation/the-16-best-breweries-in-the-northeast) (Boston, MA being the top place at the time of running this analysis) and in the metros across the U.S.! Untappd is based in North Carolina, so it's interesting to not see a lot of activity there, but users can have their location settings turned off for privacy in Twitter. This may also be indicative of users not filling out all the check-in details such as purchase or drinking location. Often times users seem to be drinking and checking-in at home and may want to mask their location given the plethora of missing values.

```r
untp %>% group_by(place_full_name) %>% 
  summarise(n = n()) %>% 
  arrange(desc(n)) %>% 
  top_n(11) %>% 
  data.frame()
```

```
##       place_full_name     n
## 1                <NA> 14779
## 2   Pennsylvania, USA    82
## 3        Florida, USA    67
## 4        Portland, OR    62
## 5  Cape Girardeau, MO    44
## 6    Philadelphia, PA    39
## 7         Phoenix, AZ    38
## 8          Dallas, TX    37
## 9     Los Angeles, CA    36
## 10       Brooklyn, NY    32
## 11      New York, USA    32
```

There are a few off the map, but the general distribution is effectively visualized with one yellow dot per tweet.

```r
## create lat/lng variables using all available tweet and profile geo-location data
untp <- lat_lng(untp)

## plot state boundaries
par(mar = c(0, 0, 0, 0))
maps::map("state", lwd = .25)

## plot lat and lng points onto state map
with(untp, points(lng, lat, pch = 20, cex = .75, col = wes_palette("Cavalcanti1", 1)))
```

![plot of chunk map]({{ site.url }}/post_data/untp-map-1.png)

#### What are the most popular breweries?

Instead of crafting an ugly regex solution to extract the brewery from the tweet text, the column for `mentions_screen_name` is actually a decent proxy for the beer location if the brewery has a Twitter presence! I really enjoy [Tree House Brewery, Green IPA](https://untappd.com/b/tree-house-brewing-company-green/533174) and it is nice to see many others have tried out beers from their brewery.

```r
# mentions_screen_name is the brewery that produced the checked-in beer
tibble(brewery = unlist(untp$mentions_screen_name)) %>% 
        group_by(brewery) %>% 
        dplyr::filter(brewery != 'untappd') %>% 
        summarise(n = n()) %>% 
        arrange(desc(n)) %>% 
        top_n(25) %>% 
  mutate(brewery = fct_reorder(brewery, n)) %>%
    ggplot(., aes(x = brewery, y = n)) +
      geom_bar(stat = "identity", fill = wes_palette("Moonrise2", 1)) +
      theme_minimal() +
      coord_flip() +
      labs(title = "Top 25 Breweries for Untappd Twitter Shares", 
           subtitle = "", y = "Count of Tweets", x = "", caption = "by @handle occurrences")
```

![plot of chunk topbrew]({{ site.url }}/post_data/untp-topbrew-1.png)

#### How many pictures of beer are shared?

The #photo is indicative of a paired photo with a tweet from Untappd. The rest of the hash tags align with the Superbowl festivities

```r
tibble(hashtags = unlist(untp$hashtags)) %>% 
        group_by(hashtags) %>% 
        dplyr::filter(!is.na(hashtags)) %>% 
        summarise(n = n()) %>% 
        arrange(desc(n)) %>% 
        top_n(25)
```

```
## # A tibble: 37 x 2
##                hashtags     n
##                   <chr> <int>
##  1                photo  2923
##  2             brewbowl  2751
##  3        ibelieveinIPA    65
##  4            SuperBowl    41
##  5         FlyEaglesFly    39
##  6         FirstSqueeze    26
##  7            craftbeer    21
##  8 BrainDeadBottleShare    16
##  9          beerandfood    15
## 10        UntapTheStack    15
## # ... with 27 more rows
```

#### Did people share more during the Superbowl game?

There was definitely a spike on Sunday as the Superbowl was starting!

```r
## plot time series of tweets
ts_plot(untp, "1 hours") +
  ggplot2::theme_minimal() +
  ggplot2::theme(plot.title = ggplot2::element_text(face = "bold")) +
  ggplot2::labs(
    x = NULL, y = NULL,
    title = "Frequency of Untappd Twitter statuses from the past 2 days",
    subtitle = "Twitter status (tweet) counts aggregated using one-hour intervals",
    caption = "\nSource: Data collected from Twitter's REST API via rtweet"
  )
```

![plot of chunk tsplot]({{ site.url }}/post_data/untp-tsplot-1.png)

## Sentiment Analysis

We want to separate all the text before the dash (-) which is how the tweet is structured when users add additional text to their beer review share.

```r
# the first vector is the review, second is the beer/brewery, third is the url
untp_text <- str_split(untp$text[untp$structure_type == 'additional review'], "-|—")

# unnest these unnamed lists, if they were named I would have used purrr::map_df()
# https://stackoverflow.com/a/24496537/4143444
review <- sapply(untp_text, "[", 1)
beer <- sapply(untp_text, "[", 2)
user <-untp %>% 
        dplyr::filter(structure_type == 'additional review') %>% 
        select(starts_with("screen_name"))
untp_text <- data.frame(review, beer, user$screen_name)
```

Let's remove the hash tags from the beer column and the common begging of each description.

```r
untp_text$clean_beer <- str_replace(untp_text$beer,"#[a-zA-Z0-9]{1,}", "")

untp_text$clean_beer <- str_replace_all(untp_text$clean_beer, c("Drinking a |Drinking an "), "") 

untp_text$clean_beer <- str_replace_all(untp_text$clean_beer, "[[:punct:]]", "") 

untp_text$clean_beer <- trimws(untp_text$clean_beer)
```

Now that we have the reviews and beer/breweries separated, I wonder if there are any commonly reviewed beers that are shared on Twitter? (I want to keep the beer with the brewery at this point in case the [same beer name appears at different breweries](https://www.npr.org/sections/thesalt/2015/01/05/369445171/craft-brewers-are-running-out-of-names-and-into-legal-spats))

```r
untp_text %>% group_by(clean_beer) %>% 
              summarise(n = n()) %>% 
              arrange(desc(n)) %>% 
              top_n(15) %>% 
              dplyr::filter(clean_beer %notin% c("DC", "A")) %>% 
  mutate(clean_beer = fct_reorder(clean_beer, n)) %>%
    ggplot(., aes(x = clean_beer, y = n)) +
      geom_bar(stat = "identity", fill = wes_palette("BottleRocket2", 1)) +
      theme_minimal() +
      coord_flip() +
      labs(title = "Top 15 Beers for Untappd\nTwitter Shares", 
           subtitle = "", y = "Count of Tweets", x = "")
```

![plot of chunk topbeer]({{ site.url }}/post_data/untp-topbeer-1.png)

#### Translating the additional review text as proxy for empirical reviews

These tweets don't indicate what numerical value that users rated each beer on a scale of 0.0 to 5.0 (0.25 increments) on the app, so I'm going to try and derive some of users opinions about beer from tweets that have additional review text, using the [`tidytext`](https://www.tidytextmining.com/) package. I think there is going to be some sentiment shared that is linked to the Super Bowl, and some selection bias from user's most likely sharing preferred beers.

```r
top_beers <- untp_text %>% group_by(clean_beer) %>% 
              summarise(n = n()) %>% 
              arrange(desc(n)) %>% 
              top_n(20) %>% 
              dplyr::filter(clean_beer %notin% c("DC", "A")) %>% 
              select(clean_beer)

# subset the data into topic (beers) and review (text) for tokenization
untp_text_tiny <- untp_text[, c("clean_beer", "review")]

# need to inner_join top beers with the reviews
merge_untp <- untp_text_tiny %>% 
              inner_join(top_beers)

# tokenize the reviews and remove some of the specific football words
untp_text_tiny <- merge_untp %>% 
                  unnest_tokens(word, review) %>% 
                  dplyr::filter(word %notin% c("super", "superbowl", "superbowlsunday"
))
```


```r
untp_sentiment <- 
  untp_text_tiny %>%
    inner_join(get_sentiments("bing")) %>%
    count(clean_beer, sentiment) %>%
    spread(sentiment, n, fill = 0) %>%
    mutate(sentiment = positive - negative) 

head(untp_sentiment)
```

```
## # A tibble: 6 x 4
##                                             clean_beer negative positive
##                                                  <chr>    <dbl>    <dbl>
## 1                                    6 by relicbrewing        0        2
## 2                                  Abbey by newbelgium        0        3
## 3                                               Barrel        3        4
## 4                                       Bourbon Barrel        2        2
## 5            Bourbon County Brand Stout by GooseIsland        0        2
## 6 Canadian Breakfast Stout CBS 2017 by foundersbrewing        0        2
## # ... with 1 more variables: sentiment <dbl>
```

The ['Drifter Pale Ale
Widmer Brothers Brewing'](https://untappd.com/b/widmer-brothers-brewing-drifter-pale-ale/55591) having the lowest associated sentiment and currently rated: **3.43** and the ['Stone Loral & Dr. Rudi's Inevitable Adventure by Stone Brewing'](https://untappd.com/b/stone-brewing-stone-loral-and-dr-rudi-s-inevitable-adventure/2391432) (which is a IPA - Imperial / Double) having the highest associated sentiment which is currently rated: **3.88**. 

```r
ggplot(untp_sentiment, aes(x = clean_beer, y = sentiment, fill = clean_beer)) +
  geom_col(show.legend = FALSE) +
  coord_flip() +
  theme_minimal() +
  labs(x = "")
```

![plot of chunk sentiment]({{ site.url }}/post_data/untp-sentiment-1.png)

Now, I want to visualize the words to see the most common occurrences from added reviews. The largest word being 'Beer' is the most obvious given the specific Untappd reviews. Then the other words appear to be popular hash tags from the Superbowl such as ['flyeaglesfly'](https://twitter.com/search?q=flyeaglesfly&src=typd).

```r
untp_text_tiny %>%
  anti_join(stop_words) %>%
  count(word) %>%
  with(wordcloud(word, n, max.words = 100, colors = wes_palette("Zissou1")))
```

![plot of chunk wordcloud]({{ site.url }}/post_data/untp-wordcloud-1.png)


#### Notes:

1. Untappd has a [supporter program](https://untappd.com/supporter) which comes with a feature for downloading your personal check-in data.

2. I did not intentionally set out to run this analysis during the Superbowl and I did not watch the game!
