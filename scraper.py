import requests
from bs4 import BeautifulSoup

def get_live_jobs():

    jobs = []

    try:

        url = "https://www.freejobalert.com/"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.find_all("a")[10:20]:

            title = a.text.strip()
            link = a.get("href")

            if title and link:

                jobs.append({
                    "title": title,
                    "link": link
                })

    except:
        jobs.append({
            "title": "Unable To Fetch Jobs",
            "link": "#"
        })

    return jobs