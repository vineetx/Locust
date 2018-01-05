from locust import HttpLocust, TaskSet, task

request = {
    Dictionay
}

class Tasks(TaskSet):
	def on_start(self):
		self.login()

	def login(self):
		self.client.post("/login", {'username': '<>', 'password': '<>'})

	def redeemption(self):
		self.client.post("api", req)

class Tasks(HttpLocust):
	task_set = Tasks
	min_wait = 5000
	max_wait = 9000
