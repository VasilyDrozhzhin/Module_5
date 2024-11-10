import hashlib, time


class User:
	def __init__(self, nickname, password, age):
		self.nickname = nickname
		self.password = hash(password)
		self.age = age
	def __str__(self):
		return self.nickname


class Video:
	def __init__(self, title, duration, time_now=0, adult_mode=False):
		self.title = title
		self.duration = duration
		self.time_now = time_now
		self.adult_mode = adult_mode


class UrTube:
	def __init__(self):
		self.users = []
		self.videos = []
		self.current_user = None

	def log_in(self, nickname, password):
		for user in self.users:
			if user.nickname == nickname and user.password == hash(password):
				self.current_user = user

	def register(self, nickname, password, age):
		new_user = User(nickname, password, age)
		for user in self.users:
			if user.nickname == nickname:
				print(f'Пользователь {nickname} уже существует.')
				return
		self.users.append(new_user)
		UrTube.log_in(self, nickname, password)

	def log_out(self):
		self.current_user = None

	def add(self, *args):
		for i in args:
			flag = True
			for j in self.videos:
				if i.title == j.title:
					flag = False
					break
			if flag:
				self.videos.append(i)

	def get_videos(self, search):
		search_list = []
		for i in self.videos:
			if search.lower() in i.title.lower():
				search_list.append(i.title)
		return search_list

	def watch_video(self, title):
		if self.current_user == None:
			print('Войдите в аккаунт, чтобы смотреть видео')
		else:
			for i in self.videos:
				if title == i.title:
					if self.current_user.age < 18 and i.adult_mode:
						print('Вам нет 18 лет, пожалуйста покиньте страницу')
					else:
						current_time = 1
						while current_time <= i.duration:
							print(current_time)
							time.sleep(1)
							current_time += 1
						print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)


print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
