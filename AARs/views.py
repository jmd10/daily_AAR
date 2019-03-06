from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Actions
from .forms import TopicForm, ActionForm

def index(request):
    ''' The home page for After Action Reports (AARs) '''
    return render(request, 'AARs/index.html')

def topics(request):
    ''' shows all topics '''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'AARs/topics.html', context)

def topic(request, topic_id):
    '''Show a single topic and all its entries '''
    topic = Topic.objects.get(id=topic_id)
    actions = topic.actions_set.order_by('-date_added')
    context = {'topic': topic, 'actions': actions}
    return render(request, 'AARs/topic.html', context)

def new_topic(request):
    """ Add a new topic """
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm
    else:
        # POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('AARs:topics'))
    context = {'form': form}
    return render(request, 'AARs/new_topic.html', context)


def new_action(request, topic_id):
    """ Add a new action to review """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = ActionForm()
    else:
        # POST data submitted; process data
        form = ActionForm(data=request.POST)
        if form.is_valid():
            new_action = form.save(commit=False)
            new_action.topic = topic
            new_action.save()
            return HttpResponseRedirect(reverse('AARs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'AARs/new_action.html', context)

def edit_action(request, action_id):
    ''' Edit an existing action entry '''
    action = Actions.objects.get(id=action_id)
    topic = action.topic

    if request.method != 'POST':
        # Initial request. Pre-fill form with current action
        form = ActionForm(instance=action)
    else:
        # POST data submitted, process data
        form = ActionForm(instance=action, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('AARs:topic', args=[topic.id]))
    context = {'action':action, 'topic':topic, 'form': form}
    return render(request, 'AARs/edit_action.html', context)
