---
layout: post
title: Adding Tags to your beautiful-jekyll site
tags: [website, design, beautiful-jekyll]
---


There are a lot of [inquires](http://pavdmyt.com/how-to-implement-tags-at-jekyll-website/) and [posts](http://charliepark.org/tags-in-jekyll/) to add tags to jekyll-powered blogs on GitHub. Here is a step-by-side guide on how to add a tag in order to creates a designated XML feed, necessary if you want to list your blog aggregators and sites such as [R-bloggers](https://www.r-bloggers.com/). Some features are extra to add social share buttons the the bottom of the page.

* Create a file called **share-section.html** in the "includes" folder:

```
{% if page.show-share or page.show-subscribe %}
  <div class="share-section">
    <h1 class="share-title">Liked what you read?</h1>

    {% if page.show-share %}
      <div class="share-buttons">
        {% capture urlmessage %}{{ site.url }}/contact{% endcapture %}

        {% capture urlfb %}https://www.facebook.com/dialog/feed?app_id={{ site.fb_app_id }}&link={{ site.url }}{{ page.url }}&name={{ page.title }}&caption={{ site.url-pretty }}&redirect_uri={{ site.url }}{{ page.url }}?message=Thanks for sharing!{% endcapture %}
        {% if page.share-img %}
          {% capture urlfb %}{{ urlfb }}&picture={{ page.share-img }}{% endcapture %}
        {% endif %}

        {% capture urltwitter %}https://twitter.com/intent/tweet?url={{ site.url }}{{ page.url }}&via=jasdumas{% endcapture %}
        {% if page.tags contains 'rstats' %}
          {% assign maxlength = 94 %}
          {% capture urltwitter %}{{ urltwitter }}&hashtags=rstats{% endcapture %}
        {% else %}
          {% assign maxlength = 102 %}
        {% endif %}
        {% capture urltwitter %}{{ urltwitter }}&text={{ page.title | truncate: maxlength }}{% endcapture %}

        <a href="{{ urlmessage }}" data-ga-event=1 data-ga-category="share" data-ga-action="message" data-ga-label="{{ page.url }}">
          Let me know
        </a>
        <!--
        <a href="{{ urlfb }}" data-ga-event=1 data-ga-category="share" data-ga-action="facebook" data-ga-label="{{ page.url }}">
          Share on Facebook
        </a>
        -->

        <a href="{{ urltwitter }}" data-ga-event=1 data-ga-category="share" data-ga-action="twitter" data-ga-label="{{ page.url }}">
          Tweet it
        </a>
      </div>
    {% endif %}
  </div>
{% endif %}
```

* Edit the css file **main.css** with the following code above the /*--- Pager ---*/ section label:

```
blog-tags {
  font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  color: #999;
  font-size: 15px;
  margin-bottom: 30px;
 }
```

* Edit the existing **feed.xml** file which lives in the root folder of the GitHub repo:

```
{% if post.tags %}
  {% for tag in post.tags %}
  <category>{{ tag | xml_escape }}</category>
    {% endfor %}
{% endif %}
{% if post.categories %}
{% for tag in post.categories %}
<category>{{ tag | xml_escape }}</category>
 {% endfor %}
 {% endif %}
```

* Create a file called **r-bloggers-feed.xml** in the root folder of the GitHub repo:

```
---
layout: null
sitemap:
  exclude: true
---
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{{ "Jasmine Dumas' R Blog" | xml_escape }}</title>
    <description>{{ "RSS feed especialy for R-bloggers" | xml_escape }}</description>
    <link>{{ site.url }}</link>
    <atom:link href="{{ site.url }}/feed.xml" rel="self" type="application/rss+xml" />
    {% for post in site.posts limit:50 %}
	{% if post.tags and post.tags contains "rstats" %}
      <item>
        <title>{{ post.title | xml_escape }}</title>
		<description>
		  {% if post.subtitle %}{{ post.subtitle | xml_escape }} - {% endif %}
		  {{ post.content | xml_escape }}
		</description>
        <pubDate>{{ post.date | date_to_rfc822 }}</pubDate>
        <link>{{ site.url }}{{ post.url }}</link>
        <guid isPermaLink="true">{{ site.url }}{{ post.url }}</guid>
		{% if post.tags %}
		  {% for tag in post.tags %}
		    <category>{{ tag | xml_escape }}</category>
		  {% endfor %}
		{% endif %}
		{% if post.categories %}
		  {% for tag in post.categories %}
		    <category>{{ tag | xml_escape }}</category>
		  {% endfor %}
		{% endif %}
      </item>
	{% endif %}
    {% endfor %}
  </channel>
</rss>
```

* Edit your **exiting posts** and add the tags line in the **yaml** header:

```
tags: [website, design, rstats]
```

* Congrats! - check out your newly rendered blog posts with the social share buttons at the bottom and the new tags created. Visit your new XML feed by going to the page, for example: [jasdumas.github.io/r-bloggers-feed.xml](http://jasdumas.github.io/r-bloggers-feed.xml) - it will have a collection of your tagged post ready to submit to a blog roll.
