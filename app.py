from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resource.movie import MovieInfoResouce, MovieListResouce, MovieSearchResource
from resource.rating import MovieRatingResource, RatingListResource
from resource.recommend import MovieRecomRealTimeResource, MovieRecomResource
from user import UserLoginResource, UserLogoutResource, UserRegisterResource, jwt_blacklist
from config import Config

app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)

# JWT 토큰 라이브러리 만들기
jwt = JWTManager(app)

# 로그아웃된 토큰이 들어있는 set 을, jwt에 알려준다.
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload): 
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

# 경로와 리소스(API 코드)를 연결한다.

api.add_resource(UserRegisterResource, '/users/register')

api.add_resource(UserLoginResource, '/users/login')

api.add_resource(UserLogoutResource, '/users/logout')

api.add_resource(MovieListResouce, '/movie')

api.add_resource(MovieInfoResouce, '/movie/<int:movie_id>')

api.add_resource(MovieSearchResource, '/movie/search')

api.add_resource(RatingListResource, '/rating')

api.add_resource(MovieRatingResource, '/movie/<int:movie_id>/rating')

api.add_resource(MovieRecomRealTimeResource, '/movie/recommend')

if __name__=="__main__" :
    app.run()