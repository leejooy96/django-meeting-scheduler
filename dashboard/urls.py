from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('schedule/view/week', views.MainView.as_view(), name='schedule_view_weekly'),
    path('meeting/<int:pk>/', views.MeetingDetailView.as_view(), name='meeting_detail'),
    path('meeting/edit/<int:pk>/', views.MeetingEditView.as_view(), name='meeting_edit'),
    path('meeting/comment/delete/', views.Comments.delete, name='comment_delete'),
    path('meeting/comment/modify/', views.Comments.modify, name='comment_modify'),
]
