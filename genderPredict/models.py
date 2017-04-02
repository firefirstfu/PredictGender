from django.db import models



class Gender(models.Model):
	"""
	只有字串可以使用blank=True, 其餘的欄位型態要用null=True
	"""
	# 姓名
	name = models.CharField(max_length=60, blank=False)
	# 預測性別
	gender = models.CharField(max_length=10, blank=True, null=True)

	# 預測是否正確 - 布林值
	is_predict_right = models.NullBooleanField(null=True)
	# 預測次數 - 正整數
	predict_num = models.IntegerField(null=True)
	
	def __str__(self):
		return self.name






