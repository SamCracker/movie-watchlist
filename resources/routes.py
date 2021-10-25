from .movie import MoviesApi, UserMovieApi, UserMoviesApi
from .auth import SignUpApi, LoginApi

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(UserMoviesApi, '/api/usermovies/<w_id>')
    api.add_resource(UserMovieApi, '/api/usermovies')
    
    api.add_resource(SignUpApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
