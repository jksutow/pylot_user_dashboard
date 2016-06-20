from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.load_model('Message')
        self.db = self._app.db

    def register(self):
        # validate registration information
        validation_result = self.models['User'].validate_reg_info(request.form)


        # if registration info is valid, login user automatically and send to dashboard
        # no errors
        # if invalid, send back to login_reg with errors
        return self.handle_login_reg_response(validation_result)
        # if type(validation_result) == list:
        #     session['val_errors'] = validation_result
        #     return redirect('/login_reg', errors = validation_result)
        # self.set_user_session(validation_result)
        # return redirect('/dashboard')
    def new(self):
        return self.load_view('loginreg.html')

    def handle_login_reg_response(self, result):
        if type(result) == list:
            session['val_errors'] = result
            return redirect('/login_reg')
        self.set_user_session(result)
        return redirect('/dashboard')

    def login(self):
        login_result = self.models['User'].login(request.form)
        return self.handle_login_reg_response(login_result)
        return redirect('/login_reg')

    def logout(self):
        session.clear()
        return redirect('/')

    def set_user_session(self, validation_result):
        session['user'] = validation_result
        return

    def index(self):
        #Grab all users
        users = self.models['User'].fetch_all_users(session['user']['id'])
        return self.load_view('dashboard.html', users=users)

    def show(self, id):
        user = self.models['User'].fetch_user_by_id(id)
        messages = self.models['Message'].fetch_messages_by_user_id(id)
        return self.load_view('users/show.html', user=user, messages=messages)

    def edit(self, id):
        user = self.models['User'].fetch_user_by_id(id)
        return self.load_view('users/edit.html', user=user)
    def update(self, id):
        # Give model updated user information
        result = self.models['User'].update_user_by_id(id, request.form)
        print "UPDATED USER AND RECEIVED BACK: {}".format(result)
        return redirect('/dashboard')
    # def edit_user(self, id):
    #     edit_result = self.models['User'].edit_user(request.form)
    #     return self.edit(edit_result)
    #     return redirect('/dashboard')

    def delete_user(self, id):
        self.models['User'].delete_user(id)
        return redirect('/')
