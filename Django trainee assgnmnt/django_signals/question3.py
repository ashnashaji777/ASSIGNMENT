#Question 3: Do Django signals run in the same database transaction as the caller?
#Answer: Yes, Django signals run in the same transaction as the caller. 
#If there’s an error in the signal receiver, it can cause the entire transaction to roll back.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Define the signal receiver function
@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print("Signal receiver executed")
    raise Exception("Simulating an error in the signal receiver")  # Force an error

# Attempt to create a user within a transaction
try:
    with transaction.atomic():
        user = User.objects.create(username="testuser")
except Exception as e:
    print("Transaction rolled back due to:", e)
    user_exists = User.objects.filter(username="testuser").exists()
    print("User exists in the database after rollback?", user_exists)
