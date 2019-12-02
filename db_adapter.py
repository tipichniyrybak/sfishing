import psycopg2
from psycopg2 import Error

class DB():

    def query(query_str):
        try:
            connection = psycopg2.connect(user="gzszrrxcjdobkb",
                                          password="41aced1ba593952a5acfbb4fc26346adcdf6637bbc8b94d8ab1a18a6d1fac35c",
                                          host="ec2-54-228-246-214.eu-west-1.compute.amazonaws.com",
                                          port="5432",
                                          database="d15h7ch0tposfh")
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