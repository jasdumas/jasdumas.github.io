---
title: 'Automating GitHub Issue Creation with Python'
layout: post
tags: [python, productivity, hacks]
social-share: true
---

I'm a stickler for To-do lists at work as they help me keep track of meeting notes, data science tasks, and professional development resources that I find. Last year, I began documenting my daily and weekly responsibilities in the form of [GitHub issues](https://help.github.com/articles/creating-an-issue/) and noticed a opportunity to automated the issue creation process, thereby saving me around ~30 seconds a day 🤣.

The first step in automating issues, comes from creating an [issue template](https://github.com/blog/2111-issue-and-pull-request-templates) in the repository (mine is called `ToDo`), which helps to standardize a format and ensures that the bare minimum amount of content is included in each issue. My issue template leverages the [task list](https://help.github.com/articles/about-task-lists/) feature, which enables me to keep track of completed tasks and offers a informative look back at how much I was able to accomplish each day or week. The format that I finally settled on includes headers for:

1. Professional development
2. Meetings
3. Tasks

![task-list-summary](https://help.github.com/assets/images/help/issues/task-list-summary.png)

The second step, that I recently implemented was automate the title of each issue, which I honestly didn't realize I could do until I spent a year creating issues with the same title conventions. ⏳ I originally started out creating a issue each day, titled: **Weekday, MM/DD/YY**, until recently where I only create a new To-do issue each week on Mondays, with formatted titles: **Week: month, day - month, day, year**. To perform this automation I wrote a small `python` function that computes the weekly date range and constructs a url which creates a new GitHub issue that [pre-fills the issue](https://eric.blog/2016/01/08/prefilling-github-issues/) title. There are actually 4 additional parameters that can be appended to the url query string, which are: body content, labels, milestone, and assignee.

For this productivity hack I only needed to have the title parameter, but the function is modifiable to include the other parameters as well. After executing the script, your browser should pop open the issue ready for you to fill out the other details and press the submit button! 🎉

```python
def create_gh_issue(owner="username", repo="ToDo"):
    '''
    Creates a new GitHub issue for a repository, which follows a
    repeatable title each week that can be semi-automated via cmd which
    alleviates a little bit of calendar guesswork.

    Arguments:
    owner: an object type of class 'str'
    repo: an object type of class 'str'

    Example use in Terminal:
    python3 create_gh_issue.py "jasdumas" "ToDo"

    Gotchas:
    make sure the repo already exists to avoid the 404 octocat!
    '''
    import datetime
    from time import strftime
    import os
    import sys
     # sys.argv[0] is the name of the script
    owner = sys.argv[1]
    repo = sys.argv[2]
    # today is usually Mondays for me
    today = datetime.date.today()
    friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
    date_range = today.strftime("%B %d") + " - " + friday.strftime("%B %d, %Y")
    # string concatenation of the query parameters
    url_stump = "https://github.com/" + owner + "/" + repo + "/issues/new?title=Week: "
    new_url = "open " + "'" + url_stump + date_range + "'"
    # launches the url in your browser
    os.popen(new_url)

create_gh_issue()

```

Here are some of the resources I used: [SO: How to print date in a regular format in Python?](https://stackoverflow.com/questions/311627/how-to-print-date-in-a-regular-format-in-python), [SO: How to calculate next Friday in Python?](https://stackoverflow.com/a/8801540/4143444), and in the future, I'm thinking about [fully automating this function on a schedule](https://stackoverflow.com/a/15090893/4143444).
