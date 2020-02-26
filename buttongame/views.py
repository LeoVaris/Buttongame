from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django import forms

import datetime
import uuid
import operator

number = 1

leaderboard = []

def button_press(request):
	global number
	coins = 20
	if request.method == "GET":
		if 'coins' in request.COOKIES:
			coins = int(request.COOKIES['coins'])
			print("Got coin count: " + str(coins))
	coins -= 1
	number += 1
	dst_to_win = 10 - (number % 10)
	if number % 10 == 0:
		if number % 500 == 0:
			coins += 250
			response = render(request, 'wintemplate.html', {'coins': coins, 'win_amount': 250})
		elif number % 100 == 0:
			coins += 40
			response = render(request, 'wintemplate.html', {'coins': coins, 'win_amount': 40})
		else:
			coins += 5
			response = render(request, 'wintemplate.html', {'coins': coins, 'win_amount': 5})
	else:
		if coins == 0:
			response = render(request, 'nocoins.html', {'to_next': dst_to_win})
		else:
			response = render(request, 'nowin.html', {'coins': coins, 'to_next': dst_to_win})
	response.set_cookie('coins', coins)
	return response


def homepage(request):
	global number
	global leaderboard
	coins = 20
	idn = None
	if request.method == "GET":
		if 'coins' in request.COOKIES:
			coins = request.COOKIES['coins']
		if 'id' in request.COOKIES:
			idn = request.COOKIES['id']
	elif request.method == "POST":
		if 'coins' in request.COOKIES:
			coins = request.COOKIES['coins']
		if 'id' in request.COOKIES:
			idn = request.COOKIES['id']
		if idn != None:
			print("idn1: " + idn)
		else:
			print("idn1 not def")
		if idn == None:
			idn = uuid.uuid1()
		if idn != None:
			print("idn2: " + str(idn))
		else:
			print("idn2 not def")
		name_form = AddName(request.POST)
		if name_form.is_valid():
			name = str(name_form.cleaned_data['new_name'])
			player = Player(coins, name, idn)
			if player in leaderboard:
				print("should remove")
				leaderboard.remove(player)
				leaderboard.append(player)
			else:
				print("wrong path")
				leaderboard.append(player)
		response = HttpResponseRedirect('/')
		response.set_cookie('id', idn)
		return response
	if int(coins) == 0:
		coins = 20
	form = AddName()
	leaderboard.sort(key=operator.attrgetter('hs'))
	leaderboard.reverse()
	response = render(request, 'index.html', {'coins': coins, 'number': number, 'name_form': form, 'id': idn, 'ldb': leaderboard[:5]})
	response.set_cookie('coins', coins)
	return response


def admin(request):
	global number
	coins = 20
	if request.method == 'POST':
		counter_form = ChangeNumber(request.POST)
		coin_form = ChangeCoinCount(request.POST)
		if counter_form.is_valid():
			new_number = int(counter_form.cleaned_data['new_number'])
			if new_number >= 0:
				number = new_number
		if coin_form.is_valid():
			new_value = int(coin_form.cleaned_data['new_value'])
			if new_value >= 0:
				response = HttpResponseRedirect('/superadmin')
				response.set_cookie('coins', new_value)
				return response
		return HttpResponseRedirect('/superadmin')
	else:
		counter_form = ChangeNumber()
		coin_form = ChangeCoinCount()
		coins = request.COOKIES['coins']

	response = render(request, 'adminfile.html', 
		{'number': number, 'coins': coins, 'counter_form': counter_form, 'coin_form': coin_form})
	return response
	
class Player():
	def __init__(self, hscore, name, idn):
		self.hs = hscore
		self.name = name
		self.idn = idn

	def __eq__(self, other):
		return str(self.idn) == str(other.idn)



class ChangeNumber(forms.Form):
    new_number = forms.IntegerField(label="Uusi arvo")

class ChangeCoinCount(forms.Form):
	new_value = forms.IntegerField(label="Uusi arvo")

class AddName(forms.Form):
	new_name = forms.CharField(label="Nimi", max_length=20)