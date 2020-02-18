import redis
import mysql.connector
from mysql.connector import Error
from flight.config import Config


def redisConnect():

    pool = redis.ConnectionPool(
        host=Config.redis_host, port=Config.redis_port, db=Config.redis_db, password=Config.redis_password)

    return redis.Redis(connection_pool=pool)


def sqlconnect():
    cursor = None
    try:
        mySQLConnection = mysql.connector.connect(host=Config.maria_host,
                                                  database=Config.maria_db,
                                                  user=Config.maria_user,
                                                  password=Config.maria_pass)

        return mySQLConnection
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))



def getdata(sqlquery):
    
    mySQLConnection = sqlconnect()
    cursor = mySQLConnection.cursor(buffered=True)
    cursor.execute(sqlquery)
    records = cursor.fetchall()

    delconnect(mySQLConnection, cursor)
    return records


def delconnect(mySQLConnection, cursor):
    if (mySQLConnection.is_connected()):
        cursor.close()
        mySQLConnection.close()
