# In this lesson, you will learn to create a Python virtual environment, activate and use a virtual environment, install packages to that environment, deactivate and leave a virtual environment. 

# By default, when you install packages, you are installing them across your user environment. This means that they are shared by all of the projects in that environment. 
# This is mostly fine if you only develop locally. But if you wish to develop portable projects, sharing dependencies leads to two problems. 
# The first, it is challenging to determine which packages are requirements for any individual project. 
# If you recreate a requirements file from a shared environment, that file may reference packages not needed for your current project. 
# When you distribute these requirements along with your project, you are wasting time and disk space by installing unneeded packages. 
# Second, over time, you may have projects which require different versions of the same package. 
# If you are sharing the installed packages, you will need to either change the installed version whenever you change projects or constantly update older projects to use new packaged versions. 
# To avoid these challenges, it is ideal to have a unique environment per project. There are different ways to achieve this, including virtual machines and containers. 
# But a light-weight option for Python projects is Python virtual environments. 
# When you're in a Python virtual environment, packages installed are installed to that environment only. It's easy to create a virtual environment per project, and hence, keep each project's dependencies isolated. 
# When you create a virtual environment, you specify a location to store the associated packages and configuration. There are different opinions onto the best place to store your virtual environments. 
# One convention is to store all of your virtual environments in a central location, often in a subdirectory of your home directory. Another is to store them in their associated project directories. 
# The ability to create virtual environments historically depended on the package virtual env. But since Python version 3.5, a standard library module venv is provided. 
#In this lesson, we will introduce the shell commands, make directory, which is used to create a new directory, print-working directory, which displays the path of your current location, change directory, 
#which moves into a specified directory, and source, which reads and executes the contents of a file.

# The first step to setting up a new project is to create a directory to hold its code and documentation. 
# Let's create a directory named, my first project by using the make directory command. 
mkdir my_first_project 
# Now, we can change into this directory and use print-working directory to see where we are. 
cd my_first_project
pwd
# To create a virtual environment,
# we code Python with the module flag dash m, the module venv, and the path to the spot we wish to store the new environment. 
python -m venv env
# This case, we've named our environment env, and we'll store it in the current project directory. Using list, we can see that this command has created a new directory with the environment's name. 
ls
# If we peek into this directory, 
ls env
# we see three subdirectories and a configuration file. 
# In order to use our new environment, we need to activate it. 
source env/bin/activate
#We do this by sourcing the activate script, which exists in the bin subdirectory of the environment directory. 
# Now, we're in our virtual environment. We can use pip list to see that only the minimal needed packages are available. 
pip list
#If we install a package while in our environment, it will be installed for this environment only.
pip install request
# This means that if we create a requirements file in this environment, it will only reflect the packages we've installed for this project. 
# When we're ready to stop working on this project, we need to deactivate the environment. The venv module automatically supplies the deactivate command. Now we're back to our shared user environment. 
deactivate
# In this lesson, you have learned to create a virtual environment, activate and use a virtual environment, install packages to that environment only, and deactivate, leave it.
# Now it's time for you to practice with virtual environments.
