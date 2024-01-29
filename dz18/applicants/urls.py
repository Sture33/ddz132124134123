from django.urls import path
from applicants import views
urlpatterns = [
    path('resume-list/', views.ResumeListView.as_view(), name='resume_list'),
    path('resume-detail/<int:pk>', views.ResumeDetailView.as_view(), name='resume_detail'),
    path('resume-create/', views.ResumeCreateView.as_view(), name='resume_create'),
    path('resume-update/<int:pk>', views.ResumeUpdateView.as_view(), name='resume_update'),
    path('resume-delete/<int:pk>', views.ResumeDeleteView.as_view(), name='resume_delete'),
]