#  I will show you how to save the current state of your Python package installation to a requirements file. How to uninstall packages enumerated in a requirements file and how to install packages using a requirement file.

# Once you have installed the packages, you need to implement a Python project as the best practice to save a record of these packages. This makes your project portable, 
# which means that you can set your project to run on different machines.

# For example, once you have your Python program working, you might want to move it to a production server or share it with a colleague for their use. 
# In either case, you will need to document the packages your program needs to run. As part of this lesson, we will use two shell commands, list and cat.
#    List shows the contents of the current directory or if we supply a path, the contents of that path.
ls
# Cat will echo the contents of a file to your screen, remember that the pip list command will display the current installed packages and their version numbers.
cat

# Let's see what we have installed in this environment.
pip list
# The pip freeze command displays the same information, But in a format that can be used with the installed and uninstalled commands. 
pip freeze
# We can redirect the output from pip freeze to a file by using the redirect operator which is the right words arrow.
pip freeze > requirements.txt
# Here, we are out putting the text to a file named requirements dot text, any file name will work at the convention is to name it requirements detect.

# We can use the cat command to see the contents of the file by typing cat filed by the file names.
cat requirements.txt

# See that the packages listed the file match those installed in our environment. 
# To uninstall the package is enumerated in the file, use the dash our flag the file name with pip installed.
pip -r uninstall requirements.txt

# We can see with pip list that the only packages left are those required for pip's use. 
# The more common usage is to combine their requirements file with pips installed command, once again using the dash our flag and the file name.
pip install -r requirements.txt
# And once again, we can check the results using the pip list command.

# This is the standard way to install packages for someone else's project that you are setting up, or for your own project in a new environment. 
# In this lesson, you have learned how to create a requirements file, continuing a record of your package installation, and how to use the file to install and uninstall packages. 
# Now, you should practice creating and using requirements files.
