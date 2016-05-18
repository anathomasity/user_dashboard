from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.load_model('Message')

        self.db = self._app.db
 
    def index(self):

        return self.load_view('index.html')

    def signin(self):
        return self.load_view('signin.html')

    def signin_user(self):
        info = {
            "email" : request.form['email'],
            "password" : request.form['password']
        }
        userlogin = self.models['User'].login_user(info)
        

        if userlogin:
            session['id'] = userlogin['id']
            session['name'] = userlogin['name']
            session['level']=userlogin['level']
            if userlogin['level'] == 9:
                return redirect('/dashboard/admin')
            elif userlogin['level'] == 1:
                return redirect('/dashboard') 

        elif not userlogin:
            flash('Please enter a valid email and password', 'login_errors')
            return redirect('/signin')
        

    def register(self):
        return self.load_view('register.html')

    def register_user(self):
        udata = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : request.form['password'],
            'pw_confirmation': request.form['pw_confirmation']
            }

        create_status = self.models['User'].create_user(udata)

        if create_status['status'] == True:
            session['id'] = create_status['user']['id'] 
            print session['id']         
            if create_status['user']['user_level'] == 9:
                return redirect('/admin_dashboard')
            elif create_status['user']['user_level'] == 1:
                return redirect('/dashboard')

        else:
            print create_status['errors']
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            
            return redirect('/register')

    def admin_dashboard(self):
        if session['level'] == 1:
            return redirect('/dashboard')
        users = self.models['User'].get_users()
        return self.load_view('admin_dashboard.html', users = users)

    def dashboard(self):
        users = self.models['User'].get_users()

        return self.load_view('dashboard.html', users = users)

    def admin_edit(self,id):
        user = self.models['User'].show_user(id)
        
        return self.load_view('admin_edituser.html', user = user[0])

    def edit(self,id):
        id = id
        udata = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'level' : request.form['level']
            }


        self.models['User'].update(id,udata)
        return redirect('/dashboard/admin') 

    def passwordedit(self,id):
        id = id
        udata = {
            'password' : request.form['password'],
            'pw_confirmation': request.form['pw_confirmation']
        }
        result = self.models['User'].updatepas(id,udata)
        if result['status'] == False:
            for message in result['errors']:
                    flash(message, 'paserrors')
                    return redirect('/admin_edit')
        else:
            return redirect('/dashboard/admin')

    def editprofile(self,id):
        id = id
        user = self.models['User'].show_user(id)
        udata = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "email" : user[0]['email'],

        }
        return self.load_view('edituser.html', user = udata)

    def editprofile1(self,id):
        id = id
        udata = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email': request.form['email']
        }

        self.models['User'].editprofile1(id, udata)
        return redirect('/dashboard')

    def editprofile2(self,id):
        id = id
        udata = {
            'password' : request.form['password'],
            'pw_confirmation': request.form['pw_confirmation']
        }
        result = self.models['User'].updatepas(id,udata)
        if result['status'] == False:
            for message in result['errors']:
                    flash(message, 'paserrors')
                    return redirect('/editprofile')
        else:
            return redirect('/dashboard')
        

    def editprofile3(self,id):
        id = id
        udata = {
            "description": request.form['description']
        }
        result = self.models['User'].editprofile3(id,udata)
        return redirect('/dashboard')



    def remove(self,id):
        id = id
        self.models['User'].remove_user(id)
        return redirect('/dashboard/admin')

    def new(self):
        return self.load_view('new.html')

    def add_user(self):
        udata = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : request.form['password']
            }

        create_status = self.models['User'].create_user(udata)
        return redirect('/dashboard/admin')

    def show_user(self,id):
        id = id
        user = self.models['User'].show_user(id)
        messages = self.models['Message'].get_messages(id)
        comments = self.models['Message'].get_comments(id)
        print comments
        return self.load_view('userinfo.html', user = user, messages = messages, comments=comments)

    def post_message(self,id):
        return redirect('show_user', id = id)

    def logout(self):
        session.clear()
        print session
        return redirect('/')