
##  Credit Scoring System

###  Business Understanding

####  Objective
The goal of this project is to build a Credit Scoring system that classifies customers into **Good**, **Average**, or **Poor** credit categories based on their financial and behavioral data.

#### Requirements & Expectations

- Understand the key business questions and challenges related to credit risk management:
  - Who are high-risk customers likely to default on loans or payments?
  - What factors most influence the credit score?
  - How can the credit scoring model help banks reduce losses and approve credit more accurately?

- Deliverables:
  - A cleaned and preprocessed dataset ready for modeling
  - A predictive model for credit scoring with evaluated performance metrics
  - Visualizations to help interpret customer credit behaviors
  - A user-friendly interface or report for displaying credit score results

- Expected Outcome:
  - A reliable credit scoring solution that supports decision-making in financial institutions
  - Improved accuracy in identifying customers with potential payment delays or defaults

---

####  Data Overview

The dataset contains customer financial and behavioral information:

| Feature                | Description                                               |
|------------------------|-----------------------------------------------------------|
| ID                     | Unique ID of the record                                   |
| Customer_ID            | Unique ID of the customer                                 |
| Month                  | Month of the year                                        |
| Name                   | The name of the person                                   |
| Age                    | The age of the person                                    |
| SSN                    | Social Security Number                                   |
| Occupation             | The occupation of the person                             |
| Annual_Income          | The annual income                                       |
| Monthly_Inhand_Salary  | Monthly in-hand salary                                  |
| Num_Bank_Accounts      | Number of bank accounts                                  |
| Num_Credit_Card        | Number of credit cards                                  |
| Interest_Rate          | Interest rate on credit card                            |
| Num_of_Loan            | Number of loans taken                                   |
| Type_of_Loan           | Types of loans                                         |
| Delay_from_due_date    | Average days delayed from due date                      |
| Num_of_Delayed_Payment | Number of payments delayed                              |
| Changed_Credit_Card    | Percentage change in credit card limit                  |
| Num_Credit_Inquiries   | Number of credit card inquiries                         |
| Credit_Mix             | Classification of credit mix                            |
| Outstanding_Debt       | Outstanding debt                                       |
| Credit_Utilization_Ratio | Credit utilization ratio                              |
| Credit_History_Age     | Age of credit history                                 |
| Payment_of_Min_Amount  | Whether minimum amount was paid (Yes/No)                |
| Total_EMI_per_month    | Total EMI per month                                     |
| Amount_invested_monthly | Monthly amount invested                                 |
| Payment_Behaviour      | Payment behaviour                                      |
| Monthly_Balance        | Monthly balance left                                   |
| Credit_Score           | The credit score (target variable)                      |

---

### Installation
- numpy
- pandas
- matplotlib
- seaborn
- sklearn.
