from bs4 import BeautifulSoup
import requests
import re   

URL = ["https://www.megastream.lol/index.php", "https://www.cpasmieux.run/index.php", "https://wiflix.studio/"]
film = "Rick morty"#remplacer par le user imput de telegram
search_lower = film.lower()


search = search_lower.replace(' ', '+')#POST Payload convert
str_search = str(search)
data = {"do":"search", "subaction":"search", "story": {search}}

result = search_lower.split()#fait une liste avec le nom du film si plusieurs mots pour chercher dans les URL


for i in URL:
    page = requests.post(i, data=data)
    soup = BeautifulSoup(page.content, 'html.parser').find_all(lambda t: t.name == "a")
    url_list = [a["href"] for a in soup]#https://stackoverflow.com/questions/65168254/how-to-get-href-link-by-text-in-python
    for __ in result:
        links = list(filter(lambda x: re.search(__, x), url_list))

    print(f'LA PTN DE LIST DURL DE SES MORTS :\n\n\n {links}')
    print(f'SITE : {page.url} \n {page}')