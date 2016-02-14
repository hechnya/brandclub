#-*- coding: utf-8 -*-
from django.forms import ModelForm,Form
from django import forms
from authentication import models



class AccountForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {'placeholder':'Ваш email', 'class':'form-control'}
        self.fields['username'].widget.attrs = {'placeholder':'Имя пользователя', 'class':'form-control'}
        self.fields['password'].widget.attrs = {'placeholder':'Придумайте пароль', 'class':'form-control'}
        self.fields['first_name'].widget.attrs = {'placeholder':'Ваше Имя', 'class':'form-control'}
        self.fields['last_name'].widget.attrs = {'placeholder':'Ваша Фамилия', 'class':'form-control'}
        self.fields['zip'].widget.attrs = {'placeholder':'Индекс', 'class':'form-control'}
        self.fields['city'].widget.attrs = {'placeholder':'Город', 'class':'form-control'}
        self.fields['address'].widget.attrs = {'placeholder':'Адрес', 'class':'form-control'}
        self.fields['phone'].widget.attrs = {'placeholder':'Телефон', 'class':'form-control'}

    class Meta:
        model = models.Account
        fields = [
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
            'zip',
            'city',
            'address',
            'phone'
        ]
        labels = {
            "email": u"",
            "username": u"",
            "password": u"",
            "first_name": u"",
            "last_name": u"",
            "zip": u"",
            "city": u"",
            "address": u"",
            "phone": u"",
        }

class PureAccountForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PureAccountForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {'placeholder':'Ваше Имя', 'class':'form-control'}
        self.fields['last_name'].widget.attrs = {'placeholder':'Ваше Фамилия', 'class':'form-control'}
        self.fields['zip'].widget.attrs = {'placeholder':'Ваш Индекс', 'class':'form-control'}
        self.fields['city'].widget.attrs = {'placeholder':'Ваш Город', 'class':'form-control'}
        self.fields['address'].widget.attrs = {'placeholder':'Ваш Адрес', 'class':'form-control'}
        self.fields['phone'].widget.attrs = {'placeholder':'Ваш Телефон', 'class':'form-control'}

    class Meta:
        model = models.Account
        fields = [
            'first_name',
            'last_name',
            'zip',
            'city',
            'address',
            'phone'
        ]
        labels = {
            "first_name": u"Ваше Имя",
            "last_name": u"Ваша Фамилия",
            "zip": u"Индекс",
            "city": u"Город",
            "address": u"Адрес",
            "phone": u"Телефон",
        }


class DeliveryForm(Form):
    REGIONS = [('АБАКАН', 'АБАКАН'),  ('АНАДЫРЬ', 'АНАДЫРЬ'),  ('АРХАНГЕЛЬСК', 'АРХАНГЕЛЬСК'),  ('АСТРАХАНЬ', 'АСТРАХАНЬ'), ('БАРНАУЛ', 'БАРНАУЛ'),  ('БЕЛГОРОД', 'БЕЛГОРОД'),  ('БИРОБИДЖАН', 'БИРОБИДЖАН'),  ('БЛАГОВЕЩЕНСК', 'БЛАГОВЕЩЕНСК'),  ('БРЯНСК', 'БРЯНСК'),  ('ВЕЛИКИЙ НОВГОРОД', 'ВЕЛИКИЙ НОВГОРОД'),  ('ВЛАДИВОСТОК', 'ВЛАДИВОСТОК'),  ('ВЛАДИКАВКАЗ', 'ВЛАДИКАВКАЗ'),  ('ВЛАДИМИР', 'ВЛАДИМИР'),  ('ВОЛГОГРАД', 'ВОЛГОГРАД'),  ('ВОЛОГДА', 'ВОЛОГДА'),  ('ВОРОНЕЖ', 'ВОРОНЕЖ'),  ('ГОРНО-АЛТАЙСК', 'ГОРНО-АЛТАЙСК'),  ('ГРОЗНЫЙ', 'ГРОЗНЫЙ'),  ('ЕКАТЕРИНБУРГ', 'ЕКАТЕРИНБУРГ'),  ('ИВАНОВО', 'ИВАНОВО'),  ('ИЖЕВСК', 'ИЖЕВСК'),  ('ИРКУТСК', 'ИРКУТСК'), ('ЙОШКАР-ОЛА', 'ЙОШКАР-ОЛА'), ('КАЗАНЬ', 'КАЗАНЬ'), ('КАЛИНИНГРАД', 'КАЛИНИНГРАД'),  ('КАЛУГА', 'КАЛУГА'),  ('КЕМЕРОВО', 'КЕМЕРОВО'),  ('КИРОВ', 'КИРОВ'),  ('КОСТРОМА', 'КОСТРОМА'),  ('КРАСНОДАР', 'КРАСНОДАР'),  ('КРАСНОЯРСК', 'КРАСНОЯРСК'),  ('КУРГАН', 'КУРГАН'),  ('КУРСК', 'КУРСК'),  ('КЫЗЫЛ', 'КЫЗЫЛ'),  ('ЛИПЕЦК', 'ЛИПЕЦК'),  ('МАГАДАН', 'МАГАДАН'),  ('МАЙКОП', 'МАЙКОП'),  ('МАХАЧКАЛА', 'МАХАЧКАЛА'),  ('МОСКВА', 'МОСКВА'),  ('МУРМАНСК', 'МУРМАНСК'),  ('НАЗРАНЬ', 'НАЗРАНЬ'),  ('НАЛЬЧИК', 'НАЛЬЧИК'),  ('НАРЬЯН-МАР', 'НАРЬЯН-МАР'),  ('НИЖНИЙ НОВГОРОД', 'НИЖНИЙ НОВГОРОД'),  ('НОВОСИБИРСК', 'НОВОСИБИРСК'),  ('ОМСК', 'ОМСК'),  ('ОРЕНБУРГ', 'ОРЕНБУРГ'),  ('ОРЁЛ', 'ОРЁЛ'),  ('ПЕНЗА', 'ПЕНЗА'),  ('ПЕРМЬ', 'ПЕРМЬ'),  ('ПЕТРОЗАВОДСК', 'ПЕТРОЗАВОДСК'),  ('ПЕТРОПАВЛОВСК-КАМЧАТСКИЙ', 'ПЕТРОПАВЛОВСК-КАМЧАТСКИЙ'),  ('ПСКОВ', 'ПСКОВ'),  ('РОСТОВ-НА-ДОНУ', 'РОСТОВ-НА-ДОНУ'),  ('РЯЗАНЬ', 'РЯЗАНЬ'),  ('САЛЕХАРД', 'САЛЕХАРД'),  ('САМАРА', 'САМАРА'),  ('САНКТ-ПЕТЕРБУРГ', 'САНКТ-ПЕТЕРБУРГ'),  ('САРАНСК', 'САРАНСК'),  ('САРАТОВ', 'САРАТОВ'),  ('СИМФЕРОПОЛЬ', 'СИМФЕРОПОЛЬ'),  ('СМОЛЕНСК', 'СМОЛЕНСК'),  ('СТАВРОПОЛЬ', 'СТАВРОПОЛЬ'),  ('СЫКТЫВКАР', 'СЫКТЫВКАР'),  ('ТАМБОВ', 'ТАМБОВ'),  ('ТВЕРЬ', 'ТВЕРЬ'),  ('ТОМСК', 'ТОМСК'),  ('ТУЛА', 'ТУЛА'),  ('ТЮМЕНЬ', 'ТЮМЕНЬ'),  ('УЛАН-УДЭ', 'УЛАН-УДЭ'),  ('УЛЬЯНОВСК', 'УЛЬЯНОВСК'),  ('УФА', 'УФА'),  ('ХАБАРОВСК', 'ХАБАРОВСК'),  ('ХАНТЫ-МАНСИЙСК', 'ХАНТЫ-МАНСИЙСК'),  ('ЧЕБОКСАРЫ', 'ЧЕБОКСАРЫ'),  ('ЧЕЛЯБИНСК', 'ЧЕЛЯБИНСК'),  ('ЧЕРКЕССК', 'ЧЕРКЕССК'),  ('ЧИТА', 'ЧИТА'),  ('ЭЛИСТА', 'ЭЛИСТА'),  ('ЮЖНО-САХАЛИНСК', 'ЮЖНО-САХАЛИНСК'),  ('ЯКУТСК', 'ЯКУТСК'),  ('ЯРОСЛАВЛЬ', 'ЯРОСЛАВЛЬ'),]
    region = forms.ChoiceField(choices=REGIONS, widget=forms.Select(attrs={'class': 'set_region'}))


