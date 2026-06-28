
# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

'''
pip freeze > requirements.txt  # Save the list of installed packages in the system interpreter to a requirements file

virtualenv myenv  # Create a new virtual environment named 'myenv'

.\myenv\Scripts\activate.ps1  # Activate the virtual environment (Windows)

pip install -r requirements.txt  # Install the packages listed in requirements.txt into the virtual environment

'''
