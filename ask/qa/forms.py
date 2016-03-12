# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.IntegerField(widget=forms.HiddenInput, required=False)

    def set_author(self, user):
        if user.is_authenticated():
            self.author = user
        else:
            self.author = None

    def clean_author(self):
        return self.author

    def clean_title(self):
        title = self.cleaned_data['title']
        if not len(title):
            raise forms.ValidationError(u'Поле title не должно быть пустым')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if not len(text):
            raise forms.ValidationError(u'Поле text не должно быть пустым')
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    author = forms.IntegerField(widget=forms.HiddenInput, required=False)

    def set_author(self, user):
        if user.is_authenticated():
            self.author = user
        else:
            self.author = None

    def clean_author(self):
        return self.author

    def get_user(self, user):
        if user.is_authenticated():
            self.cleaned_data['author'] = user

    def clean_question(self):
        question = Question.objects.get(id=self.cleaned_data['question'])
        if question is None:
            raise forms.ValidationError(u'Выберите вопрос')
        return question

    def clean_text(self):
        text = self.cleaned_data['text']
        if not len(text):
            raise forms.ValidationError(u'Введите ответ')
        return text

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)

    def login(self):
        user = authenticate(**self.cleaned_data)
        return user
