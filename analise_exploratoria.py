import pandas
import json
import requests as r
from hdfs import InsecureClient

# url = "https://api.calendario.com.br/"
# query_params = dict(json="true", cidade="SAO_PAULO", estado="SP",
#                     token="Y2FybG9zbWFydGludWNjaUBnbWFpbC5jb20maGFzaD0yNTI0Nzc5MDg")
# response = r.get(url, query_params)
# print(response.status_code)
# print(response.content)
# json.loads(response.content)


client_hdfs = InsecureClient('http://192.168.204.146:50070')
df = pandas.read_csv('BrFlights2.csv', header=1)
writer = client_hdfs.write('/dados/flights')
df.to_csv(writer)




