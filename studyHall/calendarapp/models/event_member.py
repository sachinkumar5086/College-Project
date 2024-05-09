from django.db import models

# from accounts.models import User
from calendarapp.models import Event, EventAbstract
from student.models import student

class EventMember(EventAbstract):
    """ Event member model """

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    user = models.CharField(max_length=100)

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)
