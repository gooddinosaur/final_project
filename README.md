# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv
----
# File in this repo
- role.py
- database.py
- project_manage.py
- README.md
- Proposal.md
- Project.csv
- persons.csv
- Member_pending_request.csv
- login.csv
- Advisor_pending_request.csv
- TODO.md

###  1.Role.py

- Admin class
  - Class for all function(command) that admin role can do.
    1. ask_need
       - Ask what admin want to do
    2. see_table
       - Function that make admin can see table in database (specific/all)
    3. add_entry
       - Function for add new person to database.
    4. remove_entry
       - Function for remove existed person from database.
    5. update_table
       - Function for update(change info) in specific table.


- Student class
  - Class for all function(command) that student role can do.
    1. ask_need
       - Ask what student want to do
    2. response_request
       - Function for student to see his pending member request.
         - Which can response by 
           - Accept
           - Deny
    3. create_project
       - Function for student to create his own project.


- Member class
  - Note: Member is student who already in a group.
  - Class for all function(command) that member role can do.
    1. ask_need
       - Ask what member want to do
    2. see_modified
       - Function for member to see his project.
       - Function for member to modified his project
         - Want to modify
         - Doesn't want to modify
    3. see_proj_status
       - Function for member to see his project status.
    4. see_response
       - Function for member to see his project pending request.
         - Pending member request
         - Pending advisor request


- Lead class
  - Note: Lead is student who created his own project.
  - Class for all function(command) that lead role can do.
    1. ask_need
       - Ask what lead want to do
    2. see_proj_status
       - Function for lead to see his project status.
    3. see_modified
       - Function for lead to see his project.
       - Function for lead to modified his project
          - Want to modify
          - Doesn't want to modify
    4. see_response
       - Function for lead to see his project pending request.
         - Pending member request
         - Pending advisor request
    5. find_member
       - Function for lead to sent request to find members.
    6. find_advisor
       - Function for lead to sent request to find an advisor.
    7. update_proj_status
       - Function for lead to make his project status up to date.
    8. submit_project
       - Function for lead to submit his project for advisor/faculty will evaluate.


- Faculty class
  - Class for all function(command) that faculty role can do.
    1. ask_need
       - Ask what faculty want to do
    2. see_req
       - Function for faculty to see his request to be advisor
         - Accept
         - Deny
    3. see_proj
       - Function for faculty to see project information
         - All project information
         - Specific project (1 project)
    4. evaluate
       - Function for faculty to evaluate project that ready to evaluate.
         - Score 0 - 10


- Advisor class
  - Note: Advisor is faculty who accept to be advisor for any group.
  - Class for all function(command) that faculty role can do.
    1. ask_need
       - Ask what advisor want to do
    2. see_proj
       - Function for advisor to see project information
         - All project information
         - Specific project (1 project)
    3. evaluate
       - Function for faculty to evaluate project that ready to evaluate.
         - Score 0 - 10
 
   
###  2.database.py
- Read class
  - Class for read csv file.
    1. insert
       - Function for insert information into a table.


- DB class
  - Class for database function
    1. insert
       - Function for insert new table into database.
    2. remove
       - Function for remove existed table from database.
    3. search
       - Function for search table in database by table_name
         - Return table


- Table class
  - Class for table function 
    1. join
       - Function for joining between table and table
    2. insert
       - Function for add new dic into a table
    3. update
       - Function to update information in a table
    4. remove
       - Function to remove dic from a table
    5. filter
       - Function to filter table from selected input
    6. aggregate
       - Function to make function to a table
    7. select
       - Function to select key in a dic in a table
          - Return all dic in table with only selected key.
    8. find_from_id
       - Function to check that input id is in a table or not.
    9. search
       - Function to return information about that input id.


###  3.project_manage.py
- Initializing function
  - To start program
  - Create all table that need to use in program
- Login function
  - To login user and return user's id and user's role
- Exit function
  - To write all new information into csv files.
- Check_role function
  - To check role of user's role and do user's role related activity.


###  4.README.md
- To describe all this final project.


###  5.Proposal.md
- To describe about evaluation step


###  6.Project.csv
- To store information about project (project table)


###  7.persons.csv
- To store information about all person in database.


### 8.Member_pending_request.csv
- To store all member pending request from every project.


### 9.login.csv
- To store all user login information 


### 10.Advisor_pending_request.csv
- To store all advisor pending request from every project. 


### 11.TODO.md
- To describe what to do in this final project.
----
# How to compile and run your project.
- Open project_mange.py and run
----
# Table detailing each role and its actions

| Role    | Action                                  | Method              | Class   | Completion |
|---------|-----------------------------------------|---------------------|---------|------------|
| admin   | Begin admin class                       | init                | admin   | 100%       |
| admin   | See table in database                   | see_table           | admin   | 100%       |
| admin   | Add new user                            | add_entry           | admin   | 100%       |
| admin   | Remove user                             | remove_entry        | admin   | 100%       |
| admin   | Update information in table             | update_table        | admin   | 100%       |
| student | Begin student class                     | init                | student | 100%       |
| student | See pending to be member                | response_request    | student | 100%       |
| student | Create a project                        | create_project      | student | 100%       |
| member  | See project status                      | see_proj_status     | student | 100%       |
| member  | See and Modified project information    | see_modified        | student | 100%       |
| member  | See who response to pending request     | see_response        | student | 100%       |
| lead    | See project status                      | see_proj_status     | lead    | 100%       |
| lead    | See and Modified project information    | see_modified        | lead    | 100%       |
| lead    | See who response to pending request     | see_response        | lead    | 100%       |
| lead    | Send out requests to find members       | find_member         | lead    | 100%       |
| lead    | Send out requests to find advisor       | find_advisor        | lead    | 100%       |
| lead    | Update project status                   | update_proj_status  | lead    | 100%       |
| lead    | Submit project                          | submit_project      | lead    | 100%       |
| faculty | See request to be a supervisor          | see_req             | faculty | 100%       |
| faculty | See details of all/specific the project | see_proj            | faculty | 100%       |
| faculty | Evaluate a project                      | evaluate            | faculty | 100%       |
| advisor | See details of all/specific the project | see_proj            | advisor | 100%       |
| advisor | Evaluate a project                      | evaluate            | advisor | 100%       |

----
