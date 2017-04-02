import os
import pickle


FILE_NAME = '''names.csv'''
PICKLE_NAME = '''name_word.pickle'''

FILE_NAME = os.path.join(os.path.abspath(os.path.dirname(__file__)), FILE_NAME)
PICKLE_NAME = os.path.join(os.path.abspath(os.path.dirname(__file__)), PICKLE_NAME)



# load name.csv
def load_data():
	data_x = []
	data_y = []
	with open(FILE_NAME, 'r') as f:
	    first_line = True
	    for line in f:
	        if first_line is True:
	            first_line = False
	            continue
	        sample = line.strip().split(',')
	        if len(sample) == 2:
	            data_x.append(sample[0])
	            if sample[1] == '男':
	            	# 男
	                data_y.append([0, 1])  
	            else:
	            	# 女
	                data_y.append([1, 0])
	
    # max_name_length = max([len(name) for name in train_x])
	# print("最長名字的String: ", max_name_length)
	return data_x, data_y



# convert names.csv to word list
def convert_names_word_list():

	if os.path.exists(PICKLE_NAME):
		pickle_in = open(PICKLE_NAME, 'rb')
		pickle_data = pickle.load(pickle_in)
		return pickle_data

	else:
		data_x, data_y = load_data()
		counter = 0
		vocabulary = {}
		for name in data_x:
		    counter += 1
		    tokens = [word for word in name]
		    # print(tokens)
		    for word in tokens:
		        if word in vocabulary:
		            vocabulary[word] += 1
		        else:
		            vocabulary[word] = 1
		vocabulary_list = [' '] + sorted(vocabulary, key=vocabulary.get, reverse=True)

		# save pickle
		with open(PICKLE_NAME, 'wb') as f:
			pickle.dump(vocabulary_list, f)
		return vocabulary_list








def main():
	# name_word_list = convert_names_word_list()
	# print(name_word_list)
	print(FILE_NAME)
	print(PICKLE_NAME)



if __name__ == '__main__':
	main()






