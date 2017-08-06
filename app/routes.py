from .api.v1.user.handler import CreateUsers, GetUser, GetUsers, UpdateUser, DeleteUser

app_routes = [
    {'class': GetUser, 'route': '/users/<string:user_id>'},
    {'class': GetUsers, 'route': '/users'},
    {'class': CreateUsers, 'route': '/users'},
    {'class': UpdateUser, 'route': '/users/<string:user_id>'},
    {'class': DeleteUser, 'route': '/users/<string:user_id>'},
]
