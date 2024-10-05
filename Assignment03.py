## Assignment03.py
## Author: [Mehran Khodabakhshi]
## Submission Date: [10-04-2024]

## Purpose:
## Creating several pandas data frames using summarizing methods such as groupby
## and aggregation or filtering data frame to get specific result .

## Statement of Academic Honesty:

## The following code represents my own work. I have neither
## received nor given inappropriate assistance. I have not copied
## or modified code from any source other than the course webpage
## or the course textbook. I recognize that any unauthorized
## assistance or plagiarism will be handled in accordance with
## the Georgia State University's Academic Honesty Policy and the
## policies of this course. I recognize that my work is based
## on an assignment created by the Institute for Insight at the
## Georgia State University. Any publishing
## or posting of source code for this project is strictly
## prohibited unless you have written consent from the Institute
## for Insight at the Georgia State University.

import pandas as pd
import numpy as np 
Employees=pd.read_excel("Employees.xls")
Customers=pd.read_excel("Customers.xls")
ItemsOrdered=pd.read_excel("itemsOrdered.xls")
SalesTerritory=pd.read_excel("SalesTerritory.xls")


# define a fucntion to work on employees data frame
def getEmployeesManagers():

   
# Merge to attain first name and last name of manager , Note:  managger is an employee as well
    result = pd.merge(
    Employees, 
    Employees[["EmployeeID", "FirstName", "MiddleName", "LastName"]], 
    left_on="ManagerID", 
    right_on="EmployeeID", 
    how="left", 
    suffixes=('', '_Manager')
    )

# Get the columns of employee and manger name
    result_df = result[[
    "EmployeeID", 
    "FirstName", 
    "MiddleName", 
    "LastName", 
    "FirstName_Manager", 
    "LastName_Manager"
    ]]
    
# Assign appropiate names for columns as question 
    result_df.columns = ["EmployeeID","FirstName","MiddleName","LastName","ManagerFirstName","ManagerLastName"]
    print(result_df)
    print(f"Returned Data structure type is : {type(result_df)}")
    print(f"Shape of the dataframe is : {result_df.shape}")
    return result_df



# Define a function to get total spent on each item for each customer
def getSpendbyorder():

    ItemsOrdered["TotalSpent"]=ItemsOrdered["Quantity"]*ItemsOrdered["Price"]
    
    # Merge to get customers and total spending in one data frame
    result2=pd.merge(Customers[["CustomerID","FirstName","LastName"]],ItemsOrdered[["CustomerID","Item","TotalSpent"]], on="CustomerID" ,how="left")
    result2_df=result2[["FirstName","LastName","Item","TotalSpent"]]
    nonnull_result2=result2_df.dropna()
    print("\n\n", nonnull_result2, "\n\n")
    print(f"Returned Data structure type is : {type(nonnull_result2)}")
    print(f"Shape of the dataframe is : {nonnull_result2.shape}")
   



# Define a function to get total items for each location ordered for each customer
def getOrderLocation():
    
    # a groupby and a agg sum() to have total items
    df_t=ItemsOrdered.groupby("CustomerID")["Item"].sum()
    df_t.columns=["CustomerID","TotalItem"]
    
    # a merge to have sales territory and customers in one data frame 
    result3=pd.merge(Customers[["CustomerID","SalesTerritoryID"]],df_t, on="CustomerID",how="left")
    result3_df=pd.merge(result3,SalesTerritory[["Name","TerritoryID"]], left_on="SalesTerritoryID", right_on= "TerritoryID",how="left")
    result3_df_final=result3_df[["CustomerID","Name","Item" ]]
    result3_df_final.columns=["CustomerID","Name","TotalItem"]
    print("\n\n", result3_df_final, "\n\n")
    print(f"Returned Data structure type is : {type(result3_df_final)}")
    print(f"Shape of the dataframe is : {result3_df_final.shape}")




# Define a function to get total number of employee for each job title agg by mean of vacation Days
def getEmployeeGroupInfo():
    
    # Groupby and agg so that we define two new columns:  one for count of employees and one for mean of vacation hours
    result4=Employees.groupby("JobTitle").agg(totalEmployeeNumber=("EmployeeID" ,"count") , 
                                  vacHoursMean=("VacationHours","mean")).reset_index()
    # Convert Vacaton hours to day!
    result4["vacDayMean"]=result4["vacHoursMean"]/24
    result4.drop("vacHoursMean",axis=1, inplace=True)
    print("\n\n", result4, "\n\n")
    print(f"Returned Data structure type is : {type(result4)}")
    print(f"Shape of the dataframe is : {result4.shape}")
    



# Define a function to check areas with a positive sales change
def getTerritorySalesInfo():
    SalesTerritory["SalesChange"]=SalesTerritory.apply(lambda x: x["SalesYTD"]-x["SalesLastYear"], axis=1)
    positive_df=SalesTerritory[SalesTerritory["SalesChange"]>0]
    result5=pd.merge(positive_df,Employees[["TerritoryID","EmployeeID", "FirstName", "LastName","EmailAddress"]], on= "TerritoryID",how="left" )
    result5_df=result5.sort_values("SalesChange", ascending=False)
    print("\n\n", result5_df, "\n\n")
    print(f"Returned Data structure type is : {type(result5_df)}")
    print(f"Shape of the dataframe is : {result5_df.shape}")
    


getEmployeesManagers()
getSpendbyorder()
getOrderLocation()
getEmployeeGroupInfo()
getTerritorySalesInfo()
