print("Hello world")

print("Hello World")


"""
git init
git add .
git commit -m "first commit"
git branch -M tanzila
git remote add my_origin https://github.com/tanzila009/uzum_market.git
git push -u my_origin tanzila
"""

"""
ila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git config --global user.name "tanzila009"
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git config --global user.email "tanzilakhusanovaa@gmail.com"
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /home/tanzila/PycharmProjects/Uzum/.git/
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ ls -a
.  ..  .git  .gitignore  .idea  main.py  .venv
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git add .
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git status\
> ^C
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   .idea/.gitignore
        new file:   .idea/Uzum.iml
        new file:   .idea/inspectionProfiles/profiles_settings.xml
        new file:   .idea/misc.xml
        new file:   .idea/modules.xml
        new file:   main.py

(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ rm -rf .git
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ ls -a
.  ..  .gitignore  .idea  main.py  .venv
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /home/tanzila/PycharmProjects/Uzum/.git/
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git add .
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   main.py

(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git commit -m "uzum market projectini qurdim"
[master (root-commit) 0184c51] uzum market projectini qurdim
 2 files changed, 13 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 main.py
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git branch -M tanzila
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git remote add my_origin https://github.com/tanzila009/uzum_market.git
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git push -u my_origin tanzila
Username for 'https://github.com': tanzila009
Password for 'https://tanzila009@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 420 bytes | 420.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/tanzila009/uzum_market.git
 * [new branch]      tanzila -> tanzila
Branch 'tanzila' set up to track remote branch 'tanzila' from 'my_origin'.
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ tanzila009/uzum_market

^C
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git init
Reinitialized existing Git repository in /home/tanzila/PycharmProjects/Uzum/.git/
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ ls -a
.  ..  .git  .gitignore  .idea  main.py  .venv
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git add .
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git status
On branch tanzila
Your branch is up to date with 'my_origin/tanzila'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   main.py

(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git commit -m "yengi project"
[tanzila ad0f6a6] yengi project
 1 file changed, 3 insertions(+), 3 deletions(-)
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git branch -M tanzila
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git remote add origin https://github.com/tanzila009/amazon.git
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git push -u my_origin tanzila
Username for 'https://github.com': tanzila009
Password for 'https://tanzila009@github.com': 
remote: Repository not found.
fatal: repository 'https://github.com/tanzila009/uzum_market.git/' not found
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ rm -rf .git
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /home/tanzila/PycharmProjects/Uzum/.git/
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git add .
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git commit -m "project"
[master (root-commit) 0889c23] project
 2 files changed, 13 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 main.py
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git branch -M main
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git remote add origin https://github.com/tanzila009/amazon.git
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ git push -u origin main
Username for 'https://github.com': tanzila009
Password for 'https://tanzila009@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 410 bytes | 410.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/tanzila009/amazon.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
(.venv) tanzila@tanzila-Lenovo-V15-G2-ALC:~/PycharmProjects/Uzum$ 


pip freeze                     : library list
deactivate                     : local environment deactivate
pwd                            : current path
. .venv_name/bin/activate      : local environment activate
python3 -m venv venv_name      : local environment create
sudo apt install python3-venv  : tizimga venv o'rnatish
"""


