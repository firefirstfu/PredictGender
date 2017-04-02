import tensorflow as tf
from keras.models import load_model
import numpy as np
import os
import cleaner

MODEL_NAME = "./gender_model.h5"
MODEL_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), MODEL_NAME)



def setOfWords2Vec(names_word_list, inputSet):
	"""
	convert string to vector --OneHotEncoding
	"""
	returnVec = [0]*len(names_word_list)
	for word in inputSet:
		if word in names_word_list:
			returnVec[names_word_list.index(word)] = 1
	return returnVec

def convert_name_to_vector(name):
	"""
	name string to vector
	"""
	names_word_list = cleaner.convert_names_word_list()
	name_vector = setOfWords2Vec(names_word_list, name)
	name_vector = np.array(name_vector).reshape(1, len(name_vector))
	return name_vector


def get_model():
	model = load_model(MODEL_PATH)
	return model

def prediction(model=None, name=''):
	if model == None:
		return None

	name_vector = convert_name_to_vector(name)
	result = model.predict(name_vector)
	del model
	if result[0][1] > result[0][0]:
		return 'male' # 男
		# print('男')
	else:
		return 'female' # 女
		# print('女')







def main():
	test_name = '黃秋生'
	name_vector = convert_name_to_vector(test_name)
	model = get_model()
	result = model.predict(name_vector)
	del model
	if result[0][1] > result[0][0]:
		# return 'male' # 男
		print('男')
	else:
		# return 'female' # 女
		print('女')


if __name__ == '__main__':
	main()

