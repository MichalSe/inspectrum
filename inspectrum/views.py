from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from inspectrum.forms import SignUpForm, LoginForm
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, QueryDict
from django.views import View
from inspectrum.models import *
import json
import pytz


# Create your views here.

#
# def db(request):
#
#     greeting = Greeting()
#     greeting.save()
#
#     greetings = Greeting.objects.all()
#
#     return render(request, 'db.html', {'greetings': greetings})


def home(request):
    return render(request, 'base.html')


@login_required
def inspectrum(request):
    return render(request, 'inspectrum.html')


def verified(request):
    if request.user.is_authenticated:
        return JsonResponse({"verified": True})
    else:
        return JsonResponse({"verified": False})



class StatesPerUserView(View):
    # returns a query set of all states belonging to a user
    def get(self, request, url):
        try:
            if request.user.is_authenticated:
                # Do something for logged-in users.
                states = States.objects.filter(owner_id=request.user.id, url=url).order_by('date_created')
                state_list = []
                for state in states:
                    state_list.append({'id': state.name, 'css': state.css_code})
                states_json = json.dumps(state_list)
                return JsonResponse({"states": states_json, "user": request.user.id})
            else:
                # Do something for anonymous users.
                return JsonResponse({"error": "not logged in"})
        except Exception as e:
                print("%s (%s)" % (e.message, type(e)))
                return HttpResponse(status=400)

    def post(self, request, url):
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                state_name = body['id']
                css = body['css']
                #todo add followers later on
                state, created = States.objects.get_or_create(owner_id=request.user.id, url=url, name=state_name)
                state.css_code = css
                state.date_created = datetime.now(tz=pytz.utc)
                state.save()

                response = JsonResponse({"updated": "true"})
                response['Access-Control-Allow-Origin'] = '*'
                response["Access-Control-Allow-Methods"] = "POST, GET"
                response["'Access-Control-Allow-Credentials"] = "true"
                response["Access-Control-Allow-Headers"] = "x-requested-with"
                return response
            except Exception as e:
                print("%s (%s)" % (e.message, type(e)))
                return HttpResponse(status=400)

    def delete(self, request, url): #TODO check delete
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            state = body['data']
            state_to_remove = States.objects.filter(owner_id=request.user.id, url=url, name=state.name)
            States.remove(state_to_remove)
            return JsonResponse({"deleted": "true"})
        except Exception as e:
                print("%s (%s)" % (e.message, type(e)))
                return HttpResponse(status=400)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.team_id = form.cleaned_data.get('team_id')
            user.username = user.email
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('inspectrum')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_success(request):
    return render(request, 'registration/login_success.html')
