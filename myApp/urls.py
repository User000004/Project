from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_entry, name='new_entry'),
    path('page2/', views.show_list, name='show_list'),
    path('experiments', views.experiments, name='experiments'),
    path('experiments/<int:pk>/info/', views.experiment_info, name='experiment_info'),
    path('experiments/new', views.experiment_new, name='experiment_new'),
    path('experiments/<int:pk>/videos/new', views.video_new, name='video_new'),
    path('experiments/<int:pk>/edit', views.experiment_edit, name='experiment_edit'),
    path('experiments/<int:pk>/video/<int:pk2>/info', views.video_info, name='video_info'),
    path('experiments/<int:pk>/video/<int:pk2>/edit', views.video_edit, name='video_edit'),
]
