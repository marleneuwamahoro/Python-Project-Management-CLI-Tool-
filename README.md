# Python Project Management CLI Tool

A command-line application built in Python to manage users, projects, and tasks. It demonstrates object-oriented programming, CLI development using argparse, and data persistence using JSON files.

---

## Features

- Create and manage users
- Create projects assigned to users
- Add tasks to projects
- Mark tasks as completed
- View all projects
- Search users
- Persistent storage using JSON files
- Modular code structure (models, utils, tests)
- Unit testing support
- CLI-based interaction

---

## Project Structure

project-management-cli/
│
├── main.py
├── models/
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── utils/
│   ├── storage.py
│   └── helpers.py
│
├── tests/
│   ├── test_user.py
│   ├── test_project.py
│   └── test_task.py
│
├── users.json
├── projects.json
├── tasks.json
├── requirements.txt
├── Pipfile
└── README.md

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/project-management-cli.git
cd project-management-cli

Set up virtual environment:
pipenv install
pipenv shell
dependecies install
pip install -r requirements.txt