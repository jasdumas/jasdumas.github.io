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

# change attributes for plotly tooltip
attributes(merge_time_sheet$time_diff)$units <- "hours"

# so I travel through hartford alot on the highway or walk around
# hartford for lunch, so I want to remove small time diff observations
merge_time_sheet = merge_time_sheet[-c(which(merge_time_sheet$time_diff < 1)), ]

# there are some duplicates so i will remove those by distinct date
merge_time_sheet <- merge_time_sheet %>% group_by(date) %>% distinct(date, .keep_all = TRUE)

# round time diff
merge_time_sheet$time_diff <- round(merge_time_sheet$time_diff, 2)

#################
# time summaries
#################
mean(merge_time_sheet$time_diff) # mean of 5.1 hours (even though it says secs)

##########
# data viz
##########
library(ggplot2) # devtools::install_github('hadley/ggplot2')
library(dumas)
library(wesanderson)
work_hrs <- 
  merge_time_sheet %>% dplyr::filter(date <= as.Date("2016-10-17"), time_diff >= mean(time_diff)) %>% 
  ggplot(., aes(date, time_diff)) +
  geom_col(fill = wes_palette("FantasticFox1", 1), position = "dodge") +
  theme_minimal() +
  theme_jasmine(title = "Extrapolated working hours \nLocation check-ins to/from Hartford, CT", 
                subtitle = "", x = "Date", y = "Working Hours")
work_hrs
library(plotly)
ggplotly(work_hrs) # preview the interactive one

## provided my username and API key before this step
s <- signup('jasdumas', 'jasmine.dumas@gmail.com')
api_create(work_hrs, "Time Series Analysis of Work Hours", fileopt = "overwrite", sharing = "public")
