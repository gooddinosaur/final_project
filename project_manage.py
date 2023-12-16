# import database module
from database import Read, DB, Table
from role import admin, student, member, lead
import csv

my_DB = DB()


# define a funcion called initializing

def initializing():
    read_person = Read('persons.csv')
    read_login = Read('login.csv')
    Read.insert(read_person)
    Read.insert(read_login)
    persons_table = Table('persons', read_person.info)
    login_table = Table('login', [])
    for i in range(len(persons_table.table)):
        role = persons_table.table[i]['type']
        login_table.insert({'person_id': persons_table.table[i]['ID'],
                            'username': persons_table.table[i]['fist'] + "." +
                                        persons_table.table[i]['last'][0],
                            'password': read_login.info[i]['password'],
                            'role': role})
    project_table = Table('Project', [])
    # for x in range(len(num_project):
    # project_table.insert({})
    Advisor_pending_request_table = Table('Advisor_pending_request', [])
    Member_pending_request_table = Table('Member_pending_request', [])
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
    username = input("Enter username : ")
    password = input("Enter password : ")
    login_info = my_DB.search('login')
    for i in login_info.table:
        if username == i['username'] and password == i['password']:
            print(f"{username} logged in as {i['role']}")
            return [i['person_id'], i['role']]
    return None


def exit():
    for table in my_DB.database:
        file = open(table.table_name, 'w')
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
    if val[1] == 'admin':
        person = admin(val[0], my_DB)
        choice = admin.ask_need(person)
        if choice == 1:
            admin.see_table(person)
        elif choice == 2:
            admin.manage_database(person)
        elif choice == 3:
            admin.manage_table(person)
    # see and do admin related activities
    elif val[1] == 'student':
        person = student(val[0], my_DB)
        choice = student.ask_need(person)
        if choice == 1:
            student.response_request(person)
        elif choice == 2:
            student.create_project(person)
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
    # see and do lead related activities
    elif val[1] == 'faculty':
        pass
    # see and do faculty related activities
    elif val[1] == 'advisor':
        pass


# make calls to the initializing and login functions defined above

initializing()
val = login()
check_role(val)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id
# see and do advisor related activities
# once everyhthing is done, make a call to the exit function
exit()
