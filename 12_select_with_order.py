import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()

# mycursor.execute(" SELECT * FROM movies ORDER BY name")
mycursor.execute(" SELECT * FROM movies ORDER BY name DESC")


result = mycursor.fetchall()

print(result)




