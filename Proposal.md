# Draft code for evaluation step
### Note: 
- I have already added update function in table class, So I'll use it in this function.
- my_DB is defined in project_manage.py
```python
def evaluation(project_id):
    project_table = my_DB.search('project')
    print(f"Evaluation for project id: {project_id}")
    result = input("Pass/Not pass")
    if result == "Pass":
        project_table.update(project_id, 'Evaluation_status', 'Pass')
        return True
    elif result == "Not Pass":
        project_table.update(project_id, 'Evaluation_status', 'Not Pass')
        return False    
    print("Project ID not found")
    
   ```