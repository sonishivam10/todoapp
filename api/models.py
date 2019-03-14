from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255, blank=False)
    completionDate = models.DateTimeField(blank=True,null=True)
    dueDate = models.DateTimeField(blank=True,null=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}".format(self.name)