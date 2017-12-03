import mysql.connector

def main():
    conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='nicks', port='3306')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM usuario
    """)

    users = cursor.fetchall()

    for user in users:
        print("%i - %s - %s - %s - %s - %s - %s - %s\n" % (user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7]))

    conn.close()


if __name__ == '__main__':
    main()