from celery import shared_task
from .scraper import scrape_jobs

@shared_task
def update_jobs():
    scrape_jobs()
    return "Job listings updated successfully"
