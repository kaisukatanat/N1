{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8774a281",
   "metadata": {},
   "outputs": [],
   "source": [
    "##  Credit Scoring System\n",
    "\n",
    "###  Business Understanding\n",
    "\n",
    "####  Objective\n",
    "The goal of this project is to build a Credit Scoring system that classifies customers into **Good**, **Average**, or **Poor** credit categories based on their financial and behavioral data.\n",
    "\n",
    "#### Requirements & Expectations\n",
    "\n",
    "- Understand the key business questions and challenges related to credit risk management:\n",
    "  - Who are high-risk customers likely to default on loans or payments?\n",
    "  - What factors most influence the credit score?\n",
    "  - How can the credit scoring model help banks reduce losses and approve credit more accurately?\n",
    "\n",
    "- Deliverables:\n",
    "  - A cleaned and preprocessed dataset ready for modeling\n",
    "  - A predictive model for credit scoring with evaluated performance metrics\n",
    "  - Visualizations to help interpret customer credit behaviors\n",
    "  - A user-friendly interface or report for displaying credit score results\n",
    "\n",
    "- Expected Outcome:\n",
    "  - A reliable credit scoring solution that supports decision-making in financial institutions\n",
    "  - Improved accuracy in identifying customers with potential payment delays or defaults\n",
    "\n",
    "---\n",
    "\n",
    "####  Data Overview\n",
    "\n",
    "The dataset contains customer financial and behavioral information:\n",
    "\n",
    "| Feature                | Description                                               |\n",
    "|------------------------|-----------------------------------------------------------|\n",
    "| ID                     | Unique ID of the record                                   |\n",
    "| Customer_ID            | Unique ID of the customer                                 |\n",
    "| Month                  | Month of the year                                        |\n",
    "| Name                   | The name of the person                                   |\n",
    "| Age                    | The age of the person                                    |\n",
    "| SSN                    | Social Security Number                                   |\n",
    "| Occupation             | The occupation of the person                             |\n",
    "| Annual_Income          | The annual income                                       |\n",
    "| Monthly_Inhand_Salary  | Monthly in-hand salary                                  |\n",
    "| Num_Bank_Accounts      | Number of bank accounts                                  |\n",
    "| Num_Credit_Card        | Number of credit cards                                  |\n",
    "| Interest_Rate          | Interest rate on credit card                            |\n",
    "| Num_of_Loan            | Number of loans taken                                   |\n",
    "| Type_of_Loan           | Types of loans                                         |\n",
    "| Delay_from_due_date    | Average days delayed from due date                      |\n",
    "| Num_of_Delayed_Payment | Number of payments delayed                              |\n",
    "| Changed_Credit_Card    | Percentage change in credit card limit                  |\n",
    "| Num_Credit_Inquiries   | Number of credit card inquiries                         |\n",
    "| Credit_Mix             | Classification of credit mix                            |\n",
    "| Outstanding_Debt       | Outstanding debt                                       |\n",
    "| Credit_Utilization_Ratio | Credit utilization ratio                              |\n",
    "| Credit_History_Age     | Age of credit history                                 |\n",
    "| Payment_of_Min_Amount  | Whether minimum amount was paid (Yes/No)                |\n",
    "| Total_EMI_per_month    | Total EMI per month                                     |\n",
    "| Amount_invested_monthly | Monthly amount invested                                 |\n",
    "| Payment_Behaviour      | Payment behaviour                                      |\n",
    "| Monthly_Balance        | Monthly balance left                                   |\n",
    "| Credit_Score           | The credit score (target variable)                      |\n",
    "\n",
    "---\n",
    "\n",
    "### Installation\n",
    "- numpy\n",
    "- pandas\n",
    "- matplotlib\n",
    "- seaborn\n",
    "- sklearn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ca27b1e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
