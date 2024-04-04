import os
import requests
from bs4 import BeautifulSoup

URL = "https://www.w3resource.com/python-exercises/python-basic-exercises.php"
# Link can be changed for different task pages

folder_name = "Python/Python_basic_(Part -I)"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

start = int(input("File index to srtart: "))
end = int(input("Amount of files to create: "))

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'lxml')

p_tags_with_strong = soup.select('p > strong')  # To find every p tags which contain strong tag
p_tags_with_strong = p_tags_with_strong[2:-2]

for i in range(start, start + end):
    for strong_tag in p_tags_with_strong:

        parent_p_tag = strong_tag.parent
        
        a_tag = parent_p_tag.find('a')
        
        if a_tag:
            link = "Link: " + "https://www.w3resource.com/python-exercises/" + a_tag['href']
        else:
            link = "\nLink: " + "https://www.w3resource.com/python-exercises/python-basic-exercise-" + str(i) + ".php"

        result_string = parent_p_tag.text.strip().replace('Click me to see the sample solution', '')

        task_index = result_string[:3].replace(' ', '').replace('.', '')
        
        if int(task_index) == i:
            file_name = os.path.join(folder_name, "task_{}.py".format(i))
            with open(file_name, "w") as file:
                file.write(f'"""\n{result_string}\n{link}\n"""\n\n# Solution\n\n')

            print("'{}' has been created successfully.".format(file_name))
            break
