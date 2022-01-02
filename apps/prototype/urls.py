from django.urls import path
from .views import HomeView, CriticismView, GameView, CriticFormView, GameFormView,\
    RegisterView, LoginView, UICheckView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from core import settings

urlpatterns = [
    path("home/", HomeView.as_view()),
    path("criticism/", CriticismView.as_view()),
    path("game/", GameView.as_view()),
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("critic-form/", CriticFormView.as_view()),
    path("game-form/", GameFormView.as_view()),
    path("ui-check/", UICheckView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)