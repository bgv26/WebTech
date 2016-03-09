from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, null=True)
    rating = models.IntegerField(blank=True)
    author = models.ForeignKey(User, blank=True)
    likes = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.title

    def get_url(self):
        return reverse('question', kwargs={'id': self.pk})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, null=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, blank=True)

    def __unicode__(self):
        return self.question
