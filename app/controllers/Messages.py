from system.core.controller import *

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)

        self.load_model('Message')
        self.db = self._app.db

    def create(self):
        # session ['user']['id'] == author id
        self.models['Message'].create_message(request.form, session['user']['id'])
        return redirect('/users/{}'.format(request.form['user_id']))

    def create_comment(self, id):
        # session ['user']['id'] == author id
        self.models['Message'].create_comment(request.form, session['user']['id'])
        return redirect('/users/{}'.format(id))
