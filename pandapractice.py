import pandas as pd

df=pd.read_csv("pandas.csv")
# df["Sales_Person"]=["Raj","Rohan","Kabita","Nabaraj","Sakira","Raj","Raj","Raj","Ram","Ram","Ram","Sakira"]


# print(df["Total_Sales"].sum())
# print(df["Total_Sales"].mean())
# print(df["Total_Sales"].max())
# print(df["Total_Sales"].min())
# print(df["Total_Sales"].count())
# print(df["City"].value_counts())
# print(df["Payment_Method"].value_counts())
# print(df.groupby("City")["Total_Sales"].sum())
# print(df.groupby("Category")["Total_Sales"].sum())
# print(df.groupby("Category")["Total_Sales"].mean())
# print(df.groupby("City")["Order_ID"].count())
# print(df.groupby("City")["Total_Sales"].agg(["sum","mean","max","min"]))
# print(df.loc[df["City"]=="Butwal",["Customer","Category","Total_Sales"]])
# df["Date"]=pd.to_datetime(df["Date"])
# df["Month"]=df["Date"].dt.month
# print(df["Month"])
# df["Year"]=df["Date"].dt.year
# print(df["Year"])
# df["Month_Name"] = df["Date"].dt.month_name()
# print(df["Month_Name"])
# 

# class Engine:
#     def start(self):
#         print("Engine Started")

# class Car:
#     def __init__(self):
#         self.engine=Engine()

#     def drive(self):
#         self.engine.start()
#         print("Car drive when engine starts")

# car1=Car()
# car1.drive()


# class Address:
#     def __init__(self,street,city):
#         self.street=street
#         self.city=city

# class Person:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=Address(15,"Bhairahawa")

# address1=Address(14,"Butwal")
# person1=Person("Jack",address1)
# print(person1.address.street)
# print(person1.name)
# print(person1.address)
# print(person1.name,person1.address.street,person1.address.city)

# class CreditCard:
#     def pay(self):
#         print("Paid via creditcard")
# class Esewa:
#     def pay(self):
#         print("Paid via esewa")
# class Cash:
#     def pay(self):
#         print("Paid via cash")

# def make_payment(method):
#     method.pay()

# cc=CreditCard()
# esewa=Esewa()
# cash=Cash()
# cc.pay()
# cash.pay()
# esewa.pay()

# make_payment(cc)
# make_payment(cash)

class PetrolEngine:
    def start(self):
        print("Petrol engine started")

class ElectricEngine:
    def start(self):
        print("Electric engine started")

class Car:
    def __init__(self,engine):
        self.engine=engine
    def start(self):
        print(f"{self.engine}car started")
        

pp=PetrolEngine()
car1=Car("Petrol")
ee=ElectricEngine()
car2=Car("Electric")
car1.start()
car2.start()













      







