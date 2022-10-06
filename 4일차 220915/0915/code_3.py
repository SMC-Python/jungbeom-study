from bs4 import BeautifulSoup

with open('./result1.html', 'r', encoding='utf-8') as f : 
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
link = soup.select_one('#pastecontainer > div.whiteBG.rounded10.pad10 > div:nth-child(2)')
print(link)