# -*- coding: utf-8 -*-
#%%
#dane
plansza = [[[11],[12],[13]],[[21],[22],[23]],[[31],[32],[33]]]
pola = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
dane = [(1, ' x'), (2, ' o')]
play = 1
tura = 0

# funkcje  
def print_board():
    for i in range(0, 3):
        print(' ' * 10, plansza[i])
          
def ruch(gracz, znak):
    pole = input('Gracz {}\nPodaj pole, gdzie chcesz wstawić{}: '.format(gracz, znak))     
    if pole in pola:
        pola.remove(pole)            
        for i in range(0, 3):
            plansza[int(pole[0])-1][int(pole[1])-1] = znak
        print_board()
        czy_koniec()
        global tura
        tura += 1
    else:
        print('\nWprowadziłes niepoprawną nazwę pola.\nSpróbuj jeszcze raz!')
        print_board()

def czy_koniec():
    if (plansza[0][0] == plansza[0][1] == plansza[0][2]) or (plansza[1][0] == plansza[1][1] == plansza[1][2]) or (plansza[2][0] == plansza[2][1] == plansza[2][2]) or (plansza[0][0] == plansza[1][0] == plansza[2][0]) or (plansza[0][1] == plansza[1][1] == plansza[2][1]) or (plansza[0][2] == plansza[1][2] == plansza[2][2]) or (plansza[0][0] == plansza[1][1] == plansza[2][2]) or (plansza[0][2] == plansza[1][1] == plansza[2][0]):
        print('Gracz {}'.format(gracz))
        print('Wygrałes!!')
        global play
        play = 0        
    elif len(pola) == 0:
        print('Koniec gry. Remis!')
        play = 0   
       
# intro
print('-----------------------------')
print('Witamy w grze kółko-krzyżyk')
print('-----------------------------')
print('Nazwy pól wyglądają następująco:')
print_board()

# gra
while play:
    gracz, znak = dane[tura % 2]
    ruch(gracz, znak)
#%%