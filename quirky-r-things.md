---
title: "Quirky R things"
subtitle: "Keep R Weird"
layout: post
---
  



## Partial Matching

```r
df = data.frame("a"= letters[1:10], "abc" = 1:10)

head(df)
```

```
##   a abc
## 1 a   1
## 2 b   2
## 3 c   3
## 4 d   4
## 5 e   5
## 6 f   6
```

```r
df$ab # returns the column named "abc"
```

```
##  [1]  1  2  3  4  5  6  7  8  9 10
```

## Ploting

How did the plot function know about the x and y variables to be ploted and labeled?

```r
plot(pressure)
```

![plot of chunk quirkyplot]({{ site.url }}/post_data/quirky-r-quirkyplot-1.png)

## Sub-setting

When you subset with brackets by 1 column, the resultant is a numeric vector not a data.frame of length 1. You can then change it back into a data.frame if necessary.


```r
i = iris[, 1]
class(i)
```

```
## [1] "numeric"
```

```r
length(i)
```

```
## [1] 150
```

```r
i2 = iris[, 1:2]
class(i2)
```

```
## [1] "data.frame"
```

```r
length(i2)
```

```
## [1] 2
```

```r
nrow(i2)
```

```
## [1] 150
```

