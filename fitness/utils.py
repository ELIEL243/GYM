import datetime

from .models import Abonnement
import pytz
utc = pytz.UTC


def check_abonnement():
    abonnements = Abonnement.objects.all()

    for abonnement in abonnements:
        if (abonnement.date + datetime.timedelta(days=30)) < datetime.datetime.now():
            abonnement.status = True
            abonnement.save()
