from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_POST
from models import Question
from forms import AskForm, AnswerForm


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


@require_GET
def question(request, id):
    quest = get_object_or_404(Question, id=id)
    form = AnswerForm()
    return render(request, "question_detail.html", {'question': quest, 'form': form})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(post.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


@require_POST
def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            post, quest = form.save()
            return HttpResponseRedirect(quest.get_url())
