# -*- coding: utf-8 -*-
#%%
import random

def gra(l_gier, l_prob):
    points = 0
    dlugosc = []
    for i in range(0, l_gier):            
        while True:
            slowo = input('Gracz 1. Wpisz dowolne słowo: ')
            if slowo.isalpha():        
                break
            else:
                print('Słowo może zawierać tylko litery')
                
        tablica = list(slowo.lower())
        dlugosc.append(len(slowo))
        pomieszane_slowo = ''
        
        for i in range(0, len(tablica)):
            los = random.choice(tablica)
            pomieszane_slowo += los
            tablica.remove(los)
            
        for i in range(0, l_prob):
            proba_zgadniecia = input('Gracz 2. {} próba. Ułóż słowo z liter <{}>:'.format(i+1, pomieszane_slowo))
            if proba_zgadniecia.lower() == slowo.lower():
                points += 1
                print ('Gracz 2. Wygrałes!')
                break
        else:
            print('Gracz 2. Przegrałes!')
            
    print('--------------------------------------')
    print('STATS')            
    print('Rozegrałes', l_gier, 'gier.')        
    print('Zdodyłes', points, 'Pkt.')    
    print('Zdodyłes srednio', points / l_gier, 'Pkt. na grę.')
    print('Średnia długosć słowa wyniosła', sum(dlugosc) / len(dlugosc), 'słowa.')
    
#%%

gra(1, 3)
        
#%%    
while True:
    liczba_gier = input('Podaj liczbę gier: ')
    liczba_prob = input('Podaj liczbę prób: ')
    if liczba_gier.isnumeric() and liczba_prob.isnumeric():
        liczba_gier = int(liczba_gier)
        liczba_prob = int(liczba_prob)        
        break
    else:
        print('Proszę podać wartosć liczbową.')
        
gra(liczba_gier, liczba_prob)




