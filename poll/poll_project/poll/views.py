from django.shortcuts import render
from django.shortcuts import redirect


from .forms import CreatePollForm
from .models import Poll

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
        }
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form': form
    }
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    context = {}
    return render(request, 'poll/vote.html', context)

def results(request, poll_id):
    context = {}
    return render(request, 'poll/results.html', context)