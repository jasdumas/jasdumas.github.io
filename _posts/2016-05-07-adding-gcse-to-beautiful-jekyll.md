---
layout: post
title: Adding a Google Custom Search Engine to your beautiful-jekyll site
---

The author and developer of the beautiful-jekyll template, [Dean Attali](http://deanattali.com/2015/03/12/beautiful-jekyll-how-to-build-a-site-in-minutes/) briefly explains the details to include a Google Custom Search Engine to your blog, but I thought I would document the tasks more succinctly for others to follow.

1. Navigate to [cse.google.com/cse](https://cse.google.com/cse/all) and add a new engine. (sign in if necessary)

2. Add the links of your beautiful-jekyll site which end in .md (all of your markdown files you want indexed for search) in the url link boxes.

3. Copy the script code which is provided after making any presentation changes in color (font, border, background, link color options are all available to customize) in the [Look and Feel section](https://cse.google.com/cse/lookandfeel/) after pressing the **"Save & Get Code"** button.

4. Create a new file called **search.md** in your main repository file structure (ie username.github.io/search.md) which will be alongside your other **.md** markdown pages. Here is where you place your copied code, wrapped in a special div

    ```
    ---
    layout: default
    title: "Search jasdumas.github.io"
    css: "/css/search.css"
    ---
    
    ## Search username.github.io with Google!
    
    <div id="google-custom-search">
    
    // Your script goes right here between the <div></div>
    
    
    </div>
    ```
5. Add this line to your **_config.yml**: `nav-search: search` underneath the **# List of links in the navigation bar section**

6. Add this section of code to your **nav.html** file which is located in your *_includes/* folder after the *endif endfor* on line 32. (i.e. before the  `</ul> </div>` lines in the `collapse navbar-collapse` section)

    ```
    {% if site.nav-search %}
    		<li>
    		  <a href="{{ site.baseurl }}/{{ site.nav-search }}" class="nav-search-link" title="Search">
    		    <span class="fa fa-search nav-search-icon"></span>
    			<span class="nav-search-text">Search</span>
    		  </a>
    		</li>
    		{% endif %}
    
    ```

7. Add this code block to the **main.css** file in the *css* folder, right above the **/* Multi-level navigation links */** line:

    ```
    .nav-search-link .nav-search-icon {
      display: none;
    }
    .nav-search-link .nav-search-text {
      display: inline;
    }
    @media only screen and (min-width: 768px) {
      .nav-search-link .nav-search-icon {
        display: inline;
      }
      .nav-search-link .nav-search-text {
        display: none;
      }
      
    }
    ```

8. Your should be all set with a nifty search icon on your beautiful-jekyll page which helps users navigate and find relevant content on your page!
