### data has been modified in excel intially to remove NA's as ? and colnames have been added

library(readr)
adult <- read_csv("C:/Users/JD87417/Desktop/python work/Coursera/adult_income.csv")
View(adult)
adult$income_target_binary <- ifelse(adult$income_target == ">50K", 1, 0)

adult2 <- model.matrix(income_target_binary ~., data = adult)
adult2 <- as.data.frame(adult2)
dput(colnames(adult2)) # get colnames
colnames(adult2)[98] = "income_target_50k"

write_csv(x=adult2, path="C:/Users/JD87417/Desktop/python work/Coursera/adult2_income.csv")
