import requests
from bs4 import BeautifulSoup
import csv

print("Hi!, Welcome to my Python script!")
print("This Python script retrieves and displays the Premier League standings for a specific\nseason from the Eurosport website")
season = input("Entre The Season  EXEMPLE: 2021-2022 >  ")
page = requests.get(f"https://www.eurosport.com/football/premier-league/{season}/standings.shtml")
src = page.text
soup = BeautifulSoup(src,"lxml")

def main():
    table = soup.find("tbody" ,class_="w-full divide-y divide-br-2-80").find_all("tr")
    lista = []   

    for t in table:
        rank = t.find("td" ,class_="whitespace-nowrap").text.strip()
        team = t.find("div" ,class_="relative flex items-center").text.strip()
        points = t.find_all("td" ,class_="whitespace-nowrap")[-1].text.strip()
        lista.append({"Rank":rank , "Team":team, "Points":points })        
        keys = lista[0].keys()

    with open("rank.csv","w", newline='' ,encoding='utf-8-sig') as f:
        diwriter = csv.DictWriter(f,keys)
        diwriter.writeheader()
        diwriter.writerows(lista)   
    print("File is created")   

main()