from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
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

    def set_user_session(self, validation_result):
        session['user'] = validation_result
        return

    def index(self):
        #Grab all users
        return self.load_view('dashboard.html')
