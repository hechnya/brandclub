# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/')

def login_view(request,template_name="core/login.html"):
    if request.user.is_authenticated():

        return HttpResponseRedirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # url = request.session['last_url']
                # del request.session['last_url']
                return HttpResponseRedirect('/account')

        else:
            message = u'неправильно введен логин или пароль! Попробуйте еще раз'


    # return  HttpResponseRedirect('/login')
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))