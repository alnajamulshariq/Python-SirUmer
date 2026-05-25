# todo


task = []
for i in range(3):
    item = input("Enter a task to add to the to-do list: ")
    task.extend([item])
print("Your to-do list:", task)


# remove a task from the to-do list
task_to_remove = input("Enter a task to remove from the to-do list: ")
if task_to_remove in task:
    task.remove(task_to_remove)
    print("Task removed. Your to-do list:", task)
else:    print("Task not found in the to-do list.")
