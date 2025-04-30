from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

CHROME_DRIVER_PATH = r"D:\ChomeDriver\chromedriver-win32\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

all_jobs = []

# ---------------- RemoteOK ----------------
def scrape_remoteok():
    jobs = []
    driver.get("https://remoteok.com/remote-data-jobs")
    time.sleep(3)
    job_elements = driver.find_elements(By.CLASS_NAME, "job")
    for job in job_elements:
        try:
            title = job.find_element(By.TAG_NAME, "h2").text
            company = job.find_element(By.TAG_NAME, "h3").text
            tags = [tag.text for tag in job.find_elements(By.CLASS_NAME, "tag")]
            location = job.find_element(By.CLASS_NAME, "location").text if job.find_elements(By.CLASS_NAME, "location") else "Remote"
            salary = next((tag for tag in tags if "$" in tag), "N/A")

            jobs.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Salary": salary,
                "Tags": ", ".join(tags),
                "Source": "RemoteOK"
            })
        except:
            continue
    return jobs

# ---------------- We Work Remotely ----------------
def scrape_weworkremotely():
    jobs = []
    driver.get("https://weworkremotely.com/categories/remote-data-jobs")
    time.sleep(3)
    job_sections = driver.find_elements(By.CLASS_NAME, "jobs")

    for section in job_sections:
        job_posts = section.find_elements(By.TAG_NAME, "li")
        for post in job_posts:
            try:
                title = post.find_element(By.CLASS_NAME, "title").text
                company = post.find_element(By.CLASS_NAME, "company").text
                location = post.find_element(By.CLASS_NAME, "region").text
                tags = []  # WWR doesn't use tags, so keep empty
                jobs.append({
                    "Title": title,
                    "Company": company,
                    "Location": location,
                    "Salary": "N/A",
                    "Tags": ", ".join(tags),
                    "Source": "We Work Remotely"
                })
            except:
                continue
    return jobs

# Collect from all sources
all_jobs.extend(scrape_remoteok())
all_jobs.extend(scrape_weworkremotely())

driver.quit()

# Save
df = pd.DataFrame(all_jobs)
df.index += 1
df.to_csv("data/jobs.csv", index_label="No.")
print(f"Scraped {len(df)} jobs from multiple sources.")
