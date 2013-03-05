# -*- coding: utf-8 -*-
from django import forms
from django.template.response import TemplateResponse
from phonenumber_field.formfields import PhoneNumberField
from models import Bouquet, Client


def load_client(request):
    try:
        return Client.objects.get(code=request.get_signed_cookie('code'))
    except:
        return


class OrderForm(forms.Form):
    bouquet_id = forms.IntegerField(widget=forms.HiddenInput())
    client_name = forms.CharField(max_length=100, required=True, label="ФИО", help_text="Ваши имя и фамилия")
    client_email = forms.EmailField(required=True, label="Email", help_text="Адресс вашей электронной почты")
    client_phone = PhoneNumberField(required=True, label="Телефон", help_text="Ваш телефон")
    date = forms.DateField(required=True, label="Дата", help_text="Дата, к которой должен быть готов букет")
    note = forms.CharField(widget=forms.Textarea, label="Примечание", help_text="Дополнительная информация к заказу.")


def home(request):
    return TemplateResponse(request, 'home.html', context=dict(
        bouquets=Bouquet.objects.all(),
    ))


def order(request, bouquet_id=None):
    bouquet = Bouquet.objects.get(id=bouquet_id) if bouquet_id else None
    return TemplateResponse(request, 'order.html', context=dict(
        bouquet=bouquet,
        active_menu='order',
    ))
