from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_POST
from django.contrib import auth
from models import Question
from forms import AskForm, AnswerForm, SignUpForm


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def index(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    questions = Question.objects.order_by('-added_at')
    paginator = Paginator(questions, 10)
    paginator.baseURL = reverse('index') + "?page="
    page = paginator.page(page)
    return render_to_response('questions_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    questions = Question.objects.order_by('-rating')
    paginator = Paginator(questions, 10)
    paginator.baseURL = reverse('popular') + "?page="
    page = paginator.page(page)
    return render_to_response('questions_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question(request, quest_id):
    quest = get_object_or_404(Question, id=quest_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form.set_author(request.user)
        if form.is_valid():
            post = form.save()
    else:
        form = AnswerForm()
    return render(request, "question_detail.html", {'question': quest, 'form': form})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form.set_author(request.user)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(post.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


@require_POST
def answer(request, quest):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(quest.get_url())


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            needs_login = login(request)
            if needs_login:
                return needs_login
            # username = request.POST['username']
            # password = request.POST['password']
            # user = auth.authenticate(
            #     username=username,
            #     password=password
            # )
            # if user is not None:
            #     auth.login(request, user)
            #     return HttpResponseRedirect(reverse('index'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(
                username=username,
                password=password
        )
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            message = u'Check you type your login and password correctly'
    return render(request, 'login.html', {'error': message})
