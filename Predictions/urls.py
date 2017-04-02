from django.conf.urls import url
from django.contrib import admin


from genderPredict.views import gender_predict
from weatherPredict.views import weather_predict



urlpatterns = [
    url(r'^backend/admin/', admin.site.urls),

    # 天氣預測
    # url(r'^predict/weather/$', weather_predict),
    # 姓名預測性別
    url(r'^predict/gender/$', gender_predict),
]
