# Student
- See an invitational message from the lead student that already created his own project
  - Accept
  - Deny
- See and modify his project details
### Lead student
  - Create a project
  - See project status (pending member, pending advisor, or ready to solicit an advisor)
  - See and modify project information
  - Find members
    - See who has responded to the requests sent out
    - Send out requests to potential members
      - Member_pending_request table needs to be updated	
  - Send out request messages to a potential advisor
    - Advisor_pending_request table needs to be updated
    - Submit the final project report
### Member student
 - See project status (like pending member or advisor)
 - See and modify project information
   - Project table needs to be updated
 - See who has responded to the requests sent out
# Faculty
### Normal faculty who isn't an advisor
- See request to be a supervisor
  - Deny
- Can see all information of all project
- Evaluate projects
  - Pass
  - Not pass

### Advising faculty
- See request to be a supervisor
  - Accept (for project that want to be an advisor)
  - Deny (for project that not want to be an advisor)
- Can see all information of all project
- Evaluate projects
  - Pass
  - Not pass
- Approve the project

# Admin
 - Managing the database
   - Can update or change all tables in database
     - Remove
     - Insert
 
