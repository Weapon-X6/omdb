from django.core.mail import mail_admins

from celery import shared_task

from movies import omdb_integration


@shared_task
def search_and_save(search):
    return omdb_integration.search_and_save(search)


@shared_task
def notify_of_new_search_term(search_term):
    mail_admins("New Search Term", f"A new search term was used: '{search_term}'")
