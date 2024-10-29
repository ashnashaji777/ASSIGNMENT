#Question 2: Do Django signals run in the same thread as the caller?
#Answer: Django signals run in the same thread as the caller by default.

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Define the signal receiver function
@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print("Signal receiver thread:", threading.current_thread().name)

# Main program prints thread name, then creates a user to trigger the signal
print("Main thread:", threading.current_thread().name)
user = User.objects.create(username="testuser")
