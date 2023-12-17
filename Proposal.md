# Draft code for evaluation step
### Faculty (Both normal and advisor)
- Evaluate projects
  - 0 - 10 score
### Note: 
- I have already added search and update function in table class, So I'll use it in this function.
- my_DB is defined in project_manage.py
```python
def evaluation():
    project_table = my_DB.search('Project')
    print("Project that you can evaluate: ")
    all_proj_id = []
    for i in project_table.filter(lambda x: x['Status'] == "Ready to evaluate"):
        print(i)
        all_proj_id.append(i['ProjectID'])
    proj_id = input("Which project do you want to evaluate?: ")
    while proj_id not in all_proj_id:
        print("Invalid project id, Enter again.")
        proj_id = input("Which project do you want to evaluate?: ")
    print(f"Evaluation for project id: {proj_id}")
    result = int(input("Enter score for this project(0-10): "))
    eval_proj_score = project_table.search(proj_id)
    score = eval_proj_score['Score'] + result
    if score >= 30:
        project_table.update(proj_id, "Status", "Approved")
    project_table.update(proj_id, "Score", score)
    
    
   ```