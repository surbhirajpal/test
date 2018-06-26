import sqlite3

#Q1
hey=sqlite3.connect('acadview.db')
print("opened database sucessfully")

hey.execute('''CREATE TABLE BOOKS 
(BOOK_ID INT PRIMARY KEY NOT NULL,
TITLE_ID INT,
LOCATION TEXT,
GENRE TEXT);''')  

hey.execute('''CREATE TABLE TITLES
(TITLE_ID INT PRIMARY KEY NOT NULL,
TITLES TEXT,
ISBN INT,
PUBLISHER_ID INT,
PUBLICATION_YEAR INT);''')

hey.execute('''CREATE TABLE AUTHORSTITLE
(AUTHORS_TITLE_ID INT PRIMARY KEY NOT NULL,
AUTHOR_ID INT,
TITLE_ID INT);''')

hey.execute('''CREATE TABLE AUTHORS
(AUTHOR_ID INT PRIMARY KEY NOT NULL,
FIRST_NAME TEXT,
MIDDLE_NAME TEXT,
LAST_NAME TEXT);''')

hey.execute('''CREATE TABLE PUBLISHERS
(PUBLISHER_ID INT PRIMARY KEY NOT NULL,
NAME TEXT,
STREET_ADDRESS TEXT,
SUITE_NUMBER INT,
ZIP_COD_ID INT );''')

hey.execute('''CREATE TABLE ZIPCODES
(ZIP_CODE_ID INT PRIMARY KEY NOT NULL,
CITY TEXT,
STATE TEXT,
ZIP_CODE INT );''')

print("table created succesfully")



#q2
hey.execute('''INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES('1','2','california','comic');''')
hey.execute('''INSERT INTO TITLES(TITLE_ID,TITLES,ISBN,PUBLISHER_ID,PUBLICATION_YEAR)VALUES('2','ABC','1234','100','2000');''')
hey.execute('''INSERT INTO AUTHORSTITLE(AUTHORS_TITLE_ID,AUTHOR_ID,TITLE_ID)VALUES('4','200','2');''')
hey.execute('''INSERT INTO PUBLISHERS(PUBLISHER_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIP_COD_ID)VALUES('100','SURBHI','XYZ','NMO','4');''')
hey.execute('''INSERT INTO AUTHORS(AUTHOR_ID,FIRST_NAME,MIDDLE_NAME)VALUES('200','SURBHI','RAJPAL');''')
hey.execute('''INSERT INTO ZIPCODES(ZIP_CODE_ID,CITY,STATE,ZIP_CODE)VALUES('3','PANCHKULA','HARYANA','1234');''')
hey.commit()
print("inserted successfully")



#Q3
cursor=hey.execute("SELECT * FROM BOOKS;")
for row in cursor:
    print("BOOK_ID= ", row[0])
    print("TITLE= ", row[1])
    print("LOCATION= ", row[2])
    print("GENRE= ", row[3])
    print("")


hey.execute("UPDATE BOOKS SET LOCATION ='chandigarh' WHERE BOOK_ID = '1';")
hey.execute("UPDATE BOOKS SET GENRE='horror'WHERE BOOK_ID='1';")
cursor=hey.execute("SELECT * FROM BOOKS;")
for row in cursor:
    print("BOOK_ID= ", row[0])
    print("TITLE= ", row[1])
    print("LOCATION= ", row[2])
    print("GENRE= ", row[3])
    print("")
    




