from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    score = models.FloatField(default=0.00)

    def __str__(self):
        return self.name + " " + self.score

class Software(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    trust_score = models.FloatField(default=0.00)

    def __str__(self):
        return self.name + " " + self.trust_scores