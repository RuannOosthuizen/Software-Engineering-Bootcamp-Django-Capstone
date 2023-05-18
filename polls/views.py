from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
def index(request):
    """
    Render the index page for the polls application.

    Args:
        request (HttpRequest): The HTTP request object generated by the client.

    Returns:
        HttpResponse: The rendered HTML template as an HTTP response.

    Raises:
        None

    Example usage:
        >>> request = HttpRequest()
        >>> index(request)
        <HttpResponse object at 0x00000123ABCDEF>
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/poll.html', context)

def detail(request, question_id):
    """
    Render the detail page for a specific question in the polls application.

    Args:
        request (HttpRequest): The HTTP request object generated by the client.
        question_id (int): The ID of the question to be displayed.

    Returns:
        HttpResponse: The rendered HTML template as an HTTP response.

    Raises:
        Http404: If the specified question does not exist.

    Example usage:
        >>> request = HttpRequest()
        >>> question_id = 1
        >>> detail(request, question_id)
        <HttpResponse object at 0x00000123ABCDEF>
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required
def vote(request, question_id):
    """
    Process the vote for a specific question in the polls application.

    Args:
        request (HttpRequest): The HTTP request object generated by the client.
        question_id (int): The ID of the question for which the vote is being processed.

    Returns:
        HttpResponseRedirect: Redirects to the results page of the voted question.

    Raises:
        None

    Example usage:
        >>> request = HttpRequest()
        >>> question_id = 1
        >>> vote(request, question_id)
        <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/polls/1/results/">
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    """
    Render the results page for a specific question in the polls application.

    Args:
        request (HttpRequest): The HTTP request object generated by the client.
        question_id (int): The ID of the question whose results are to be displayed.

    Returns:
        HttpResponse: The rendered HTML template as an HTTP response.

    Raises:
        Http404: If the specified question does not exist.

    Example usage:
        >>> request = HttpRequest()
        >>> question_id = 1
        >>> results(request, question_id)
        <HttpResponse object at 0x00000123ABCDEF>
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})