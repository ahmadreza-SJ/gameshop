
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Creator(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    founded_at = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)

    def __str__(self):
        return self.username


class Game(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    release_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)
    image = models.ImageField()
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)
    type = models.ForeignKey(UserType, on_delete=models.RESTRICT)

    def __str__(self):
        return self.username


class Comment(models.Model):
    text = models.CharField(max_length=500, null=False, blank=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)

    def __str__(self):
        return "{user} - {game} - {text}".format(text=self.text, game=self.game, user=self.user)


class Receipt(models.Model):
    paid_cost = models.IntegerField(null=False, blank=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)

    def __str__(self):
        return "{user} - {game}".format(game=self.game, user=self.user)


class Criticism(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    text = models.CharField(max_length=5000, null=False, blank=False)
    score = models.IntegerField(null=False, blank=False)
    image = models.ImageField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)

    def __str__(self):
        return self.title
