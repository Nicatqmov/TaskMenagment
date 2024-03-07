import argparse
class Task:
    def __init__(self, id, title, description, completed):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    def mark_as_completed(self):
        self.completed = True
class TaskManager:
    def __init__(self):
        self.tasks = {}
    def add_task(self, title, description):
        id = 0
        with open("tasks.txt", "r") as file:
            for line in file:
                id, *other = line.strip().split(",")
                id = int(id)
        task = Task(id + 1, title, description, False)
        self.tasks[task.id] = task
    def remove_task(self, id):
        if id in self.tasks.keys():
            del self.tasks[id]
            print("task removed succesfully")
        else:
            print("task is not found")
    def mark_task_completed(self, id):
        if id in self.tasks.keys():
            self.tasks[id].mark_as_completed()
            print("task marked as completed succesfully")
        else:
            print("task is not found")
    def list_tasks(self):
        if self.tasks.values():
            for task in self.tasks.values():
                print(f"{task.id}, {task.title}, {
                    task.description}, {task.completed}")
        else:
            print("there is no file")
    def find_task(self, id):
        if id in self.tasks.values():
            task = self.tasks[id]
            print(f"{task.id, task.title, task.description, task.completed}")
        else:
            print("task is not found")
    def write_to_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks.values():
                file.write(f"{task.id},{task.title},{task.description},{task.completed}\n")
    def take_from_file(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    id, title, description, completed = line.strip().split(",")
                    self.tasks[int(id)] = Task(int(id), title, description, completed == "True")
        except FileNotFoundError:
            print("file is not found")
argparser = argparse.ArgumentParser(description = "Task manager system")
subparser = argparser.add_subparsers(dest = "command")
# add command
add_parser = subparser.add_parser("add", help = "to add task to system")
add_parser.add_argument("-t", "--title", required = True, help = "task title")
add_parser.add_argument("-d", "--description", required = True, help = "task description")
# remove command
remove_parser = subparser.add_parser("remove", help = "to remove task from system")
remove_parser.add_argument("-i", "--id", type = int , required = True, help = "task id")
# show tasks
shower_parser = subparser.add_parser("list", help = "to show all tasks")
# complete parser
complete_parser = subparser.add_parser("complete", help = "to mark task as completed")
complete_parser.add_argument("-i", "--id", type = int, required = True, help = "task id")
args = argparser.parse_args()
task_manager = TaskManager()
task_manager.take_from_file()
if args.command == "add":
    task_manager.add_task(args.title, args.description)
    task_manager.write_to_file()
elif args.command == "remove":
    task_manager.remove_task(args.id)
    task_manager.write_to_file()
elif args.command == "complete":
    task_manager.mark_task_completed(args.id)
    task_manager.write_to_file()
elif args.command == "list":
    task_manager.list_tasks()
else:
    print("this command is not presented")