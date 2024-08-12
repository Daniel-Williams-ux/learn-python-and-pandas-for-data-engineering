# When code is saved to a file with the purpose of re-use, it is called a module. 
# When a module or a group of modules is bundled together specifically for distribution to an installation in multiple python environments. It is referred to as a package. 
# Along with every installation of python is a group of packages known as the python Standard Library. 
# These packages can be used in any python program. 
# In addition to the Standard Library, there's a huge ecosystem of third party packages. These packages add all sort of specialized functionality to the default installation. The main location for these packages is the python package index. Also known as pypi.

# Pip is the package installer for python. It is the default tool for managing the installation of python packages. 
# By default, it will download installed packages from the python package index though it can be pointed to other locations. 
# Since python version 3.4, pip is installed as part of the python default installation

# Pip can generally be accessed in two ways firstly invoked using the python module dash M. 
python -m pip --version
# Or as a separate standalone command.
pip --version
# The pip help command lists all of the commands and general options available.
pip --help
#  To see the documentation for a particular command type. The command name after the help command
pip help list

# The three commands we will use for the rest of this lesson. Our list, install and uninstall. 
pip list
# The list command lists the packages along with version numbers that are currently installed in your environment. Use the install command followed by a module name or a list of module names to install them. 
# Let's install the popular testing library pie test. We can see that pip not only installed by test.
pip install pytest
# But also other packages that we did not specifically request. These are the packages on which pip test depends pip automatically installed. 
# The libraries needed by a package that we have requested to uninstall a package. Use the uninstall command followed by the package name. 
pip unistall pytest
# Notice that pip is uninstalled pytest test but not its dependencies. 
# We would have to explicitly name them with the uninstalled command to remove them as well. The install command will install the latest available version of a package. 
# By default, we can install a specific version by using the install command with double equal signs after the module name. 
# One hack to see what versions are available is to leave the version number blank. 
pip install pytest==
# This displays an error but the error message reports on all of the available versions. To install a specific version put that version number directly after the double equals. 
pip install pytest==6.2.4
# And we can see that the specified version is installed. If we wish to upgrade to the latest version of a package. We can either uninstall and reinstall it or use the upgrade option with the install command.
pip install pytest --upgrade
pip list
