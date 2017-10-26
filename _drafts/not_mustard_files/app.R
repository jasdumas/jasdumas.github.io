library(shiny)
library(shinydashboard)
library(shinythemes)
library(yelpr)
library(httr)
library(stringr)
library(purrr)
# Define UI for application
ui <- dashboardPage(skin = "yellow",
  dashboardHeader(title = "Not Mustard"),
  dashboardSidebar(
    
    textInput("location", "Location Search: ", value = "Hartford, CT", placeholder = "Anytown, USA"), 
    
    uiOutput("restaurant")
  ),
  dashboardBody(
    
    box(title = "Do reviews contain mustard?", solidHeader = TRUE,
        "Select a restaurant from the location search to explore exerpts from Yelp reviews for the keyword 'mustard' that potentially indicate regional differences in hamburger prep", hr(),
        status = "warning",
        verbatimTextOutput("result")) ,
    box(title = "Additional reading: ", status = "primary", solidHeader = TRUE,
        HTML("<a href='http://aht.seriouseats.com/archives/2010/03/dear-aht-differences-in-regional-mustard-use-on-mcdonalds-hamburgers.html'>Differences in Regional Mustard Use on McDonald's Hamburgers</a>"),
        hr(),
        HTML("<a href='https://www.mcdonalds.com/us/en-us/full-menu/burgers.html'>McDonald's burger menu</a>"))
  )
)

# Define server logic
server <- function(input, output) {
  
  

  api_reactive <- reactive({
    ############################################
    # 1. search for business by creating an app
    ############################################
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
                            use_oob = F, cache = T)
    # craft a url to make calls to the business search endpoint
    (url <-
        modify_url("https://api.yelp.com", path = c("v3", "businesses", "search"),
                   query = list(term = "McDonalds",
                                location = input$location, limit = 25)))
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
    return(biz_info$id)
  })
  
  
  output$restaurant <- renderUI({
    selectizeInput("restaurant", "Select Restaurant: ", 
                   choices = api_reactive())
  })
  
  biz_reviews_reactive <- reactive({
    
    ##########################
    # 2. get business reviews
    ##########################
    (url_id <-
       modify_url("https://api.yelp.com", path = c("v3", "businesses", input$restaurant, "reviews"),
                  query = list( locale = "en_US")))
    # retrieve info from the server
    res3 <- GET(url_id, config(token = token))
    # was this api request successful?
    http_status(res3)
    # return some geolocation data, business info & categories
    ct3 <- content(res3)
    # 3. Detect for string of 'mustard'
    not_mustard <- ct3$reviews %>% 
      map_df(`[`, c("text")) %>% 
      str_detect("mustard")
    return(not_mustard)
    
  })
  
  
  output$result <- renderText({
    print(biz_reviews_reactive()) })
}

# Run the application 
shinyApp(ui = ui, server = server)

