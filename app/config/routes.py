from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Users'
routes['/signin'] = 'Users#signin'
routes['POST']['/signin_user'] = 'Users#signin_user'
routes['/register'] = 'Users#register'
routes['POST']['/register_user'] = 'Users#register_user'
routes['/dashboard/admin'] = 'Users#admin_dashboard'
routes['/dashboard'] = 'Users#dashboard'
routes['/users/edit/<id>'] = 'Users#admin_edit'
routes['/editprofile/<id>'] = 'Users#editprofile'
routes['POST']['/editprofile/1/<id>'] = 'Users#editprofile1'
routes['POST']['/editprofile/2/<id>'] = 'Users#editprofile2'
routes['POST']['/editprofile/3/<id>'] = 'Users#editprofile3'
routes['POST']['/users/edit/<id>'] = 'Users#edit'
routes['POST']['/password/<id>'] = 'Users#passwordedit'
routes['/users/remove/<id>'] = 'Users#remove'
routes['/users/new'] = 'Users#new'
routes['POST']['/users/add_user'] = 'Users#add_user'
routes['/users/show/<id>'] = 'Users#show_user'
routes['POST']['/post_message/<id>'] = 'Users#post_message'
routes['/logout'] = 'Users#logout'
routes['POST']['/users/show/post_message/<id>'] = 'Messages#post_message'
routes['POST']['/users/show/post_comment/<mid>/<uid>'] = 'Messages#post_comment'
"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
