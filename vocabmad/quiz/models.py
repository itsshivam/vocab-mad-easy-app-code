from __future__ import unicode_literals
from django.db import models

# Create your models here.

class initial_details(models.Model):
    purpose = models.CharField(max_length = 100)
    working = models.CharField(max_length = 100)
    aware = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __unicode__(self):
        return self.purpose

class contact_details(models.Model):
    username = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    message = models.TextField(max_length = 400)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    def __unicode__(self):
        return self.username

class basic_details(models.Model):
    username = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30, blank = True)
    mobile = models.CharField(max_length = 20, blank = True)
    profession = models.CharField(max_length = 20, blank = True)
    gender = models.CharField(max_length = 20, blank = True)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    def __unicode__(self):
        return self.username

class word_lists(models.Model):
    word = models.CharField(max_length = 30)
    pronunciation = models.CharField(max_length = 40)
    hindi = models.CharField(max_length = 200)
    english = models.CharField(max_length = 200, blank = True)
    example = models.CharField(max_length = 500, blank = True)
    synonym = models.CharField(max_length = 200, blank = True)
    note = models.CharField(max_length = 200, blank = True)
    mnemotrick = models.CharField(max_length = 300)
    def __unicode__(self):
        return self.word

class quest_list(models.Model):
    word = models.CharField(max_length = 30)
    question = models.TextField(blank = True, null = True)
    opt1 = models.TextField(blank = True, null = True)
    opt2 = models.TextField(blank = True, null = True)
    opt3 = models.TextField(blank = True, null = True)
    opt4 = models.TextField(blank = True, null = True)
    ans = models.IntegerField()
    def __unicode__(self):
        return self.word

class user_stats(models.Model):
    username = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    words_completed = models.IntegerField(null = True, blank = True, default = 0)
    questions_correct = models.IntegerField(null = True, blank = True, default = 0)
    questions_wrong = models.IntegerField(null = True, blank = True)
    def __unicode__(self):
        return self.username
