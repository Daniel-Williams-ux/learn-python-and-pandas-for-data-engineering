# Key Terms
# Package - Python code bundled together for distribution and installation

# Module - Python code saved to a file for reuse

# venv - create a virtual environment

# activate - activate/enter the virtual environment

# pip install - install packages into the active virtual environment

# pip list - list packages installed in the current environment

# pip freeze - output installed packages to a requirements file

# deactivate - exit the active virtual environment

# Create virtual environment 
python3 -m venv my_env

# Activate virtual environment
source my_env/bin/activate 

# Install packages to virtual environment
pip install pandas

# List packages installed in environment
pip list 

# Save installed packages to requirements file
pip freeze > requirements.txt

# Deactivate virtual environment 
deactivate
