class User:
    def __init__(self, name, birthday, fav_singer, fav_colour, topics, blogs):
        self.name = name
        self.birthday = birthday
        self.fav_singer = fav_singer 
        self.fav_colour = fav_colour
        self.blogs: list = blogs 