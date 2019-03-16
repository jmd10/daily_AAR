from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    ''' A topic categorizing actions or outcomes '''
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        ''' returns a string representation of the model '''
        return self.text

class Actions(models.Model):
    ''' a specific action or outcome to be reviewed '''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        ''' returns string representation of model '''
        return self.text[0:50] + "..."
