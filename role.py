from database import Read, DB, Table
import random


class admin:
    def __init__(self, id, db):
        self.id = id
        self.db = db
        self.pt = db.search('persons')
        self.lt = db.search('login')

    def ask_need(self):
        while True:
            print("1.See table in database (specific/all)\n2.Add entry\n"
                  "3.Remove entry\n4.Update table in database\n"
                  "5.Log out")
            choice = int(input("What do you want to do?: "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_table(self):
        all_table_name = ["all", 'cancel']
        for x in self.db.database:
            all_table_name.append(x.table_name)
        choice = input(
            "Which table you want to see (type table name/all or cancel type cancel): ")
        while choice not in all_table_name:
            print("Invalid table, Enter again")
            choice = input(
                "Which table you want to see (type table name/all): ")
        if choice == 'cancel':
            return
        elif choice == "all":
            for i in self.db.database:
                print(i)
            return True
        elif self.db.search(choice) is not None:
            print(self.db.search(choice))
            return True
        print("Table doesn't exist.")
        return False

    def add_entry(self):
        id_info = self.pt.select(['ID'])
        id_info_list = []
        for x in id_info:
            id_info_list.append(x['ID'])
        new_id = ""
        for k in range(7):
            new_id += str(random.randint(0, 9))
        while new_id in id_info_list:
            new_id = ""
            for k in range(7):
                new_id += str(random.randint(0, 9))
        new_first_name = input("Enter first name: ")
        new_last_name = input("Enter last name: ")
        new_role = input("What is your role(admin, student, faculty): ")
        while new_role not in ['admin', 'student', 'faculty']:
            print("Role doesn't exist, Enter your role again.")
            new_role = input("What is your role(admin, student, faculty): ")
        new_password = input("Set your password(4 digits integer): ")
        if len(new_password) != 4:
            print("Please enter 4 digit password.")
            new_password = input("Set your password(4 digits integer): ")
        self.pt.insert(
            {'ID': new_id, 'first': new_first_name, 'last': new_last_name,
             'type': new_role})
        self.lt.insert(
            {'ID': new_id, 'username': new_first_name + "." + new_last_name[0],
             'password': new_password, 'role': new_role})

    def remove_entry(self):
        id_info = self.pt.select(['ID'])
        id_info_list = ['cancel']
        for x in id_info:
            id_info_list.append(x['ID'])
        id_remove = input(
            "Which id you want to remove?(if cancel type cancel): ")
        while id_remove not in id_info_list:
            print("ID not existed, Enter again")
            id_remove = input(
                "Which id you want to remove?(if cancel type cancel): ")
        if id_remove == 'cancel':
            return
        check = input("Are you sure you want to delete(confirm/cancel): ")
        while check not in ['confirm', 'cancel']:
            print("Your choice invalid, Enter again")
            check = input("Are you sure you want to delete(confirm/cancel): ")
        if check == 'confirm':
            self.pt.remove(id_remove)
            self.lt.remove(id_remove)
            print("Remove successful")
            print(f"{id_remove} has removed by {self.id}")

    def update_table(self):
        all_table_name = ['cancel']
        for i in self.db.database:
            all_table_name.append(i.table_name)
        table_name = input("Which table you want to interact with? "
                           "(table name/ if cancel type cancel): ")
        while table_name not in all_table_name:
            print("Invalid table name, Enter again")
            table_name = input("Which table you want to interact with? "
                               "(table name/ if cancel type cancel): ")
        if table_name == 'cancel':
            return
        table = self.db.search(table_name)
        print("Before update")
        print(table.table)
        id = input("Which ID you want to update?: ")
        key = input("Which key you want to update?: ")
        value = input("What value you want to update?: ")
        table.update(id, key, value)
        print(f"{self.id} has updated {table_name} table.")
        print(table.table)


class student:
    def __init__(self, id, db):
        self.id = id
        self.mpr = db.search('Member_pending_request').filter(
            lambda x: x['member_id'] == id and x['Response'] == 'pending')
        self.pjt = db.search('Project')
        self.log = db.search('login').filter(lambda x: x['ID'] == id)

    def ask_need(self):
        while True:
            print("1.See pending to be member requests\n"
                  "2.Create a project\n"
                  "3.Log out")
            choice = int(input("What do you want to do?: "))
            if choice in [1, 2, 3]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def response_request(self):
        if len(self.mpr.table) == 0:
            print("You have no pending request.")
        elif len(self.mpr.table) >= 1:
            print(f"All pending request:")
            all_proj_id = ['none']
            for y in self.mpr.table:
                all_proj_id.append(y['ProjectID'])
                print(y)
            proj_id = input(
                "Which project you want to accept (if none type none): ")
            while proj_id not in all_proj_id:
                print("Invalid choice, Enter again")
                proj_id = input(
                    "Which project you want to accept (if none type none): ")
            for i in self.pjt.table:
                if i['ProjectID'] == proj_id:
                    if i['Member1'] == "-":
                        i['Member1'] = self.id
                        i['Status'] = "Have 1 member"
                    elif i['Member2'] == "-":
                        i['Member2'] = self.id
                        i['Status'] = "Have 2 members"
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
            for s in self.log.table:
                if s['ID'] == self.id:
                    s['role'] = "member"
            print("Logout and login again to access your project")

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
                         "Status": "Just Created No member, No advisor",
                         "Score": 0})
        for s in self.log.table:
            if s['ID'] == self.id:
                s['role'] = "lead"
        print("Project has created.")
        print("Logout and login again to access your project")


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
                  "3.See who has responded to the requests sent out\n"
                  "4.Log out")
            choice = int(input("What do you want to do?: "))
            if choice in [1, 2, 3, 4]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_modified(self):
        print("Your project information:")
        print(self.pjt)
        choice = input("Do you want to modified(yes/no): ")
        if choice == "yes":
            key = input("Which key you want to modified?: ")
            value = input("What value you want to modified?: ")
            self.pjt.update(self.proj_id, key, value)
            dic = self.pjt.search(self.proj_id)
            k = [i for i in dic if dic[i] == self.id]
            print(f"{self.id} ({k[0]}) has updated project")

    def see_proj_status(self):
        print("Your project status:")
        print(self.pjt.table[0]['Status'])

    def see_response(self):
        if len(self.mpr.table) == 0:
            print("You haven't sent request to anyone.")
        elif len(self.mpr.table) >= 1:
            print("Here's your pending request.")
            for i in self.mpr.table:
                print(i)


class lead:
    def __init__(self, id, db):
        self.id = id
        self.lt = db.search('login')
        self.pjt = db.search('Project')
        self.opjt = self.pjt.filter(lambda x: self.id in x['Lead'])
        self.mpr = db.search('Member_pending_request')
        self.apr = db.search('Advisor_pending_request')
        for i in self.pjt.table:
            if i['Lead'] == self.id:
                self.proj_id = i.get('ProjectID')

    def ask_need(self):
        while True:
            print("1.See your project status\n"
                  "2.See and modify your project information\n"
                  "3.See who has responded to the requests sent out\n"
                  "4.Send out requests to find members\n"
                  "5.Send out requests to find a potential advisor\n"
                  "6.Update your project status\n"
                  "7.Submit your project\n"
                  "8.Log out")
            choice = int(input("What do you want to do?: "))
            if choice in [1, 2, 3, 4, 5, 6, 7,8]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_proj_status(self):
        print("Your project status:")
        proj_dic = self.pjt.search(self.proj_id)
        print(proj_dic['Status'])

    def see_modified(self):
        print("Your project information:")
        print(self.opjt)
        choice = input("Do you want to modified(yes/no): ")
        if choice == "yes":
            key = input("Which key you want to modified?: ")
            value = input("What value you want to modified?: ")
            self.pjt.update(self.proj_id, key, value)
            print(f"{self.id} (Lead) has updated project modified")

    def see_response(self):
        filter_mpr = self.mpr.filter(lambda x: x['ProjectID'] == self.proj_id)
        if len(filter_mpr.table) == 0:
            print("You haven't sent request to anyone.")
        elif len(filter_mpr.table) >= 1:
            for i in filter_mpr.table:
                print(i)

    def find_member(self):
        print("All people that you can request:")
        can_req = self.lt.filter(lambda x: x['role'] == 'student')
        for i in can_req.table:
            print(i)
        member_id = input("Who will you request him to be member"
                          "(type his ID): ")
        message = input("A message to him: ")
        self.mpr.insert({'ProjectID': self.proj_id, 'to_be_member': message,
                         'Response': 'pending', "Response_date": "-",
                         "member_id": member_id})

    def find_advisor(self):
        print("All people that you can request:")
        can_req = self.lt.filter(lambda x: x['role'] == 'faculty')
        for i in can_req.table:
            print(i)
        advisor_id = input("Who will you request him to be member"
                           "(type his ID): ")
        message = input("A message to him: ")
        self.apr.insert({'ProjectID': self.proj_id, 'to_be_advisor': message,
                         'Response': 'pending', "Response_date": "-",
                         "advisor_id": advisor_id})

    def update_proj_status(self):
        proj_dic = self.pjt.search(self.proj_id)
        if proj_dic['Member1'] != "-" and proj_dic['Member2'] == "-" and proj_dic['Advisor'] == "-":
            self.pjt.update(self.proj_id, "Status", "Have 1 member, No advisor")
        elif proj_dic['Member1'] != "-" and proj_dic['Member2'] != "-" and proj_dic['Advisor'] == "-":
            self.pjt.update(self.proj_id, "Status", "Have 2 members, No advisor")
        elif proj_dic['Member1'] != "-" and proj_dic['Member2'] != "-" and proj_dic['Advisor'] != "-":
            self.pjt.update(self.proj_id, "Status", "Ready to evaluate")

    def submit_project(self):
        proj_dic = self.pjt.search(self.proj_id)
        proj_value = list(proj_dic.values())
        if "-" not in proj_value:
            self.pjt.update(self.proj_id, "Status", "Ready to evaluate")
            print("Your project has submitted.")
        else:
            print("Your project can't submit yet, because there's missing "
                  "some information.")


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
                  "3.Evaluate a project\n"
                  "4.Log out")
            choice = int(input("What do you want to do: "))
            if choice in [1, 2, 3, 4]:
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
            for y in self.pjt.table:
                if y['ProjectID'] == proj_id:
                    y['Status'] += ", Have advisor"
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
            for s in self.log.table:
                s['role'] = "advisor"

    def see_proj(self):
        all_proj_id = ['all', 'cancel']
        for i in self.pjt.table:
            all_proj_id.append(i['ProjectID'])
        choice = input("Which project you want to see (type project id/ "
                       "all/ cancel type cancel): ")
        while choice not in all_proj_id:
            print("Invalid project id, Enter again.")
            choice = input("Which project you want to see (type project id/ "
                           "all/ cancel type cancel): ")
        if choice == 'cancel':
            return
        elif choice == "all":
            for i in self.pjt:
                print(i)
        elif self.pjt.find_from_id(choice):
            print(self.pjt.search(choice))

    def evaluate(self):
        all_proj_id = []
        for i in self.pjt.filter(lambda x: x['Status'] == "Ready to evaluate").table:
            all_proj_id.append(i['ProjectID'])
        if len(all_proj_id) == 0:
            print("There's not any project that ready to be evaluate.")
        elif len(all_proj_id) >= 1:
            print("Project that you can evaluate: ")
            for i in self.pjt.filter(
                    lambda x: x['Status'] == "Ready to evaluate").table:
                print(i)
            proj_id = input("Which project do you want to evaluate?(type project id/ cancel): ")
            while proj_id not in all_proj_id or proj_id != 'cancel':
                print("Invalid project id, Enter again.")
                proj_id = input("Which project do you want to evaluate?: ")
            if proj_id == 'cancel':
                return
            print(f"Evaluation for project id: {proj_id}")
            result = int(input("Enter score for this project(0-10): "))
            eval_proj_score = self.pjt.search(proj_id)
            score = eval_proj_score['Score'] + result
            if score >= 30:
                self.pjt.update(proj_id, "Status", "Approved")
            self.pjt.update(proj_id, "Score", score)


class advisor:
    def __init__(self, id, db):
        self.id = id
        self.pjt = db.search('Project')

    def ask_need(self):
        while True:
            print("1.See details of all/specific the project\n"
                  "2.Evaluate a project\n"
                  "3.Log out")
            choice = int(input("What do you want to do?: "))
            if choice in [1, 2, 3]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_proj(self):
        all_proj_id = ['all', 'cancel']
        for i in self.pjt.table:
            all_proj_id.append(i['ProjectID'])
        choice = input("Which project you want to see (type project id/ "
                       "all/ cancel type cancel): ")
        while choice not in all_proj_id:
            print("Invalid project id, Enter again.")
            choice = input("Which project you want to see (type project id/ "
                           "all/ cancel type cancel): ")
        if choice == 'cancel':
            return
        elif choice == "all":
            for i in self.pjt:
                print(i)
        elif self.pjt.find_from_id(choice):
            print(self.pjt.search(choice))



    def evaluate(self):
        all_proj_id = []
        for i in self.pjt.filter(lambda x: x['Status'] == "Ready to evaluate").table:
            all_proj_id.append(i['ProjectID'])
        if len(all_proj_id) == 0:
            print("There's not any project that ready to be evaluate.")
        elif len(all_proj_id) >= 1:
            print("Project that you can evaluate: ")
            for i in self.pjt.filter(lambda x: x['Status'] == "Ready to evaluate").table:
                print(i)
            proj_id = input("Which project do you want to evaluate?(type project id/ cancel): ")
            while proj_id not in all_proj_id or proj_id != 'cancel':
                print("Invalid project id, Enter again.")
                proj_id = input("Which project do you want to evaluate?: ")
            if proj_id == 'cancel':
                return
            print(f"Evaluation for project id: {proj_id}")
            result = int(input("Enter score for this project(0-10): "))
            eval_proj_score = self.pjt.search(proj_id)
            score = eval_proj_score['Score'] + result
            if score >= 30:
                self.pjt.update(proj_id, "Status", "Approved")
            self.pjt.update(proj_id, "Score", score)
