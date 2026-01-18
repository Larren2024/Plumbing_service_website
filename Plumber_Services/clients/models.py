from django.db import models

class ServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    problem_description = models.TextField()
    preferred_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Assigned', 'Assigned'),
            ('Completed', 'Completed'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"{self.name} - {self.problem_description[:20]}"
