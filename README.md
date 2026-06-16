# Python Project Management CLI Tool

## Features

- Add users
- Add projects
- Add tasks
- Complete tasks
- View projects
- JSON storage
- Unit tests

## Installation

```bash
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Usage

```bash
python main.py add-user --name Alex --email alex@gmail.com

python main.py add-project \
--user Alex \
--title "CLI Tool" \
--description "Python Project" \
--due-date "2026-07-01"

python main.py add-task \
--project "CLI Tool" \
--title "Implement add-task" \
--assigned-to Alex

python main.py complete-task --title "Implement add-task"
```