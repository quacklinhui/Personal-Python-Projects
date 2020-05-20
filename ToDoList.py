def user_option():
    while True:
        #This also be done without the try except this way so users will know more specifically what error they are making
        try:
            option = int(input(" Welcome to my TODO simple app\n--------------------------------\n1. Viewing Todo List\n2. Add in Todo Item\n3. Completed an Item\n4. Exit\nEnter your option:"))
            if option == 1:
                viewtodo()
                break;
            elif option == 2:
                addtodo()
                break;
            elif option == 3:
                completetheitem()
                break;
            elif option == 4:
                exitthething()
                break;
            else:
                print("That number is not part of the options. Please enter 1, 2, 3 or 4.") #for inputs that are numbers but are not part of the choices
        except ValueError: #for inputs that are not even numbers
            print("Please enter a valid number based on your desired choice(1,2,3,4).")

def viewtodo():
    print("Todo List.")
    i = 1
    while i < len(namelist):
        if urgentlist[i] == "No":
            urgency = "not urgent"
        elif urgentlist[i] == "Yes":
            urgency = "urgent"
        if importantlist[i] == "Yes":
            important = "important"
        elif importantlist[i] == "No":
            important = "not important"
        if completedlist[i] == "Yes":
            completion = ", it has been completed."
        elif completedlist[i] == "No":
            completion = ", it has not been completed."
        print(i,": ", namelist[i],"is", important,"and", urgency + completion)
        i += 1
        continue;
    user_option()

def addtodo():
    f = open ("todo.txt","w") #write file
    Name = input("Enter the name of the new item: ")

    #Getting the Urgent information
    while True:
        Urgent_input = input("Is it urgent? [Yes/No] ")
        if Urgent_input == "Yes":
            Urgent = "urgent"
            break;
        elif Urgent_input == "No":
            Urgent = "not urgent"
            break;
        else:
            print("Please enter either 'Yes' or 'No'.")

    #Getting the important information
    while True:
        Important_input = input ("Is it important? [Yes/No]")
        if Important_input == "Yes":
            Important = "important"
            break;
        elif Important_input == "No":
            Important = "not important"
            break;
        else:
            print("Please enter either 'Yes' or 'No'.")

    #Setting the default completion to be no
    Completion = "No"

    #Printing in the output (In this function all items have not been completed)
    print("The item has been added as follows: "+Name+" is "+Important+" and is "+Urgent+", it has not been completed." )

    #Rewriting the textfile
    namelist.append(Name) #adding the newly added elements into namelist
    importantlist.append(Important_input) #adding the newly added items into importantlist
    urgentlist.append(Urgent_input) #adding the newly added items into the urgentlist
    completedlist.append(Completion) #adding newly items into completedlist

    x = 0
    while (x < len(namelist)):
        print(namelist[x]+","+importantlist[x]+","+ urgentlist[x] +","+completedlist[x],file = f)
        x += 1
    f.close()
    user_option()

#function to complete the task
def completetheitem():
    f = open("todo.txt", "w")  # function to write file
    while True:
        try:
            i = int(input("Enter item number you have completed: "))
            if urgentlist[i] == "No":
                urgency = "not urgent"
            elif urgentlist[i] == "Yes":
                urgency = "urgent"
            if importantlist[i] == "Yes":
                important = "important"
            elif importantlist[i] == "No":
                important = "not important"
            print("The item being marked completed: ", namelist[i],"is", important,"and", urgency+ ", it has been completed")
            completedlist[i] = "Yes"
            break;
        except:
            print("Enter a number within the range.")

    #Rewriting the text file
    x = 0
    while (x < len(namelist)):
        print(namelist[x]+","+importantlist[x]+","+urgentlist[x] +","+completedlist[x],file = f)
        x += 1
    f.close()
    user_option()

def exitthething():
    print("Good bye!")


#This is the main function
namelist =['Name'] #List for names of tasks
importantlist = ['Important'] #List for whether they are important
urgentlist = ['Urgent'] #List for their urgency
completedlist = ['Completed']
#Reading what was previously in the Text file
entirelist=[]
with open('todo.txt','r') as f:
    for line in f:
        entirelist.extend(line.strip().split(','))
x=4
while (x < len(entirelist)):
    n = (x // 4)
    if x%4==0:
        namelist.append(entirelist[x])
        x += 1
    elif x%4==1:
        importantlist.append(entirelist[x])
        x += 1
    elif x%4==2:
        urgentlist.append(entirelist[x])
        x += 1
    else:
        completedlist.append(entirelist[x])
        x+=1
user_option()



