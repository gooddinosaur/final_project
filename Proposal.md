# Draft code for evaluation step
### Faculty (Both normal and advisor)
- Evaluate projects
  - 0 - 10 score for each faculty
  - If score >= 30 then project is approved
### Note: 
- I have already added search and update function in table class, So I'll use it in this function.
- my_DB is defined in project_manage.py
```python
    def evaluate(self):
        all_proj_id = ['cancel']
        for i in self.pjt.filter(
                lambda x: x['Status'] == "Pending evaluate").table:
            all_proj_id.append(i['ProjectID'])
        if len(all_proj_id) == 1:
            print("There's not any project that ready to be evaluate.")
        elif len(all_proj_id) >= 2:
            print("Project that you can evaluate: ")
            for i in self.pjt.filter(
                    lambda x: x['Status'] == "Pending evaluate").table:
                print(i)
            proj_id = input(
                "Which project do you want to evaluate?"
                "(type project id/ cancel): ")
            while proj_id not in all_proj_id:
                print("Invalid project id, Enter again.")
                proj_id = input("Which project do you want to evaluate?: ")
            if proj_id == 'cancel':
                return
            proj_info = self.pjt.search(proj_id)
            scorers = proj_info['Scorer']
            if self.id not in scorers:
                print(f"Evaluation for project id: {proj_id}")
                result = int(input("Enter score for this project(0-10): "))
                print(f"You have scored project id: {proj_id}")
                print()
                score = int(proj_info['Score']) + result
                self.pjt.update(proj_id, "Score", score)
                if scorers == "":
                    scorers = self.id
                elif scorers != "":
                    scorers += f"-{self.id}"
                self.pjt.update(proj_id, "Scorer", scorers)
                if score >= 30 and len(scorers) == 47:
                    self.pjt.update(proj_id, "Status", "Approved")
            elif self.id in proj_info['Scorer']:
                print("You have already evaluate this project.")
                print()
    
    
   ```