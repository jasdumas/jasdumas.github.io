---
title: "Exploratory & sentiment analysis of beer tweets from Untappd on Twitter"
layout: post
tags: [r, rstats, beer-analytics, text-mining, tidyverse, data-science, data-analysis]
output: 
  html_document: 
  self_contained: no
bigimg: /post_data/beer_flights.JPG
share-img: /post_data/untp-sentiment-1.png
social-share: true
---




## Project Objective

Untappd has some usage restrictions for their [API](https://untappd.com/api/register), namely not allowing any exploration for analytics or data mining use cases, so [I'm](https://untappd.com/user/jasdumas) going to explore tweets of beer and brewery check-ins from the Untappd app to find some _implicit_ trends in how users share their activity.

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
library(magrittr)
library(emo)
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
## [1] "I just earned the 'Tower of Beer (Level 20)' badge on @untappd! https://t.co/Cv5kwOxquc"   
## [2] "I just earned the 'Belgian Holiday  (Level 31)' badge on @untappd! https://t.co/soGN8iihKw"
## [3] "I just earned the 'Flan-didly-anders (Level 3)' badge on @untappd! https://t.co/RFY0CKXlaI"
## [4] "I just earned the 'Hopped Down (Level 16)' badge on @untappd! https://t.co/9BWWwsEX1O"     
## [5] "I just earned the 'Master' badge on @untappd! https://t.co/plOOnWFovi"                     
## [6] "Just added Victory at Sea by @BallastPoint to our menu https://t.co/7ify5kXSyA"
```

#### Let's explore some descriptive stats about the 18,000 tweets that were extracted

How many unique users are in the data set?

```r
n_distinct(untp$user_id)
```

```
## [1] 5867
```

What is the range of dates in the data set?

```r
paste(as.Date(min(untp$created_at)), as.Date(max(untp$created_at)), sep = " to " )
```

```
## [1] "2018-02-04 to 2018-02-06"
```

My initial assumptions were that all the tweets would be posted from the app, but it seems there is a little bit cross-posting going on from Facebook and some 🤓 nerds who have set up [IFTTT](https://ifttt.com/discover) applet recipes.

```r
count(untp, source)
```

```
## # A tibble: 4 x 2
##                 source     n
##                  <chr> <int>
## 1             Facebook     6
## 2 Flamingo for Android     1
## 3                IFTTT     6
## 4              Untappd 17987
```

#### How many types of these check-ins are shared?

There a few different types of tweet structures that can be shared from the Untappd app, as noticed from the text sample above. They include:

1. Earning Badges (i.e. tweets that contain 'I just earned the...' or even the word 'badge')
2. Added review text (i.e. text which ends in a '-' before the default template of 'Drinking a')
3. Default check-ins (i.e. tweets that begin with 'Drinking a')
4. Brewery offering updates (i.e. tweets that begin with 'Just added ...' for new beers added)

There are granular account social settings available that enable the ease of sharing check-in info to certain linked social media accounts.

Let's detect the string patterns and create a new column in the data set to house them.

```r
untp %<>%
  mutate(structure_type = case_when (
    str_detect(text, "I just earned the") ~ "badge achievement", 
    str_detect(text, "^Drinking") ~ "default check-in", 
    str_detect(text, "^Just added") ~ "brewery update", 
    TRUE ~ "additional review"
  ))
```


Given that a single check-in can result in multiple badges and therefore multiple social shares, this makes sense to have more tweets associated with the type of beer check-in.

```r
untp %>% 
  count(structure_type) %>% 
  mutate(structure_type = fct_reorder(structure_type, n)) %>%
  ggplot(aes(x = structure_type, y = n)) +
      geom_bar(stat = "identity", fill = wes_palette("BottleRocket1", 1)) +
      theme_minimal() +
      labs(title = "Count of Tweet Types for Untappd Twitter Shares", 
           subtitle = "Most users have shared their badge acheivements", y = "Count of Tweets", x = "")
```

![plot of chunk tweettype]({{ site.url }}/post_data/untp-tweettype-1.png)


#### What kind of badges are users earning?

The 'Brew Bowl LII' badge is the most popular earned badge available during this Superbowl weekend. Consequently, I visited a brewery this weekend and earned this badge as well. 

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Drinking a Golden Messenger by <a href="https://twitter.com/HogRiverBrewing?ref_src=twsrc%5Etfw">@HogRiverBrewing</a> at <a href="https://twitter.com/HogRiverBrewing?ref_src=twsrc%5Etfw">@hogriverbrewing</a> — <a href="https://t.co/70GqltpVXP">https://t.co/70GqltpVXP</a> <a href="https://twitter.com/hashtag/photo?src=hash&amp;ref_src=twsrc%5Etfw">#photo</a></p>&mdash; Jasmine Dumas (@jasdumas) <a href="https://twitter.com/jasdumas/status/959878581936586753?ref_src=twsrc%5Etfw">February 3, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

The badge names are located between single quotes, so we'll have to extract out that text to learn what specific badges are earned.

```r
untp %<>% 
  mutate(badge_type = str_extract(text, "(?<=').*?(?=')"))
```

There were numerous 'Middle of the Road' badges awarded of various levels. The description of the Level 5 of that badge is:

> Looking for more kick than a session beer, but want to be able to stay for a few rounds? You have to keep it in the middle. That's 25 beers with an ABV greater than 5% and less than 10%.

So, it would appear that is a popular [range of ABV](https://vinepair.com/articles/dark-beer-light-beer/) that users are trying. 

```r
untp %>% 
  count(badge_type) %>% 
  dplyr::filter(!is.na(badge_type)) %>% 
  arrange(desc(n)) %>% 
  top_n(25) %>% 
  ggplot(aes(x = fct_reorder(badge_type, n), y = n)) +
      geom_bar(stat = "identity", fill = wes_palette("GrandBudapest1", 1)) +
      theme_minimal() +
      coord_flip() +
      labs(title = "Count of Badge Types for Untappd Twitter Shares", 
           subtitle = "Brew Bowl LII was the most awarded badge this weekend", y = "Count of Tweets", x = "")
```

![plot of chunk topbadge]({{ site.url }}/post_data/untp-topbadge-1.png)


#### Where do people check-in from?

There is a lot of activity on the [east coast](https://www.thrillist.com/drink/nation/the-16-best-breweries-in-the-northeast) (Pennsylvania being the top place at the time of running this analysis) and in the metros across the U.S.! Untappd is based in North Carolina, so it's interesting to not see a lot of activity there as expected, but users can have their location settings turned off for privacy in Twitter. This may also be indicative of users not filling out all the check-in details such as purchase or drinking location. Often times users seem to be drinking and checking-in at home and may want to mask their location given the plethora of missing values.

```r
untp %>% 
  count(place_full_name) %>% 
  arrange(desc(n)) %>% 
  top_n(21) %>% 
  data.frame()
```

```
##       place_full_name     n
## 1                <NA> 14703
## 2   Pennsylvania, USA    73
## 3        Portland, OR    69
## 4        Florida, USA    56
## 5     Los Angeles, CA    45
## 6  Cape Girardeau, MO    44
## 7         Houston, TX    39
## 8         Phoenix, AZ    35
## 9       New York, USA    34
## 10        Anaheim, CA    32
## 11         Dallas, TX    32
## 12   Philadelphia, PA    32
## 13        Chicago, IL    31
## 14         Boston, MA    29
## 15       Brooklyn, NY    29
## 16         Austin, TX    26
## 17      San Diego, CA    25
## 18      Nashville, TN    22
## 19          Tempe, AZ    22
## 20       O'Fallon, MO    21
## 21      Charlotte, NC    20
## 22      Manhattan, NY    20
## 23       Monterey, CA    20
## 24        Raleigh, NC    20
## 25      Virginia, USA    20
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

Instead of crafting an ugly regex solution to extract the brewery from the tweet text, the column for `mentions_screen_name` is actually a decent proxy for the beer location if the brewery has a Twitter presence. I really enjoy [Tree House Brewery, Green IPA](https://untappd.com/b/tree-house-brewing-company-green/533174) and it is nice to see many others have tried out beers from their brewery.

```r
# mentions_screen_name is the brewery that produced the checked-in beer
untp %>% 
  unnest(brewery = mentions_screen_name) %>% 
  count(brewery) %>% 
  dplyr::filter(brewery != 'untappd') %>% 
  arrange(desc(n)) %>% 
  top_n(25) %>% 
  ggplot(aes(x = fct_reorder(brewery, n), y = n)) +
      geom_bar(stat = "identity", fill = wes_palette("Moonrise2", 1)) +
      theme_minimal() +
      coord_flip() +
      labs(title = "Top 25 Breweries for Untappd Twitter Shares", 
           subtitle = "", y = "Count of Tweets", x = "", caption = "by @handle occurrences")
```

![plot of chunk topbrew]({{ site.url }}/post_data/untp-topbrew-1.png)

#### How many pictures of beer are shared?

The #photo hashtag is included with a tweet from Untappd when the user appends a photo. The rest of the hash tags seem to align with the Superbowl festivities

```r
untp %>%
  unnest(hashtags) %>% 
  count(hashtags) %>% 
  dplyr::filter(!is.na(hashtags)) %>%
  arrange(desc(n)) %>% 
  top_n(15)
```

```
## # A tibble: 15 x 2
##                hashtags     n
##                   <chr> <int>
##  1                photo  2939
##  2             brewbowl  2498
##  3        ibelieveinIPA    62
##  4            SuperBowl    40
##  5         FlyEaglesFly    33
##  6         FirstSqueeze    26
##  7            craftbeer    24
##  8         birthdaybrew    19
##  9        UntapTheStack    17
## 10 BrainDeadBottleShare    16
## 11          beerandfood    15
## 12            Superbowl    12
## 13         flyeaglesfly    10
## 14            superbowl    10
## 15             GoEagles     9
```

#### Did people share more during the Superbowl game?

There was definitely a spike on Sunday as the Superbowl was starting (This post has since been re-ran with newer data) and its noticeable on Monday as well!

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

We want to separate all the text before the dash (-) which is how the tweet is structured when users add additional text to their beer review share to prep for text analysis.

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

Let's remove the hash tags, the 'Drinking a' and any punctuation from the beer column and create a new column.

```r
untp_text %<>%
  mutate(clean_beer = str_replace(beer,"#[a-zA-Z0-9]{1,}", "")) %>%
  mutate(clean_beer = str_replace_all(clean_beer, "Drinking a |Drinking an ", "")) %>%
  mutate(clean_beer = trimws(str_replace_all(clean_beer, "[[:punct:]]", "")))
```

Now that we have the reviews and beer/breweries separated, I wonder if there are any commonly reviewed beers that are shared on Twitter? (I want to keep the beer with the brewery at this point in case the [same beer name appears at different breweries](https://www.npr.org/sections/thesalt/2015/01/05/369445171/craft-brewers-are-running-out-of-names-and-into-legal-spats))

```r
untp_text %>% 
  count(clean_beer) %>% 
  arrange(desc(n)) %>% 
  top_n(15) %>% 
  dplyr::filter(clean_beer %notin% c("DC", "A")) %>% 
  ggplot(aes(x = fct_reorder(clean_beer, n), y = n)) +
      geom_bar(stat = "identity", fill = wes_palette("BottleRocket2", 1)) +
      theme_minimal() +
      coord_flip() +
      labs(title = "Top 15 Beers for Untappd\nTwitter Shares", 
           subtitle = "", y = "Count of Tweets", x = "")
```

![plot of chunk topbeer]({{ site.url }}/post_data/untp-topbeer-1.png)

#### Translating the additional review text as proxy for empirical reviews

These tweets don't indicate what numerical value that users rated each beer on a scale of 0.0 to 5.0 (0.25 increments) on the app, so I'm going to try and derive some of users opinions about the top 20 beers from tweets that have additional review text, using the [`tidytext`](https://www.tidytextmining.com/) package. I believe there is going to be some sentiment shared that is linked to the Super Bowl, and some selection bias from user's most likely sharing only preferred beers.

```r
top_beers <- untp_text %>%
              count(clean_beer) %>% 
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
                  mutate(review = as.character(review)) %>%
                  unnest_tokens(word, review) %>% 
                  dplyr::filter(word %notin% c("super", "superbowl", "superbowlsunday"))
```


```r
untp_sentiment <- untp_text_tiny %>%
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
## 1                                               Barrel        2        1
## 2                                       Bourbon Barrel        3        3
## 3 Canadian Breakfast Stout CBS 2017 by foundersbrewing        0        2
## 4                          Dallas Sucks by weyerbacher        1        1
## 5                                           Double Dry        2        2
## 6                   Drifter Pale Ale by widmerbrothers        2        0
## # ... with 1 more variables: sentiment <dbl>
```

The ['Drifter Pale Ale
Widmer Brothers Brewing'](https://untappd.com/b/widmer-brothers-brewing-drifter-pale-ale/55591) having the lowest associated sentiment and currently rated on Untappd: **3.43** and the ['Stone Loral & Dr. Rudi's Inevitable Adventure by Stone Brewing'](https://untappd.com/b/stone-brewing-stone-loral-and-dr-rudi-s-inevitable-adventure/2391432) having the highest associated sentiment which is currently rated on Untappd: **3.81**. 

**Sentiment when paried with frequency of rating could definetly be an indicator to other beer drinkers or breweries about how people liked a particular beer without the numerical rating system.**

```r
ggplot(untp_sentiment, aes(x = clean_beer, y = sentiment, fill = clean_beer)) +
  geom_col(show.legend = FALSE) +
  coord_flip() +
  theme_minimal() +
  labs(x = "")
```

![plot of chunk sentiment]({{ site.url }}/post_data/untp-sentiment-1.png)

Now for fun, I want to visualize the words on a word cloud to see the most common occurrences from the reviews. The largest word being 'Beer' is the most obvious given the specific Untappd reviews. Then the other words appear to be popular hash tags from the Superbowl such as ['flyeaglesfly'](https://twitter.com/search?q=flyeaglesfly&src=typd).

```r
untp_text_tiny %>%
  anti_join(stop_words) %>%
  count(word) %>%
  with(wordcloud(word, n, max.words = 100, colors = wes_palette("Zissou1")))
```

![plot of chunk wordcloud]({{ site.url }}/post_data/untp-wordcloud-1.png)


#### Notes:

1. Untappd has a [supporter program](https://untappd.com/supporter) which comes with a feature for downloading your personal check-in data, which I'm not apart of.

2. I did not intentionally set out to run this analysis during the 🏈 Superbowl and I did not watch the game!
