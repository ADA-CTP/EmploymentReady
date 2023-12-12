# EmploymentReady
EmploymentReady contains a predictive model that predicts your employability for a software developer role based on your current skill set and provides recommendations of skills you can learn to increase your employability rating.

![ER_model_prediction](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/08fd635f-5a91-4d4a-ae07-dc1e91f5339c)
![ER_update](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/1733c71b-81ec-4f92-97a1-2c0e85523b6f)

<details><summary>Table Of Contents</summary>

  *  [Project Description](https://github.com/ADA-Sleep-Analysis/EmploymentReady/blob/main/README.md#project-description)
  *  [Design Strategy](https://github.com/ADA-Sleep-Analysis/EmploymentReady/blob/main/README.md#design-strategy)
  *  [Demo](https://github.com/ADA-Sleep-Analysis/EmploymentReady/blob/main/README.md#demo)
  *  [Future Aspirations](https://github.com/ADA-Sleep-Analysis/EmploymentReady/edit/main/README.md#future-aspirations)
  *  [Contact](https://github.com/ADA-Sleep-Analysis/EmploymentReady/edit/main/README.md#contact)

</details>


## Project Description
### Problem Statement
Have you ever been rejected for a role? The tech job market is extremely competitive. With the copious amounts of technologies that are available in conjunction with other variables such as education and even location, it might be difficult to understand the employability of a candidate from the employer’s perspective or even understand what skills employers want to see in a candidate from an applicant's perspective. 

### Our Solution
EmploymentReady can predict the possibility of employment given some information. We intend to help job applicants, like yourself, understand your employability and increase it with recommendations for skills. (Currently only for software developer roles) <br>

**Predictive Modeling**: We utilized a 70k+ dataset of software developer job applicants to train and develop a predictive model that assesses the employability of new applicants for software developer roles based on their current skill set. Applicants can understand their employability for the role. Organizations can prioritize candidates more efficiently. <br>

**Feature Analysis**: By analyzing the dataset, our model shows the top skills that are most important for the software developer role. Applicants can prepare more efficiently for the qualifications of the role. Recruiters can gain insights into the key attributes and qualifications that contribute most significantly to a candidate's employability. This information can guide the development of effective job descriptions and candidate evaluation criteria.


## Design Strategy
*  Jupyter Notebook, Google Colab, Deepnote (Data Cleaning, Exploratory Data Analysis)
*  Gradient Boosting Classifier Model (training and testing our predictive model)
*  Streamlit (build an application to accept user input and output prediction of user employability using our model)
*  Visual Studio Code & Python (code for Streamlit application and our model)
*  Git & Github (to share code and collaborate)
*  Python Libraries: streamlit, pandas, numpy, seaborn, plotly.express, matplotlib.pyploy, joblib, sklearn.metrics, sklearn.ensemble, sklearn.model_selction
*  [70k+ Job Applicants Dataset from Kaggle](https://www.kaggle.com/datasets/ayushtankha/70k-job-applicants-data-human-resource/data)

## Demo
### Navigate Between Different Pages
![ER_Nagivate](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/980a7848-e4d3-4a5b-b4b5-9157b418bcdb) <br>

### User Input Section
![ER_user_input](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/e6f4bc83-fe4f-44a1-8e09-90bc64cdd75a) <br>

### Model Prediction
![ER_model_prediction](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/08fd635f-5a91-4d4a-ae07-dc1e91f5339c) <br>

### Update Function
![ER_update](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/696bffec-91cf-48ec-9819-1b112bd75ff1) <br>

### Raw Dataset
![ER_raw_dataset](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/6a2d2df1-540e-4d2a-85ca-c1294585b464) <br>

### Clean Dataset
![ER_clean_dataset](https://github.com/ADA-Sleep-Analysis/EmploymentReady/assets/93285387/3ea595d0-783c-4b68-8204-12bf8179555f) <br>

## Future Aspirations
*  Utilize natural language processing to read a resume document(pdf) and calculate the likelihood of a user to get a job
*  Add predictive modeling and calculate employability for other tech roles (currently it is only for software engineers)
*  Candidates may contribute to the dataset by adding data points in which we can further improve our predictions 


## Contact
Our development team consists of:
*  Anthony Zhu
*  Daphne Tang
*  Andy Zheng

My name is Anthony, I study Computer Science at the City College of New York and I’m expected to graduate in Spring of 2024. <br>
Email: Anthonyzhu137@gmail.com | [LinkedIn](https://www.linkedin.com/in/anthony-zhu-cs/) | [Github](https://github.com/azhu000)

My name is Daphne Tang. I am a Senior at City College of New York studying Computer Science. <br>
Email: Daphnetang2002@gmail.com | [LinkedIn](https://www.linkedin.com/in/daphnetang-cs/) | [Github](https://github.com/DTang127)
 
My name is Andy Zheng. I’m a senior studying computer science at the City College of New York. <br>
Email: Andyzheny@gmail.com | [LinkedIn](https://www.linkedin.com/in/andyzheng7/) | [Github](https://github.com/Falselysium)

