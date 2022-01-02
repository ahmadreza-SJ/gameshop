# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .models import Genre, Game, Creator, User, UserType, Country, Comment, Receipt, Criticism

from django.contrib import admin


class CreatorAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "email", "founded_at", "created_at", "country"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "email", "created_at", "type"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "game", "user", "created_at"]


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ["user", "game", "paid_cost", "created_at"]


class CriticismAdmin(admin.ModelAdmin):
    list_display = ["title", "game", "critic", "created_at"]


class GameAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "release_date"]


admin.site.register(Genre)
admin.site.register(UserType)
admin.site.register(Country)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Criticism, CriticismAdmin)
