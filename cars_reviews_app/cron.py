# noticias_app/crons.py
from django_cron import CronJobBase, Schedule
#from .utils import obtener_noticias_scraping
from cars_reviews_app.scraper import obtener_noticias_scraping  # Importa tu función de scraping
from .models import Noticia


class ScrapeNoticiasCronJob(CronJobBase):
    schedule = Schedule(run_every_mins=1440)  # Ejecuta cada 1440 minutos (1 vez al día)
    code = 'cars_reviews_app.scrape_noticias_cron'  # Código único para la tarea

    def do(self):
        obtener_noticias_scraping()

class ObtenerNoticiasCronJob(CronJobBase):
    schedule = Schedule(run_every_mins=60)  # Esto hará que se ejecute cada 60 minutos
    code = 'cars_reviews_app.obtener_noticias_cronjob'  # Código único para este cronjob

    def do(self):
        # Aquí llamamos a la función que realiza el scraping y guarda las noticias
        noticias = obtener_noticias_scraping()  # Asegúrate de que esta función esté en tu archivo de scraping
        for noticia in noticias:
            Noticia.objects.get_or_create(
                titulo=noticia['titulo'],
                link=noticia['link']
            )