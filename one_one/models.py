from django.db import models

class one(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    comment = models.CharField(max_length=500)
    dAnswer_2 = models.CharField(max_length=200,default='選択肢2',)
    dAnswer_3 = models.CharField(max_length=200,default='選択肢3',)
    dAnswer_4 = models.CharField(max_length=200,default='選択肢4',)
    dAnswer_5 = models.CharField(max_length=200,default='選択肢5',)

    def __str__(self):
        return self.question + ' | ' + str(self.answer) + ' | ' + str(self.comment) 
