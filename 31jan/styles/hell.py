import pymysql

def mysqlconnect():
	# To connect MySQL database
	conn = pymysql.connect(
		host='localhost',
		user='root',
		password = "2023",
		db='sys',
		)
	
	cur = conn.cursor()
	cur.execute("select @@version")
	output = cur.fetchall()
	print(output)
	
	# To close the connection
	conn.close()

# Driver Code
if __name__ == "__main__" :
	mysqlconnect()
