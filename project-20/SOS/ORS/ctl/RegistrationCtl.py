from operator import truediv

from django.shortcuts import render

from .BaseCtl import BaseCtl
from ..models import User
from ..service.UserService import UserService
from ..utility.DataValidator import DataValidator


class RegistrationCtl(BaseCtl):


    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['firstName'] = requestForm['firstName']
        self.form['lastName'] = requestForm['lastName']
        self.form['loginId'] = requestForm['loginId']
        self.form['password'] = requestForm['password']
        self.form['confirmPassword'] = requestForm['confirmPassword']
        self.form['dob'] = requestForm['dob']
        self.form['address'] = requestForm['address']
        self.form['gender'] = requestForm['address']
        self.form['mobileNumber'] = requestForm['mobileNumber']
        self.form['roleId'] = 2
        self.form['roleName'] = 'student'


    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if (DataValidator.isNull(self.form['firstName'])):
            inputError['firstName'] = 'First name is required'
            self.form['error'] = True
        elif (DataValidator.isalphacehck(self.form['firstName'])):
            inputError['firstName'] = 'Name must have aplhabates only'

        if (DataValidator.isNull(self.form['lastName'])):
            inputError['lastName'] = 'Last name is required'
            self.form['error'] = True
        elif (DataValidator.isalphacehck(self.form['lastName'])):
            inputError['lastName'] = 'last name must have alphabates only'

        if (DataValidator.isNull(self.form['loginId'])):
            inputError['loginId'] = 'Login id is required'
            self.form['error'] = True
        elif (DataValidator.isemail(self.form['loginId'])):
            inputError['loginId'] = 'loginId must be of type abc@gmail.com'
            self.form['error'] = True

        if (DataValidator.isNull(self.form['password'])):
            inputError['password'] = 'Password is needed'
            self.form['error'] = True

        if (DataValidator.isNull(self.form['confirmPassword'])):
            inputError['confirmPassword'] = 'Retype password'
            self.form['error'] = True
        if (DataValidator.isNotNull(self.form['confirmPassword'])):
            if self.form['password'] != self.form['confirmPassword']:
                inputError['confirmPassword'] = 'password and confirmpassword are not same'
                self.form['error'] = True

        if(DataValidator.isNull(self.form['dob'])):
            inputError['dob'] = 'date of birth needed'
            self.form['error'] = True
        elif(DataValidator.isDate(self.form['dob'])):
            inputError['dob'] = 'date must not be more than current date and must be in form yyyymmdd'
            self.form['error'] = True


        if(DataValidator.isNull(self.form['address'])):
            inputError['address'] = 'Address is needed'
            self.form['error'] = True

        if(DataValidator.isNull(self.form['gender'])):
            inputError['gender'] = 'Gender is needed'
            self.form['error'] = True

        if(DataValidator.isNull(self.form['mobileNumber'])):
            inputError['mobileNumber'] = 'Mobile number is needed'
            self.form['error'] = True

        elif(DataValidator.ismobilecheck(self.form['mobileNumber'])):
            inputError['mobileNumber'] = 'Enter correct mobile number'
            self.form['error'] = True

        return self.form['error']

    def display(self,request, params = {}):
        return render(request, self.get_template(),{'form':self.form})

    def submit(self,request, params = {}):

        obj = self.form_to_model(User())
        self.get_service().save(obj)
        self.form['error'] = False
        self.form['message'] = 'User Registration is successfull'
        return render (request, self.get_template(), {'form': self.form})


    def get_template(self):
        return "Registration.html"

    def get_service(self):
        return UserService()

    def form_to_model(self,obj):
        pk = int(self.form['id'])

        if pk > 0:
            obj.id = pk

        obj.firstName = self.form['firstName']
        obj.lastName = self.form['lastName']
        obj.loginId = self.form['loginId']
        obj.password = self.form['password']
        obj.confirmPassword = self.form['confirmPassword']
        obj.dob = self.form['dob']
        obj.address = self.form['address']
        obj.gender = self.form['gender']
        obj.mobileNumber = self.form['mobileNumber']
        obj.roleId = self.form['roleId']
        obj.roleName = self.form['roleName']
        return obj