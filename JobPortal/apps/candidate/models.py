from django.db import models
from ..account.models import User


class CandidateManager(models.Manager):
    def create(self, *args, **kwargs):
        candidate = super(CandidateManager, self).create(*args, **kwargs)
        Resume.objects.create(candidate=candidate)
        return candidate


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    git_url = models.URLField(null=True, blank=True)
    current_salary = models.IntegerField(default=0, )

    objects = CandidateManager()


class Resume(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, primary_key=True)

    class Education(models.TextChoices):
        MIDDLE_SCHOOL = 'Middle school'
        HIGH_SCHOOL = 'High school'
        HIGHER_EDUCATION = 'Higher education'

    education = models.CharField(max_length=50, choices=Education.choices)


# class Responses(models.Model):
    # candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
