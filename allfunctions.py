from abc import ABC, abstractmethod
import json
import datetime

class WorkLog: 
    def __init__(self):
        self.__worklog = {}
    
    def add_worklog(self, client, obj_work, description):
        title = obj_work.title
        rate = obj_work.return_rate
        hours = obj_work.return_hour
        date = obj_work.date
        self.__worklog[client] = {"Title" : title, 
                                  "Description" : description,
                                  "Rate per hour" : rate,
                                  "Total hours" : hours,
                                  "Date finished" : date}
    @property
    def see_worklog(self):
        return self.__worklog
    
class Project:
    def __init__(self, title, rate_per_hour, total_hours, status):
        self.title = title
        self.__rate_per_hour = int(rate_per_hour)
        self.__total_hours = total_hours
        self.status = status
        self.date = ""
    
    @property
    def return_rate(self):
        return self.__rate_per_hour
    
    @property
    def return_hour(self):
        return self.__total_hours

    @property
    def calculate_total(self):
        return self.__rate_per_hour * self.__total_hours
    
    def mark_complete(self, date):
        self.status = True
        self.date = date

class Client:
    def __init__(self, name):
        self.name = name
        self.project = {} # I use dict for easier acsess
        self.money = 0
        self.counter = 0
    def add_project(self, title, obj_project):
        self.project[title] = obj_project
    
    @property
    def total_project(self):
        for key in self.project:
            self.counter += 1
        return self.counter

    @property
    def get_total_due(self):
        """This method will be called by the manager, it will return the money client will give"""
        for key in self.project:
            self.money += self.project[key].calculate_total
        return self.money
    
    @property
    def project_summary(self):
        project = {}
        try :
            for key in self.project:
                project[key] = {"title" : self.project[key].title,
                            "rate per hour" : self.project[key].return_rate,
                            "total hours / deadline" : self.project[key].return_hour,
                            "status" : self.project[key].status,
                            "date of completion" : self.project[key].date}
        except:
            for key in self.project:
                project[key] = {"title" : self.project[key].title,
                            "rate per hour" : self.project[key].return_rate,
                            "total hours / deadline" : self.project[key].return_hour,
                            "status" : self.project[key].status}
        return project

class FreeLanceManager:
    def __init__(self):
        self.clients = {}
        self.completed = {}
        self.worklog = WorkLog()
        self.invoice = 0
        self.average_calculator = 0

    def add_clients(self, client_name):
        self.clients[client_name] = Client(client_name)
    
    def add_project(self, client, title, rate, hour, status):
        if client in self.clients:
            self.clients[client].add_project(title, Project(title, rate, hour, status))
            print("Added !")
        else:
            print("Client isn't found !")
    
    def log_work(self, client, title, description, date): #log work means complete !
        if client in self.clients:
            if title in self.clients[client].project:
                self.clients[client].project[title].mark_complete(date)
                self.worklog.add_worklog(client, self.clients[client].project[title], description)
                print("Sucsessfully logged !")
            else:
                print("Work doesn't exist !")
        else:
            print("Client doesn't exist !")
            
    def mark_complete(self, client, title, date): #log work means complete !
        if client in self.clients:
            if title in self.clients[client].project:
                self.clients[client].project[title].mark_complete(date)
                print("Sucsessfully marked !")
            else:
                print("Work doesn't exist !")
        else:
            print("Client doesn't exist !")

    def project_summary(self, client):
        return self.clients[client].project_summary

    
    @property
    def generate_invoice(self):
        for key in self.clients:
            self.invoice += self.clients[key].get_total_due
            self.average_calculator += self.clients[key].total_project
        average = self.invoice / self.average_calculator
        return {"Invoice" : self.invoice,
                "Average" : average}
    
    def save_to_json(self, file):
        data = {}
        data["client"] = {}

        for client_name in self.clients:
            data["client"][client_name] = {}
            for project_name, project in self.clients[client_name].project.items():
                data["client"][client_name][project_name] = {
                    "title": project.title,
                    "rate": project.return_rate,
                    "hour": project.return_hour,
                    "status": project.status
                }

        data["worklog"] = self.worklog.see_worklog
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
        print("Saved !\n")
    
    def load_json(self, file):
        with open(file, "r") as f:
            data = json.load(f)
            for client in data["client"]:
                self.clients[client] = Client(client)
                for key in data["client"][client]:
                    title = data["client"][client][key]["title"]
                    rate = data["client"][client][key]["rate"]
                    hour = data["client"][client][key]["hour"]
                    status = data["client"][client][key]["status"]
                    if status == True:
                        try:
                            date = data["client"][client]["date"]
                        except:
                            pass
                    self.clients[client].add_project(title, Project(title, rate, hour, status))
            try:
                for people in data["worklog"]:
                    person = people
                    for work in data["worklog"][people]:
                        titles = work
                        desc = data["worklog"][people][work]["Description"]
                        rate_hourly = data["worklog"][people][work]["Rate per hour"]
                        total_hour = data["worklog"][people][work]["Total hours"]
                        finished = data["worklog"][people][work]["Date finished"]
                        self.worklog.add_worklog(person, Project(titles, rate_hourly, total_hour, finished), desc)
            except:
                for people in data["worklog"]:
                    person = people
                    for work in data["worklog"][people]:
                        titles = work
                        desc = data["worklog"][people]["Description"]
                        rate_hourly = data["worklog"][people]["Rate per hour"]
                        total_hour = data["worklog"][people]["Total hours"]
                        finished = data["worklog"][people]["Date finished"]
                        self.worklog.add_worklog(person, Project(titles, rate_hourly, total_hour, finished), desc)
        print("Loaded !\n")

        