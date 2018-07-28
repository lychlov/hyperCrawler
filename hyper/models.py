from django.db import models


# Create your models here.
class Fund(models.Model):
    logo_url = models.URLField()
    name = models.CharField(max_length=100)
    website = models.URLField()
    ath = models.CharField(max_length=500)
    atl = models.CharField(max_length=500)
    rating = models.CharField(max_length=10)
    projects = models.CharField()
    source_url = models.URLField()
    interested = models.CharField()
    pass


class Project(models.Model):
    funds = models.ManyToManyField(Fund)
    logo_url = models.URLField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    ico_date = models.DateTimeField()
    fund_rising_goal = models.CharField(max_length=100)
    fund_rising_progress = models.CharField(max_length=100)
    website = models.URLField()
    whitepaper = models.URLField()
    profile = models.TextField()
    country = models.CharField(max_length=100)
    social_link = models.CharField()
    youtube_link = models.URLField()
    market_returns = models.CharField()
    token_metrics = models.CharField()
    token_allocation = models.CharField()
    other_rating = models.CharField()
    media_page = models.CharField()
    team = models.CharField()
    advisors = models.CharField()
    partners = models.CharField()
    sale_in_time = models.CharField()
    telegram = models.CharField()
    source_url = models.URLField()
    pass


class Person(models.Model):
    project = models.ManyToManyField(Project)
    avatar_url = models.URLField()
    name = models.CharField(max_length=100)
    social_link = models.CharField()
    rating = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    profile = models.TextField()
    participated_ico = models.CharField()
    colleagues = models.CharField()
    source_url = models.URLField()
    pass
