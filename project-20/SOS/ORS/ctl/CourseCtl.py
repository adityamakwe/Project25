from django.shortcuts import render
from django.http import HttpResponse

from .BaseCtl import BaseCtl
from ..models import College, Course
from ..service.CourseService import CourseService
from ..utility.DataValidator import DataValidator


class CourseCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['name'] = requestForm['name']
        self.form['description'] = requestForm['description']
        self.form['duration'] = requestForm['duration']

    def form_to_model(self, obj):

        pk = int(self.form['id'])

        if pk > 0:
            obj.id = pk
        obj.name = self.form['name']
        obj.description = self.form['description']
        obj.duration = self.form['duration']

        return obj

    def model_to_form(self, obj):

        if obj == None:
            return

        self.form['name'] = obj.name
        self.form['description'] = obj.description
        self.form['duration'] = obj.duration

    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']
        if DataValidator.isNull(self.form['name']):
            inputError['name'] = "Course Name can not be null"
            self.form['error'] = True

        else:
            if DataValidator.isalphacehck(self.form['name']):
                inputError['name'] = "Course Name considers only letters"
                self.form['error'] = True

        if DataValidator.isNull(self.form['description']):
            inputError['description'] = "Description can not be null"
            self.form['error'] = True

        else:
            if DataValidator.isalphacehck(self.form['description']):
                inputError['description'] = "Description only letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['duration'])):
            inputError['duration'] = "Duration can not be null"
            self.form['error'] = True

        return self.form['error']

    def submit(self, request, params={}):

        r = self.form_to_model(Course())
        self.get_service().save(r)
        self.form['message'] = False
        self.form['message'] = "Course saved successfully"
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "Course.html"

    def get_service(self):
        return CourseService()
