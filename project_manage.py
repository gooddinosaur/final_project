# import database module
from database import Read, DB, Table

my_DB = DB()
# define a funcion called initializing

def initializing():
    read_person = Read('persons.csv')
    read_login = Read('login.csv')
    Read.insert(read_person)
    Read.insert(read_login)
    persons_table = Table('persons', read_person.info)
    my_DB.insert(persons_table)
    login_table = Table('login', [])
    for i in range(len(persons_table.table)):
        if persons_table.table[i]['type'] == 'admin':
            role = "Admin"
        elif persons_table.table[i]['type'] == 'student':
            role = "Member"
        elif persons_table.table[i]['type'] == 'faculty':
            role = "Faculty"
        login_table.insert({'person_id': persons_table.table[i]['ID'],
                            'username': persons_table.table[i]['fist'] + "." +
                                        persons_table.table[i]['last'][0],
                            'password': read_login.info[i]['password'],
                            'role': role})
        my_DB.insert(login_table)
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
            return [i['person_id'], i['role']]
    return None

# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
