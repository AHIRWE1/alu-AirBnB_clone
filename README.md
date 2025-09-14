# AirBnB Clone - The Console

The console is the first step of the AirBnB project at ALU/Holberton School. This project introduces fundamental concepts of higher-level programming by creating a simple command interpreter to manage objects for the AirBnB clone web application (HBnB).

## Features

This command interpreter currently allows you to:

- Start an interactive shell session
- Execute basic commands (`help`, `quit`, `EOF`)

Future expansions will allow you to:

- Create new objects (e.g., User, Place)
- Retrieve objects from storage
- Update object attributes
- Delete objects

## Table of Contents

- Environment
- Installation
- Usage
- Examples
- Authors

## Environment

- Language: Python 3 (version 3.8.5)
- OS: Ubuntu 20.04 LTS
- Style guide: pycodestyle (version 2.7.*)

## Installation

Clone this repository:

```bash
git clone https://github.com/<your-github-username>/alu-AirBnB_clone.git
```

Move into the project directory:

```bash
cd alu-AirBnB_clone
```

Make the console script executable (Linux/macOS only):

```bash
chmod +x console.py
```

## Usage

### Interactive Mode

```bash
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
```

### Non-Interactive Mode

```bash
echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Examples

```bash
(hbnb) help quit
Quit command to exit the program
(hbnb) quit
$
```

## Authors

Gabriella Ange Ahirwe