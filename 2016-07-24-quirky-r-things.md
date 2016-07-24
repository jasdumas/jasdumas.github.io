---
title: "Quirky R things"
subtitle: "Keep R Weird"
layout: page
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

