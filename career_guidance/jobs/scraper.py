import requests
from bs4 import BeautifulSoup
from .models import Job
from datetime import datetime

def scrape_jobs():
    url = "https://www.brightermonday.co.ug/jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs_list = soup.find_all("div", class_="job-item")  # Modify based on actual HTML structure

    for job in jobs_list:
        title = job.find("h2").text.strip()
        company = job.find("span", class_="company").text.strip()
        location = job.find("span", class_="location").text.strip()
        job_type = job.find("span", class_="job-type").text.strip()
        job_url = job.find("a")["href"]
        posted_date = datetime.today().date()

        # Update existing jobs instead of inserting duplicates
        job_obj, created = Job.objects.update_or_create(
            job_url=job_url,
            defaults={
                "title": title,
                "company": company,
                "location": location,
                "job_type": job_type,
                "posted_date": posted_date
            }
        )

        if created:
            print(f"New job added: {title} at {company}")
        else:
            print(f"Job updated: {title} at {company}")
