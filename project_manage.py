# import database module
from database import Read, DB, Table
from role import admin, student, member, lead, faculty, advisor
import csv

my_DB = DB()


# define a funcion called initializing

def initializing():
    read_person = Read('persons.csv')
    read_login = Read('login.csv')
    read_project = Read('Project.csv')
    read_ad_pen_req = Read('Advisor_pending_request.csv')
    read_mem_pen_req = Read('Member_pending_request.csv')
    Read.insert(read_person)
    Read.insert(read_login)
    Read.insert(read_project)
    Read.insert(read_ad_pen_req)
    Read.insert(read_mem_pen_req)
    persons_table = Table('persons', read_person.info)
    login_table = Table('login', read_login.info)
    project_table = Table('Project', read_project.info)
    Advisor_pending_request_table = Table('Advisor_pending_request', read_ad_pen_req.info)
    Member_pending_request_table = Table('Member_pending_request', read_mem_pen_req.info)
    my_DB.insert(persons_table)
    my_DB.insert(login_table)
    my_DB.insert(project_table)
    my_DB.insert(Advisor_pending_request_table)
    my_DB.insert(Member_pending_request_table)
    print(persons_table)
    print(login_table)


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a funcion called login

def login():
    print("If you want to exit program just press enter")
    username = input("Enter username : ")
    password = input("Enter password : ")
    login_info = my_DB.search('login')
    for i in login_info.table:
        if username == i['username'] and password == i['password']:
            print(f"***  {username} logged in as {i['role']}  ***")
            return [i['ID'], i['role']]
    return None


def exit():
    for table in my_DB.database:
        file = open(table.table_name + ".csv", 'w')
        writer = csv.writer(file)
        keys = []
        if len(table.table) >= 1:
            for key in table.table[0].keys():
                keys.append(key)
            writer.writerow(keys)
            for dict in table.table:
                writer.writerow(dict.values())
        file.close()


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries.
# For this project, you also need to know how to do the reverse, i.e.,
# writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python
def check_role(val):  # val 0 is id, val 1 is roles
    if val is None:
        print("No user exist")
    elif val[1] == 'admin':
        person = admin(val[0], my_DB)
        choice = admin.ask_need(person)
        if choice == 1:
            admin.see_table(person)
        elif choice == 2: #Add entry
            admin.add_entry(person)
        elif choice == 3: #remove entry
            admin.remove_entry(person)
        elif choice == 4:
            admin.update_table(person)
        elif choice == 5:
            return -99
    # see and do admin related activities
    elif val[1] == 'student':
        person = student(val[0], my_DB)
        choice = student.ask_need(person)
        if choice == 1:
            student.response_request(person)
        elif choice == 2:
            student.create_project(person)
        elif choice == 3:
            return -99
    # see and do student related activities
    elif val[1] == 'member':
        person = member(val[0], my_DB)
        choice = member.ask_need(person)
        if choice == 1:
            member.see_proj_status(person)
        elif choice == 2:
            member.see_modified(person)
        elif choice == 3:
            member.see_response(person)
        elif choice == 4:
            return -99
    # see and do member related activities
    elif val[1] == 'lead':
        person = lead(val[0], my_DB)
        choice = lead.ask_need(person)
        if choice == 1:
            lead.see_proj_status(person)
        elif choice == 2:
            lead.see_modified(person)
        elif choice == 3:
            lead.see_response(person)
        elif choice == 4:
            lead.find_member(person)
        elif choice == 5:
            lead.find_advisor(person)
        elif choice == 6: #Submit project
            pass
        elif choice == 7:
            return -99
    # see and do lead related activities
    elif val[1] == 'faculty':
        person = faculty(val[0], my_DB)
        choice = faculty.ask_need(person)
        if choice == 1:
            faculty.see_req(person)
        elif choice == 2:
            faculty.see_req(person)
        elif choice == 3: #Evaluate
            pass
        elif choice == 4:
            return -99
    # see and do faculty related activities
    elif val[1] == 'advisor':
        person = advisor(val[0], my_DB)
        choice = advisor.ask_need(person)
        if choice == 1:
            advisor.see_proj(person)
        elif choice == 2: #Evaluate
            pass
        elif choice == 3:
            return -99


# make calls to the initializing and login functions defined above

initializing()
val = login()
while val is not None: # ต้องทำให้หยุดโปรแกรมได้
    i = check_role(val)
    while i != -99:
        i = check_role(val)

    val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id
# see and do advisor related activities
# once everyhthing is done, make a call to the exit function
exit()
