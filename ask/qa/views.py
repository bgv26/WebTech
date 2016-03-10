from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from models import Question

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
    question = get_object_or_404(Question, id=id)
    return render_to_response("question_detail.html", {"question": question})


