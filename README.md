# Git and Github
git -local version control system
github - cloud respository website, website that is integrated with git system,
shareable repository/location, that produces shareable link

Git
- local vs cloud (github)
- create project -> enable git (enable vsc) -. define cloud -. add the cloud link (add origin)
    -. create repository on the github -> use the link as origin
    -> configure global git configuration (name email)
    -> add file (select files ) and commit, push , pull


-----------Today------
1. Git commands you will use for local project:
cd projectDirectory
git init
git add folder1 scenario1.py
git commit -m 'message for your commit'
git status
git log
git push
git pull

2. Branching:
create new branch, switch to new branch , create pull request ( highlights the changes)
    a. Create new local branch:
        a- Pycharm:
            Select new branch option for the current branch (bottom right)
            push each branch separately, creates origin:feature1-scen1 automaticlly
        b- git bash, git CLI (command line interface)
            git checkout -b 'new-branch-name'
            git and folder1 /scenario1.py
            git commit -m 'message for your commit'
            git push
            git push -- set - upstream origin feature1-scen2

    2. Collaboration in Github:
        a. creating the pull requests, get review and approval from sr. engineer
        b. Merge your code in a your branch to master(main) branches
    3. Get github project to your local location:
        cd /c/dev
        mkdir temp
        pwd
            c/dev/temp
        git clone 'web base'
        cd pythonBasics
        git log # shows latest commit in the log
    - Igrone files
        -create .gitignore (list of files to be ignored by git)
        -you can copy the standard .gitignore file for python projects (like we did in the class)

    -MD files for project Documentation
### Markdown (.md) files for Project Documantation.
Readme files are previewed in github projects by deafult , so usually Readme files are created 
in MArdkdown language so text formal loooks more readable and neal, links images can be also included 
in the document. (most of functionalities you could in MS word or other text editors)

* marking the text as bold**
* italic test is covered with asterisk*

## Below you can see the bullet points:
-point 1 of many points
-point 2 of many points
-point 3 of many points

## Highlight the code or command line
you can highlight the code with apostrope (') or with indentation:
```Python
print('Python code inside the code black in md file')```
#this is how comment line of the python code black
``` 
```commandline
pwd
cd /c/dev/
mkdir 'pythonBasics'
# cd pythonBasics
```
b. indent the line to put in code box
    print('hello world')

## Displaying links in MD file

Please click [click here](https://github.com/Nodir0624/pythonBasics) to see more details about md features.

## Displaying the pictures in md file
you can see the picture below

![img.png](img.png)

Picture will be between the text

## Reference to the files
1. Find the examples [here](./src/functions/functions_exec.py)
2. Check the [getignore](.getignore) file as well


## References:
1. Level up github account [link](https://github.com/Nodir0624/pythonBasics).
2. [Markdown support](https://github.com/Nodir0624/pythonBasics).


