# -*- coding: utf-8 -*-
from django import forms
from models import *


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

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
    question = forms.IntegerField()

    # def clean_question(self):
    #     question = self.cleaned_data['question']
    #     if question is None:
    #         raise forms.ValidationError(u'Выберите вопрос')
    #     return question

    def clean_text(self):
        text = self.cleaned_data['text']
        if not len(text):
            raise forms.ValidationError(u'Введите ответ')
        return text

    def save(self):
        self.cleaned_data['question'] = Question.objects.get(id=self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.save()
        return (answer, self.cleaned_data['question'])
