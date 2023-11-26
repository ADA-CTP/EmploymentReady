import pandas as pd
from joblib import load

class Model_Input:
    def __init__(self, gender=0, age=0, accessibility=0, employment=0, mental_health=0,
                main_branch=0, years_code=0, years_code_pro=0, previous_salary=0,
                education='', tools=''):
        self.gender = gender
        self.age = age
        self.accessibility = accessibility
        self.employment = employment
        self.mental_health = mental_health
        self.main_branch = main_branch
        self.years_code = years_code
        self.years_code_pro = years_code_pro
        self.previous_salary = previous_salary
        self.education = education
        self.tools = tools

    def run(self):
        identity_input = {
            'gender': self.gender,
            '<35': 0,
            'accessibility': self.accessibility,
            'employment': self.employment,
            'mentalhealth': self.mental_health,
            'mainbranch': self.main_branch,
            'yearscode': self.years_code,
            'yearscodepro': self.years_code_pro,
            'previoussalary': self.previous_salary
        }

        education_input = {
            'edlevel_master': 0,
            'edlevel_nohighered': 0,
            'edlevel_other': 0,
            'edlevel_phd': 0
        }

        code_language_input = {
            'node.js': 0,
            'typescript': 0,
            'c#': 0,
            'java': 0,
            'bash/shell': 0,
            'javascript': 0,
            'html/css': 0,
            'php': 0,
            'ruby': 0,
            'sql': 0,
            'lisp': 0
        }

        technology_input = {
            'npm': 0,
            'yarn': 0,
            'microsoft sql server': 0,
            'asp.net core ': 0,
            'ruby on rails': 0,
            'mongodb': 0,
            'jquery': 0,
            'sqlite': 0
        }

        # Fill in education
        education_input[self.education] = 1

        # Fill in Age aka <35
        identity_input['<35'] = 1 if self.age < 35 else 0

        # Parse tools
        tools_list = self.tools.split(',')
        for tool in map(str.lower, tools_list):
            if tool in code_language_input:
                code_language_input[tool] = 1
            elif tool in technology_input:
                technology_input[tool] = 1

            # Edge case for HTML/CSS
            if tool == 'html':
                code_language_input['html/css'] = 1
            elif tool == 'css':
                code_language_input['html/css'] = 1

        feature_input = {}
        feature_input.update(identity_input)
        feature_input.update(code_language_input)
        feature_input.update(technology_input)
        feature_input.update(education_input)

        feature_input = pd.DataFrame.from_dict({k: [v] for k, v in feature_input.items()})

        col_order = [
            'node.js', 'typescript', 'microsoft sql server', 'c#', 'jquery', 'mongodb', 'npm',
            'sqlite', 'java', 'bash/shell', 'javascript', 'sql', 'asp.net core ', 'html/css',
            'php', 'yarn', 'ruby', 'previoussalary', 'ruby on rails', 'gender', '<35', 'lisp',
            'accessibility', 'employment', 'mentalhealth', 'mainbranch', 'yearscode', 'yearscodepro',
            'edlevel_master', 'edlevel_nohighered', 'edlevel_other', 'edlevel_phd'
        ]

        feature_input = feature_input[col_order]
        return feature_input
    
class UNEMPLOYMENTMODEL:
    def __init__(self,path,input):
        self.input = input
        self.model = load(path)

    def predict(self):
        class_prediction = self.model.predict(self.input)
        if not class_prediction:
            return "Will not be Employed"
        else:
            return "Good Chance of being Employed"

    def proba(self):
        proba_score = self.model.predict_proba(self.input)[0][1]
        return proba_score

    def feature_importances(self):
        important = self.model.feature_names_in_
        return important

    def recommend_skills(self):
        input_skills = set(self.input.columns[self.input.eq(1).any()])
        important_skills = set(self.feature_importances())
        feature_map = {k:v for k,v in zip(self.model.feature_names_in_,self.model.feature_importances_)}
        recommended_skills = list(important_skills - input_skills)
        recommended_skills.sort(key=lambda x: feature_map[x],reverse=True)
        
        return recommended_skills[:5]
        

m_input = Model_Input(1,1,1,1,1,1,9999999,9999999,9999999,"edlevel_other","c++,C#,node.js,typescript").run()
model = UNEMPLOYMENTMODEL('./model/gradientboost.joblib',m_input)
print(model.recommend_skills())
print(model.predict())
print("Chances of being employed:",model.proba())
# print(model.feature_importances()) 


