


import psycopg2
from psycopg2 import Error

class DB():

    def query(query_str):
        try:
            connection = psycopg2.connect(user="ezfhdiiyfyfnul",
                                          password="0ebccaa759c4eb556fca9dd7fc7573e8a07d24989872d376fcc32e98e85b33e7",
                                          host="ec2-54-75-235-28.eu-west-1.compute.amazonaws.com",
                                          port="5432",
                                          database="d3l35hvgdquvnm")
            connection.autocommit = True
            cursor = connection.cursor()
            print(query_str)
            cursor.execute(query_str)
            result = cursor.fetchall()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        return result