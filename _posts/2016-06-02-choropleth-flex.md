---
layout: post
title: A Choropleth Map, Shiny, & Flexdashboard Walk into a Bar...
---

Like most R Programmers, I'm a fan of the R packages that RStudio develops. They recently announced [**Flexdashboards**](https://blog.rstudio.org/2016/05/17/flexdashboard-easy-interactive-dashboards-for-r/): Easy interactive dashboards written in RMarkdown. I'm always trying to expand my R skills with side projects so I've put together a *Flexdashboard* to visualize USA zipcodes on a *choropleth map* and a *shiny* dropdown to dynamically switch States. A choropleth map is a shaded map to show numerical variations such as population density. 

These are the general steps of the project: 

1. Locate and download shapefiles from [www2.census.gov](www2.census.gov) 
2. Locate and download zipcode data which contain corresponding zipcodes, city, county and demographic information about estimated population
3. Clean and format the zipcode data and merge with the [shapefile](https://en.wikipedia.org/wiki/Shapefile) data object
4. Create a choropleth map with the [htmlwidget: leaflet](https://rstudio.github.io/leaflet/)

Here it is: [https://jasminedumas.shinyapps.io/Choropleth_Zipcodes/](https://jasminedumas.shinyapps.io/Choropleth_Zipcodes/)

Let me know what you think!
