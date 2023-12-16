from database import Read, DB, Table
import random


class admin:
    def __init__(self, id, db):
        self.id = id
        self.db = db

    def ask_need(self):
        while True:
            print("1.See table in database (specific/all)\n2.Manage the "
                  "database (insert/remove)\n3.Manage table in database\n"
                  "4.Log out")
            choice = int(input("What do you want to do?: "))
            if choice in [1, 2, 3, 4]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_table(self):
        choice = input("Which table you want to see (type table name/all): ")
        all_table_name = []
        for x in self.db.database:
            all_table_name.append(x.table_name)
        if choice == "all":
            for i in self.db.database:
                print(i)
            return True
        elif self.db.search(choice) is not None:
            print(self.db.search(choice))
            return True
        print("Table doesn't exist.")
        return False

    def manage_database(self):
        choice = input("Do you want to insert or remove? (insert/remove): ")
        if choice == "insert":
            table_name = input("What table name you want to insert?: ")
            table_info = input("Insert table info (dict): ")
            table = Table(table_name, table_info)
            self.db.insert(table)
        elif choice == "remove":
            table_name_to_remove = input("Which table you want to remove? "
                                         "(table name): ")
            table_to_remove = self.db.search(table_name_to_remove)
            self.db.remove(table_to_remove)
            print(f"{self.id} has removed {table_name_to_remove} table.")

    def manage_table(self):
        print(
            "1.Add new info to table\n2.Update info in existing table\n"
            "3.Remove info in existing table")
        choice = input("What do you want to do?: ")
        table_name = input("Which table you want to interact with? "
                           "(table name): ")
        table = self.db.search(table_name)
        if choice == "1":
            new_info = input("Enter your new info:")
            table.insert(new_info)
        elif choice == "2":
            print("Before update")
            print(table.table)
            id = input("Which ID you want to update?: ")
            key = input("Which key you want to update?: ")
            value = input("What value you want to update?: ")
            table.update(id, key, value)
            print(f"{self.id} has updated {table_name} table.")
            print(table.table)
        elif choice == "3":
            id = input("Which ID you want to remove?: ")
            table.remove(id)


# my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
class student:
    def __init__(self, id, db):
        self.id = id
        self.mpr = db.search('Member_pending_request').filter(
            lambda x: x['member_id'] == id)
        self.pjt = db.search('Project')
        self.log = db.search('login').filter(lambda x: x['ID'] == id)

    def ask_need(self):
        while True:
            print("1.See pending to be member requests\n2.Create a project")
            choice = int(input("What do you want to do?: "))
            if choice in [1, 2]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def response_request(self):
        if len(self.mpr.table) == 0:
            print("You have no pending request.")
        elif len(self.mpr.table) >= 1:
            print(f"All pending request:")
            for y in self.mpr.table:
                print(y)
            proj_id = input(
                "Which project you want to accept (if none type none): ")
            for i in self.pjt.table:
                if i['ProjectID'] == proj_id:
                    if i['Member1'] == "-":
                        i['Member1'] = self.id
                    elif i['Member2'] == "-":
                        i['Member2'] = self.id
            response_date = input("Enter response date: ")
            for x in self.mpr.table:
                if x['ProjectID'] == proj_id:
                    if x['member_id'] == self.id:
                        x['Response'] = "Accept"
                        x['Response_date'] = response_date
                elif x['ProjectID'] != proj_id:
                    if x['member_id'] == self.id:
                        x['Response'] = "Deny"
                        x['Response_date'] = response_date
            for s in self.log:
                if s['ID'] == self.id:
                    s['Role'] = "member"

    def create_project(self):
        date = input("Enter date: ")
        for x in self.mpr.table:
            if x['member_id'] == self.id:
                x['Response'] = "Deny"
                x['Response_date'] = date
        project_id = ""
        for k in range(7):
            project_id += str(random.randint(0, 9))
        title = input("Enter title of your project: ")
        self.pjt.insert({"ProjectID": project_id, "Title": title,
                         "Lead": self.id, "Member1": "-", "Member2": "-",
                         "Advisor": "-",
                         "Status": "Just Create No member, No advisor"})
        for s in self.log:
            if s['ID'] == self.id:
                s['role'] = "lead"


class member:
    def __init__(self, id, db):
        self.id = id
        self.pjt = db.search('Project').filter(lambda x: self.id in x.values())
        self.proj_id = self.pjt.table[0].get('ProjectID')
        self.mpr = db.search('Member_pending_request').filter(
            lambda x: x['ProjectID'] == self.proj_id)

    def ask_need(self):
        while True:
            print("1.See your project status.\n"
                  "2.See and modify project information\n"
                  "3.See who has responded to the requests sent out")
            choice = int(input("What do you want to do?: "))
            if choice in [1, 2, 3]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_modified(self):
        print("Your project information:")
        print(self.pjt.table)
        key = input("Which key you want to modified?: ")
        value = input("What value you want to modified?: ")
        self.pjt.update(self.proj_id, key, value)
        k = [i for i in self.pjt if self.pjt[i] == self.id]
        print(f"{self.id}{k[0]} has updated project modified")

    def see_proj_status(self):
        print("Your project status:")
        print(self.pjt.table[0]['Status'])

    def see_response(self):
        for i in self.mpr.table:
            print(i)


class lead:
    def __init__(self, id, db):
        self.id = id
        self.pjt = db.search('Project').filter(
            lambda x: self.id in x['Lead'])  # อาจจะผิด
        self.proj_id = self.pjt.table[0].get('ProjectID')
        self.mpr = db.search('Member_pending_request').filter(
            lambda x: x['ProjectID'] == self.proj_id)
        self.apr = db.search('Advisor_pending_request')

    def ask_need(self):
        while True:
            print("1.See your project status\n"
                  "2.See and modify your project information\n"
                  "3.See who has responded to the requests sent out\n"
                  "4.Send out requests to find members\n"
                  "5.Send out requests to find a potential advisor\n"
                  "6.Submit your project")
            choice = int(input("What do you want to do?: "))
            if choice in [1, 2, 3, 4, 5, 6]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_proj_status(self):
        print("Your project status:")
        print(self.pjt.table[0]['Status'])

    def see_modified(self):
        print("Your project information:")
        print(self.pjt.table)
        choice = input("Do you want to modified(yes/no): ")
        if choice == "yes":
            key = input("Which key you want to modified?: ")
            value = input("What value you want to modified?: ")
            self.pjt.update(self.proj_id, key, value)
            print(f"{self.id}(Lead) has updated project modified")

    def see_response(self):
        for i in self.mpr.table:
            print(i)

    def find_member(self):
        member_id = input("Who will you request him to be member"
                          "(type his ID): ")
        message = input("A message to him: ")
        self.mpr.insert({'ProjectID': self.proj_id, 'to_be_member': message,
                         'Response': 'pending', "Response_date": "-",
                         "member_id": member_id})

    def find_advisor(self):
        advisor_id = input("Who will you request him to be member"
                           "(type his ID): ")
        message = input("A message to him: ")
        self.apr.insert({'ProjectID': self.proj_id, 'to_be_advisor': message,
                         'Response': 'pending', "Response_date": "-",
                         "advisor_id": advisor_id})

    def submit_project(self):
        pass


class faculty:
    def __init__(self, id, db):
        self.id = id
        self.apr = db.search('Advisor_pending_request').filter(
            lambda x: x['advisor_id'] == self.id)
        self.pjt = db.search('Project')
        self.log = db.search('login').filter(lambda x: x['ID'] == self.id)

    def ask_need(self):
        while True:
            print("1.See request to be a supervisor\n"
                  "2.See details of all/specific the project\n"
                  "3.Evaluate a project")
            choice = int(input("What do you want to do"))
            if choice in [1, 2, 3]:
                return choice
            print("Invalid choice, Enter again")

    def see_req(self):
        if len(self.apr.table) == 0:
            print("You have no pending request.")
        elif len(self.apr.table) >= 1:
            print("Your pending request: ")
            for i in self.apr.table:
                print(i)
            proj_id = input("Which project you want to accept(type project id/"
                            " if none type none)?: ")
            if proj_id == "none":
                return False
            for i in self.pjt.table:
                if i['ProjectID'] == proj_id:
                    i['Advisor'] = self.id
            response_date = input("Enter response date: ")
            for x in self.apr.table:
                if x['ProjectID'] == proj_id:
                    if x['advisor_id'] == self.id:
                        x['Response'] = "Accept"
                        x['Response_date'] = response_date
                elif x['ProjectID'] != proj_id:
                    if x['advisor_id'] == self.id:
                        x['Response'] = "Deny"
                        x['Response_date'] = response_date
            for s in self.log:
                s['role'] = "advisor"

    def see_proj(self):
        choice = input("Which project you want to see (type project id/all): ")
        if choice == "all":
            for i in self.pjt:
                print(i)
            return True
        elif self.pjt.find_from_id(choice):
            print(self.pjt.search(choice))
            return True
        print("Project doesn't exist.")
        return False

    def evaluate(self):
        pass


class advisor:
    def __init__(self, id, db):
        self.id = id
        self.pjt = db.search('Project')

    def ask_need(self):
        while True:
            print("1.See details of all/specific the project\n"
                  "2.Evaluate a project")
            choice = int(input("What do you want to do?: "))
            if choice in [1,2]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_proj(self):
        choice = input("Which project you want to see (type project id/all): ")
        if choice == "all":
            for i in self.pjt:
                print(i)
            return True
        elif self.pjt.find_from_id(choice):
            print(self.pjt.search(choice))
            return True
        print("Project doesn't exist.")
        return False

    def evaluate(self):
        pass
