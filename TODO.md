# Student
- See an invitational message from the lead student that already created his own project
  - Accept
  - Deny
    - Project table needs to be updated
    - Member pending request table needs to be updated.
- Create a Project
  - Project table needs to be updated
  - If that student have pending member request from other student
    - Member pending request table needs to be updated.
### Lead student
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
  - Accept
  - Deny
- Can see all information of all project
- Evaluate projects
  - Score 0 - 10
  - Project will approve, If score >= 30 after all faculty evaluate.

### Advising faculty
- Can see all information of all project
- Evaluate projects
  - Score 0 - 10
  - Project will approve, If score >= 30 after all faculty evaluate.

# Admin
 - Managing the database
   - Can add entry and remove entry in database
     - Add user
     - Remove user
   - Update table in database
     - Change value 
