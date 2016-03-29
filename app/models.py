from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

# Activity. AcivityID,ActivityName,ActivityClass
class Activity(models.Model):
    activity_name = models.CharField(max_length=50)
    search_term = models.CharField(max_length=50)
    activity_desc = models.CharField(max_length=50)
    places_term = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.activity_name 

# Tags. TagID,TagName,QuestionText 
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    question_text = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

# ActivityTags. ActivityID,TagID
class ActivityTag(models.Model):
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.activity_id) + str(self.tag_id)

# User Selections. Outcome,(QTagID,QTagOutcome) x 5
class UserSelection(models.Model):
    outcome = models.BooleanField()
    suggested_activity = models.ForeignKey(Activity,on_delete=models.PROTECT)
    datetime = models.DateTimeField(auto_now=True)
    lat = models.FloatField()
    lng = models.FloatField()
    yes_list = models.CharField(max_length=128)
    no_list = models.CharField(max_length=128)
    json_field = JSONField()

    def __str__(self):
        return str(self.datetime) + str(self.suggested_activity) + str(self.outcome)
