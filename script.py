from allfunctions import WorkLog, Project, Client, FreeLanceManager

if __name__ == "__main__":
    Manager = FreeLanceManager()
    with open("welcome.txt", "r")as f:
        text = f.readlines()
        for line in text:
            print(line)
    print("\n-------------------------------------------------------------\n")
    while True:
        userinput = input("What do you want to do ? : ").lower()
        
        if userinput == "add client": #Done
            new_client = input("Input the client's name : ")
            try:
                Manager.add_clients(new_client)
                print(f"Added {new_client} !")
            except:
                print("Invalid name !")
            print("\n-------------------------------------------------------------\n")
        
        elif userinput == "add project to client": #Done
            client = input("Input the client's name : ")
            project = input("Enter the title, rate per hour, total hour, and status : ").replace(" ","").split(",")
            try:
                Manager.add_project(client, project[0], int(project[1]), int(project[2]), project[3])
            except:
                print("Invalid input !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "log work": #done 
            print("Careful ! Logging work means it has been completed !")
            client1 = input("Enter the client's name : ")
            title = input("Enter the project title : ")
            description = input("Enter the description of task : ")
            date = input("Enter the date of completion : ")
            try:
                Manager.log_work(client1, title, description, date)
            except:
                print("Unable to find the client/task !")
            print("\n-------------------------------------------------------------\n")
        
        elif userinput == "view project": #done
            client_name = input("Enter the client's name : ")
            try:
                dictionary = Manager.project_summary(client_name)
                print(dictionary)
                print(" ")
            except:
                print("Client doesn't exist !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "mark project as completed": #done
            clients = input("Enter the client's name : ")
            titles = input("Enter the project title : ")
            date = input("Enter the date of completion : ")
            try:
                Manager.mark_complete(clients, titles, date)
            except:
                print("Unable to find the client/task !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "generate invoice": #done
            try:
                print(Manager.generate_invoice)
                print(" ")
            except:
                print("Unable to find the invoice !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "save to json":
            jsonfile = input("Enter the file's name [file.json]: ")
            try:
                Manager.save_to_json(jsonfile)
            except:
                print("Invalid file's name !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "load from json": 
            jsonfile1 = input("Enter file name [file.json] : ")
            try :
                Manager.load_json(jsonfile1)
            except:
                print("Invalid File Name !")
            print("\n-------------------------------------------------------------\n")

        elif userinput == "exit": #done
            print("See you ! Don't forget, More work = Brighter future !")
            break
            
        else: #done
            print("Invalid Command !")
            print("\n-------------------------------------------------------------\n")