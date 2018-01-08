from locust import HttpLocust, TaskSet, task
import uuid
from datetime import datetime
import json
import csv

headers={'Content-Type' : "application/json"}

#Dynamic requests
#my_file = open('<file.csv>', 'r')

#def get_coupon():
#	return my_file.readline()

def newdict():
#	code = get_coupon()
	req = {
		#Dict
	}
	return req

class Tasks(TaskSet):
	@task()
	def redeemption(self):
		req = newdict()
		self.client.post("</api/>", data=json.dumps(req), headers=headers)

class Tasks(HttpLocust):
	task_set = Tasks
	min_wait = 5000
	max_wait = 9000
