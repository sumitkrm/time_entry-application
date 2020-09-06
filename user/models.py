from django.db import models

# Create your models here.
class UserTaskList(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    task_name = models.CharField(max_length=45, blank=True, null=True)
    project_name = models.CharField(max_length=45, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_task_list'