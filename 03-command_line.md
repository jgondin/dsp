# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

- **pwd**: print current work-directory.
- **cd**: change directory.
- **ls**: list directory.
- **head**: print the first part of the text file.
- **tail**: print the final part of the text file.
- **cat**: contatena file.
- **>**: sign output into.
- **find**: search for file.
- **man**: print manual page.
- **kill**: kill a process

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>

- `ls`: list directory.
- `ls -a` list 'all' directory, i.e. including hiden files.
- `ls -l` list directory with info (permitions, group, size e others).
- `ls -lh` list directory with info, but display size in readable format (2G, 30M, 100K). 
- `ls -lah` list all directory with info, but display size in readable format.
- `ls -t` list directory sorted by time modification.
- `ls -Glp` list directory with info excepted by group, but append "/" to indicate directory.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

- **a**: Display all files.
- **l**: Display a long format list.
- **t**: Displays newest files first.
- **R**: Displays subdirectories as well.
- **u**: Displays files by the file access time.


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs combine multipos commands.

ls -m ~/metis/bootcamp/dsp/  | xargs -n 2 >> list.txt

It take 2 by 2 elements of the list "ls -m ~/metis/bootcamp/dsp/" and add to the end of list.txt 



 

