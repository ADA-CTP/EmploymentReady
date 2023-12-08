# EmploymentReady
EmploymentReady contains a predictive model that predicts your employability for a software developer role based on your current skill set and provides recommendations of skills you can learn to increase your employability rating.

![ER1](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/5d7d4392-91f1-4860-823d-428f9fbe38e2)
![ER2](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/9e3afbed-7a44-4646-802e-6300ac92a877)

<details><summary>Table Of Contents</summary>

  *  [Project Description](https://github.com/ADA-Sleep-Analysis/EmploymentReady/blob/main/README.md#project-description)
  *  [Design Strategy]
  *  [Demo]
  *  [Future Aspirations]
  *  [Contact]

</details>


### Project Description
___
##### Problem Statement
Have you ever been rejected for a role? The tech job market is extremely competitive. With the copious amounts of technologies that are available in conjunction with other variables such as education and even location it might be difficult to understand the hireability of a candidate from the employer’s perspective or even understand what skills employers want to see in a candidate from an applicant's perspective. 

##### Our Solution
EmploymentReady can predict the possibility of employment given some information. We intend to help job applicants, like yourself, understand your employability and increase it with recommendations for skills. (Currently only for software developer roles) <br>

**Predictive Modeling**: We utilized a 70k+ dataset of software developer job applicants to train and develop a predictive model that assess the employability of new applicants for software developer role based on their profile attributes and current skill set. Applicants can understand their employability for the role. Organizations can prioritize candidates more efficiently. <br>

**Feature Analysis**: By analyzing the dataset, our model shows the top skills that are most important for the software developer role. Applicants can prepare more efficiently for the qualifications of the role. Recruiters can gain insights into the key attributes and qualifications that contribute most significantly to a candidate's employability. This information can guide the development of effective job descriptions and candidate evaluation criteria.


### Design Strategy
___
*  Jupyter Notebook, Google Colab, Deepnote (Data Cleaning, Exploratory Data Analysis)
*  Gradient Boosting Classifier Model (training and testing our predictive model)
*  Streamlit (build application to accept user input and output prediction of user employability using our model)
*  Visual Studio Code & Python (code for Streamlit application and our model)
*  Git & Github (to share code and collaborate)
*  Python Libraries: streamlit, pandas, numpy, seaborn, plotly.express, matplotlib.pyploy, joblib, sklearn.metrics, sklearn.ensemble, sklearn.model_selction

### Demo
___
**Navigate Between Different Pages** <br>
![ER3](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/356aaede-e582-41a2-ad90-ad670a0f5bd1) <br>

**User Input Section** <br>
![ER4](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/11038a27-09db-4ab3-b7e9-30b8cb303f4b)
![ER7](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/7ad4921b-bee9-4f0e-9c8e-3d914ecf235c)
![ER5](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/dbc57a05-fd93-4241-81e0-458fa2215a61)
![ER6](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/60bd6e79-ce37-4379-a67f-97c21086a5bb) <br>

**Model Prediction** <br>
![ER1](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/5d7d4392-91f1-4860-823d-428f9fbe38e2)
![ER2](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/9e3afbed-7a44-4646-802e-6300ac92a877) <br>

**Raw Dataset** <br>
![ER8](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/636be20c-89b5-4faf-8659-eab2831b0f96) <br>

**Clean Dataset** <br>
![ER9](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/8d2bb197-3464-4dd1-918e-81f52939f0cc) <br>

### Future Aspirations
___
*  Utilize NLP to read a resume document(pdf) and calculate the likelihood of a user to get a job
*  Add predictive modeling and calculate employability for other tech roles (currently it is only for software engineers)
*  Candidates may contribute to the dataset by adding data points in which we can further improve our predictions 


### Contact
___
Our development team consists of:
*  Anthony Zhu
*  Daphne Tang
*  Andy Zheng

##### Introductions
My name is Anthony, I study Computer Science at the City College of New York and I’m expected to graduate in Spring of 2024. <br>
Email: Anthonyzhu137@gmail.com | [LinkedIn](https://www.linkedin.com/in/anthony-zhu-cs/) | [Github](https://github.com/azhu000)

My name is Daphne Tang. I am a Senior at City College of New York studying Computer Science. <br>
Email: Daphnetang2002@gmail.com | [LinkedIn](https://www.linkedin.com/in/daphnetang-cs/) | [Github](https://github.com/DTang127)
 
My name is Andy Zheng. I’m a senior studying computer science at the City College of New York. <br>
Email: Andyzheny@gmail.com | [LinkedIn](https://www.linkedin.com/in/andyzheng7/) | [Github](https://github.com/Falselysium)

