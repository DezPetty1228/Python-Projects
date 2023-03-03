from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default=0, blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        return self.campus_name

    # Removes added 's ' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
