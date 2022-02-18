#module dictionnaire
import requests
from bs4 import BeautifulSoup

def desc (word):
	url = "https://dictionnaire.lerobert.com/definition/" + word
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	try:
	  text=soup.find_all("span", "d_dfn")[0].get_text()
	except IndexError:
	  text ="Mot introuvable"
	return text

def syno(word):
	url = "http://www.synonymo.fr/synonyme/"+word
	erreur="Aucun résultat"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	text =soup.ul.get_text()
	if erreur in soup.h1.get_text():
	  text="Synonyme introuvable"
	text= text.replace("\n\n\n", ", ")
	text= text.replace("\n", "")
	return text

def anto(word):
	url = "http://www.antonyme.org/antonyme/" + word
	erreur="Aucun résultat"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	text=soup.ul.get_text()
	if erreur in soup.h1.get_text():
	  text="Antonyme introuvable"
	text= text.replace("\n\n\n", ", ")
	text= text.replace("\n", "")
	return text
