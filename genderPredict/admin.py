from django.contrib import admin
from .models import Gender



# 自定義model admin顯示方式
class GenderAdmin(admin.ModelAdmin):
	list_display = ('name', 'gender', 'predict_num')

# register admin model
admin.site.register(Gender, GenderAdmin)
