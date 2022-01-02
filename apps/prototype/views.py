from django.shortcuts import render
from django.views import View
from .forms import CriticForm, GameForm, CommentForm


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, template_name="my_project/home.html")


class CriticismView(View):
    def get(self, request):
        return render(request, "my_project/criticism.html")


class GameView(View):

    def get(self, request):
        form = CommentForm(request.POST or None)

        return render(request, "my_project/game.html", {"form": form})


class RegisterView(View):
    def get(self, request):
        return render(request, "my_project/register.html")


class LoginView(View):
    def get(self, request):
        return render(request, "my_project/login.html")


class UICheckView(View):
    def get(self, request):
        return render(request, template_name="home/ui-forms.html")


class CriticFormView(View):

    def get(self, request):
        form = CriticForm(request.POST or None)

        return render(request, "my_project/critic-form.html", {"form": form})


class GameFormView(View):

    def get(self, request):
        form = GameForm(request.POST or None)

        return render(request, "my_project/game-form.html", {"form": form})
