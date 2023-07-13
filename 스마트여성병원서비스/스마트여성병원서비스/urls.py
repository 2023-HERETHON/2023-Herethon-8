from django.contrib import admin
from django.urls import path, include
from qnas.views import question_view, detail, question_create
from qnas import views

app_name = 'qnas'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question_write/question_list/', question_view),
    path('question_list/question/<int:question_id>/', views.detail, name='detail'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question_write/', views.question_create, name='question_write'),
    path('question_list/', views.question_view, name = 'question_view')
]