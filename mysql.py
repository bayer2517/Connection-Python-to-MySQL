import pymysql
from config import user, password, host, db_name # we must to create config.py and add information to connect python with mysql.


try:
    connection = pymysql.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

    # try:
    #     with connection.cursor() as cur:
    #         new_table = 'CREATE TABLE `ncos`(id int AUTO_INCREMENT, name varchar(32), dob DATE, dod int, pay_grade varchar(32), PRIMARY KEY (id));' # NCO it's a list of Non Commision officers and information about them
    #
    #         cur.execute(new_table)
    # finally:
    #     connection.close()
    # print("Connected")

    try:
        with connection.cursor() as cur:
           insert_query = 'INSERT INTO `ncos`(name,pay_grade) VALUE ("Alan Po", "E-6");' # We add information with name and pay grade
           cur.execute(insert_query)
           connection.commit()
        print("Everything connected")

    finally:
        connection.close()

except Exception as ex:
    print(ex)
