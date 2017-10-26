# not mustard
# A simple app that will do a simple keyword search from reviews of 
# whether a McDonald's location serves mustard on hamburgers, which varies by region.
## code from: https://github.com/jennybc/yelpr

library(yelpr)
library(httr)
library(stringr)

Sys.getenv("YELP_CLIENT_ID")

Sys.getenv("YELP_SECRET")

# 1. search for business by creating an app
yelp_app <- oauth_app("yelp", key = Sys.getenv("YELP_CLIENT_ID"),
                      secret = Sys.getenv("YELP_SECRET"))

# authenticate an endpoint
## https://www.yelp.com/developers/documentation/v3/authentication
yelp_endpoint <- oauth_endpoint(NULL,
                 authorize = "https://api.yelp.com/oauth2/token",
                 access = "https://api.yelp.com/oauth2/token")
# get an access token
## just enter anything for the authorization code
token <- oauth2.0_token(yelp_endpoint, yelp_app,
                        user_params = list(grant_type = "client_credentials"),
                        use_oob = TRUE)
# craft a url to make calls to the business search endpoint
(url <-
    modify_url("https://api.yelp.com", path = c("v3", "businesses", "search"),
               query = list(term = "McDonalds",
                            location = "Boston, MA", limit = 10)))
# retrieve info from the server
res2 <- GET(url, config(token = token))
# was this api request successful?
http_status(res2)
# return some geolocation data, business info & categories
ct2 <- content(res2)
# create an object with resturant name and id for further calls
#sapply(ct2$businesses, function(x) x[c("name", "id")])
biz_info <- ct2$businesses %>% 
  map_df(`[`, c("name", "id", "phone", "review_count"))
biz_info

# 2. get business reviews
(url_id <-
    modify_url("https://api.yelp.com", path = c("v3", "businesses","mcdonalds-brighton-2", "reviews"),
               query = list( locale = "en_US")))

url_id_f <- function(id) {
  modify_url("https://api.yelp.com", path = c("v3", "businesses", id, "reviews"),
             query = list( locale = "en_US"))
}

biz_reviews <- data.frame()
biz_reviews <-  map_chr(biz_info$id, url_id_f) %>% 
                data.frame(url = .)
biz_reviews
# retrieve info from the server
res3 <- GET(url_id, config(token = token))

#res3_f <- map(as.character(biz_reviews$url[5]), GET, config(token = token))

# was this api request successful?
http_status(res3)
# return some geolocation data, business info & categories
ct3 <- content(res3)

# 3. Detect for string of 'mustard'
#str_detect(ct3[["reviews"]][[3]][["text"]], "mustard")
ct3$reviews %>% 
  map_df(`[`, c("text")) %>% 
  str_detect("mustard")
