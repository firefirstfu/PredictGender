# response and template
from django.shortcuts import render_to_response
# 重導向
from django.shortcuts import redirect


# response only string
from django.http import HttpResponse
# response json
from django.http import JsonResponse
# until for parse serialize
from django.http import QueryDict


# utils library
from bs4 import BeautifulSoup
import requests
import lxml



def weather_predict(request):


	if request.method == 'GET' and request.is_ajax():

		post_data = QueryDict(request.GET['city'])
		city = post_data['city']
		# clear work blank
		city = city.replace(" ", "")

		# weather API
		weather = get_weather_from_api(city)
		json_info = {'respond': weather};
		return JsonResponse(json_info)
	else:
		return render_to_response('weather_predict.html', locals())




# weather API
def get_weather_from_api(city=''):
	

	url = 'http://www.weather-forecast.com/locations/{city}/forecasts/latest'
	res = requests.get(url.format(city=city))
	soup = BeautifulSoup(res.text, 'lxml')
	# weather prediction
	predict_weather = soup.select('.phrase')
	try:
		predict_weather = predict_weather[0].text
	except Exception as e:
		predict_weather = 'error input'
	
	print(predict_weather)
	return predict_weather


















