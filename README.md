#
Awaards

## Description

This is web application that allows the user to creat an account, login,create and view their profile view projects posted by others, rate the projects and create their own project.
## SETUP INSTRUCTIONS:

### Installation

1.Python 3.6.5 

2.Django 1.11.8

### Cloning the repository

git clone https://github.com/sharonmaswai/awards.git

### Creating a virtual environment

sudo apt-get install python3.6-venv python3.6 -m venv --without-pip virtual source virtual/bin/activate

### Installing dependencies

pip install -r requirements.txt

### Running tests

python3.6 manage.py test photos awaards

### Running the Development server

python3.6 manage.py runserver

## BEHAVIOUR DRIVEN DEVELOPMENT

| Behaviour | Input  | Output |
| -- |-- |--|
|Sign up| Create credentials| Successful sign up if credentials are viable|
|Login|Enter login credentials | Go to landing page|
|Upload project|Click post prroject on taskbar |access project post form|
|View projects|Click projects on navbar| Go to projects page|
|View a single project|Click on view button on the image|View a single project|
|Rate project|Click on rate project button|Access rate project form|
|Search projects|Enter project name on the search bar|Results of the search|
|View actual projects|Click live project button|access the actual project |





##CONTACTS

For more information and clarification contact me through chepsharon@gmail.com

## LICENSE

MIT License

Copyright (c) [2019] [SharonMaswai]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
