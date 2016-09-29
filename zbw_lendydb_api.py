import sqlite3
from sys import exit
db=None
cursor=None
#操作member表增删改查
def insert_member(Name,Email):
    query='''insert into member(Name,Email)VALUES (?,?)'''
    oldata1=select_member_details_by_name(Name)
    #print(Name,Email)
    oldata2=select_member_details_by_email(Email)
    #print(oldata1,oldata2)
    if not oldata1 and not oldata2:
        cursor.execute(query,(Name,Email))
    else:
        if not oldata2:
            print("There is a record has same name:",oldata1)
        else:
            print("There is a record has same email:",oldata2)
def update_member(id,name=None,email=None):
    query='''update member set name=?,email=? where id=?'''
    oldata=select_member_details_by_id(id)[0]
    print(oldata)
    if not name:name=oldata[1]
    if not email:email=oldata[2]
    cursor.execute(query,(id,name,email))
    newData=select_member_details_by_id(id)
    print("update successful!",newData)
def select_max_member_id():
    query='''select max(ID) from member'''
    return cursor.execute(query).fetchall()[0][0]
def select_member_email(id):
    return select_member_details_by_id(id)[2]
def select_member_name(id):
    return select_member_details_by_id(id)[1]
def select_member_details_by_id(id):
    query1='''select ID,Name,Email from member where id=? '''
    try:
        return cursor.execute(query1,(id,)).fetchall()[0]
    except:
        return None
def select_member_details_by_name(name):
    query1='''select ID,Name,Email from member where name=? '''
    try:
        return cursor.execute(query1,(name,)).fetchall()[0]
    except:
        return None
def select_member_details_by_email(email):
    query1='''select ID,Name,Email from member where email=? '''
    try:
        return cursor.execute(query1,(email,)).fetchall()[0]
    except:
        return None
def select_member_id_by_name(name):
    query='''select id from member where name=?'''
    try:
        return cursor.execute(query,(name,)).fetchall()[0][0]
    except:
        return None
def select_member_id_by_email(email):
    query='''select id from member where email=?'''
    try:
        return cursor.execute(query,(email,))[0][0]
    except:
        return None
def select_members():
    query='''select ID,Name,Email from member'''
    return cursor.execute(query).fetchall()
def delete_member(id):
    query='''delete from member where id=?'''

    oldata=select_member_details_by_id(id)
    if not oldata:
        print("No record!")
    else:
        cursor.execute(query,(id,))
        print("Successful Delete!")
#操作item表增删改查
def insert_item(Name,Description,OwnerID,Price,Condition,DateRegistered):
    query='''insert into item(Name,Description,OwnerID,Price,Condition,DateRegistered)VALUES (?,?,?,?,?,DATE(?))'''
    cursor.execute(query,(Name,Description,OwnerID,Price,Condition,DateRegistered))
    print("successful insert!")
    print(select_items())
def update_item(id,Name=None,Description=None,OwnerID=None,Price=None,Condition=None,DateRegistered=None):
    query='''update item set Name=?,Description=?,OwnerID=?,Price=?,Condition=?,DateRegistered=? '''
    oldata=select_item_details(id)
    if not Name:Name=oldata[1]
    if not Description:Description=oldata[2]
    if not OwnerID:OwnerID=oldata[3]
    if not Price:Price=oldata[4]
    if not Condition:Condition=oldata[5]
    if not DateRegistered:DateRegistered=oldata[6]
    cursor.execute(query,(Name,Description,OwnerID,Price,Condition,DateRegistered))
    print("Successful update")
    print(select_items())
def delete_item(id):
    query='''delete from item where id=?'''
    cursor.execute(query,(id,))
    print("successful delete!")
    print(select_items())
def select_item_id_by_name(Name):
    query='''select id from item where name=?'''
    try:
        return cursor.execute(query,(Name,)).fetchall()[0][0]
    except:
        raise "No record!"
def select_item_id_by_ownerID(OwnerID):
    query='''select id from item where OwnerID=?'''
    try:
        return cursor.execute(query,(OwnerID,)).fetchall()[0][0]
    except:
        raise "No record!"
def select_items():
    query='''select * from item'''
    return cursor.execute(query).fetchall()
def select_item_details(id):
    query='''select * from item where id=?'''
    return cursor.execute(query,(id,)).fetchall()[0]
#操作loan表增删改查
def insert_loan(itemID,BorrowerID,DateBorrowed,DateReturned):
    query='''insert into loan(itemID,BorrowerID,DateBorrowed,DateReturned)VALUES (?,?,DATE(?),DATE(?))'''
    cursor.execute(query,(itemID,BorrowerID,DateBorrowed,DateReturned))
    print("successful insert!")
    print(select_loans())
def update_loan(id,itemID=None,BorrowerID=None,DateBorrowed=None,DateReturned=None):
    query='''update loan set itemID=?,BorrowerID=?,DateBorrowed=?,DateReturned=? where id=?'''
    oldata=select_loan_details(id)
    if not itemID:itemID=oldata[1]
    if not BorrowerID:BorrowerID=oldata[2]
    if not DateReturned:DateBorrowed=oldata[3]
    if not DateReturned:DateReturned=oldata[4]
    cursor.execute(query,(itemID,BorrowerID,DateBorrowed,DateReturned))
    print("Successful update")
    print(select_loans())

def delete_loan(id):
    query='''delete from loan where id=?'''
    cursor.execute(query,(id,))
    print("successful delete!")
    print(select_loans())
def select_loan_id_by_itemID(itemID):
    query='''select id from loan where itemID=?'''
    try:
        return cursor.execute(query,(itemID,)).fetchall()[0][0]
    except:
        raise "No record!"
def select_loan_id_by_BorrowerID(BorrowerID):
    query='''select id from loan where BorrowerID=?'''
    try:
        return cursor.execute(query,(BorrowerID,)).fetchall()[0][0]
    except:
        raise "No record!"
def select_loans():
    query='''select * from loan'''
    return cursor.execute(query).fetchall()
def select_loan_details(id):
    query='''select * from item where id=?'''
    return cursor.execute(query,(id,)).fetchall()[0]
#初始化数据库连接
def initDB(filePath=None):
    global db,cursor
    if not filePath:
        filePath="D:\\sql\\zbw.db"
    try:
        db=sqlite3.connect(filePath)
        cursor=db.cursor()
    except:
        raise("Error to connect..",filePath)
#提交并关闭数据库连接
def closeDB():
    try:
        cursor.close()
        db.commit()
        db.close()
    except:
        raise("Error to stop the connection...")

