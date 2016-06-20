from system.core.router import routes

routes['GET']['/'] = 'Welcome#index'
routes['GET']['/login_reg'] = 'Welcome#display_login_reg'


routes['POST']['/login'] = 'Users#login'
routes['GET']['/logout'] = 'Users#logout'
routes['POST']['/register'] = 'Users#register'
# dashboard is to show every user
routes['GET']['/users/new'] = 'Users#new'
routes['GET']['/dashboard'] = 'Users#index'
routes['GET']['/users/<int:id>'] = 'Users#show'
routes['GET']['/users/edit/<int:id>'] = 'Users#edit'
routes['POST']['/users/edit/<int:id>'] = 'Users#update'
routes['GET']['/users/destroy/<int:id>'] = 'Users#delete_user'
routes['POST']['/messages'] = 'Messages#create'
routes['POST']['/users/<int:id>/comments'] = 'Messages#create_comment'

"""

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
