from django.urls import path
from employers import views
urlpatterns = [
    path('vacancy-list/', views.VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy-detail/<int:pk>', views.VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy-create/', views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy-update/<int:pk>', views.VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy-delete/<int:pk>', views.VacancyDeleteView.as_view(), name='vacancy_delete'),
]