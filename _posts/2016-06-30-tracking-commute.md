---
layout: post
title: Tracking my Work Hours with IFTTT and R
subtitle: An ongoing effort to work more efficiently and smarter
bigimg: /post_data/working-hours-static.png
---


TD;DR: For the forgetful, IFTTT can be a great way to track your work hours and provide insight about trends.

Manually entering your own timesheet and logging your specific project time hours for work (and contracting) can cause inconsistencies, namely forgetting how may hours to submit. In November 2015 I began a new role as a Data Science Intern at The Hartford Insurance Group headquartered in Hartford, CT and I was responsible for logging my working hours in both the contractor database as well as The Hartford's database so that I can be *promptly* paid each week. After the first few days, I made an honest assessment about how likely I was to screw up my actual work hours for entry and decided if I wanted to not be scolded, I should think of a automated way of recording hours.

It has been said that:

>  “When you can measure what you are speaking about, and express it in numbers, you know something about it, when you cannot express it in numbers, your knowledge is of a meager and unsatisfactory kind; it may be the beginning of knowledge, but you have scarely, in your thoughts advanced to the stage of science.” - [William Thomson, 1st Baron Kelvin](http://www.goodreads.com/quotes/166961-when-you-can-measure-what-you-are-speaking-about-and)

So with previous exposure to [IFTTT](https://en.wikipedia.org/wiki/IFTTT), which is a free web-based service which creates recipes that connect the digital and physical world in the realm of IoT (Internet of Things), I set out the create a recipe that would use my iPhone's location services and a google spreadsheet for tracking timestamps to and from work. I established a perimeter around my work location in the IFTTT application and specified that I wanted the arrival and departure time from that area. Back in November I only intended for this recipe to be a plan b if I had forgot how many hours I had worked for my timesheets. In the interest of becoming more informed about the entirety of my work hours and after accumulating approximately 258 check-ins over the last 7 months on the google spreadsheet, I set out to extract some meaning and tangible statistics to understand how often I was working.

For this project analysis I used the [`googlesheets`](https://github.com/jennybc/googlesheets) package by Jenny Bryan which is a Google Spreadsheets R API, **dplyr** for tidy data forms and **ggplot2 and plotly** for interactive graphics.

Here is the resulting visualization:

![](https://plot.ly/~jasdumas/54.embed)



From the graph above, it is pretty clear when I switched from being a part-time intern to a full-time data scientist in early April. Also its interesting to see when I started to work a compressed work week in early June. I unfortunately sometimes walk to lunch events that inadvertently exit my location services out out of the original perimeter and also when traveling through Hartford to visit family in New York.

In conclusion, IFTTT was a bit irregular and not completely accurate for logging the location coordinates but overall this is a good start to generating more data and providing insight to about my working hours!

```r
##############################
# Explore my work schedule from a google sheet where I log
# my travel time to Hartford, CT with IFTTT
##############################
library(magrittr)
################
# data clean
################
# install googlesheets
library(googlesheets)
# register the google sheet as a URL with share ability enable
sheet <- gs_url("https://docs.google.com/spreadsheets/d/1EFH_QytjB661YUe0VKZkuik-wx-v_w2sJvL12IiEMOY/edit?usp=sharing",
                lookup = T)
# read the sheet in
time_sheet <- sheet %>% gs_read(ws = "Sheet1")
head(time_sheet)
sapply(time_sheet, class)

# remove duplicates
time_sheet <- time_sheet[-c(96:98),]

# extract date from time
library(stringr)
date <-str_extract_all(string=time_sheet$date_time, pattern='\\w+\\s\\d+(st)?(nd)?(rd)?(th)?,\\s+\\d+')
time_sheet$date <- date

# extract out the time to a separate column
time <- str_extract_all(string=time_sheet$date_time, pattern='\\b((1[0-2]|0?[1-9]):([0-5][0-9])([AaPp][Mm]))')
time_sheet$time <- time

# transform the types for later data munging
library(lubridate)
time_sheet$date_format <- mdy(time_sheet$date)
time_sheet$time <- as.character(time_sheet$time)
head(time_sheet)

# remove the second column
time_sheet = time_sheet[, -c(2)]

# look at a data frame with specific types of exit, enter times
library(dplyr)
exit <- filter(time_sheet, type == 'exited')
enter <- filter(time_sheet, type == 'entered')

# merge the two, which will align the dates with enter and exit time labels
merge_time_sheet <- merge(enter, exit, by = 'date_format')

# remove duplicate middle columns of unformatted date and labels
merge_time_sheet = merge_time_sheet[, -c(2:3, 5:6)]

# change column names
colnames(merge_time_sheet) <- c("date", "enter_time", "exit_time")
head(merge_time_sheet)

# format the time column to get the difference from enter and exit (in seconds)
merge_time_sheet$time_diff <- strptime(merge_time_sheet$enter_time, "%H:%M%p") - strptime(merge_time_sheet$exit_time, "%H:%M%p")
merge_time_sheet$time_diff <- abs(merge_time_sheet$time_diff)

# change seconds into hours (3600 in an hour)
merge_time_sheet$time_diff <- merge_time_sheet$time_diff / 3600

# so I travel through hartford alot on the highway or walk around
# hartford for lunch, so I want to remove small time diff observations
merge_time_sheet = merge_time_sheet[-c(which(merge_time_sheet$time_diff < 3.51666666666667)), ]
# there are some duplicates but I will leave those for now

# round time diff
merge_time_sheet$time_diff <- round(merge_time_sheet$time_diff, 2)

#################
# time summaries
#################
mean(merge_time_sheet$time_diff) # mean of 5.1 hours (even though it says secs)

##########
# data viz
##########
library(ggplot2)
work_hrs <- ggplot(merge_time_sheet, aes(date, c(time_diff))) +
                  geom_line(color = "dodgerblue") +
                  xlab("") +
                  ylab("Working Hours")
work_hrs
library(plotly)
ggplotly(work_hrs)
## provided my username and API key before this step
plotly_POST(work_hrs, "Time Series Analysis of Work Hours")


```
