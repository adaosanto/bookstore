from celery import shared_task
from django.core.management import call_command
from django.utils import timezone


@shared_task
def backup():
    print("backup... ", end='')
    try:
        call_command('dbbackup', '--encrypt')
        print("done on " + str(timezone.now()))
    except:
        print("Error during backup on " + str(timezone.now()))
