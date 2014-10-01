from random import randint

num_of_resources = randint(1, 30)
num_of_users = randint(1, 30)

class Resource:
	def __init__(self, id):
		self.ID = id
		self.users_list = []
		self.is_available = True
		self.current_user = None

class User:
	def __init__(self, id):
		self.ID = id
		self.resource_num = randint(1, num_of_resources)
		self.time = randint(1, 30)

class Real_Time_System:
	def __init__(self):
		self.resources = []
		for i in range(num_of_resources):
			self.resources.append(Resource(i+1))

		self.users = []
		for i in range(num_of_users):
			self.users.append(User(i+1))

		for user in self.users:
			for resource in self.resources:
				if user.resource_num == resource.ID:
					resource.users_list.append(user)

		print "Resource - (User ID, Time to use resource)"
		for resource in self.resources:
			print resource.ID, "-", 
			for user in resource.users_list:
				print "(", user.ID, "," , user.time, ")",
			print ""
		print ""

	def run_system(self):
		all_available = False
		time_step = 1

		while not all_available:
			print "TIME", time_step, "\n"
			for resource in self.resources:
				print "Resource no. \t\t\t\t", resource.ID
				if resource.is_available:
					if len(resource.users_list) > 0:
						user = resource.users_list[0]
						resource.users_list.remove(user)
						resource.current_user = user
						resource.is_available = False
						print "Current user (User ID)\t\t", resource.current_user.ID
						print "Time left for this user\t\t", resource.current_user.time
						if len(resource.users_list) > 0:
							print "User Requests (ID, waiting time)\t"
							time = resource.current_user.time
							for user in resource.users_list:
								print "\t- (", user.time, ",", time, ")"
								time += user.time
							print "Processing time remaining\t", time
						print "Status\t\t\t\t\t\tIn use"
					else:
						print "Status\t\t\t\t\t\tAvailable\n",
				else:
					resource.current_user.time -= 1
					print "Current user (User ID)\t\t", resource.current_user.ID
					print "Time left for this user\t\t", resource.current_user.time
					if len(resource.users_list) > 0:
						print "User Requests (ID, waiting time)\t"
						time = resource.current_user.time
						for user in resource.users_list:
							print "\t- (", user.time, ",", time, ")"
							time += user.time
						print "Processing time remaining\t", time
					if resource.current_user.time == 0:
						resource.is_available = True
						print "Status\t\t\t\t\t\tAvailable\n",
					else:
						print "Status\t\t\t\t\t\tIn use"

				print "\n"

			time_step += 1
			print "_______________________________________________"
			print ""

			for resource in self.resources:
				if not resource.is_available or len(resource.users_list) > 0:
					break
				elif (resource.ID) == len(self.resources):
					all_available = True



rst = Real_Time_System()
rst.run_system()
