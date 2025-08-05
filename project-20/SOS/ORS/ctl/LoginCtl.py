from django.shortcuts import render, redirect

from .BaseCtl import BaseCtl
from ..service.UserService import UserService
from ..utility.DataValidator import DataValidator


class LoginCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['loginId'] = requestForm['loginId']
        self.form['password'] = requestForm['password']

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['loginId'])):
            inputError['loginId'] = "Login Id is required"
            self.form['error'] = True

        elif (DataValidator.isemail(self.form['loginId'])):
            inputError['loginId'] = "Email must be in form abc@gmail.com"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['password'])):
            inputError['password'] = 'Password is required'
            self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):
        user = self.get_service().authenticate(self.form)
        if (user is None):
            self.form['error'] = True
            self.form['message'] = 'Invalid id and password....!'
            res = render(request, self.get_template(), {'form': self.form})
        else:
            request.session['user'] = user.firstName
            res = redirect('/ORS/Welcome/')
        return res

    def get_template(self):
        return "Login.html"

    def get_service(self):
        return UserService()
