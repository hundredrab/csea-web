from django.db import models


class Event(models.Model):
    """Events organized by the CSEA.

    May be one of:
        Sports Events, e.g., Intra Dept Tournaments etc.
        Academic Events, e.g., Open Days, etc.
        Others, which don't fit the above.
    """
    EVENT_TYPE_CHOICES = (
        ('sports', 'Sports'),
        ('acad', 'Academic'),
        ('other', 'Other')
    )
    name = models.CharField(max_length=30,
                            help_text="Short name for the event.")
    type = models.CharField(max_length=30,
                            choices=EVENT_TYPE_CHOICES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    expire_on = models.DateField(
        help_text="Date after which this event will not be visible except in"
                  " the archives."
    )
    venue = models.CharField(max_length=30, blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    detail = models.TextField()
