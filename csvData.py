import csv
import pandas as pd

pola = ['div','ldiv','sr', 'lsr']

def dataToFile(div,ldiv,sr,lsr):
    with open('data.csv', mode='a', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, delimiter=';', fieldnames=pola)
        merg = [{'div':div, 'ldiv':ldiv, 'sr':sr, 'lsr':lsr}]
        for x in merg:
            writer.writerow(x)

def clearFile():
    open('data.csv', 'w').close()
