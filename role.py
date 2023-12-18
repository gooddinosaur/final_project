"""Code for every role"""
from datetime import date
import random


class admin:
    """Class for all function(command) that admin role can do."""
    def __init__(self, _id, _db):
        self.id = _id
        self.db = _db
        self.pt = _db.search('persons')
        self.lt = _db.search('login')

    def ask_need(self):
        """Ask what admin want to do"""
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
        """Function that make admin can see table in database (specific/all)"""
        all_table_name = ["all", 'cancel']
        for x in self.db.database:
            all_table_name.append(x.table_name)
        choice = input(
            "Which table you want to see (type table name/"
            "all or cancel type cancel): ")
        while choice not in all_table_name:
            print("Invalid table, Enter again")
            choice = input(
                "Which table you want to see (type table name/"
                "all or cancel type cancel): ")
        if choice == 'cancel':
            print()
            return
        elif choice == "all":
            for i in self.db.database:
                print(i)
            print()
        elif self.db.search(choice) is not None:
            print(self.db.search(choice))
            print()

    def add_entry(self):
        """Function for add new person to database."""
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
        print(f"Created id: {new_id} successful")
        print(f"ID: {new_id} created by {self.id}")
        print()

    def remove_entry(self):
        """Function for remove existed person from database."""
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
            print(f"Remove id:{id_remove} successful")
            print(f"{id_remove} has removed by {self.id}(admin)")
            print()

    def update_table(self):
        """Function for update(change info) in specific table."""
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
        _id = input("Which ID you want to update?: ")
        key = input("Which key you want to update?: ")
        value = input("What value you want to update?: ")
        table.update(_id, key, value)
        print(f"{self.id} has updated {table_name} table.")
        print("After update")
        print(table.table)
        print()


class student:
    """Class for all function(command) that student role can do."""
    def __init__(self, id, db):
        self.id = id
        self.mpr = db.search('Member_pending_request').filter(
            lambda x: x['member_id'] == id and x['Response'] == 'pending')
        self.pjt = db.search('Project')
        self.log = db.search('login').filter(lambda x: x['ID'] == id)

    def ask_need(self):
        """Ask what student want to do"""
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
        """Function for student to see his pending member request."""
        if len(self.mpr.table) == 0:
            print("You have no pending request.")
            print()
        elif len(self.mpr.table) >= 1:
            print(f"All pending request:")
            all_proj_id = ['none']
            for y in self.mpr.table:
                all_proj_id.append(y['ProjectID'])
                print(y)
            print()
            proj_id = input(
                "Which project you want to accept (if deny all type none): ")
            while proj_id not in all_proj_id:
                print("Invalid choice, Enter again")
                proj_id = input(
                    "Which project you want to accept "
                    "(if deny all type none): ")
            for i in self.pjt.table:
                if i['ProjectID'] == proj_id:
                    if i['Member1'] == "-":
                        i['Member1'] = self.id
                        i['Status'] = "Have 1 member"
                    elif i['Member2'] == "-":
                        i['Member2'] = self.id
                        i['Status'] = "Have 2 members"
            for x in self.mpr.table:
                if x['ProjectID'] == proj_id:
                    if x['member_id'] == self.id:
                        x['Response'] = "Accept"
                        x['Response_date'] = date.today().strftime("%Y-%m-%d")
                elif x['ProjectID'] != proj_id:
                    if x['member_id'] == self.id:
                        x['Response'] = "Deny"
                        x['Response_date'] = date.today().strftime("%Y-%m-%d")
            for s in self.log.table:
                if s['ID'] == self.id:
                    s['role'] = "member"
            print("Logout and login again to access your project")

    def create_project(self):
        """Function for student to create his own project."""
        lead_proj = self.pjt.select(['Lead'])
        for i in lead_proj:
            if i['Lead'] == self.id:
                print(
                    "Can't create project, You have already created project.")
                return
        for x in self.mpr.table:
            if x['member_id'] == self.id:
                x['Response'] = "Deny"
                x['Response_date'] = date.today().strftime("%Y-%m-%d")
        proj_id_info = self.pjt.select(['ProjectID'])
        proj_id_info_list = []
        for x in proj_id_info:
            proj_id_info_list.append(x['ProjectID'])
        project_id = ""
        for k in range(7):
            project_id += str(random.randint(0, 9))
        while project_id in proj_id_info_list:
            project_id = ""
            for k in range(7):
                project_id += str(random.randint(0, 9))
        title = input("Enter title of your project: ")
        self.pjt.insert({"ProjectID": project_id, "Title": title,
                         "Lead": self.id, "Member1": "-", "Member2": "-",
                         "Advisor": "-",
                         "Status": "Just Created No member, No advisor",
                         "Score": 0, "Scorer": ""})
        for s in self.log.table:
            if s['ID'] == self.id:
                s['role'] = "lead"
        print("Project has created.")
        print("Logout and login again to access your project")
        print()


class member:
    """Class for all function(command) that member role can do."""
    def __init__(self, id, db):
        self.id = id
        self.pjt = db.search('Project').filter(lambda x: self.id in x.values())
        self.proj_id = self.pjt.table[0].get('ProjectID')
        self.mpr = db.search('Member_pending_request').filter(
            lambda x: x['ProjectID'] == self.proj_id)
        self.apr = (db.search('Advisor_pending_request').filter
                    (lambda x: x['ProjectID'] == self.proj_id))

    def ask_need(self):
        """Ask what member want to do"""
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
        """Function for member to see and modify his project."""
        print("Your project information:")
        print(self.pjt.table)
        choice = input("Do you want to modified(yes/no): ")
        allowed_key = ['ProjectID', 'Title', 'Lead', 'Member1', 'Member2',
                       'Advisor']
        not_allowed_key = ['Status', 'Score']
        if choice == "yes":
            key = input("Which key you want to modified?: ")
            while key in not_allowed_key or key not in allowed_key:
                if key == 'Score':
                    print(
                        "You aren't able to score by yourself!!, Enter again")
                elif key == 'Status':
                    print(
                        "You aren't able to change project status by "
                        "yourself!!, Enter again")
                elif key not in ['Score', 'Status']:
                    print("Key is invalid, Enter again")
                key = input("Which key you want to modified?: ")
            value = input("What value you want to modified?: ")
            self.pjt.update(self.proj_id, key, value)
            dic = self.pjt.search(self.proj_id)
            k = [i for i in dic if dic[i] == self.id]
            print(f"{self.id} ({k[0]}) has updated project id:{self.proj_id}")
            print()

    def see_proj_status(self):
        """Function for member to see his project status."""
        print("Your project status:")
        print(self.pjt.table[0]['Status'])
        print()

    def see_response(self):
        """Function for member to see his project pending request."""
        filter_mpr = self.mpr
        filter_apr = self.apr
        if len(filter_mpr.table) == 0:
            print("You haven't sent request to be member to any student.")
            print()
        elif len(filter_mpr.table) >= 1:
            print("All member pending request:")
            for i in filter_mpr.table:
                print(i)
            print()
        if len(filter_apr.table) == 0:
            print("You haven't sent request to be advisor to any faculty.")
            print()
        elif len(filter_apr.table) >= 1:
            print("All advisor pending request:")
            for i in filter_apr.table:
                print(i)
            print()


class lead:
    """Class for all function(command) that lead role can do."""
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
        """Ask what lead want to do"""
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
            if choice in [1, 2, 3, 4, 5, 6, 7, 8]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_proj_status(self):
        """Function for lead to see his project status."""
        print("Your project status:")
        proj_dic = self.pjt.search(self.proj_id)
        print(proj_dic['Status'])
        print()

    def see_modified(self):
        """Function for lead to see and modify his project."""
        print("Your project information:")
        print(self.opjt.table)
        choice = input("Do you want to modified(yes/no): ")
        allowed_key = ['ProjectID', 'Title', 'Lead', 'Member1', 'Member2',
                       'Advisor']
        not_allowed_key = ['Status', 'Score']
        if choice == "yes":
            key = input("Which key you want to modified?: ")
            while key in not_allowed_key or key not in allowed_key:
                if key == 'Score':
                    print(
                        "You aren't able to score by yourself!!, Enter again")
                elif key == 'Status':
                    print(
                        "You aren't able to change project status "
                        "by yourself!!, Enter again")
                elif key not in ['Score', 'Status']:
                    print("Key is invalid, Enter again")
                key = input("Which key you want to modified?: ")
            value = input("What value you want to modified?: ")
            self.pjt.update(self.proj_id, key, value)
            print(f"{self.id} (Lead) has updated project id: {self.proj_id}")
            print()
        elif choice == "no":
            print()

    def see_response(self):
        """Function for lead to see his project pending request."""
        filter_mpr = self.mpr.filter(lambda x: x['ProjectID'] == self.proj_id)
        filter_apr = self.apr.filter(lambda x: x['ProjectID'] == self.proj_id)
        if len(filter_mpr.table) == 0:
            print("You haven't sent request to be member to any student.")
            print()
        elif len(filter_mpr.table) >= 1:
            print("All member pending request:")
            for i in filter_mpr.table:
                print(i)
            print()
        if len(filter_apr.table) == 0:
            print("You haven't sent request to be advisor to any faculty.")
            print()
        elif len(filter_apr.table) >= 1:
            print("All advisor pending request:")
            for i in filter_apr.table:
                print(i)
            print()

    def find_member(self):
        """Function for lead to sent request to find members."""
        print("All people that you can request:")
        can_req = self.lt.filter(lambda x: x['role'] == 'student')
        for i in can_req.table:
            print(i)
        member_id = input("Who will you request him to be member"
                          "(type his ID): ")
        message = input("A message to him: ")
        print("Request has been sent.")
        print()
        self.mpr.insert({'ProjectID': self.proj_id, 'to_be_member': message,
                         'Response': 'pending', "Response_date": "-",
                         "member_id": member_id})

    def find_advisor(self):
        """Function for lead to sent request to find an advisor."""
        print("All people that you can request:")
        can_req = self.lt.filter(lambda x: x['role'] == 'faculty')
        for i in can_req.table:
            print(i)
        advisor_id = input("Who will you request him to be member"
                           "(type his ID): ")
        message = input("A message to him: ")
        print(f"Request has been sent to advisor id: {advisor_id}.")
        print()
        self.apr.insert({'ProjectID': self.proj_id, 'to_be_advisor': message,
                         'Response': 'pending', "Response_date": "-",
                         "advisor_id": advisor_id})

    def update_proj_status(self):
        """Function for lead to make his project status up to date."""
        proj_dic = self.pjt.search(self.proj_id)
        if proj_dic['Status'] == 'Approved':
            print("Your project is already approved, No need to update.")
            print()
            return
        status = ""
        if proj_dic['Member1'] == "-" and proj_dic['Member2'] == "-" and \
                proj_dic['Advisor'] == "-":
            print("Your project status has updated.")
            print()
            return
        elif proj_dic['Member1'] != "-" and proj_dic['Member2'] == "-" and \
                proj_dic['Advisor'] == "-":
            status += "Have 1 member, No advisor"
        elif proj_dic['Member1'] != "-" and proj_dic['Member2'] != "-" and \
                proj_dic['Advisor'] == "-":
            status += "Have 2 members, No advisor"
        elif proj_dic['Member1'] != "-" and proj_dic['Member2'] != "-" and \
                proj_dic['Advisor'] != "-":
            status += "Have 2 members, 1 advisor"
        filter_mpr = self.mpr.filter(lambda x: x['ProjectID'] == self.proj_id)
        filter_apr = self.apr.filter(lambda x: x['ProjectID'] == self.proj_id)
        self.pjt.update(self.proj_id, "Status", status)
        count_pending_m = 0
        count_pending_a = 0
        for i in filter_mpr.table:
            if i['Response'] == 'pending':
                count_pending_m += 1
        for j in filter_apr.table:
            if j['Response'] == 'pending':
                count_pending_a += 1
        if count_pending_m == 0 and count_pending_a == 0:
            status += "and Ready to submit."
        elif count_pending_m >= 1 or count_pending_a >= 1:
            status += "and Not ready to submit."
        print("Your project status has updated.")
        print()

    def submit_project(self):
        """Function for lead to submit his project for advisor/
        faculty will evaluate."""
        proj_dic = self.pjt.search(self.proj_id)
        if proj_dic['Status'] == 'Approved':
            print("Your project is already approved, Can't submit again.")
            print()
            return
        filter_mpr = self.mpr.filter(lambda x: x['ProjectID'] == self.proj_id)
        filter_apr = self.apr.filter(lambda x: x['ProjectID'] == self.proj_id)
        count_pending_m = 0
        count_pending_a = 0
        for i in filter_mpr.table:
            if i['Response'] == 'pending':
                count_pending_m += 1
        for j in filter_apr.table:
            if j['Response'] == 'pending':
                count_pending_a += 1
        if count_pending_m == 0 and count_pending_a == 0:
            check = input("Are you sure you want to submit?(confirm,cancel): ")
            while check not in ['confirm', 'cancel']:
                print("Invalid choice, Enter again")
                check = input(
                    "Are you sure you want to submit?(confirm,cancel): ")
            if check == 'confirm':
                self.pjt.update(self.proj_id, "Status", "Pending evaluate")
                print("Your project has submitted.")
                print()
            elif check == 'cancel':
                print("Canceled submission")
        else:
            print(
                "Your project can't submit yet, because there's "
                "pending request.")
            if count_pending_m >= 1:
                print(f"{count_pending_m} pending member request.")
                print(f"{count_pending_a} pending adviser request.")
                print()


class faculty:
    """Class for all function(command) that faculty role can do."""
    def __init__(self, id, db):
        self.id = id
        self.apr = db.search('Advisor_pending_request').filter(
            lambda x: x['advisor_id'] == self.id and x[
                'Response'] == 'pending')
        self.pjt = db.search('Project')
        self.log = db.search('login').filter(lambda x: x['ID'] == self.id)

    def ask_need(self):
        """Ask what faculty want to do"""
        while True:
            print("1.See request to be a supervisor\n"
                  "2.See details of all/specific the project\n"
                  "3.Evaluate a project\n"
                  "4.Log out")
            choice = int(input("What do you want to do: "))
            if choice in [1, 2, 3, 4]:
                return choice
            print("Invalid choice, Enter again")
            print()

    def see_req(self):
        """Function for faculty to see his request to be advisor"""
        all_proj_id = ['quit']
        for x in self.apr.table:
            all_proj_id.append(x['ProjectID'])
        if len(self.apr.table) == 0:
            print("You have no pending request.")
        elif len(self.apr.table) >= 1:
            print("Your pending request: ")
            for i in self.apr.table:
                print(i)
            proj_id = input("Which project you want to accept/deny "
                            "(accept projectID / deny projectID / "
                            "quit)?: ").split()
            while proj_id[0] != 'quit':
                while proj_id[1] not in all_proj_id:
                    print("Invalid project id, Enter again")
                    proj_id = input(
                        "Which project you want to accept/deny(accept project"
                        "ID / deny projectID / quit)?: ").split()
                    if proj_id[0] == 'quit':
                        print()
                        return
                if proj_id[0] == 'accept':
                    for s in self.log.table:
                        s['role'] = "advisor"
                    for i in self.pjt.table:
                        if i['ProjectID'] == proj_id[1]:
                            i['Advisor'] = self.id
                    for y in self.pjt.table:
                        if y['ProjectID'] == proj_id[1]:
                            y['Status'] += ", Have advisor"
                    for x in self.apr.table:
                        if x['ProjectID'] == proj_id[1]:
                            if x['advisor_id'] == self.id:
                                x['Response'] = "Accept"
                                x['Response_date'] = date.today().strftime(
                                    "%Y-%m-%d")
                elif proj_id[0] == 'deny':
                    for i in self.apr.table:
                        if i['ProjectID'] == proj_id[1]:
                            if i['advisor_id'] == self.id:
                                i['Response'] = 'Deny'
                                i['Response_date'] = date.today().strftime(
                                    "%Y-%m-%d")
                proj_id = input(
                    "Which project you want to accept/deny(accept project"
                    "ID / deny projectID / quit)?: ").split()
            print()

    def see_proj(self):
        """Function for faculty to see project information"""
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
            print()
        elif self.pjt.find_from_id(choice):
            print(self.pjt.search(choice))
            print()

    def evaluate(self):
        """Function for faculty to evaluate project that ready to evaluate."""
        all_proj_id = ['cancel']
        for i in self.pjt.filter(
                lambda x: x['Status'] == "Pending evaluate").table:
            all_proj_id.append(i['ProjectID'])
        if len(all_proj_id) == 1:
            print("There's not any project that ready to be evaluate.")
        elif len(all_proj_id) >= 2:
            print("Project that you can evaluate: ")
            for i in self.pjt.filter(
                    lambda x: x['Status'] == "Pending evaluate").table:
                print(i)
            proj_id = input(
                "Which project do you want to evaluate?(type project "
                "id/ cancel): ")
            while proj_id not in all_proj_id:
                print("Invalid project id, Enter again.")
                proj_id = input("Which project do you want to evaluate?: ")
            if proj_id == 'cancel':
                return
            proj_info = self.pjt.search(proj_id)
            scorers = proj_info['Scorer']
            if self.id not in scorers:
                print(f"Evaluation for project id: {proj_id}")
                result = int(input("Enter score for this project(0-10): "))
                print(f"You have scored project id: {proj_id}")
                print()
                score = int(proj_info['Score']) + result
                self.pjt.update(proj_id, "Score", score)
                if scorers == "":
                    scorers = self.id
                elif scorers != "":
                    scorers += f"-{self.id}"
                self.pjt.update(proj_id, "Scorer", scorers)
                if score >= 30 and len(scorers) == 47:
                    self.pjt.update(proj_id, "Status", "Approved")
            elif self.id in proj_info['Scorer']:
                print("You have already evaluate this project.")
                print()


class advisor:
    """Class for all function(command) that faculty role can do."""
    def __init__(self, id, db):
        self.id = id
        self.pjt = db.search('Project')

    def ask_need(self):
        """Ask what advisor want to do"""
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
        """Function for advisor to see project information"""
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
            print()
        elif self.pjt.find_from_id(choice):
            print(self.pjt.search(choice))
            print()

    def evaluate(self):
        """Function for faculty to evaluate project that ready to evaluate."""
        all_proj_id = ['cancel']
        for i in self.pjt.filter(
                lambda x: x['Status'] == "Pending evaluate").table:
            all_proj_id.append(i['ProjectID'])
        if len(all_proj_id) == 1:
            print("There's not any project that ready to be evaluate.")
        elif len(all_proj_id) >= 2:
            print("Project that you can evaluate: ")
            for i in self.pjt.filter(
                    lambda x: x['Status'] == "Pending evaluate").table:
                print(i)
            proj_id = input(
                "Which project do you want to evaluate?"
                "(type project id/ cancel): ")
            while proj_id not in all_proj_id:
                print("Invalid project id, Enter again.")
                proj_id = input("Which project do you want to evaluate?: ")
            if proj_id == 'cancel':
                return
            proj_info = self.pjt.search(proj_id)
            scorers = proj_info['Scorer']
            if self.id not in scorers:
                print(f"Evaluation for project id: {proj_id}")
                result = int(input("Enter score for this project(0-10): "))
                print(f"You have scored project id: {proj_id}")
                print()
                score = int(proj_info['Score']) + result
                self.pjt.update(proj_id, "Score", score)
                if scorers == "":
                    scorers = self.id
                elif scorers != "":
                    scorers += f"-{self.id}"
                self.pjt.update(proj_id, "Scorer", scorers)
                if score >= 30 and len(scorers) == 47:
                    self.pjt.update(proj_id, "Status", "Approved")
            elif self.id in proj_info['Scorer']:
                print("You have already evaluate this project.")
                print()
