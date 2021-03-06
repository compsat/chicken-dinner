from django.urls import path, include
from rest_framework import routers
from project.user import views

router = routers.DefaultRouter()
router.register('citizens', views.CitizenViewSet)
router.register('users', views.UserViewSet)
router.register('preferences', views.PreferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all/', views.CitizenList.as_view()),
    path('<int:pk>/', views.CitizenDetail.as_view()),
    path('create/', views.create),
    # path('1/', views.CitizenPref.as_view())
]
