from django.shortcuts import render
import requests
import json


def home_page(request):
	r = requests.get('https://steamkeysfunc.azurewebsites.net/api/GetUser?code=46xwD0SDkLk64p8orAYo0gdH52SiqZmbaoZPOIiyhSnbhy3cqFKOVA==&upn=8489f052-b432-4451-b081-f8780d6d4cdc')
	res = r.json()
	context = {'messages': res['messages']}
	return render(request, 'index.html', context)
