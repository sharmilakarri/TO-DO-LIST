print("******TO-DO LIST******")
print("1.Add Task")
print("2.Display Tasks")
print("3.Exit")
Tasks=[]
while(True):
    choice=int(input("Enter the choice:"))
    if(choice==1):
        task=input("Enter the task:")
        Tasks.append(task)
        print(task + " is added")
    elif(choice==2):
        print("The tasks in the list are:")
        for task in Tasks:
            print(task)
    elif(choice==3):
        break
    else:
        print("Enter correct choice")