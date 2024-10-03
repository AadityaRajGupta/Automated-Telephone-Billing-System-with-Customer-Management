import os
from tabulate import tabulate
import mysql.connector as c
d=c.connect(user='root', password='#######',host='localhost',auth_plugin='mysql_native_password',database='BILL')
cur=d.cursor()

os.system('cls')

def create_database():
    sql="create database BILL"
    cur.execute(sql)
    d.commit()

def create_table():
    sql="create table CUSTOMER (ConsumerName varchar(20) primary key,TelephoneNo varcher(12) unique key,AadharNo varchar(12) unique key,City varchar(20) default '{}',CallingTime int(5) default 0,Amount float(5,2) default 0.0,Status char(6) default '{}')".format('Delhi','Unpaid')
    cur.execute(sql)
    d.commit()

def adddata():
    print("\n\t\t\t New Customer Registration")
    print("\t\t\t---------------------------\n")
    ph=input("Enter Your Telephone No.: ")
    name=input("Enter Name: ")
    adh=int(input("Enter Aadhar No.: "))
    city=input("Enter City: ")
    sql="insert into Customer(ConsumerName,TelephoneNo,AadharNo,City) values('{}','{}','{}','{}')"
    cur.execute(sql.format(name,ph,adh,city))
    d.commit()
    print("\n Successfully Registered The User")

def displayall():
    sql="select * from Customer"
    cur.execute(sql)
    rec=cur.fetchall()
    headers=["ConsumerName","TelephoneNo","AadharNo","City","CallingTime","Amount","Status"]
    print(tabulate(rec, headers, tablefmt="grid"))
    ''' print("ConsumerName","TelephoneNo","AadharNo","City","    CallingTime","Amount","       Status",sep="\t\t")
    for i in rec:
        print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],sep="   \t\t") '''

def delrecord():
    ph=int(input("Enter The Telephone No.: "))
    sql="select * from Customer where TelephoneNo = '{}'"
    cur.execute(sql.format(ph))
    rec=cur.fetchall()
    if rec==[]:
        print("Customer Doesn't Exist")
    else:
        ch=input("Are You Sure To Remove The Customer Y/N: ")
        if ch in ['Y','y']:
            sql = "delete from Customer where TelephoneNo = '{}'"
            cur.execute(sql.format(ph))
            d.commit()
            print("Successfully Removed The Customer From Database")
        else:
            print("No Change Made In Your Database")

def modifyrec():
    print("\n\t\t\t Update Customer Data")
    print("\t\t\t----------------------\n")
    ph=int(input("Enter The Telephone No.: "))
    sql="select * from Customer where TelephoneNo = '{}'".format(ph)
    cur.execute(sql)
    rec=cur.fetchall()
    if rec==[]:
        print("Customer Doesn't Exist")
    else:
        print("1. CustomerName\n2. City")
        ch=int(input("Enter Choice To Update: "))
        if ch==1:
            name=input("Enter New Name: ")
            sql="update Customer set ConsumerName = '{}' where TelephoneNo = '{}'"
            cur.execute(sql.format(name,ph))
            d.commit()
            print("\n Successfully Updated Name")
        elif ch==2:
            city=input("Enter New City: ")
            sql="update Customer set City = '{}' where TelephoneNo = '{}'"
            cur.execute(sql.format(city,ph))
            d.commit()
            print("\n Successfully Updated City")
        else:
            print("Please Choose Correct Choice")

def search():
    print("\n\t\t\t Search Customer")
    print("\t\t\t-----------------")
    print("\n1. Search By Name")
    print("2. Search By Telephone No.")
    print("3. Search By Aadhar No.")
    print("4. Search By City")
    ch=int(input("Enter Your Choice To Search: "))
    if ch==1:
        name=input("Enter Name: ")
        sql="select * from Customer where ConsumerName = '{}'"
        cur.execute(sql.format(name))
        rec=cur.fetchall()
        if rec==[]:
            print("Customer Doesn't Exist")
        else:
            headers=["ConsumerName","TelephoneNo","AadharNo","City","CallingTime","Amount","Status"]
            print(tabulate(rec, headers, tablefmt="grid"))
    elif ch==2:
        ph=input("Enter The Telephone No.: ")
        sql="select * from Customer where TelephoneNo = '{}'"
        cur.execute(sql.format(ph))
        rec=cur.fetchall()
        if rec==[]:
            print("Customer Doesn't Exist")
        else:
            headers=["ConsumerName","TelephoneNo","AadharNo","City","CallingTime","Amount","Status"]
            print(tabulate(rec, headers, tablefmt="grid"))
    elif ch==3:
        adh=input("Enter Aadhar No.: ")
        sql="select * from Customer where AadharNo = '{}'"
        cur.execute(sql.format(adh))
        rec=cur.fetchall()
        if rec==[]:
            print("Customer Doesn't Exist")
        else:
            headers=["ConsumerName","TelephoneNo","AadharNo","City","CallingTime","Amount","Status"]
            print(tabulate(rec, headers, tablefmt="grid"))
            
    elif ch==4:
        city=input("Enter The City: ")
        sql="select * from Customer where City = '{}'"
        cur.execute(sql.format(city))
        rec=cur.fetchall()
        if rec==[]:
            print("Customer Doesn't Exist")
        else:
            headers=["ConsumerName","TelephoneNo","AadharNo","City","CallingTime","Amount","Status"]
            print(tabulate(rec, headers, tablefmt="grid"))

def billing():
    print("\t\t\t  Billing")
    print("\t\t\t-----------\n")
    ph=int(input("Enter Your Telephone No.: "))
    sql="select * from Customer where TelephoneNo = '{}'".format(ph)
    cur.execute(sql)
    rec=cur.fetchall()
    if rec==[]:
        print("Customer Doesn't Exist")
    else:
        headers=["ConsumerName","TelephoneNo","AadharNo","City","CallingTime","Amount","Status"]
        print(tabulate(rec, headers, tablefmt="grid"))
        call=int(input("Enter Total Calling Time Of This Month(in mins): "))
        bill= 200
        if call > 1200:
            bill=bill+(call-1200)*0.4 + 800*0.8 + 800*1.5
        elif 800 < call <= 1200:
            bill=bill + (call-800)*0.9 + 800*1.5
        elif call <= 800:
            bill=bill + call*1.5
    print("\n\t\t\t  Billing")
    print("\t\t\t-----------\n")
    if rec[0][6]!="Paid":
        old_bill=rec[0][5]
    else:
        old_bill=0
    print("\n\t\t Pending Bill Amount: ",old_bill)
    print("\n\t\t New Bill Amount: ",bill)
    print("\t\t---------------------------")
    print("\t\t Total Bill Amount: ",bill + old_bill)
    print("\t\t-----------------------------")
    ch=input("\n Press Y to Pay Bill Now or Any Other Key to Pay Later: ")
    if ch in ['y','Y']:
        sql="update Customer set Amount = {}, Status = 'Paid', CallingTime = {} where TelephoneNo = '{}'"
        cur.execute(sql.format(bill + old_bill,call,ph))
        d.commit()
        print("\n Successsfully Paid The Bill")
    else:
        sql="update Customer set Amount = {}, Status = 'Unpaid', CallingTime = {} where TelephoneNo = '{}'"
        cur.execute(sql.format(bill + old_bill,call,ph))
        d.commit()
        print("Please Make Payment As Soon As Possible")


def menu():
    print("\n\t\t\t\t MAIN MENU")
    print("\n\t\t\t Press 1: To Generate a Bill")
    print("\n\t\t\t Press 2: To List all Customers")
    print("\n\t\t\t Press 3: To Manage Customers")
    print("\n\t\t\t Press 4: To Exit")
    
def menucust():
    print("\n\t\t\t\t CUSTOMER MENU")
    print("\n\t\t\t Press 1: To List all Customers")
    print("\n\t\t\t Press 2: To Add a Customer")
    print("\n\t\t\t Press 3: To Show All Details of a Customer")
    print("\n\t\t\t Press 4: To Delete a Customer Record")
    print("\n\t\t\t Press 5: To Modify a Existing Customer Record")
    print("\n\t\t\t Press 6: To Go Back to Previous Menu")
ch=0
c = 'Y'
while ch!=4:
    while c in ['Y','y']:
        menu()
        ch=int(input("\n Enter Your Choice: "))
        if ch==1:
            billing()
            c=input("\n Do You Want to Continue (Y/N): ")
            if c=="n" or c=="N":
                print("\nThanks")
                break
        elif ch==2:
            displayall()
            c=input("\n Do You Want to Continue (Y/N) : ")
            if c=="n" or c=="N":
                print("\n Thanks")
                break
        elif ch==3:
            a='Y'
            while a in ['Y','y']:
                menucust()
                opt=0
                opt=int(input("\n Enter Your Choice on Customer Menu: "))
                if opt==1:
                    displayall()
                    a=input("\n Press 'Y' to Continue on Customer Menu: ")
                elif opt==2:
                    adddata()
                    a=input("\n Press 'Y' to Continue on Customer Menu: ")
                elif opt==3:
                    search()
                    a=input("\n Press 'Y' to Continue on Customer Menu: ")
                elif opt==4:
                    delrecord()
                    a=input("\n Press 'Y' to Continue on Customer Menu: ")
                elif opt==5:
                    modifyrec()
                    a=input("\n Press 'Y' to Continue on Customer Menu: ")
                elif opt==6:
                    break
                else:
                    print("\n Invalid Choice")
                    a=input("\n Press 'Y' to Continue")
        elif ch==4:
            print("\n Thanks")
            break
        else:
            print("\n Invalid Choice")
            input("\n Press Any Key to Continue")
    break
d.close()


