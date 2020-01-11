# Start with identifying is Django is available to use
# Run this command in terminal/bash
# python3 -m django --version

# If Django is available it'll return with the version
# Example: 3.0.1

# Once you can see that Django is available, think of a project name you want to use.
# Now type this into the terminal/bash
# django-admin startproject "My Project Name"
# "My Project Name" is what you decide to put in as a project name
# Example: django-admin startproject robertsproject

# Let's now test to see if the project is visible on the web
# Type this into the terminal/bash
# python3 manage.py runserver
# By default it runs a server on port 8000
# If you want to specify the port, you want type in:
# python3 manage.py runserver 8080

# The Watchman Plugin
# If you want to constantly watch the development server, you can install something called 