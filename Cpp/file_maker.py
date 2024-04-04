import os
import requests
from bs4 import BeautifulSoup

URL = "https://www.w3resource.com/cpp-exercises/basic/index.php"
# Link can be changed for different task pages

cpp_code = '''
#include <iostream>
using namespace std;

int main()
{
    cout << "\\n\\n  :\\n"; // Outputting a message
    cout << "-----------------------------------\\n"; // Outputting a separator line

    
    
    cout << endl;

    return 0;
}
'''


path = "Cpp/"
folder_name = path + "C++Basic"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

start = int(input("File index to srtart: "))
end = int(input("Amount of files to create: "))

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'lxml')

p_tags_with_strong = soup.select('p > strong')  # To find every p tags which contain strong tag
p_tags_with_strong = p_tags_with_strong[1:-2]

for i in range(start, start + end):
    for strong_tag in p_tags_with_strong:

        parent_p_tag = strong_tag.parent
        
        a_tag = parent_p_tag.find('a')
        
        if a_tag:
            link = "Link: " + "https://www.w3resource.com/cpp-exercises/basic/" + a_tag['href']
        else:
            link = "\nLink: " + "https://www.w3resource.com/cpp-exercises/basic/cpp-basic-exercise-" + str(i) + ".php"

        result_string = parent_p_tag.text.strip().replace('Click me to see the sample solution', '')

        task_index = result_string[:3].replace(' ', '').replace('.', '')
     
        if int(task_index) == i:
            file_name = os.path.join(folder_name, "task{}.cpp".format(i))
            with open(file_name, "w") as file:
                file.write(f'/*\n{result_string}\n{link}\n*/\n\n// Solution\n{cpp_code}')

            print("'{}' has been created successfully.".format(file_name))
            break
