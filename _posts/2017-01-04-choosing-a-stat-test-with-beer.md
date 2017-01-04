---
layout: post
title: "Explaining Statistical Goodness of fit Tests with Beer"
subtitle: "Statistics + Beer = Comprehension"
tags: [rstats, r, statistics]
---

A [goodness of fit test](https://en.wikipedia.org/wiki/Goodness_of_fit) are a collection of statistical techniques used to summarize the differences between observed values and expected values. These tests can be used be used for hypothesis testing, testing residual normality, distribution comparisons, and outcome frequency distribution comparisons.

It can be difficult to know which statistical test to select given a problem domain and *often* the results won't point you to any mistakes if the wrong assumptions are made. In this post, I have detailed three common goodness of fit tests, the `R` code to perform the tests, interpretation of the results while using beer (analytics) in the examples.

## [Chi-squared test or χ2 test](https://en.wikipedia.org/wiki/Chi-squared_test)

*Chi-squared tests compare observed frequencies to expected frequencies given independent normally distributed data.*

For example, is the distribution of beer style and production volume by year occur by random chance or is there a difference between beer style and how much is produced as a condition of year (either higher, lower, or the same form year to year)?

The beer style and production volume attributes are independent if the probability distribution of one attribute is not affected by the presence of the other. So, let's test the (null) hypothesis that there is no difference between beer style from each of production volume figures by year at the 0.05 (5%) significance level. At this level we are accepting the 5% risk of saying that there is a difference between beer styles and production volume count when there is no actual difference.

```r
set.seed(20170103)
production = matrix(
  data = floor(runif(12, min=10000, max=20000)),
  nrow = 4,
  ncol = 3,
  dimnames = list(c("red_ale", "stout", "lager", "ipa"),
                  c(2016, 2015, 2014))
)
production
```
```r
#         2016  2015  2014
# red_ale 18421 17138 14157
# stout   18753 14833 13701
# lager   11035 16021 17017
# ipa     19180 14607 18113

```
Results:
```r
chisq.test(production)

# Pearson's Chi-squared test
#
# data:  production
# X-squared = 3267.2, df = 6, p-value < 2.2e-16
```

As the p-value is less than our significance level of 0.05 at 2.2e-16 (*there is a really low probability that this occurred just by chance*), we fail to reject the null hypothesis that there is no difference in beer style and production volume by year and can state that the alternative hypothesis that there is a difference between beer style and production volume fro year to year. As the values were randomly generated, this analysis can be furthered by exploring the potential popularity of certain styles increasing or decreasing the demand for production over the years.


## [t-Test](https://en.wikipedia.org/wiki/Student's_t-test)

*t-tests can be used to determine if two sets of data are significantly different from each other.*

For example, do brewery tour attendance differ on different weekend days - Do the amount of visitors on Saturday differ than on Sunday? let's pose the question of interest by hypothesizing that there is no difference between attendance counts for Saturday or Sunday at the 0.05 significance level.

```r
tours = data.frame("attendance_count" = floor(runif(105, min = 3, max = 35)),
                   "day" = rep(c("Saturday", "Sunday")))

head(tours)
```

```r
#   attendance_count      day
# 1               21 Saturday
# 2               17   Sunday
# 3               16 Saturday
# 4               10   Sunday
# 5                7 Saturday
# 6               11   Sunday
```
Results:
```r
t.test(attendance_count ~ day, data = tours, var.equal = TRUE)
#       Two Sample t-test
#
# data:  attendance_count by day
# t = 0, df = 104, p-value = 1
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -3.43306  3.43306
# sample estimates:
#   mean in group Saturday   mean in group Sunday
# 19                     19
```

As the p-value is larger than our 0.05 significance level, we can fail to reject the null hypothesis that there is no difference in the attendance count for each weekend day. Tis type of statistical test could be useful for breweries to determine if having tours on either day of the weekend resulted in a statistical difference in attendance.


## [ANOVA (Analysis of Variance)](https://en.wikipedia.org/wiki/Analysis_of_variance)

*ANOVA, or Analysis of Variance tests the significance of group differences between two or more groups. This tests that there is a difference between groups but not which ones are different.*

For example, do beer ratings differ between age groups, 21-25, 26-30, 31+? As a hypothesis we can state that beer ratings will be no different among age groups - Beer drinkers of all ages give the same ratings for some beer that they are surveyed on.

```r
ratings = data.frame("age_group" = c(rep("21-25", 9), rep("26-30", 9), rep("31+", 9)),
                     "rating" = floor(runif(27, min = 1, max = 5)))


head(ratings)
```

```r
#    age_group rating
# 1      21-25      1
# 2      21-25      1
# 3      21-25      4
# 4      21-25      4
# 5      21-25      1
# 6      21-25      2

```
Results:
```r
fit_anova <- aov(rating ~ age_group, data = ratings)
summary(fit_anova)


#             Df Sum Sq Mean Sq F value Pr(>F)
# age_group    2   0.22  0.1111   0.073   0.93
# Residuals   24  36.44  1.5185    
```

As the p-value is higher than our significance level, we can fail to reject the hypothesis that beer ratings are no different between age groups. We can accept the alternative hypothesis that different age groups rate beer differently. In a real world analysis, you can determine beer ratings by gathering more data between age groups or ratings from a given platform, such as [**untapped**](https://untappd.com/) or [**Beer Advocate**](https://www.beeradvocate.com/).

----

I hope this post is helpful to those interested in selecting the right statistical test for the appropriate questions!

![](http://i.giphy.com/RqbkeCZGgipSo.gif)


### Additional Resources

* [When to Use a Particular Statistical Test (PDF)](http://www.csun.edu/~amarenco/Fcs%20682/When%20to%20use%20what%20test.pdf)
* [Fitting & Interpreting Linear Models in R](http://blog.yhat.com/posts/r-lm-summary.html)
* [Independent t-test for two samples](https://statistics.laerd.com/statistical-guides/independent-t-test-statistical-guide.php)
* [WHAT A P-VALUE TELLS YOU ABOUT STATISTICAL DATA](http://www.dummies.com/education/math/statistics/what-a-p-value-tells-you-about-statistical-data/)
* [Example of Kolmogorov-Smirnov test](https://jasdumas.github.io/tech-short-papers/Example_of_Kolmogorov_Smirnov_test2.html)
* [Hypothesis Testing - Analysis of Variance (ANOVA)](http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_HypothesisTesting-ANOVA/BS704_HypothesisTesting-Anova_print.html)
* [Five 2016 beer statistics and why they matter](http://draftmag.com/five-2016-beer-statistics-and-why-they-matter/)
