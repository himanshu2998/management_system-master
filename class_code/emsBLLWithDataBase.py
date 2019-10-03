#BLL(Business Logic Layer)

import pymysql

myCon=pymysql.connect(host="localhost",user="pathak",password="arpitdadlove",database="ems")
myCursor=myCon.cursor()

class Employee:

    @staticmethod
    def checkId(id): # this function helps in checking the class type of the id and returns object of that class
        query="select * from employee_info where id = %s"
        rowAffected=myCursor.execute(query,(id))
        if(rowAffected!=0):
                row=myCursor.fetchone()
                if (row[2] == "d"):
                    return Director()
                elif (row[2] == "m"):
                    return Manager()
                else:
                    return TT()
        else:
                return -1;

    def __init__(self):
        self.id=0
        self.name=None
        self.type=None

    def add(self):
        query = "insert into employee_info values(%s,%s,%s)"
        rowAffected = myCursor.execute(query, (self.id, self.name, self.type))
        if(rowAffected!=0):
            myCon.commit()
        else:
            raise Exception

    def search(self, id): # search a record in list
        query="select * from employee_info where id = %s"
        rowAffected=myCursor.execute(query,(id))
        if(rowAffected!=0):
            row=myCursor.fetchone()
            self.name=row[1]
            self.type=row[2]
        else:
            raise Exception


    def update(self,id): # update a record in list
        query="update employee_info set name = %s where id = %s"
        rowAffected=myCursor.execute(query,(self.name,id))
        if(rowAffected!=0):
            myCon.commit()
        else:
            myCon.rollback()
            raise Exception

    def delete(self,id): # delete a record in list
        query="delete from employee_info where id = %s"
        rowAffected=myCursor.execute(query,(id))
        if(rowAffected==0):
            raise Exception
        else:
            myCon.commit()

    def sort(self): # to sort database according to id
        query = "(select * from employee_info natural join director) union (select * from employee_info natural join manager) union (select * from employee_info natural join tt) order by id"
        myCursor.execute(query)
        return myCursor.fetchall()

class Director(Employee):

    def __init__(self):
        self.special=None
        self.sal=0
        super().__init__()

    def add(self):
        query="insert into director values(%s,%s,%s)"
        rowAffected=myCursor.execute(query,(self.id,self.special,self.sal))
        if(rowAffected!=0):
             super().add()
        else:
            raise Exception

    def search(self,id):
        super().search(id)
        query="select * from director where id = %s"
        rowAffected=myCursor.execute(query,(id))
        if(rowAffected!=0):
            row=myCursor.fetchone()
            self.special=row[1]
            self.sal=row[2]
            myCon.commit()
        else:
            myCon.rollback()
            raise Exception

    def update(self,id):
        query="update director set salary = %s, special = %s where id = %s"
        rowAffected=myCursor.execute(query,(self.sal,self.special,id))
        if(rowAffected!=0):
            myCon.commit()
            super().update(id)
        else:
            myCon.rollback()
            raise Exception

    def delete(self,id):
        query="delete from director where id = %s"
        rowAffected=myCursor.execute(query,(id))
        if(rowAffected==0):
            myCon.rollback()
            raise Exception
        else:
            myCon.commit()
            super().delete(id)

class Manager(Employee):

    def __init__(self):
        self.special=None
        self.sal=0
        super().__init__()

    def add(self):
        query = "insert into manager values(%s,%s,%s)"
        rowAffected = myCursor.execute(query, (self.id, self.special, self.sal))
        if (rowAffected != 0):
            super().add()
        else:
            raise Exception

    def search(self,id):
        super().search(id)
        query = "select * from manager where id = %s"
        rowAffected = myCursor.execute(query, (id))
        if (rowAffected != 0):
            row = myCursor.fetchone()
            self.special = row[1]
            self.sal = row[2]
            myCon.commit()
        else:
            myCon.rollback()
            raise Exception

    def update(self,id):
        query = "update manager set salary = %s,special = %s where id = %s"
        rowAffected = myCursor.execute(query, (self.sal,self.special, id))
        if (rowAffected != 0):
            myCon.commit()
            super().update(id)
        else:
            myCon.rollback()
            raise Exception

    def delete(self,id):
        query = "delete from manager where id = %s"
        rowAffected = myCursor.execute(query, (id))
        if (rowAffected == 0):
            myCon.rollback()
            raise Exception
        else:
            myCon.commit()
            super().delete(id)

class TT(Employee):

    def __init__(self):
        self.special=None
        self.sal=0
        super().__init__()

    def add(self):
        query = "insert into tt values(%s,%s,%s)"
        rowAffected = myCursor.execute(query, (self.id, self.special, self.sal))
        if (rowAffected != 0):
            super().add()
        else:
            raise Exception

    def search(self,id):
        super().search(id)
        query = "select * from tt where id = %s"
        rowAffected = myCursor.execute(query, (id))
        if (rowAffected != 0):
            row = myCursor.fetchone()
            self.special = row[1]
            self.sal = row[2]
            myCon.commit()
        else:
            myCon.rollback()
            raise Exception

    def update(self,id):
        query = "update tt set salary = %s, special = %s where id = %s"
        rowAffected = myCursor.execute(query, (self.sal,self.special, id))
        if (rowAffected != 0):
            myCon.commit()
            super().update(id)
        else:
            myCon.rollback()
            raise Exception

    def delete(self,id):
        query = "delete from tt where id = %s"
        rowAffected = myCursor.execute(query, (id))
        if (rowAffected == 0):
            myCon.rollback()
            raise Exception
        else:
            myCon.commit()
            super().delete(id)


#End of BLL
