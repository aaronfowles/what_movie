from __future__ import unicode_literals

from django.db import models

# Activity. AcivityID,ActivityName,ActivityClass
class Activity(models.Model):
    activity_name = models.CharField(max_length=50)
    activity_class = models.CharField(max_length=50)
    activity_desc = models.CharField(max_length=50)

# Tags. TagID,TagName,QuestionText 
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    question_text = models.CharField(max_length=50)

# ActivityTags. ActivityID,TagID
class ActivityTag(models.Model):
    activity_id = models.IntegerField()
    tag_id = models.IntegerField()

# User Selections. Outcome,(QTagID,QTagOutcome) x 5
class UserSelection(models.Model):
    outcome = models.BooleanField()
    q1_tag_id = models.IntegerField()
    q1_tag_outcome = models.BooleanField()
    q2_tag_id = models.IntegerField()
    q2_tag_outcome = models.BooleanField()
    q3_tag_id = models.IntegerField()
    q3_tag_outcome = models.BooleanField()
    q4_tag_id = models.IntegerField()
    q4_tag_outcome = models.BooleanField()
    q5_tag_id = models.IntegerField()
    q5_tag_outcome = models.BooleanField()
