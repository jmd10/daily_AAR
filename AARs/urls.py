''' Defines URL patterns for AARs app '''

from django.urls import path

from . import views

app_name = 'AARs'

urlpatterns = [
    # Home Page
    path('', views.index, name ='index'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding new actions to review
    path('new_action/<int:topic_id>/', views.new_action, name = 'new_action'),

    # Page for editing an entry
    path('edit_action/<int:action_id>/', views.edit_action,
        name='edit_action'),

]
