from django.db import models

# Create your models here.
class Question(models.Model):
    """
    A class representing a question in the polls application.

    Attributes:
        question_text (str): The text of the question.
        pub_date (DateTimeField): The date and time when the question was published.

    Example usage:
        >>> question = Question(question_text="What is your favorite color?", pub_date=datetime.now())
        >>> question.save()
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Return a string representation of the question.

        Returns:
            str: The question text.

        Example usage:
            >>> question = Question(question_text="What is your favorite color?", pub_date=datetime.now())
            >>> question.__str__()
            'What is your favorite color?'
        """
        return self.question_text

class Choice(models.Model):
    """
    A class representing a choice for a question in the polls application.

    Attributes:
        question (ForeignKey): The question to which this choice belongs.
        choice_text (str): The text of the choice.
        votes (int): The number of votes received for this choice.

    Example usage:
        >>> question = Question.objects.get(pk=1)
        >>> choice = Choice(question=question, choice_text="Red", votes=0)
        >>> choice.save()
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Return a string representation of the choice.

        Returns:
            str: The choice text.

        Example usage:
            >>> choice = Choice(question=question, choice_text="Red", votes=0)
            >>> choice.__str__()
            'Red'
        """
        return self.choice_text