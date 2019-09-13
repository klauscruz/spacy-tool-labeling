import sys, os
from os import listdir
from os.path import isfile, join, isdir
import json

#INPUT = "/home/klaus/area_trabalho/claro_filesPOC/all_files_txt_no_line_break/ip/"

#INPUT = "/home/klaus/area_trabalho/aprendizado_cob/klaus/"
#INPUT = "/home/klaus/area_trabalho/aprendizado_cob/fernando/"
#INPUT = "/home/klaus/area_trabalho/aprendizado_cob/paulo/"
#INPUT = "/home/klaus/area_trabalho/aprendizado_cob/GA/" 
INPUT = "/home/klaus/area_trabalho/aprendizado_cob/teste/"


#_d = '['
_d = ""
for r, d, f in os.walk(INPUT):
    for file in f:
        if '.json' in file:
            print(file)
            filename = os.path.join(r, file)
            print(filename)
            with open(filename, 'r') as train_data:
                train = json.load(train_data)
            
            TRAIN_DATA = []
            
            
            for data in train:
                #_d = ""
                ents = [tuple(entity) for entity in data['entities']]
                _data = (data['content'],{'entities':ents})
                TRAIN_DATA.append(_data)
                
                _d += '(\"'
                
                _d += str(data['content']).replace('\'', ' ').replace('\"', ' ')

                _d += "\", {\'entities\': "

                _d += str(ents)

                _d += "})"
                #_d += ","
                _d += "\n"


                # print('-------------Copy and Paste to spacy training-------------')
                # print()
                # print()
                # print(_d)
                # print()
                # print()
                # print('--------------------------End-----------------------------')

#_d += "]"

print(_d)
