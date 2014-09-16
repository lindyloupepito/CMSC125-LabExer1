# your code goes here
import threading
import Queue
from random import randint

class MPExercise:
	def __init__(self):
		self.num_of_resources = randint(1, 30)
		self.num_of_users = randint(1, 30)
		print self.num_of_users
		users = []
		for i in range(self.num_of_users):
			users.append("User" + str(i+1))
			
		print users


if __name__ == '__main__':	
	MP = MPExercise()
