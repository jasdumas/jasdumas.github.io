## Lasso regression for Coursera Machine Learning for Data Analysis
# http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.names
library(RCurl)
url = getURL("http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv")
forest_fires <- read.csv(text = url)
head(forest_fires)
# get a model matrix
ff_clean = model.matrix(~.,  data=forest_fires)
ff_clean = as.data.frame(ff_clean)
# write the csv file to my coursera folder
library(readr)
write_csv(x=ff_clean, path="C:/Users/JD87417/Desktop/python work/Coursera/forest_fires.csv")
# get column print out for python (line 19)
library(pystr)
cols = colnames(ff_clean)
dput(pystr_upper(cols))
