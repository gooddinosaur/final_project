"""For starting project manager program"""
import csv
from database import Read, DB, Table
from role import admin, student, member, lead, faculty, advisor

my_DB = DB()


def initializing():
    """Start a program"""
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
    advisor_pending_request_table = Table('Advisor_pending_request',
                                          read_ad_pen_req.info)
    member_pending_request_table = Table('Member_pending_request',
                                         read_mem_pen_req.info)
    my_DB.insert(persons_table)
    my_DB.insert(login_table)
    my_DB.insert(project_table)
    my_DB.insert(advisor_pending_request_table)
    my_DB.insert(member_pending_request_table)
    print(login_table)


def login():
    """Login function to get user id and role"""
    print("If you want to exit program just press enter 2 times.")
    username = input("Enter username : ")
    password = input("Enter password : ")
    print()
    login_info = my_DB.search('login')
    for info in login_info.table:
        if username == info['username'] and password == info['password']:
            print(f"  ***  {username} logged in as {info['role']}  ***")
            print("----- Welcome to project manage program -----")
            print("        ----- Here's your menu -----")
            print()
            return [info['ID'], info['role']]
    return None


def _exit():
    """Exit function to write all info into csv file"""
    for table in my_DB.database:
        file = open(table.table_name + ".csv", 'w')
        writer = csv.writer(file)
        keys = []
        if len(table.table) >= 1:
            for key in table.table[0].keys():
                keys.append(key)
            writer.writerow(keys)
            for _dict in table.table:
                writer.writerow(_dict.values())
        file.close()


def check_role(val):
    """To check role of user's role and do user's role related activity."""
    if val is None:
        print("No user exist")
    elif val[1] == 'admin':
        person = admin(val[0], my_DB)
        choice = admin.ask_need(person)
        if choice == 1:
            admin.see_table(person)
        elif choice == 2:
            admin.add_entry(person)
        elif choice == 3:
            admin.remove_entry(person)
        elif choice == 4:
            admin.update_table(person)
        elif choice == 5:
            print()
            return -99
    elif val[1] == 'student':
        person = student(val[0], my_DB)
        choice = student.ask_need(person)
        if choice == 1:
            student.response_request(person)
        elif choice == 2:
            student.create_project(person)
        elif choice == 3:
            print()
            return -99
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
            print()
            return -99
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
        elif choice == 6:
            lead.update_proj_status(person)
        elif choice == 7:
            lead.submit_project(person)
        elif choice == 8:
            print()
            return -99
    elif val[1] == 'faculty':
        person = faculty(val[0], my_DB)
        choice = faculty.ask_need(person)
        if choice == 1:
            faculty.see_req(person)
        elif choice == 2:
            faculty.see_proj(person)
        elif choice == 3:
            faculty.evaluate(person)
        elif choice == 4:
            print()
            return -99
    elif val[1] == 'advisor':
        person = advisor(val[0], my_DB)
        choice = advisor.ask_need(person)
        if choice == 1:
            advisor.see_proj(person)
        elif choice == 2:
            advisor.evaluate(person)
        elif choice == 3:
            print()
            return -99


initializing()
val = login()
while val is not None:
    i = check_role(val)
    while i != -99:
        i = check_role(val)
    val = login()

_exit()
