
import json
from cassandra.cqlengine import connection
from flask import Flask, jsonify
from flask_restful import Resource, Api
#from models.CustomerSeg import CustomerSeg
import util
import pandas as pd
import json

app = Flask(__name__)

apis = Api(app)
app.debug = True



#connection.setup(['127.0.0.1'], "customer_seg", protocol_version=3)

# def get_all():
    # customer_segs = CustomerSeg.objects().all()
    # return [customer_seg.get_data() for customer_seg in customer_segs]

	

		
	
class UserAll(Resource):
	def get(self):
		#users = CustomerSeg.objects().all()
		#user=[user.get_data() for user in users]
		df = pd.read_csv('raw_data/TestDataSet.csv')
		user = df.to_json()
		return (user)
apis.add_resource(UserAll, '/users')


class UserSearch(Resource):
	def get(self,id):
		#users = CustomerSeg.objects.all().filter(party_id=id)
		#user=[user.get_data() for user in users]
		df = pd.read_csv('raw_data/TestDataSet.csv')
		df = df[df['P_Id']==id]
		#df.drop(['Priority'], axis=1, inplace=True)
		df.drop('index',axis=1)
		print(df)
		user = df.to_dict()
		print (user)
		return (user)
apis.add_resource(UserSearch, '/users/<int:id>')


