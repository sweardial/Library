import mysql.connector



db1 = mysql.connector.connect(
	host = host,
	user = user,
	password = password
)
mycursor1 = db1.cursor()
mycursor1.execute("CREATE DATABASE IF NOT EXISTS library")


db = mysql.connector.connect(
	host= host,
	user= user,
	password=password,
	database='library'
)



mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS library")

mycursor.execute("CREATE TABLE IF NOT EXISTS librarian (id INT auto_increment, primary key(id), name VARCHAR(20), book VARCHAR(50), released DATE)")



def append_book(name=None, book=None, released=None):
	if isinstance(name, str) and isinstance(book, str) and isinstance(released, str):
		mycursor.execute(f"INSERT INTO librarian(name, book, released) VALUES ('{name}','{book}','{released}')")
		db.commit()
	else:
		raise ValueError()


def updating(new_name=None, new_book=None, new_release=None, id=None):
	if len(new_name) > 0:
		updating_query = f"""UPDATE librarian SET name ='{new_name}' WHERE id  ='{id}'"""
		mycursor.execute(updating_query)
		db.commit()
	if len(new_book) > 0:
		updating_query = f"""UPDATE librarian SET book ='{new_book}' WHERE id ='{id}'"""
		mycursor.execute(updating_query)
		db.commit()
	if len(new_release) > 0:
		updating_query = f"""UPDATE librarian SET relised ='{new_release}' WHERE id ='{id}'"""
		mycursor.execute(updating_query)
		db.commit()


def delete_book(id=None):
	delete_query = f"DELETE FROM librarian WHERE id = {id}"
	mycursor.execute(delete_query)
	db.commit()


def delete_all():
	delete_query = "DELETE FROM librarian"
	mycursor.execute(delete_query)
	db.commit()

