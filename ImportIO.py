try: import simplejson as json
except ImportError: import json
from pprint import pprint
import re

with open("C:\\Users\\SERAPALISG\\PycharmProjects\\BlocketBilStats\\json\\20160612.json", encoding='utf8') as data_file:
    data = json.load(data_file)
    data = data['result']['extractorData']['data'] # data holds list
    data = data[0]['group'][0:] # list with all needed info
    # data_keys = data['result']['extractorData'].keys()

#pprint(data)
for x in data:
    pprint(x['Item link'])
    pprint(x['Listprice number'])
    # for z in x['Listprice number']:
    #     z = z['text']
    #     z = re.sub("[^0-9]", "", z)
    #     pprint(int(z))


#x = data
#pprint(x)


# for x in data:
#     for z in x['group']:
#         for y in z['Listprice number']:
#             #pprint(y['text'])
#             pass
