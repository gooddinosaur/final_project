from database import Read, DB, Table
import random
class admin():
    def __init__(self, id, db):
        self.id = id
        self.db = db

    def ask_need(self):
        print("1.See table in database (specific/all)\n2.Manage the "
              "database (insert/remove)\n3.Manage table in database")
        choice = int(input("What do you want to do?: "))
        return choice

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
        table_name = input("Which table you want to update? (table name): ")
        table = self.db.search(table_name)
        print("Before update")
        print(table.table)
        id = input("Which ID you want to update?: ")
        key = input("Which key you want to update?: ")
        value = input("What value you want to update?: ")
        Table.update(table, id, key, value)
        print(f"{self.id} has updated {table_name} table.")
        print(table.table)

class student:
    def __init__(self, id, db):
        self.id = id
        self.mpr = db.search('Member_pending_request')
        self.pjt = db.search('Project')
        self.log = db.search('login')
    def ask_need(self):
        print("1.See pending requests\n2.Create a project")
        choice = input("What do you want to do?: ")
        return choice

    def response_request(self):
        print(f"All pending request:")
        for y in self.mpr.table:
            if y['member_id'] == self.id:
                print(y)
        proj_id = input("Which project you want to accept: ")
        for i in self.pjt.table:
            if i['ProjectID'] == proj_id:
                if i['Member1'] == "":
                    i['Member1'] = self.id
                elif i['Member2'] == "":
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
                         "Lead": self.id, "Member1": "", "Member2": "",
                         "Advisor": "", "Status": "No member, No advisor"})
        for i in self.log:
            if i['ID'] == self.id:
                i['Role'] = "Lead"


