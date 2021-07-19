#this code is under the lisence 
class data_:

    def __init__(self,host:str,user:str,password:str,database:str):
    #    def __init__(self,host,user,password,database = "new_database"):

        import mysql.connector
        import random
        import pandas as pd
        import numpy as np
        self.pr_mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
            )
        try:
            self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database= database
            )
        except:
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )

            mycursor = mydb.cursor()

            mycursor.execute(f"CREATE DATABASE {database}")
            self.mydb = mysql.connector.connect(
            host="127.0.0.11",
            user="root",
            password=""
            )

    #    try:
    #        self.mydb = mysql.connector.connect(
    #            host=host,
    #            user=user,
    #            password=password,
    #            database=database
    #        )
    #        self.mycursor =self.mydb.cursor()
    #
    #
    #    except:
    #        mydb = mysql.connector.connect(
    #            host=database,
    #            user=user,
    #            password=password
    #        )
    #        mycursor = self.mydb.cursor()
    #
    #        mycursor.execute(f"CREATE DATABASE {database}")
    #        self.mydb = mysql.connector.connect(
    #            host=host,
    #            user=user,
    #            password=password,
    #            database=database
    #        )
    #        self.mycursor =self.mydb.cursor()
    def extract_name_database(self,return_:bool = True,print_:bool=True):
        mycursor = self.pr_mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        l = []
        for x in mycursor:
            l.append(x)
        if print_ == True:
            print(l)
        if return_ == True:
            return l
    def creat_tabel(self,name,colonne_name:list,nombre_caractère:list):
        mycursor = self.mydb.cursor()
        c0 = len(colonne_name)
        c1 = len(nombre_caractère)
        name_liste1 = []
        name_liste2 = []
        ln0 = []
        if c1 == c0:
            _v3 = 0
            while _v3 < c0:
                n0 = (str(colonne_name[_v3]) + "VARCHAR(" + str(nombre_caractère) + ")")
                ln0.append(n0)
            n1 = ', '.join([str(elem) for elem in ln0])
            n2 = (f"'(CREATE TABLE {name}" + n1 + ")'")
            mycursor.execute(n2)
            _v3 = _v3 + 1
        else:s = input("le nombre d'élément dans la liste des nom de colonne et la liste des nombre de caractère ne sont pas identiques.")
    def watch_table(self,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()

        mycursor.execute("SHOW TABLES")

        l = []
        for x in mycursor:
            l.append(x)
        if print_ == True:
            print(l)
        if return_ == True:
            return l

    def new_table_add_kay(self,name_table,colonne_name:list,nombre_caractère:list):
        mycursor = self.mydb.cursor()
        c0 = len(colonne_name)
        c1 = len(nombre_caractère)
        name_liste1 = []
        name_liste2 = []
        ln0 = []
        if c1 == c0:
            _v3 = 0
            while _v3 < c0:
                n0 = (str(colonne_name[_v3]) + "VARCHAR(" + str(nombre_caractère) + ")")
                ln0.append(n0)
            n1 = ', '.join([str(elem) for elem in ln0])
            n1_ = (f"(id TNT AUTO_INCREMENT PRIMARY KEY," + n1)
            n2 = (f"'CREATE TABLE {name_table} " + n1 + ")'")
            mycursor.execute(n2)
            _v3 = _v3 + 1
        else:s = input("le nombre d'élément dans la liste des nom de colonne et la liste des nombre de caractère ne sont pas identiques.")
    def add_primary_key(self,table):
        mycursor = self.mydb.cursor()

        mycursor.execute(f"ALTER TABLE {table} ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    def inser(self,tabel,list_name_collon:list,liste_value:list,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()
        str = ', '.join([str(elem) for elem in list_name_collon])
        str = ("(" + str + ")")
        str2 = ', '.join([str(elem) for elem in liste_value])
        str2 = ("(" + str2 + ")")
        a1 = "%s"
        a2 = "%s"
        for e in list_name_collon:
            a2 = (a2 + "," + a1)
        a2 = ("(" + a2 + ")")
        sql = ("INSERT INTO" + tabel + "VALUES" + str)
        val = str2
        mycursor.execute(sql,val)
        self.mydb.commit()
        if print_ == True:
            print(mycursor.rowcount, "record inserted.")
        if return_ == True:
            vt = (mycursor.rowcount, "record inserted.")
            return vt
    def inser_multie(self,tabel,list_name_collon:list,liste_value:list,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()
        str = ', '.join([str(elem) for elem in list_name_collon])
        str = ("(" + str + ")")
        a1 = "%s"
        a2 = "%s"
        for e in list_name_collon:
            a2 = (a2 + "," + a1)
        a2 = ("(" + a2 + ")")
        sql = ("ISERT INTO" + tabel + "VALUES" + str)
        val = liste_value
        mycursor.execute(sql,val)
        self.mydb.commit()
        if print_ == True:
            print(mycursor.rowcount, "record inserted.")
        if return_ == True:
            vt = (mycursor.rowcount, "record inserted.")
            return vt
    def inser_what_ID(self,tabel,list_name_collon:list,liste_value:list,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()
        str = ', '.join([str(elem) for elem in list_name_collon])
        str = ("(" + str + ")")
        str2 = ', '.join([str(elem) for elem in liste_value])
        str2 = ("(" + str2 + ")")
        a1 = "%s"
        a2 = "%s"
        for e in list_name_collon:
            a2 = (a2 + "," + a1)
        a2 = ("(" + a2 + ")")
        sql = ("ISERT INTO" + tabel + "VALUES" + str)
        val = str2
        mycursor.execute(sql,val)
        self.mydb.commit()
        if print_ == True:
            print("1 record inserted, ID:", mycursor.lastrowid)
        if return_ == True:
            vt = ("1 record inserted, ID:", mycursor.lastrowid)
            return vt
    def select_all(self,table:str,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT * FROM {table}")
        myresult = mycursor.fetchall()
        l = []
        for x in myresult:
            l.append(x)
        if print_ == True:
            print(l)
        if return_ == True:
            return l
    def select_collone(self,table:str,collonne:list,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()
        str = ', '.join([str(elem) for elem in collonne])
        n1 = (f"SELECT {str} FROM {table}")
        mycursor.execute(n1)
        mycursor.fetchall()

        l = []
        for x in mycursor:
            l.append(x)
        if print_ == True:
            print(l)
        if return_ == True:
            return l
    def select_fetchone(self,table:str,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()

        mycursor.execute(f"SELECT * FROM {table}")
        myresult = mycursor.fetchone()
        if print_:
            print(myresult)
        if return_ == True:

            return myresult
    def select_filter(self,table:str,colonne:str,filter:str,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()
        sql = f"SELECT * FROM {table} WHERE {colonne} = {filter} "
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        l = []
        for x in myresult:
            l.append(x)
        if print_:
            print(l)
        if return_:
            return l
    def select_Gcaract(self,liste:str,one_colonne:str,general_caracter:str,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()

        sql = f"SELECT * FROM {liste} WHERE {one_colonne} LIKE '%{general_caracter}%'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        l = []
        for x in myresult:
            l.append(x)
        if print_ == True:
            print(l)
        if return_ == True:
            return l
    def security_1(self,table,collon,return_:bool = True,print_:bool=False):
        mycursor = self.mydb.cursor()

        sql = f"SELECT * FROM {table} WHERE {collon} = %s"
        adr = ("Yellow Garden 2",)
        mycursor.execute(sql, adr)
        myresult = mycursor.fetchall()
        l = []
        for x in myresult:
            l.append(x)
        if print_ == True:
            print(l)
        if return_:
            return l
    def trier(self,liste:str,type:str,return_:bool = True,print_:bool=False):
        """

        :param liste: name the liste conent data in the database specifiqued in the line you actived this class.
        :param type:
                v.anglich
                name : aphabet order.
                v.français:
                name : par ordre alphabétique
        """
        mycursor = self.mydb.cursor()

        sql = f"SELECT * FROM {liste} ORDER BY {type}"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        l = []
        for x in myresult:
            l.append(x)
        if print_:
            print(l)
        if return_:
            return l
    def trier_inver(self,liste:str,type:str,return_:bool = False,print_:bool=False):
        """

        :param liste: name the liste conent data in the database specifiqued in the line you actived this class.
        :param type:
                v.anglich
                name : aphabet order.
                v.français:
                name : par ordre alphabétique
        """
        mycursor = self.mydb.cursor()

        sql = f"SELECT * FROM {liste} ORDER BY {type} DESC"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        l = []
        for x in myresult:
            l.append(x)
        if print_:
            print(l)
        if return_:
            return l
    def dellet_data_all_similary_addresse(self,liste:str,collon:str,addresse_data_delete,return_:bool = False,print_:bool=False):
        mycursor = self.mydb.cursor()
        sql = f"DELETE FROM {liste} WHERE {collon} = {addresse_data_delete}"
        mycursor.execute(sql)

        self.mydb.commit()
        if print_:
            print(mycursor.rowcount, "record(s) deleted")
        if return_:
            vt = (mycursor.rowcount, "record(s) deleted")
            return vt
    def dellete_all_data_table(self,liste):
        mycursor = self.mydb.cursor()
        sql = f"DELETE FROM {liste}"
        mycursor.execute(sql)
        self.mydb.commit()
    def security_2_dellete_data(self,liste:str,collon:str,return_:bool = False,print_:bool=False):
        mycursor = self.mydb.cursor()
        sql = f"DELETE FROM {liste} WHERE {collon} = %s"
        mycursor.execute(sql)
        self.mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        if print_:
            print(mycursor.rowcount, "record(s) deleted")
        if return_:
            vt = (mycursor.rowcount, "record(s) deleted")
            return vt
    def security_3_dellete_all_data_table(self, liste):
        mycursor = self.mydb.cursor()
        sql = f"DELETE FROM {liste} = %s"
        mycursor.execute(sql)
        self.mydb.commit()
    def dellete_table(self, liste:str):
        mycursor = self.mydb.cursor()
        sql = f"DROP TABLE IF EXISTS {liste}"
        mycursor.execute(sql)
    def uptade_data(self,liste:str,collon,data,new_data,return_:bool = False,print_:bool=False):
        mycursor = self.mydb.cursor()
        sql = f"UPDATE {liste} SET {collon} = {new_data} WHERE {collon} = {data}"
        mycursor.execute(sql)
        self.mydb.commit()
        if print_:
            print(mycursor.rowcount, "record(s) affected")
        if return_:
            vt = (mycursor.rowcount, "record(s) affected")
            return vt
    def security_4_metode_pacholder(self, collon, return_:bool = False, print_:bool=False):
        mycursor = self.mydb.cursor()

        sql = "UPDATE customers SET address = %s WHERE address = %s"
        val = ("Valley 345", "Canyon 123")

        mycursor.execute(sql, val)

        self.mydb.commit()

        if print_:
            print(mycursor.rowcount, "record(s) affected")
        if return_:
            vt = (mycursor.rowcount, "record(s) affected")
            return vt
    def limit_renvoie_for_one_requet(self,liste,limit):
        mycursor = self.mydb.cursor()

        mycursor.execute(f"SELECT * FROM {liste} LIMIT {limit}")
        myresult = mycursor.fetchall()
        l = []
        for x in myresult:
            l.append(x)
        if print_:
            print(l)
        if return_:
            return l
    def start_oder_position(self,liste:str,number_of_ellement:int,start:int,return_:bool = False,print_:bool=False):
        mycursor = self.mydb.cursor()
        start = start - 1
        mycursor.execute(f"SELECT * FROM {liste} LIMIT {number_of_ellement} OFFSET {start}")
        myresult = mycursor.fetchall()
        l = []
        for x in myresult:
            l.append(x)
        if print_:
            print(l)
        if return_:
            return l
