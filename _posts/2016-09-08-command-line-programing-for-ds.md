---
layout: post
title: Command Line Programming for Data Scientists
subtitle: Navigating the cmd and terminal
tags: [data-analysis, data-science, command-line]
---

### Why command line programming is essential to the Data Science Toolkit

**TL;DR:** You are going to use it whether you like it or not as part of your data science workflow, but it can be very useful and portable skill set that can transcend other platforms and tools.

The command line is that 'cryptic' executable program on your Mac or PC with the blinking prompt that you always see your local computer scientist feverishly typing in to at a coffee shop or in the office. The mystical whir of a dark screen with [consolas](https://en.wikipedia.org/wiki/Consolas) type font always evokes a mysterious skill that seems like it takes a lifetime to acquire. As my data science career is in the early stages, I've picked up some command line programming skills from a former internship which took me to the outer reaches of data analysis, gene prediction, and python, **ALL** in the command line. This was a daunting and enlightening experience as I diligently worked to support the post-doc bioinformatician I was working alongside. A few months later in my current experience as a Data Scientist in Industry, I'm becoming inundated with various programs and software tools, but a constant remains for using the command line but lo and behold my needs for both Windows and unix command line programming surfaces. I frequently find myself mixing up Unix commands in the Windows command line which can be confusing for new data scientists. :sadface:

Since the command line is not a program for wizards but a effective tool for anyone interested in leveling-up their data processing, I've taken a nod from a [2010 post by Hilary Mason and Chris Wiggins](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/) and have listed some useful commands and resources for **both** the terminal (unix & MacOS) and cmd (windows) that *somewhat follows* the data analysis work-flow method which can consist of: obtaining data, cleaning & pre-processing, exploration, and working and sharing with others and over different server systems.


### Useful commands

#### 1. Obtain:
_terminal(unix & MacOS)_

* `pwd`: print your working directory
* `cd`: change your working directory
* `curl`: can download pages and it can upload files and post data to web sites.
* `wget`: used to grab pages from a web site; either to test that they are available or to download them and can also be used to recursively download an entire site. [Source](http://www.computerworld.com/article/2992017/operating-systems/the-joy-of-curl.html)
* `scp -r <path_to_directory> <your_username>@<host_name>:` recursively upload/copy files from your local machine to the server (remove the `-r` for single files)
* `mv`: move files between folder locations [Source](https://www.unix.com/learn/how-move-files-using-unix-commands-or-file-managers)

_cmd (windows)_

* `cd`: change your working directory
* `cd .`: navigate to your current directory
* `cd ..`: navigate up/back one directory
* `move`: Specifies the location and name of the file or files you want to move.

#### 2. Scrub:
_terminal(unix & MacOS)_

* `sed`: Find and replace in text files. (sed 's/FindThisWord/ReplaceWithThisWord/g' file.txt) [Source](http://www.techradar.com/how-to/computing/apple/terminal-101-find-and-replace-using-sed-1305723)
* `awk`: awk is a utility/language designed for data extraction. One of the most simple and popular uses of awk is selecting a column from a text file or other command's output. [Source](https://unixconfig.org/learning-unix-commands-awk)
* `grep`: grep searches the named input FILEs (or standard input if no files are named, or if a single hyphen-minus (-) is given as file name) for lines containing a match to the given PATTERN. By default, grep prints the matching lines. [Source](https://www.techonthenet.com/unix/commands/grep.php )

_cmd (windows)_

* `get-content`: Gets the content of the item at the specified location. (`get-content somefile.txt | where { $_ -match "expression"}`) [Source on stackoverflow answer](http://stackoverflow.com/a/6028937/4143444)


#### 3. Explore:
_terminal(unix & MacOS)_

* `ls`: display files and folders in the current directory
* `tail -lines`: view the end of a file by specifying the number of lines to show
* `more`: more is a command to view (but not modify) the contents of a text file one screen at a time.
* `less`: less is a terminal pager program on Unix, Windows, and Unix-like systems used to view (but not change) the contents of a text file one screen at a time. It is similar to more, but has the extended capability of allowing both forward and backward navigation through the file. Unlike most Unix text editors/viewers, less does not need to read the entire file before starting, resulting in faster load times with large files. [Source](https://en.wikipedia.org/wiki/Less_(Unix) )
* `cut`: cut is used for text processing. You can use this command to extract portion of text from a file by selecting columns.
* http://www.gnuplot.info/: gnuplot is a command-line driven interactive function plotting utility for unix, OSX, Windows, VMS, and many other platforms.  The software is copyrighted but freely distributed (i.e., you don't have to pay for it). It was originally intended as graphical program to allow scientists and students to visualize mathematical functions and data.

_cmd (windows)_

* `dir`: display files and folders in the current directory to explore the contents
* `head -lines`: view the beginning of a file


#### 4. Reproducibility:
_terminal(unix & MacOS)_

* `vi`: write shell scripts for R and python in the vim editor and execute them.
* `chmod 777`: change file permission so that you, the group and the world can work with the files. [Figure out which numbers to supply based on security needs](http://www.onlineconversion.com/html_chmod_calculator.htm)
* `touch`: The touch command is the easiest way to create new, empty files.
* `cat`: The cat (short for 'concatenate') command is one of the most frequently used command in unix/Unix like operating systems. cat command allows us to create single or multiple files, view contain of file, concatenate files and redirect output in terminal or files.
* `pipe`: A pipe is a form of redirection that is used in unix and other Unix-like operating systems to send the output of one program to another program for further processing. [Source](http://www.linfo.org/pipes.html )

_cmd (windows)_

* `notepad filename.txt`: write and edit files. [Source](http://superuser.com/a/186860)

### Additional Resources

1. [The OSEMN method by Hilary Mason and Chris Wiggins](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/)

2. [A Quick Introduction to Unix (Wikibook)](https://en.wikibooks.org/wiki/A_Quick_Introduction_to_Unix/Job_Control)

3. [University of Connecticut (UCONN) Bioinformatics Lab Unix Tutorial](http://bioinformatics.uconn.edu/unix-basics/)

4. [Introduction to the command-line interface from the Django Girls](http://tutorial.djangogirls.org/en/intro_to_command_line/)

5. [A Command Line Primer for Beginners](http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything)

#### Notes:
* This list notably light on cmd (Windows) commands - I plan to update this post as I discover more useful features of the command line for both operating systems.
