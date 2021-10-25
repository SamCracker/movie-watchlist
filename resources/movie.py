from flask import Response, request
from flask.blueprints import Blueprint
from database.models import Movie, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

class MoviesApi(Resource):
    # @jwt_required()
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    # @jwt_required()
    def post(self):
        print("Request:: ", request)
        body = request.get_json()
        print("Body:: ", body)
        movie = Movie(**body)
        movie.save()
        id = movie.id
        return {'id':str(id)}, 200

class UserMoviesApi(Resource):
    @jwt_required()
    def delete(self, w_id):
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        user.watch_list.remove(int(w_id))
        print(user.watch_list)
        user.save()
        return 'Deletion Successful', 200

class UserMovieApi(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        print("Request:: ", request)
        body = request.get_json()
        print("User_id:: ", user_id)
        print("Body:: ", body)
        user = User.objects.get(id=user_id)
        movies = body['watch_list']
        temp_watch_list = user.watch_list
        for i in movies:
            temp_watch_list.append(i)
        set(temp_watch_list)
        user.watch_list = temp_watch_list
        user.save()
        id = user_id
        return {'id': 'Movie List Updated of User: '+str(id)}, 200
    
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        movie = Movie.objects
        watch_list = user.watch_list
        user_watch_list = []
        for w in watch_list:
            m = movie.get(movie_id=w).to_json()
            user_watch_list.append(m)
        print(user_watch_list)
        return Response(str(user_watch_list), mimetype="application/json", status=200)
