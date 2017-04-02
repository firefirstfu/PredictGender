from django.shortcuts import redirect
from django.shortcuts import render_to_response

# response only string
from django.http import HttpResponse
# response json
from django.http import JsonResponse
# until for parse serialize
from django.http import QueryDict


# import model
from .models import Gender
import os
import sys

# import mlService
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'gender_service'))
import predicter

model = predicter.get_model()


def gender_predict(request):

	if request.method == 'GET' and request.is_ajax():

		# get would to predict name from ajax
		get_data = QueryDict(request.GET['pre-name'])
		name = get_data['pre-name']
		name = name.replace(" ", "")
		print(name)

		try:
			person = Gender.objects.get(name=name)
			gender = person.gender
			num = person.predict_num
			# print('Num類型{0}'.format(type(num)))

			# update
			num += 1
			Gender.objects.filter(name=name).update(predict_num=num)

		except Exception as e:
			print(e)
			result = predicter.prediction(model, name)
			result_dic = {'male': '男', 'female': '女'}
			gender = result_dic[result]
			# save result by model
			person = Gender(name=name, gender=gender, predict_num=1)
			person.save()
			
		json_info = {'respond': gender}
		return JsonResponse(json_info)
	else:
		print('request is ok...')
		return render_to_response('gender_predict.html', locals())

