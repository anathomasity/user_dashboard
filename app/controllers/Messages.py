from system.core.controller import *

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')
        self.db = self._app.db
   
    def post_message(self,id):
        id = id
        mdata = {
            'message' : request.form['message'],
            'user_id' : session['id']
        }
        self.models['Message'].post_message(id,mdata)
        return redirect('/users/show/' + id)

    def post_comment(self,mid,uid):
        msg_id = mid
        uid = uid

        cdata = {
            'comment' : request.form['comment'],
            'message_id' : msg_id,
            'uid': session['id']
        }
        print cdata
        self.models['Message'].post_comment(cdata)
        return redirect('/users/show/' + uid)