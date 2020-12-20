from django.db import models

class one(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.question + ' | ' + str(self.answer) + ' | ' + str(self.comment) 
