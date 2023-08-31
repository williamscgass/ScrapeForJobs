import requests
import bs4
import datetime
import os

URL = "https://github.com/SimplifyJobs/Summer2024-Internships"
SEPARATOR = "\n---------------------\n"

old_stuff = set()
with open("jobs.txt", "r") as f:
    old_file = f.read()
    old_stuff = set(old_file.split(SEPARATOR))

response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, "html.parser")

new_stuff = set()
tr_elements = soup.find_all("tr")
for ele in tr_elements:
    tr_text = ele.get_text(separator=" | ")
    a_tags = ele.find_all('a')
    # Extract and print links within <a> tags
    links = [a['href'] for a in a_tags if 'href' in a.attrs]
    total_text = f"Text: {tr_text} \nLinks: {links}"
    if total_text not in old_stuff:
        print("New stuff found!")
        print(total_text)
        print(SEPARATOR)

    new_stuff.add(total_text)


with open("jobs.txt", "w") as f:
    for item in new_stuff:
        f.write(item + SEPARATOR)


current_datetime = datetime.datetime.now()
# Format the datetime as a string
formatted_datetime = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
with open(os.path.join("archived_jobs", formatted_datetime + ".txt"), "w") as f:
    for item in new_stuff:
        f.write(item + SEPARATOR)

with open(os.path.join("archived_jobs_new", formatted_datetime + "_NEW.txt"), "w") as f:
    for item in new_stuff - old_stuff:
        f.write(item + SEPARATOR)
# Get the current date and time


