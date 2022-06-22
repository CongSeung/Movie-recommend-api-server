import mysql.connector

def get_connection():
    connection = mysql.connector. connect(
        host = 'yh-db.ctttsro2er9u.ap-northeast-2.rds.amazonaws.com',
        database = 'movie_db',
        user = 'movie_user',
        password = 'leem0929'
    )
    return connection