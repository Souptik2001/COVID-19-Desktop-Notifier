import os
import datetime
import time
from bs4 import BeautifulSoup
import json
import requests
from tabulate import tabulate
from plyer import notification

URL = 'https://www.mohfw.gov.in/'
k=6

def notifyMe(title, message):
  notification.notify(
    title = title,
    message=message,
    app_icon=".\\res\cov.ico",
    timeout=15
  )

if __name__ == "__main__":
  while True:
    os.system('title COVID Analyser')
    os.system('pip install plyer')
    os.system('cls')
    os.system('pip install bs4')
    os.system('cls')
    content = requests.get(URL).text
    soup = BeautifulSoup(content, 'html.parser')
    # header
    all_tables = soup.findAll('tbody')
    table = all_tables[7]
    all_rows = table.findAll('tr')
    # print(all_rows)
    temp_str = ""
    # [[state, 43,535,33,42],[],[],....]
    for row in all_rows:
      temp_str = temp_str + row.get_text()
      # print(temp_str)
    temp_str = temp_str[1:]
    splitted_state = temp_str.split("\n\n")
    # print(splitted_state)
    t_i=0
    t_f=0
    t_c=0
    t_d=0

    table = []

    for state in splitted_state:
      temp=[]
      splitted_data = state.split("\n")
      if splitted_data[0] == 'Total number of confirmed cases in India': break
      print(splitted_data)
      # print(splitted_data[2])
      temp.append(splitted_data[0])
      temp.append(splitted_data[1])
      temp.append(splitted_data[2])
      temp.append(splitted_data[3])
      temp.append(splitted_data[4])
      temp.append(splitted_data[5])
      table.append(temp)
      t_i = t_i + int(splitted_data[2])
      t_f = t_f + int(splitted_data[3])
      t_c = t_c + int(splitted_data[4])
      t_d = t_d + int(splitted_data[5])
      # print(splitted_data[0])
    # print(splitted_data)
    os.system('color E2')
    os.system('cls')
    print("\n")
    print("\t\t\t\t\t\t\tCOVID-19 PRESENT SENARIO IN INDIA")
    print("\t\t\t\t\t\t\t---------------------------------")
    print("\n\n")
    print(tabulate(table, headers=["Sl. No.", "State", "Total Cases (Nationality:Indian)", "Total Cases (Nationality:Foreigner)", "Total Cured", "Total Deaths"]))
    ntitle = "COVID-19 present Status"
    nmessage = f"Total Cases(Nationality:Indian): {t_i} \n Total Cases(Nationality:Foreigner): {t_f} \n Total Cured: {t_c} \n Total Deaths {t_d}"
    os.system('color E4')
    print("\n\n")
    print(f"\t\t\t\t Total Cases ( Nationality : Indian )  :  {t_i} \n\t\t\t\t Total Cases ( Nationality : Foreigner )  :  {t_f} \n\t\t\t\t Total Cured/ Discharged/ Migrated  :  {t_c} \n\t\t\t\t Total Deaths  :  {t_d}")
    k = k + 1
    if k== 7:
      notifyMe(ntitle, nmessage)
      k=1
    time.sleep(300)
  