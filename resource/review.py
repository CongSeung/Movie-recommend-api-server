import datetime
from http import HTTPStatus
from flask import request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required
from flask_restful import Resource
from mysql.connector.errors import Error   
from mysql_connection import get_connection
import mysql.connector

class MovieReviewResource(Resource):
    def get(self, movie_id):
        
        offset = request.args['offset']
        limit = request.args['limit']

        # user_id = get_jwt_identity()

        # 2. 디비로부터 내 메모를 가져온다.
        try :
            connection = get_connection()

            query = '''select m.title, u.name, u.gender, r.rating
                        from rating r
                        left join user u
                        on u.id = r.user_id
                        left join movie m
                        on m.id = r.movie_id
                        where r.movie_id = %s
                        limit '''+offset+''' , '''+limit+''';'''
            
            record = (movie_id,)

            # select 문은, dictionary = True 를 해준다.
            cursor = connection.cursor(dictionary = True)

            cursor.execute(query, record)

            # select 문은, 아래 함수를 이용해서, 데이터를 가져온다.
            result_list = cursor.fetchall()

            print(result_list)

            # 중요! 디비에서 가져온 timestamp 는 
            # 파이썬의 datetime 으로 자동 변경된다.
            # 문제는! 이데이터를 json 으로 바로 보낼수 없으므로,
            # 문자열로 바꿔서 다시 저장해서 보낸다.

            # i = 0
            # for record in result_list :
            #     result_list[i]['avg'] = float(record['avg'])
            #     i = i + 1       


            cursor.close()
            connection.close()

        except mysql.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()

            return {"error" : str(e), 'error_no' : 20}, 503
        
        return {'result' : 'success' ,
                'count' : len(result_list) ,
                'items' : result_list }, 200
