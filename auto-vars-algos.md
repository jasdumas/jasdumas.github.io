---
title: "Automated Variable Selection Algorithms"
date: "November 06, 2016"
layout: page
---





# Get the data

```r
load("~/Desktop/depaul/CSC423/rdata/R/Exercises&Examples/EXEXSAL2.Rdata")
```

# Backward Elimination Selection

* Starts will all variables.
* Drops one variable at a time until dropping another variable no longer improves the model.
* Once a variable is dropped it cannot re-enter the model.
* With AIC criteria (which R uses here) lower is better. Note: lowest may include most negative.
* AIC = Akaike's Information Criteria = n * ln(SSE/n) + 2 * p


```r
library(MASS)
full.model <- lm(Y~X1+X2+X3+X4+X5+X6+X7+X8+X9+X10, data=EXEXSAL2)
model = step(full.model, direction="backward")
```

```
## Start:  AIC=-504.84
## Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9 + X10
## 
##        Df Sum of Sq     RSS     AIC
## - X10   1   0.00063 0.51583 -506.71
## - X7    1   0.00073 0.51593 -506.70
## - X8    1   0.00153 0.51673 -506.54
## - X6    1   0.00482 0.52002 -505.91
## - X9    1   0.00984 0.52504 -504.94
## <none>              0.51520 -504.84
## - X5    1   0.08810 0.60330 -491.05
## - X2    1   0.41581 0.93102 -447.66
## - X4    1   0.63133 1.14653 -426.84
## - X3    1   0.99872 1.51393 -399.05
## - X1    1   1.43512 1.95032 -373.72
## 
## Step:  AIC=-506.71
## Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9
## 
##        Df Sum of Sq     RSS     AIC
## - X7    1   0.00050 0.51633 -508.62
## - X8    1   0.00149 0.51732 -508.43
## - X6    1   0.00448 0.52031 -507.85
## - X9    1   0.00992 0.52575 -506.81
## <none>              0.51583 -506.71
## - X5    1   0.08769 0.60352 -493.01
## - X2    1   0.41593 0.93176 -449.59
## - X4    1   0.63878 1.15461 -428.14
## - X3    1   1.03375 1.54959 -398.72
## - X1    1   1.52826 2.04409 -371.02
## 
## Step:  AIC=-508.62
## Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X8 + X9
## 
##        Df Sum of Sq    RSS     AIC
## - X8    1    0.0015 0.5178 -510.33
## - X6    1    0.0040 0.5203 -509.85
## - X9    1    0.0096 0.5260 -508.77
## <none>              0.5163 -508.62
## - X5    1    0.0898 0.6061 -494.58
## - X2    1    0.4243 0.9406 -450.64
## - X4    1    0.6384 1.1547 -430.13
## - X3    1    1.0503 1.5666 -399.62
## - X1    1    3.9764 4.4927 -294.27
## 
## Step:  AIC=-510.33
## Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X9
## 
##        Df Sum of Sq    RSS     AIC
## - X6    1    0.0033 0.5211 -511.69
## - X9    1    0.0089 0.5267 -510.64
## <none>              0.5178 -510.33
## - X5    1    0.0885 0.6064 -496.55
## - X2    1    0.4230 0.9408 -452.62
## - X4    1    0.6420 1.1598 -431.69
## - X3    1    1.0490 1.5668 -401.61
## - X1    1    3.9749 4.4927 -296.27
## 
## Step:  AIC=-511.69
## Y ~ X1 + X2 + X3 + X4 + X5 + X9
## 
##        Df Sum of Sq    RSS     AIC
## - X9    1    0.0093 0.5304 -511.93
## <none>              0.5211 -511.69
## - X5    1    0.0947 0.6159 -496.99
## - X2    1    0.4347 0.9558 -453.04
## - X4    1    0.6868 1.2079 -429.63
## - X3    1    1.0466 1.5677 -403.55
## - X1    1    3.9718 4.4929 -298.27
## 
## Step:  AIC=-511.93
## Y ~ X1 + X2 + X3 + X4 + X5
## 
##        Df Sum of Sq    RSS     AIC
## <none>              0.5304 -511.93
## - X5    1    0.0879 0.6183 -498.59
## - X2    1    0.4289 0.9594 -454.67
## - X4    1    0.6908 1.2212 -430.53
## - X3    1    1.0656 1.5961 -403.76
## - X1    1    3.9627 4.4932 -300.26
```

```r
summary(model)
```

```
## 
## Call:
## lm(formula = Y ~ X1 + X2 + X3 + X4 + X5, data = EXEXSAL2)
## 
## Residuals:
##       Min        1Q    Median        3Q       Max 
## -0.201219 -0.056016 -0.003581  0.053656  0.187251 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 9.9619345  0.1010567  98.578  < 2e-16 ***
## X1          0.0272762  0.0010293  26.501  < 2e-16 ***
## X2          0.0290921  0.0033367   8.719 9.71e-14 ***
## X3          0.2246932  0.0163503  13.742  < 2e-16 ***
## X4          0.0005244  0.0000474  11.064  < 2e-16 ***
## X5          0.0019623  0.0004972   3.947 0.000153 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.07512 on 94 degrees of freedom
## Multiple R-squared:  0.9206,	Adjusted R-squared:  0.9164 
## F-statistic: 218.1 on 5 and 94 DF,  p-value: < 2.2e-16
```

```r
plot(model)
```

![plot of chunk unnamed-chunk-2]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-2-1.png)![plot of chunk unnamed-chunk-2]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-2-2.png)![plot of chunk unnamed-chunk-2]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-2-3.png)![plot of chunk unnamed-chunk-2]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-2-4.png)

# Forward Selection

* Adds one variable at a time until adding a new variable no longer improves the model.
* Once a variable is added, it never leaves the model.
* With AIC criteria (which R uses here) lower is better.


```r
min.model = lm(Y ~ 1, data=EXEXSAL2)          # aka intercept only model
biggest = formula(lm(Y ~ ., data=EXEXSAL2))   # note dot: all variables, including ID
model = step(min.model, direction='forward', scope=biggest)
```

```
## Start:  AIC=-268.57
## Y ~ 1
## 
##        Df Sum of Sq    RSS     AIC
## + X1    1    4.1364 2.5462 -363.06
## + X7    1    2.6488 4.0338 -317.05
## + X3    1    1.0492 5.6335 -283.64
## + X2    1    0.3264 6.3563 -271.57
## + X4    1    0.2897 6.3930 -271.00
## + X5    1    0.2774 6.4052 -270.81
## <none>              6.6827 -268.57
## + X10   1    0.0201 6.6625 -266.87
## + X8    1    0.0181 6.6646 -266.84
## + X6    1    0.0169 6.6657 -266.82
## + ID    1    0.0004 6.6823 -266.57
## + X9    1    0.0002 6.6824 -266.57
## 
## Step:  AIC=-363.06
## Y ~ X1
## 
##        Df Sum of Sq    RSS     AIC
## + X3    1   0.87027 1.6760 -402.88
## + X2    1   0.32522 2.2210 -374.72
## + X4    1   0.31253 2.2337 -374.15
## + X5    1   0.26811 2.2781 -372.18
## <none>              2.5462 -363.06
## + X6    1   0.04591 2.5003 -362.87
## + X10   1   0.04132 2.5049 -362.69
## + ID    1   0.01878 2.5274 -361.80
## + X8    1   0.01466 2.5316 -361.63
## + X7    1   0.00843 2.5378 -361.39
## + X9    1   0.00381 2.5424 -361.21
## 
## Step:  AIC=-402.88
## Y ~ X1 + X3
## 
##        Df Sum of Sq    RSS     AIC
## + X4    1   0.60068 1.0753 -445.26
## + X2    1   0.28150 1.3945 -419.27
## + X5    1   0.19195 1.4840 -413.04
## + X6    1   0.10205 1.5739 -407.16
## + ID    1   0.09293 1.5830 -406.58
## <none>              1.6760 -402.88
## + X8    1   0.00735 1.6686 -401.32
## + X10   1   0.00137 1.6746 -400.96
## + X9    1   0.00022 1.6757 -400.89
## + X7    1   0.00000 1.6760 -400.88
## 
## Step:  AIC=-445.26
## Y ~ X1 + X3 + X4
## 
##        Df Sum of Sq     RSS     AIC
## + X2    1   0.45697 0.61832 -498.59
## + X5    1   0.11593 0.95936 -454.67
## + ID    1   0.04073 1.03456 -447.12
## + X6    1   0.02841 1.04688 -445.94
## <none>              1.07529 -445.26
## + X7    1   0.00623 1.06906 -443.84
## + X8    1   0.00622 1.06907 -443.84
## + X10   1   0.00044 1.07485 -443.30
## + X9    1   0.00003 1.07526 -443.26
## 
## Step:  AIC=-498.59
## Y ~ X1 + X3 + X4 + X2
## 
##        Df Sum of Sq     RSS     AIC
## + X5    1  0.087902 0.53041 -511.93
## <none>              0.61832 -498.59
## + X6    1  0.009688 0.60863 -498.17
## + ID    1  0.003614 0.61470 -497.18
## + X9    1  0.002451 0.61587 -496.99
## + X8    1  0.001376 0.61694 -496.82
## + X7    1  0.000343 0.61797 -496.65
## + X10   1  0.000000 0.61832 -496.59
## 
## Step:  AIC=-511.93
## Y ~ X1 + X3 + X4 + X2 + X5
## 
##        Df Sum of Sq     RSS     AIC
## <none>              0.53041 -511.93
## + X9    1 0.0092875 0.52113 -511.69
## + X6    1 0.0037568 0.52666 -510.64
## + ID    1 0.0014483 0.52897 -510.20
## + X10   1 0.0003588 0.53006 -509.99
## + X8    1 0.0002463 0.53017 -509.97
## + X7    1 0.0000122 0.53040 -509.93
```

```r
summary(model)
```

```
## 
## Call:
## lm(formula = Y ~ X1 + X3 + X4 + X2 + X5, data = EXEXSAL2)
## 
## Residuals:
##       Min        1Q    Median        3Q       Max 
## -0.201219 -0.056016 -0.003581  0.053656  0.187251 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 9.9619345  0.1010567  98.578  < 2e-16 ***
## X1          0.0272762  0.0010293  26.501  < 2e-16 ***
## X3          0.2246932  0.0163503  13.742  < 2e-16 ***
## X4          0.0005244  0.0000474  11.064  < 2e-16 ***
## X2          0.0290921  0.0033367   8.719 9.71e-14 ***
## X5          0.0019623  0.0004972   3.947 0.000153 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.07512 on 94 degrees of freedom
## Multiple R-squared:  0.9206,	Adjusted R-squared:  0.9164 
## F-statistic: 218.1 on 5 and 94 DF,  p-value: < 2.2e-16
```

```r
plot(model)
```

![plot of chunk unnamed-chunk-3]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-3-1.png)![plot of chunk unnamed-chunk-3]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-3-2.png)![plot of chunk unnamed-chunk-3]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-3-3.png)![plot of chunk unnamed-chunk-3]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-3-4.png)

# Stepwise Regression Selection

* Adds one variable at a time until adding a new variable no longer improves the model.
* A variable may leave and re-enter the model many times.
* With AIC criteria (which R uses) lower is better.
* Note I am reusing full.model here.


```r
model = step(full.model, direction="both")
```

```
## Start:  AIC=-504.84
## Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9 + X10
## 
##        Df Sum of Sq     RSS     AIC
## - X10   1   0.00063 0.51583 -506.71
## - X7    1   0.00073 0.51593 -506.70
## - X8    1   0.00153 0.51673 -506.54
## - X6    1   0.00482 0.52002 -505.91
## - X9    1   0.00984 0.52504 -504.94
## <none>              0.51520 -504.84
## - X5    1   0.08810 0.60330 -491.05
## - X2    1   0.41581 0.93102 -447.66
## - X4    1   0.63133 1.14653 -426.84
## - X3    1   0.99872 1.51393 -399.05
## - X1    1   1.43512 1.95032 -373.72
## 
## Step:  AIC=-506.71
## Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9
## 
##        Df Sum of Sq     RSS     AIC
## - X7    1   0.00050 0.51633 -508.62
## - X8    1   0.00149 0.51732 -508.43
## - X6    1   0.00448 0.52031 -507.85
## - X9    1   0.00992 0.52575 -506.81
## <none>              0.51583 -506.71
## + X10   1   0.00063 0.51520 -504.84
## - X5    1   0.08769 0.60352 -493.01
## - X2    1   0.41593 0.93176 -449.59
## - X4    1   0.63878 1.15461 -428.14
## - X3    1   1.03375 1.54959 -398.72
## - X1    1   1.52826 2.04409 -371.02
## 
## Step:  AIC=-508.62
## Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X8 + X9
## 
##        Df Sum of Sq    RSS     AIC
## - X8    1    0.0015 0.5178 -510.33
## - X6    1    0.0040 0.5203 -509.85
## - X9    1    0.0096 0.5260 -508.77
## <none>              0.5163 -508.62
## + X7    1    0.0005 0.5158 -506.71
## + X10   1    0.0004 0.5159 -506.70
## - X5    1    0.0898 0.6061 -494.58
## - X2    1    0.4243 0.9406 -450.64
## - X4    1    0.6384 1.1547 -430.13
## - X3    1    1.0503 1.5666 -399.62
## - X1    1    3.9764 4.4927 -294.27
## 
## Step:  AIC=-510.33
## Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X9
## 
##        Df Sum of Sq    RSS     AIC
## - X6    1    0.0033 0.5211 -511.69
## - X9    1    0.0089 0.5267 -510.64
## <none>              0.5178 -510.33
## + X8    1    0.0015 0.5163 -508.62
## + X7    1    0.0005 0.5173 -508.43
## + X10   1    0.0004 0.5174 -508.41
## - X5    1    0.0885 0.6064 -496.55
## - X2    1    0.4230 0.9408 -452.62
## - X4    1    0.6420 1.1598 -431.69
## - X3    1    1.0490 1.5668 -401.61
## - X1    1    3.9749 4.4927 -296.27
## 
## Step:  AIC=-511.69
## Y ~ X1 + X2 + X3 + X4 + X5 + X9
## 
##        Df Sum of Sq    RSS     AIC
## - X9    1    0.0093 0.5304 -511.93
## <none>              0.5211 -511.69
## + X6    1    0.0033 0.5178 -510.33
## + X8    1    0.0008 0.5203 -509.85
## + X10   1    0.0003 0.5209 -509.74
## + X7    1    0.0000 0.5211 -509.70
## - X5    1    0.0947 0.6159 -496.99
## - X2    1    0.4347 0.9558 -453.04
## - X4    1    0.6868 1.2079 -429.63
## - X3    1    1.0466 1.5677 -403.55
## - X1    1    3.9718 4.4929 -298.27
## 
## Step:  AIC=-511.93
## Y ~ X1 + X2 + X3 + X4 + X5
## 
##        Df Sum of Sq    RSS     AIC
## <none>              0.5304 -511.93
## + X9    1    0.0093 0.5211 -511.69
## + X6    1    0.0038 0.5267 -510.64
## + X10   1    0.0004 0.5301 -509.99
## + X8    1    0.0002 0.5302 -509.97
## + X7    1    0.0000 0.5304 -509.93
## - X5    1    0.0879 0.6183 -498.59
## - X2    1    0.4289 0.9594 -454.67
## - X4    1    0.6908 1.2212 -430.53
## - X3    1    1.0656 1.5961 -403.76
## - X1    1    3.9627 4.4932 -300.26
```

```r
summary(model)
```

```
## 
## Call:
## lm(formula = Y ~ X1 + X2 + X3 + X4 + X5, data = EXEXSAL2)
## 
## Residuals:
##       Min        1Q    Median        3Q       Max 
## -0.201219 -0.056016 -0.003581  0.053656  0.187251 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 9.9619345  0.1010567  98.578  < 2e-16 ***
## X1          0.0272762  0.0010293  26.501  < 2e-16 ***
## X2          0.0290921  0.0033367   8.719 9.71e-14 ***
## X3          0.2246932  0.0163503  13.742  < 2e-16 ***
## X4          0.0005244  0.0000474  11.064  < 2e-16 ***
## X5          0.0019623  0.0004972   3.947 0.000153 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.07512 on 94 degrees of freedom
## Multiple R-squared:  0.9206,	Adjusted R-squared:  0.9164 
## F-statistic: 218.1 on 5 and 94 DF,  p-value: < 2.2e-16
```

```r
plot(model)
```

![plot of chunk unnamed-chunk-4]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-4-1.png)![plot of chunk unnamed-chunk-4]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-4-2.png)![plot of chunk unnamed-chunk-4]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-4-3.png)![plot of chunk unnamed-chunk-4]({{ site.url }}/post_data/auto-vars-algos-unnamed-chunk-4-4.png)

# Best-N Subset aka All Possible Regressions Selection

* Use leaps library.
* nbest shows n best models for each k predictors, for at most n*(k-1)+1 models
* For Mallow's Cp, want Cp “small and near” p (recall p = k + 1) (See slides, quote from SAS Support about Cp)
* Can use method=“Cp” then model$Cp, or method=“adjr2” then model$adjr2

## Best Subset using Cp


```r
library(leaps)
yvar = c("Y")
xvars = c("X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10")
model=leaps( x=EXEXSAL2[,xvars], y=EXEXSAL2[,yvar], names=xvars, nbest=3, method="Cp")
model$which
```

```
##       X1    X2    X3    X4    X5    X6    X7    X8    X9   X10
## 1   TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 1  FALSE FALSE FALSE FALSE FALSE FALSE  TRUE FALSE FALSE FALSE
## 1  FALSE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 2   TRUE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 2   TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 2   TRUE FALSE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE
## 3   TRUE FALSE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE
## 3   TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 3   TRUE FALSE  TRUE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE
## 4   TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE
## 4   TRUE FALSE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE
## 4   TRUE FALSE  TRUE  TRUE FALSE  TRUE FALSE FALSE FALSE FALSE
## 5   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE
## 5   TRUE  TRUE  TRUE  TRUE FALSE  TRUE FALSE FALSE FALSE FALSE
## 5   TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE  TRUE FALSE
## 6   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE FALSE
## 6   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE
## 6   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE  TRUE
## 7   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE FALSE
## 7   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE  TRUE FALSE
## 7   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE  TRUE
## 8   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE FALSE
## 8   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE FALSE
## 8   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE  TRUE
## 9   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE
## 9   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE  TRUE
## 9   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE
## 10  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE
```

```r
model$Cp
```

```
##  [1] 343.856582 600.834586 877.170522 195.519164 289.674910 291.866952
##  [7]  93.753768 148.889945 164.360626  16.812839  75.726709  90.845632
## [13]   3.627915  17.139335  18.389402   4.023513   4.978942   5.565934
## [19]   5.449923   5.885472   5.979924   7.195556   7.365877   7.384948
## [25]   9.109093   9.125678   9.263650  11.000000
```

## Best Subset using adjr2


```r
yvar = c("Y")
xvars = c("X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10")
model=leaps( x=EXEXSAL2[,xvars], y=EXEXSAL2[,yvar], names=xvars, nbest=3, method="adjr2")
model$which
```

```
##       X1    X2    X3    X4    X5    X6    X7    X8    X9   X10
## 1   TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 1  FALSE FALSE FALSE FALSE FALSE FALSE  TRUE FALSE FALSE FALSE
## 1  FALSE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 2   TRUE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 2   TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 2   TRUE FALSE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE
## 3   TRUE FALSE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE
## 3   TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## 3   TRUE FALSE  TRUE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE
## 4   TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE
## 4   TRUE FALSE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE
## 4   TRUE FALSE  TRUE  TRUE FALSE  TRUE FALSE FALSE FALSE FALSE
## 5   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE
## 5   TRUE  TRUE  TRUE  TRUE FALSE  TRUE FALSE FALSE FALSE FALSE
## 5   TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE  TRUE FALSE
## 6   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE FALSE
## 6   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE
## 6   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE  TRUE
## 7   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE FALSE
## 7   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE  TRUE FALSE
## 7   TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE  TRUE
## 8   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE FALSE
## 8   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE FALSE
## 8   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE  TRUE
## 9   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE
## 9   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE  TRUE
## 9   TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE
## 10  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE
```

```r
model$adjr2
```

```
##  [1] 0.6150915 0.3902159 0.1484006 0.7440365 0.6607935 0.6588555 0.8340647
##  [8] 0.7848111 0.7709910 0.9035788 0.8503966 0.8367486 0.9164065 0.9040798
## [15] 0.9029394 0.9169871 0.9161061 0.9155648 0.9166195 0.9162135 0.9161254
## [22] 0.9159429 0.9157824 0.9157644 0.9150913 0.9150755 0.9149441 0.9142424
```


# Additional Learning Resources

+ [Variable selection using automatic methods](https://www.r-bloggers.com/variable-selection-using-automatic-methods/)
+ [Variable selection via Columbia Stats](http://www.stat.columbia.edu/~martin/W2024/R10.pdf)
+ [Original Resource](http://billqualls.com/csc423/csc423_ex_06_01_r.html)



