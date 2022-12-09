import mysql.connector
import math
mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )
mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE medidas (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), altura VARCHAR(255), peso VARCHAR(255), IMC VARCHAR(255))")

print("Entre com o seu nome: ")
nome = input
sql = "INSERT INTO medidas (nome) VALUES (%s)"
val = nome
mycursor.execute(sql, val)
print("Entre com o seu peso: ")
peso = input
sql = "INSERT INTO medidas (peso) VALUES (%s)"
val = peso
mycursor.execute(sql, val)
print("Entre com a sua altura: ")
altura = input
sql = "INSERT INTO medidas (altura) VALUES (%s)"
val = altura
mycursor.execute(sql, val)
imc = (peso/math.sqrt(altura))
sql = "INSERT INTO medidas (IMC) VALUES (%s)"
val = imc
mycursor.execute(sql, val)
mydb.commit()
print(mycursor)
