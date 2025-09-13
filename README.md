
AirBnB Clone - The Console

The console is the first step of the AirBnB project at ALU/Holberton School. The goal of this project is to build a simple command interpreter that will later be used to manage objects for the AirBnB clone web application.

This command interpreter allows us to:

Start an interactive shell session

Execute basic commands (help, quit, EOF)

Extend functionality later to create, update, destroy, and show objects

Table of Contents

Environment

Installation

Usage

Examples

Authors

Environment

Language: Python3 (version 3.8.5)

OS: Ubuntu 20.04 LTS

Style guide: pycodestyle (version 2.7.*)

Installation

Clone this repository:

git clone https://github.com/<your-team-username>/alu-AirBnB_clone.git


Move into the project directory:

cd alu-AirBnB_clone


Make sure console.py is executable:

chmod +x console.py

Usage
Interactive Mode
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$

Non-Interactive Mode
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

Examples
(hbnb) help quit
Quit command to exit the program
(hbnb) quit
$

Authors

Gabriella Ange Ahirwe


