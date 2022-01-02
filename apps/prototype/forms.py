# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class GameForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام بازی",
                "class": "form-control"
            }
        ))

    genre = forms.ChoiceField()

    price = forms.FloatField()

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "توصیحات",
                "class": "form-control"
            }
        ))

    image = forms.ImageField()


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "نظر خود را وارد کنید",
                "class": "form-control"
            }
        ))


class CriticForm(forms.Form):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "تیتر نقد",
                "class": "form-control"
            }
        ))

    score = forms.FloatField(max_value=5, min_value=0)

    game = forms.ChoiceField(
        widget=forms.Select()
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "متن",
                "class": "form-control"
            }
        ))

    image = forms.ImageField()



