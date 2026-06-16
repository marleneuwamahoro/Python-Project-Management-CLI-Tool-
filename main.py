import argparse
from utils.storage import load_data, save_data
from utils.helpers import success, error

# ---------------- FILES ----------------
USERS_FILE = "users.json"
PROJECTS_FILE = "projects.json"
TASKS_FILE = "tasks.json"


# ---------------- USERS ----------------
def add_user(name, email):
    users = load_data(USERS_FILE)

    # prevent duplicates
    for u in users:
        if u["name"].lower() == name.lower():
            error("User already exists.")
            return

    users.append({
        "name": name,
        "email": email
    })

    save_data(USERS_FILE, users)
    success("User added successfully.")


def search_user(name):
    users = load_data(USERS_FILE)

    for user in users:
        if user["name"].lower() == name.lower():
            print(f"Found: {user['name']} ({user['email']})")
            return

    error("User not found.")


# ---------------- PROJECTS ----------------
def add_project(user, title, description, due_date):
    users = load_data(USERS_FILE)
    projects = load_data(PROJECTS_FILE)

    user_exists = any(u["name"] == user for u in users)

    if not user_exists:
        error("User not found.")
        return

    projects.append({
        "user": user,
        "title": title,
        "description": description,
        "due_date": due_date
    })

    save_data(PROJECTS_FILE, projects)
    success("Project added successfully.")


def list_projects():
    projects = load_data(PROJECTS_FILE)

    if not projects:
        print("No projects found.")
        return

    for p in projects:
        print(f"{p['title']} | {p['description']} | {p['due_date']}")


# ---------------- TASKS ----------------
def add_task(project, title, assigned_to):
    projects = load_data(PROJECTS_FILE)
    tasks = load_data(TASKS_FILE)

    project_exists = any(p["title"] == project for p in projects)

    if not project_exists:
        error("Project not found.")
        return

    tasks.append({
        "project": project,
        "title": title,
        "assigned_to": assigned_to,
        "status": "Pending"
    })

    save_data(TASKS_FILE, tasks)
    success("Task added successfully.")


def complete_task(title):
    tasks = load_data(TASKS_FILE)

    for t in tasks:
        if t["title"] == title:
            t["status"] = "Completed"
            save_data(TASKS_FILE, tasks)
            success("Task completed.")
            return

    error("Task not found.")


# ---------------- CLI SETUP ----------------
parser = argparse.ArgumentParser(description="Project Management CLI Tool")
subparsers = parser.add_subparsers(dest="command")


# add-user
user_parser = subparsers.add_parser("add-user")
user_parser.add_argument("--name", required=True)
user_parser.add_argument("--email", required=True)

# search-user
search_parser = subparsers.add_parser("search-user")
search_parser.add_argument("--name", required=True)

# add-project
project_parser = subparsers.add_parser("add-project")
project_parser.add_argument("--user", required=True)
project_parser.add_argument("--title", required=True)
project_parser.add_argument("--description", required=True)
project_parser.add_argument("--due-date", required=True)

# add-task
task_parser = subparsers.add_parser("add-task")
task_parser.add_argument("--project", required=True)
task_parser.add_argument("--title", required=True)
task_parser.add_argument("--assigned-to", required=True)

# complete-task
complete_parser = subparsers.add_parser("complete-task")
complete_parser.add_argument("--title", required=True)

# list-projects
subparsers.add_parser("list-projects")


# ---------------- EXECUTION ----------------
args = parser.parse_args()

if args.command == "add-user":
    add_user(args.name, args.email)

elif args.command == "search-user":
    search_user(args.name)

elif args.command == "add-project":
    add_project(args.user, args.title, args.description, args.due_date)

elif args.command == "add-task":
    add_task(args.project, args.title, args.assigned_to)

elif args.command == "complete-task":
    complete_task(args.title)

elif args.command == "list-projects":
    list_projects()