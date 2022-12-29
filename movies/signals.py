from django.db.models.signals import post_save
from django.dispatch import receiver

from movies.models import SearchTerm

@receiver(post_save, sender=SearchTerm, dispatch_uid="search_term_saved")
def search_term_saved(sender, instance, created, **kwargs):
    if created:
        print(f"A new SearchTerm was created: {instance.term}")
                                                          