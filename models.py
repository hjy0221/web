from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=10)
    information = models.TextField()
    human = models.CharField(max_length=15)
    code_number = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length = 15)

class Choice(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE) #Poll 모델의 id를 이용
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    votes = models.IntegerField(default = 0)     