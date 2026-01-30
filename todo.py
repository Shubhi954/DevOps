todos = []

def add_task(task):
    todos.append(task)

def show_tasks():
    for i, task in enumerate(todos):
        print (i+1, task)
        print ("Todo app started")
