from bs4 import BeautifulSoup

with open('./result1.html', 'r', encoding='utf-8') as f : 
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
# title = soup.select_one('#title')
# print(title.get_text())
#-------------------------------------------
# li_list = soup.select('#content-box > ul > li')

# for li in li_list : 
#     print(li.get_text())
#--------------------------------------------