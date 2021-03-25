from django.shortcuts import render, redirect
from myapp.models import  GameCard, GameBet
from . forms import FormName, FormHit
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + '  ' + self.suit

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


def add_card():
    deck= Deck()
    deck.shuffle()
    return deck.deal()

def populate(N=6):
    card=['']*13
    for entry in range(N):
        card = add_card()
        G_C= GameCard.objects.get_or_create(card_name=card)[0]
    #A_B=GameBet.objects.get_or_create('ACCOUNT')



# Create your views here.



def index(request):
    populate(13)
    return render(request,'myapp/index.html',)




def game(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]


    my_dict={'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,}
    return render(request,'myapp/game.html',context= my_dict)

def game_end(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]



    P1=values[str(Pcard1).split()[0]]
    P2=values[str(Pcard2).split()[0]]
    D1=values[str(Dcard1).split()[0]]
    D2=values[str(Dcard2).split()[0]]


    if (P1+P2) > 21:
        my_dict={'OUT':"You lose",'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2}
        return render(request,'myapp/game_end.html',context= my_dict)
    elif (P1+P2) == 21:
        my_dict={'OUT':'BLACK JACK','D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2}
        return render(request,'myapp/game_end.html',context= my_dict)
    elif ((P1+P2) < (D1+D2)) and ((D1+D2) < 21):
        my_dict={'OUT':"Dealer Wins",'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2}
        return render(request,'myapp/game_end.html',context= my_dict)
    elif (D1+D2) == 21:
        my_dict={'OUT':'Dealer Wins','D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2}
        return render(request,'myapp/game_end.html',context= my_dict)
    elif ((P1+P2) > (D1+D2) < 21):
        my_dict={'OUT':'You Win','D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2}
        return render(request,'myapp/game_end3.html',context= my_dict)
    return render(request,'myapp/game_end.html')

def game1(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]
    Dcard3=GameCard.objects.order_by('card_name')[8]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]
    Pcard3=GameCard.objects.order_by('card_name')[7]




    my_dict={'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3}
    return render(request,'myapp/game1.html',context= my_dict)

def game_end1(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]
    Dcard3=GameCard.objects.order_by('card_name')[8]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]
    Pcard3=GameCard.objects.order_by('card_name')[7]

    P1=values[str(Pcard1).split()[0]]
    P2=values[str(Pcard2).split()[0]]
    P3=values[str(Pcard3).split()[0]]
    D1=values[str(Dcard1).split()[0]]
    D2=values[str(Dcard2).split()[0]]
    D3=values[str(Dcard3).split()[0]]



    if (P1+P2+P3) > 21:
        my_dict={'OUT':"You lose",'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3}
        return render(request,'myapp/game_end1.html',context= my_dict)
    elif (P1+P2+P3) == 21:
        my_dict={'OUT':'BLACK JACK','D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3}
        return render(request,'myapp/game_end1.html',context= my_dict)
    elif (D1+D2+D3) > 21:
        my_dict={'OUT':"You WIN",'D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3}
        return render(request,'myapp/game_end1.html',context= my_dict)
    elif ((P1+P2+P3) < (D1+D2+D3)) and ((D1+D2+D3) < 21):
        my_dict={'OUT':'Dealer Wins','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3}
        return render(request,'myapp/game_end1.html',context= my_dict)
    elif (D1+D2+D3) == 21:
        my_dict={'OUT':'Dealer Black Jack Wins','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3}
        return render(request,'myapp/game_end1.html',context= my_dict)
    elif ((P1+P2+P3) > (D1+D2+D3) < 21):
        my_dict={'OUT':'You Win','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3}
        return render(request,'myapp/game_end3.html',context= my_dict)
    return render(request,'myapp/game_end1.html')

def game2(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]
    Dcard3=GameCard.objects.order_by('card_name')[8]
    Dcard4=GameCard.objects.order_by('card_name')[6]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]
    Pcard3=GameCard.objects.order_by('card_name')[7]
    Pcard4=GameCard.objects.order_by('card_name')[5]

    my_dict={'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3,'P_C_4':Pcard4}
    return render(request,'myapp/game2.html',context= my_dict)

def game_end2(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]
    Dcard3=GameCard.objects.order_by('card_name')[8]
    Dcard4=GameCard.objects.order_by('card_name')[6]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]
    Pcard3=GameCard.objects.order_by('card_name')[7]
    Pcard4=GameCard.objects.order_by('card_name')[5]

    P1=values[str(Pcard1).split()[0]]
    P2=values[str(Pcard2).split()[0]]
    P3=values[str(Pcard3).split()[0]]
    P4=values[str(Pcard4).split()[0]]
    D1=values[str(Dcard1).split()[0]]
    D2=values[str(Dcard2).split()[0]]
    D3=values[str(Dcard3).split()[0]]
    D4=values[str(Dcard4).split()[0]]



    if (P1+P2+P3+P4) > 21:
        my_dict={'OUT':"You lose",'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4}
        return render(request,'myapp/game_end2.html',context= my_dict)
    elif (P1+P2+P3+P4) == 21:
        my_dict={'OUT':'BLACK JACK','D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4}
        return render(request,'myapp/game_end2.html',context= my_dict)
    elif (D1+D2+D3+D4) > 21:
        my_dict={'OUT':"You WIN",'D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4}
        return render(request,'myapp/game_end2.html',context= my_dict)
    elif ((P1+P2+P3+P4) < (D1+D2+D3+D4)) and ((D1+D2+D3+D4) < 21):
        my_dict={'OUT':'Dealer Wins','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4}
        return render(request,'myapp/game_end2.html',context= my_dict)
    elif (D1+D2+D3+D4) == 21:
        my_dict={'OUT':'Dealer Black Jack Wins','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4}
        return render(request,'myapp/game_end2.html',context= my_dict)
    elif ((P1+P2+P3+P4) > (D1+D2+D3+D4) < 21):
        my_dict={'OUT':'You Win','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4}
        return render(request,'myapp/game_end3.html',context= my_dict)

    return render(request,'myapp/game_end2.html')

def game3(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]
    Dcard3=GameCard.objects.order_by('card_name')[8]
    Dcard4=GameCard.objects.order_by('card_name')[6]
    Dcard5=GameCard.objects.order_by('card_name')[4]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]
    Pcard3=GameCard.objects.order_by('card_name')[7]
    Pcard4=GameCard.objects.order_by('card_name')[5]
    Pcard5=GameCard.objects.order_by('card_name')[3]

    my_dict={'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3,'P_C_4':Pcard4,'P_C_5':Pcard5}
    return render(request,'myapp/game3.html',context= my_dict)

def game_end3(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]
    Dcard3=GameCard.objects.order_by('card_name')[8]
    Dcard4=GameCard.objects.order_by('card_name')[6]
    Dcard5=GameCard.objects.order_by('card_name')[4]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]
    Pcard3=GameCard.objects.order_by('card_name')[7]
    Pcard4=GameCard.objects.order_by('card_name')[5]
    Pcard5=GameCard.objects.order_by('card_name')[3]

    P1=values[str(Pcard1).split()[0]]
    P2=values[str(Pcard2).split()[0]]
    P3=values[str(Pcard3).split()[0]]
    P4=values[str(Pcard4).split()[0]]
    P5=values[str(Pcard5).split()[0]]
    D1=values[str(Dcard1).split()[0]]
    D2=values[str(Dcard2).split()[0]]
    D3=values[str(Dcard3).split()[0]]
    D4=values[str(Dcard4).split()[0]]
    D5=values[str(Dcard5).split()[0]]

    if (P1+P2+P3+P4+P5) > 21:
        my_dict={'OUT':"You lose",'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4, 'P_C_5':Pcard5}
        return render(request,'myapp/game_end3.html',context= my_dict)
    elif (P1+P2+P3+P4+P5) == 21:
        my_dict={'OUT':'BLACK JACK','D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4, 'P_C_5':Pcard5}
        return render(request,'myapp/game_end3.html',context= my_dict)
    elif (D1+D2+D3+D4+D5) > 21:
        my_dict={'OUT':"You WIN",'D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'D_C_5':Dcard5,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4,'P_C_5':Pcard5}
        return render(request,'myapp/game_end3.html',context= my_dict)
    elif ((P1+P2+P3+P4+P5) < (D1+D2+D3+D4+D5) < 21):
        my_dict={'OUT':'Dealer Wins','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'D_C_5':Dcard5,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4,'P_C_5':Pcard5}
        return render(request,'myapp/game_end3.html',context= my_dict)
    elif (D1+D2+D3+D4+D5) == 21:
        my_dict={'OUT':'Dealer Black Jack Wins','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'D_C_5':Dcard5,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4,'P_C_5':Pcard5}
        return render(request,'myapp/game_end3.html',context= my_dict)
    elif ((P1+P2+P3+P4+P5) == (D1+D2+D3+D4+D5)):
        my_dict={'OUT':'ITS A PUSH/DRAW','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'D_C_5':Dcard5,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4,'P_C_5':Pcard5}
        return render(request,'myapp/game_end3.html',context= my_dict)
    elif ((P1+P2+P3+P4+P5) > (D1+D2+D3+D4+D5) < 21):
        my_dict={'OUT':'You Win','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'D_C_5':Dcard5,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4,'P_C_5':Pcard5}
        return render(request,'myapp/game_end3.html',context= my_dict)

    return render(request,'myapp/game_end3.html')

def game4(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]
    Dcard3=GameCard.objects.order_by('card_name')[8]
    Dcard4=GameCard.objects.order_by('card_name')[6]
    Dcard5=GameCard.objects.order_by('card_name')[4]
    Dcard6=GameCard.objects.order_by('card_name')[2]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]
    Pcard3=GameCard.objects.order_by('card_name')[7]
    Pcard4=GameCard.objects.order_by('card_name')[5]
    Pcard5=GameCard.objects.order_by('card_name')[3]
    Pcard6=GameCard.objects.order_by('card_name')[1]
    my_dict={'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3,'P_C_4':Pcard4,'P_C_5':Pcard5,'P_C_6':Pcard6}
    return render(request,'myapp/game4.html',context= my_dict)

def game_end4(request):
    Dcard1=GameCard.objects.order_by('card_name')[12]
    Dcard2=GameCard.objects.order_by('card_name')[10]
    Dcard3=GameCard.objects.order_by('card_name')[8]
    Dcard4=GameCard.objects.order_by('card_name')[6]
    Dcard5=GameCard.objects.order_by('card_name')[4]
    Dcard6=GameCard.objects.order_by('card_name')[2]

    Pcard1=GameCard.objects.order_by('card_name')[11]
    Pcard2=GameCard.objects.order_by('card_name')[9]
    Pcard3=GameCard.objects.order_by('card_name')[7]
    Pcard4=GameCard.objects.order_by('card_name')[5]
    Pcard5=GameCard.objects.order_by('card_name')[3]
    Pcard6=GameCard.objects.order_by('card_name')[1]

    P1=values[str(Pcard1).split()[0]]
    P2=values[str(Pcard2).split()[0]]
    P3=values[str(Pcard3).split()[0]]
    P4=values[str(Pcard4).split()[0]]
    P5=values[str(Pcard5).split()[0]]
    P6=values[str(Pcard6).split()[0]]

    D1=values[str(Dcard1).split()[0]]
    D2=values[str(Dcard2).split()[0]]
    D3=values[str(Dcard3).split()[0]]
    D4=values[str(Dcard4).split()[0]]
    D5=values[str(Dcard5).split()[0]]
    D6=values[str(Dcard6).split()[0]]

    if (P1+P2+P3+P4+P5+P6) > 21:
        my_dict={'OUT':"You lose",'D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4, 'P_C_5':Pcard5, 'P_C_6':Pcard6}
        return render(request,'myapp/game_end4.html',context= my_dict)
    elif (P1+P2+P3+P4+P5+P6) == 21:
        my_dict={'OUT':'BLACK JACK','D_C_1':Dcard1,'D_C_2':Dcard2,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4, 'P_C_5':Pcard5, 'P_C_6':Pcard6}
        return render(request,'myapp/game_end4.html',context= my_dict)
    elif (D1+D2+D3+D4+D5+D6) > 21:
        my_dict={'OUT':"You WIN",'D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'D_C_5':Dcard5,'D_C_6':Dcard6,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4,'P_C_5':Pcard5, 'P_C_6':Pcard6}
        return render(request,'myapp/game_end4.html',context= my_dict)
    elif ((P1+P2+P3+P4+P5+P6) < (D1+D2+D3+D4+D5+D6)) and ((D1+D2+D3+D4+D5+D6) < 21):
        my_dict={'OUT':'Dealer Wins','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'D_C_5':Dcard5,'D_C_6':Dcard6,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4,'P_C_5':Pcard5, 'P_C_6':Pcard6}
        return render(request,'myapp/game_end4.html',context= my_dict)
    elif (D1+D2+D3+D4+D5+D6) == 21:
        my_dict={'OUT':'Dealer Black Jack Wins','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'D_C_5':Dcard5,'D_C_6':Dcard6,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4,'P_C_5':Pcard5, 'P_C_6':Pcard6}
        return render(request,'myapp/game_end4.html',context= my_dict)
    elif ((P1+P2+P3+P4+P5+P6) > (D1+D2+D3+D4+D5+D6) < 21):
        my_dict={'OUT':'You Win','D_C_1':Dcard1,'D_C_2':Dcard2,'D_C_3':Dcard3,'D_C_4':Dcard4,'D_C_5':Dcard5,'D_C_6':Dcard6,'P_C_1': Pcard1,'P_C_2':Pcard2,'P_C_3':Pcard3, 'P_C_4':Pcard4,'P_C_5':Pcard5,'P_C_6':Pcard6}
        return render(request,'myapp/game_end3.html',context= my_dict)

    return render(request,'myapp/game_end4.html')

def game5(request):
    my_dict={'OUT':'To Restart'}
    return render(request,'myapp/game5.html',context= my_dict)

def game_end5(request):
    my_dict={'OUT':'To Restart'}
    return render(request,'myapp/game_end5.html',context= my_dict)
