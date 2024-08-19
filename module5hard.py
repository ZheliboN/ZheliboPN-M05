import time


class User:
    """
    Класс пользователя, содержащие атрибуты:
    :param nickname: - имя пользователя
    :param password: - пароль
    :param age: - возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname and self.password == other.password and self.age == other.age

    def __str__(self):
        #Для вывода полных характеристих пользователя:
        #s = f'Пользователь:\n имя пользователя = {self.nickname}\n пароль = {self.password}\n возраст = {self.age}'
        #вывод только имени
        return self.nickname

    def __repr__(self):
        s = f'Класс: {self.__class__}, имя пользователя: {self.nickname}, пароль: {self.password}, возраст: {self.age}'
        return s


class Video:
    """
    Класс видео, содержащие атрибуты:
    :param title: - заголовок
    :param duration: - продолжительность, секунды
    :param time_now: - секунда остановки
    :param adult_mode: - ограничение по возрасту
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title and self.duration == other.duration and self.adult_mode == other.adult_mode

    def __str__(self):
        s = (f'Видео:\n заголовок = {self.title}\n продолжительность = {self.duration}\n '
             f'ограничение по возрасту = {self.adult_mode}')
        return s

    def __repr__(self):
        s = (f'Класс: {self.__class__}, заголовок: {self.title}, продолжительность: {self.duration} ' 
             f'ограничение по возрасту: {self.adult_mode}')
        return s


class UrTube:
    users = []
    videos = []

    def __init__(self):
        self.curent_user = None

    def add(self, *video):
        for vid in video:
            if isinstance(vid, Video):
                if not (vid in self.videos):
                    self.videos.append(vid)

    def log_in(self, nickname, password):
        find_user = False
        for user in self.users:
            if user.nickname == nickname:
                find_user = True
                if user.password == hash(password):
                    self.curent_user = user
                    break
                else:
                    print('Введен не верный пароль. Повторите ввод')
        if not find_user:
            print(f'Пользователь с именем {nickname} не найден. Пройдите регистрацию.')

    def register(self, nickname, password, age):
        finduser = False
        for user in self.users:
            if user.nickname != nickname:
                continue
            else:
                finduser = True
                print(f'Пользователь {nickname} уже существует')
                break
        if not finduser:
            user = User(nickname, password, age)
            self.users.append(user)
            self.curent_user = user

    def log_out(self):
        self.curent_user = None

    def get_videos(self, findstr):
        find_list = []
        for video in self.videos:
            if str.upper(findstr) in str.upper(video.title) or str.upper(findstr) == str.upper(video.title):
                find_list.append(video.title)
        return find_list

    def watch_video(self, title_video):
        def play_video(playing_video):
            print(f'Просмотр видео: {playing_video.title}')
            if playing_video.adult_mode:
                print('Возрастные ограничения 18+')
            for secund in range(playing_video.time_now, playing_video.duration+1):
                print(secund, end=" "),
                time.sleep(1)
            print('Конец видео')
            playing_video.time_now = 0

        index_video = 0
        find_video = False
        if self.curent_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if video.title == title_video:
                    find_video = True
                    break
                index_video += 1
            if find_video:
                if self.videos[index_video].adult_mode:
                    if self.curent_user.age >= 18:
                        play_video(self.videos[index_video])
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                else:
                    play_video(self.videos[index_video])


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 18)
v2 = Video('Для чего девушкам парень программист?', duration=10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.curent_user)
ur.watch_video('Лучший язык программирования 2024 года!')
ur.log_in('vasya_pupkin', 'lolkekchebur')
print(ur.curent_user)
ur.log_in('vasya_pukin', 'lolkekcheburek')
ur.log_out()
ur.watch_video('Лучший язык программирования 2024 года')
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Лучший язык программирования 2024 года')
print(ur.curent_user)
