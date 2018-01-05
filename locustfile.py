from locust import HttpLocust, TaskSet, task
import uuid
from datetime import datetime
import json
import csv

headers={'Content-Type' : "application/json"}

item_array = []

with open('<csv file.csv>') as my_file:
	for line in my_file:
		item_array.append(line)

def newdict():
	try:
		code = item_array.pop()
		request = {
		   'dictionary':'1'
		}
		return request
	except Exception as e:
		print("Code Over !!")


class Tasks(TaskSet):
	@task()
	def redeemption(self):
		request = newdict()
		try:
			self.client.post("<api/ /path>", data=json.dumps(request), headers=headers)
		except Exception as e:
			print("Code Over !!")

class Tasks(HttpLocust):
	task_set = Tasks
	min_wait = 5000
	max_wait = 9000
