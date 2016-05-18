from system.core.model import Model

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()

    def post_message(self,id,mdata):
        id=id
        query = "INSERT into messages (message, created_at, updated_at, user_id, rec_id) values(:message, NOW(), NOW(), :user_id, :rec_id)" 
        data = {
            'message': mdata['message'], 
            'user_id': mdata['user_id'],
            'rec_id': id,
        }
        self.db.query_db(query, data)
        return True

    def post_comment(self,cdata):
        query = "INSERT into comments (comment, created_at, updated_at, message_id, user_id) values(:comment, NOW(), NOW(), :msg_id, :user_id)" 
        data = {
            'comment': cdata['comment'], 
            'msg_id': cdata['message_id'],
            'user_id': cdata['uid']
        }
        self.db.query_db(query, data)
        return True

    def get_messages(self,id):
        query = "SELECT first_name,last_name,messages.created_at,messages.id AS message_id,message FROM messages LEFT JOIN users ON users.id = messages.user_id WHERE rec_id = :rec_id ORDER BY messages.id DESC"
        data = {
            'rec_id':id
        }
        return self.db.query_db(query, data)

    def get_comments(self,id):
        query = "SELECT users.id, first_name, last_name, comment, comments.created_at, comments.message_id FROM users JOIN comments ON users.id = comments.user_id ORDER BY comments.created_at"
        return self.db.query_db(query)


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