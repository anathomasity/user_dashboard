from system.core.model import Model
import re
class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self,udata):
        password = udata['password']
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not udata['first_name']:
            errors.append('Name cannot be blank')
        elif len(udata['first_name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not udata['last_name']:
            errors.append('Last Name cannot be blank')
        elif len(udata['last_name']) < 2:
            errors.append('Last Name must be at least 2 characters long')
        if not udata['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(udata['email']):
            errors.append('Email format must be valid!')
        if not udata['password']:
            errors.append('Password cannot be blank')
        elif len(udata['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif udata['password'] != udata['pw_confirmation']:
            errors.append('Password and confirmation must match!')


        if errors:

            return {"status": False, "errors": errors}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(password)
            query = "INSERT into users (first_name, last_name, email, password, created_at) values(:first_name, :last_name, :email, :password, NOW())"
           
            data = {
                'first_name': udata['first_name'] , 
                'last_name': udata['last_name'] ,
                'email': udata['email'] ,
                'password': hashed_pw ,
            }
            self.db.query_db(query, data)


            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query) 

            if users[0]['id'] == 1:
                query = "UPDATE users SET user_level='9' WHERE id='1';"
                self.db.query_db(query)
            elif users[0]['id'] != 1:
                query = "UPDATE users SET user_level='1' WHERE id=:id;"
                data={ "id": users[0]['id'] }
                self.db.query_db(query,data)

            users = self.db.query_db(get_user_query) 
            return {'status': True, 'user': users[0]}

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def remove_user(self,id):
        query = "DELETE FROM users where id = :id"
        data = {
            'id':id
        }
        return self.db.query_db(query, data)

    def show_user(self,id):
        query = "SELECT * FROM users where id = :id"
        data = {
            'id':id
        }
        return self.db.query_db(query, data)

    def update(self,id,udata):
        if udata['level'] == 'user':
            udata['level'] = 1
        elif udata['level'] == 'admin':
            udata['level'] = 9

        query = "UPDATE users SET first_name = :first_name, last_name= :last_name, email=:email, user_level=:level WHERE id=:id;"
        data={ 
            "id": id,
            'first_name': udata['first_name'],
            'last_name': udata['last_name'] ,
            'email': udata['email'] ,
            'level':udata['level']
            }
        self.db.query_db(query,data)
        return True

    def updatepas(self,id,udata):
        password = udata['password']
        errors = []
        if not udata['password']:
            errors.append('Password cannot be blank')
        elif len(udata['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif udata['password'] != udata['pw_confirmation']:
            errors.append('Password and confirmation must match!')

        if errors:

            return {"status": False, "errors": errors}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(password)
            query = "UPDATE users SET password=:password WHERE id=:id"
           
            data = {
                'password': hashed_pw ,
                'id':id
            }
            self.db.query_db(query, data)
            return {'status': True}

    def login_user(self,info):
        password = info['password']

        user_query = "SELECT * FROM users WHERE email = :email"
        user_data = {'email': info['email']}

        user = self.db.query_db(user_query, user_data)

        
        if user:

            id = user[0]['id']
            level = user[0]['user_level']

            name = user[0]['first_name']
            if self.bcrypt.check_password_hash(user[0]['password'], password):
                return {'id': id, 'level': level, 'name': name}
        return False

    def editprofile1(self,id,udata):
        query = "UPDATE users SET first_name = :first_name, last_name= :last_name, email=:email WHERE id=:id;"
        data={ 
            "id": id,
            'first_name': udata['first_name'],
            'last_name': udata['last_name'] ,
            'email': udata['email'] ,
            }
        self.db.query_db(query,data)
        return True

    def editprofile3(self,id,udata):
        query = "UPDATE users SET description=:description WHERE id=:id;"
        data={ 
            "id": id,
            'description': udata['description']
            }
        self.db.query_db(query,data)
        return True

    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """