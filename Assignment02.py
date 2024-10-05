## Assignment02.py
## Author: [Mehran Khodabakhshi]
## Submission Date: [09-27-2024]
##
## Purpose:
## Creating several pandas data frames and work on df
## to have a new column defined or using dta frame slicing methods as well
## as groupby summarizing methods to get specific type of results from df.
##
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

stateEntered=input("Please input State name :\n")
def getCustomers(state):
    result= Customers[Customers["StateName"]== state]
    print(result)
    print(f"Type of returned is {type(result)}\n\n")
    return result


def totalPriceCustomers():
    ItemsOrdered["total_price"]=ItemsOrdered["Quantity"]*ItemsOrdered["Price"]
    print("\n\n  Modified Data Frame:\n\n ", ItemsOrdered, "\n\n")
    return ItemsOrdered


my_number=int(input("Desired Number of Highest Spending Customers:\n"))
def getHighestSpendingCustomers(n):
    High_Customer=ItemsOrdered.groupby("CustomerID")["total_price"].sum()
    top_n=High_Customer.nlargest(n)
    top_customers_df = top_n.reset_index()
    top_customers_df.columns=["CustomerID","Sum_highestSpend" ]
    print("\n\n" , top_customers_df, "\n\n")
    print(f" Type of returned is {type(top_customers_df)}\n\n")


Cust_id=int(input("please insert id of customer:\n "))
def getCustomerInfo(CustomerID):
    customer_info=Customers[["SalesTerritoryID","FirstName","LastName","City","StateName"]][Customers["CustomerID"]==CustomerID]
    s_t=customer_info["SalesTerritoryID"].iloc[0]
    f=customer_info["FirstName"].iloc[0]
    l=customer_info["LastName"].iloc[0]
    ci=customer_info["City"].iloc[0]
    st=customer_info["StateName"].iloc[0]
    dic={"City":customer_info["City"].iloc[0], "State":customer_info["StateName"].iloc[0]}
    my_dict={"SalesTerritoryID": s_t, "FirstName": f , "LastName" : l, "Location": dic }
    print("\n\n","Here is customer info:\t" , my_dict)



getCustomers(stateEntered)
totalPriceCustomers()
getHighestSpendingCustomers(my_number)
getCustomerInfo(Cust_id)
