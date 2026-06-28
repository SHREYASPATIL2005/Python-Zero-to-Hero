# 1. Create two virtual environments, install few packages in the first one.
# How do you create a similar environment in the second one?

# create two venvs
# python3 -m venv env1
# python3 -m venv env2

# activate env1
# source env1/bin/activate

# install packages into env1
# pip install requests numpy

# snapshot installed packages
# pip freeze > requirements.txt

# deactivate env1
# deactivate

# activate env2
# source env2/bin/activate

# install same packages into env2
# pip install -r requirements.txt

# deactivate env2
# deactivate