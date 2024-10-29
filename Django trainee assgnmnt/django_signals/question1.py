
#Question 1: Are Django signals executed synchronously or asynchronously by default?
#Answer: Django signals are executed synchronously by default. This means that when a signal is sent,
#the connected receiver functions are executed immediately in the same thread and context as the caller.
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print("Signal received. Starting a time-consuming task...")
    time.sleep(5)  # Simulating a long-running task
    print("Task completed in signal receiver.")

# Simulate a user save action
user = User.objects.create(username="testuser")
print("User creation completed.")
