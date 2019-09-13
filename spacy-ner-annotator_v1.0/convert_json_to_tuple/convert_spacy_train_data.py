import sys, os
from os import listdir
from os.path import isfile, join, isdir
import json

INPUT = "/home/klaus/area_trabalho/claro_filesPOC/all_files_txt_no_line_break/criminal_consumo/"

#filename = input("Enter your train data filename : ")
#print(filename)

for r, d, f in os.walk(INPUT):
    for _file in f:
		if '.json' in _file:
			print(_file)
			# filename = os.path.join(r, file)
			# print(filename)   
			# with open(filename, 'r') as train_data:
			# 	train = json.load(train_data)

			# TRAIN_DATA = []
			# for data in train:
			# 	_d = ""
			# 	ents = [tuple(entity) for entity in data['entities']]
			# 	_data = (data['content'],{'entities':ents})
			# 	TRAIN_DATA.append(_data)

			# 	_d = '[(\"'
				
			# 	_d += str(data['content']).replace('\'', ' ')

			# 	_d += "\", {\'entities\': "

			# 	_d += str(ents)

			# 	_d += "})]"

			# #with open('{}'.format(filename.replace('json','txt')),'w') as write:
			# #	write.write(str(_d))


			# 	print('-------------Copy and Paste to spacy training-------------')
			# 	print()
			# 	print()
			# 	print()
			# 	print(_d)
			# 	print()
			# 	print()
			# 	print()
			# 	print('--------------------------End-----------------------------')