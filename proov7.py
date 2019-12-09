#Funktsioon, mis kontrollib, kas kaarte võib üksteise peale panna
def kontroll(x,y):
    for i in range(len(mast)):
        if x[1:] == mast[i]:
            v1=int(i)
    for i in range(len(mast)):
        if y[1:] == mast[i]:
            v2=int(i)
    try:
        erand=mast[v2+1]
    except:
        erand=mast[0]
        
    if mast[v1]==mast[v2-1] or mast[v1]==erand:
        return True
    else:
        return False
    
#Arvuti käib lauale kaarte
def arvuti_kaartide_asetamine():
    #print(pakk)
    for i in range(4):
        #print(laud[i])
        if arvuti[i] == 0 and len(arvuti_kaardid) > 0:
            if event.type == pygame.KEYDOWN:
                return 0
            arvuti[i] = arvuti_kaardid[0]
            del arvuti_kaardid[0]
            lao_kaart_arvuti(i)
            nimed_arvuti()
            kaarte_alles()
            pygame.display.flip()
            sleep(0.5)
    if event.type == pygame.KEYDOWN:
        return 0
    arvuti_kaartide_mängimine()
    pygame.display.flip()
            #print(laud[i])
    #print(laud)
    #print(pakk)

def arvuti_kaartide_mängimine():
    for i in range(len(arvuti)):
        if event.type == pygame.KEYDOWN:
            return 0
        try:
            if event.type == pygame.KEYDOWN:
                return 0
            if kontroll(arvuti[i], pakk1[-1]):
                tõsta_kaart_arvuti("vasak", i)
                break
            elif kontroll(arvuti[i], pakk2[-1]):
                tõsta_kaart_arvuti("parem", i)
                break
        except:
            a = 1

def ütle_pakk(pakkvasak):
    if(pakkvasak):
        tekst_3_2 = "parem pakk"
        meie_font3 = pygame.font.SysFont("Times New Roman", 22)
        teksti_pilt_3 = meie_font3.render(tekst_3_2, False, (224, 192, 224))
        ekraani_pind.blit(teksti_pilt_3, (300, 220))
        
        tekst_3_1 = "vasak pakk"
        meie_font3 = pygame.font.SysFont("Times New Roman", 22)
        teksti_pilt_3 = meie_font3.render(tekst_3_1, False, (25, 25, 155))
        ekraani_pind.blit(teksti_pilt_3, (300, 220))
    else:
        tekst_3_1 = "vasak pakk"
        meie_font3 = pygame.font.SysFont("Times New Roman", 22)
        teksti_pilt_3 = meie_font3.render(tekst_3_1, False, (224, 192, 224))
        ekraani_pind.blit(teksti_pilt_3, (300, 220))
        
        tekst_3_2 = "parem pakk"
        meie_font3 = pygame.font.SysFont("Times New Roman", 22)
        teksti_pilt_3 = meie_font3.render(tekst_3_2, False, (25, 25, 155))
        ekraani_pind.blit(teksti_pilt_3, (300, 220))
        
    pygame.display.flip()

def tõsta_kaart(arv):
    if len(mängija_kaardid) > 0:
        kaart = str(mängija[arv]) + ".png"
        kaart = pygame.image.load(kaart)
        ekraani_pind.blit(kaart, (koordinaadidX[arv], koordinaadidY[arv]))
        
        pygame.display.flip()
        
def lao_kaart_arvuti(arv):
    AkoordinaadidX = [80, 230, 380, 530]
    AkoordinaadidY = [40, 40, 40, 40]
    if len(arvuti_kaardid) > 0:
        kaart = str(arvuti[arv]) + ".png"
        kaart = pygame.image.load(kaart)
        ekraani_pind.blit(kaart, (AkoordinaadidX[arv], AkoordinaadidY[arv]))
        
        pygame.display.flip()
        
def tõsta_kaart_arvuti(kumb, indeks):
    AkoordinaadidX = [80, 230, 380, 530]
    AkoordinaadidY = [40, 40, 40, 40]
    AsihtX = [230, 380]
    AsihtY = [290, 290]
    if(kumb == "vasak"):
        arv = 0
        pakk1.append(arvuti[indeks])
    else:
        arv = 1
        pakk2.append(arvuti[indeks])
    
    AkoordinaadidX[indeks] = AsihtX[arv]
    AkoordinaadidY[indeks] = AsihtY[arv]
    #prindi vahepealne seis
    värvi_taust()
    nimed()
    kaarte_alles()
    pealmised()
    ütle_pakk(pakkvasak)
    
    arvuti[indeks] = 0
    nimed_arvuti()
    pygame.display.flip()

def pealmised():
    vasak = str(pakk1[-1]) + ".png"
    kaart_v = pygame.image.load(vasak)
    ekraani_pind.blit(kaart_v, (230, 290))
    parem = str(pakk2[-1]) + ".png"
    kaart_p = pygame.image.load(parem)
    ekraani_pind.blit(kaart_p, (380, 290))
    
    pygame.display.flip()

def kaarte_alles():
    tagus = pygame.image.load('tagus.png')
    ekraani_pind.blit(tagus, (580, 335))
    ekraani_pind.blit(tagus, (50, 335))
    meie_font = pygame.font.SysFont("Times New Roman Bold", 40)
    vasak = str(len(mängija_kaardid))
    teksti_pilt_vasak = meie_font.render(vasak, False, (25, 25, 155))
    ekraani_pind.blit(teksti_pilt_vasak, (65, 345))
    parem = str(len(arvuti_kaardid))
    teksti_pilt_parem = meie_font.render(parem, False, (25, 25, 155))
    ekraani_pind.blit(teksti_pilt_parem, (595, 345))
    pygame.display.flip()

def värvi_taust():
    #prindime esialgse väljaku
    ekraani_pind.fill( (224, 192, 224) )
    
    #mängija pakk
    asetus1 = pygame.Rect(580, 335, 70, 45)
    pygame.draw.rect(ekraani_pind, (0, 160, 160), asetus1)

    #arvuti pakk
    asetus2 = pygame.Rect(50, 335, 70, 45)
    pygame.draw.rect(ekraani_pind, (0, 160, 160), asetus2)

    if on_q:
        kaart = str(mängija[0]) + ".png"
        kaart = pygame.image.load(kaart)
        ekraani_pind.blit(kaart, (koordinaadidX[0], koordinaadidY[0]))
        
    if on_w:
        kaart = str(mängija[1]) + ".png"
        kaart = pygame.image.load(kaart)
        ekraani_pind.blit(kaart, (koordinaadidX[1], koordinaadidY[1]))
        
    if on_e:
        kaart = str(mängija[2]) + ".png"
        kaart = pygame.image.load(kaart)
        ekraani_pind.blit(kaart, (koordinaadidX[2], koordinaadidY[2]))

    if on_r:
        kaart = str(mängija[3]) + ".png"
        kaart = pygame.image.load(kaart)
        ekraani_pind.blit(kaart, (koordinaadidX[3], koordinaadidY[3]))

def uued():
    if len(mängija_kaardid) != 0 and len(arvuti_kaardid) != 0 and on_q and on_w and on_e and on_r:
        pakk1.append(mängija_kaardid[0])
        pakk2.append(arvuti_kaardid[0])
        del mängija_kaardid[0]
        del arvuti_kaardid[0]
    elif len(arvuti_kaardid) >= 2:
        pakk1.append(arvuti_kaardid[0])
        del arvuti_kaardid[0]
        pakk2.append(arvuti_kaardid[0])
        del arvuti_kaardid[0]
    elif len(mängija_kaardid) >= 2 and on_q and on_w and on_e and on_r:
        pakk1.append(mängija_kaardid[0])
        del mängija_kaardid[0]
        pakk2.append(mängija_kaardid[0])
        del mängija_kaardid[0]
    elif len(mängija_kaardid) == 1:
        pakk1.append(mängija_kaardid[0])
        del mängija_kaardid[0]
    elif len(arvuti_kaardid) == 1:
        pakk1.append(arvuti_kaardid[0])
        del arvuti_kaardid[0]

def nimed():
    n = [0, 0, 0, 0]
    if on_q:
        n[0] = 1
    if on_w:
        n[1] = 1
    if on_e:
        n[2] = 1
    if on_r: 
        n[3] = 1
    for i in range(4):
        if(n[i] == 1):
            kaart = str(mängija[i]) + ".png"
            kaart = pygame.image.load(kaart)
            ekraani_pind.blit(kaart, (koordinaadidX[i], koordinaadidY[i]))
    pygame.display.flip()
    
def nimed_arvuti():
    n = [0, 0, 0, 0]
    AkoordinaadidX = [80, 230, 380, 530]
    AkoordinaadidY = [40, 40, 40, 40]
    if arvuti[0] != 0:
        n[0] = 1
    if arvuti[1] != 0:
        n[1] = 1
    if arvuti[2] != 0:
        n[2] = 1
    if arvuti[3] != 0:
        n[3] = 1
    for i in range(4):
        if(n[i] == 1):
            kaart = str(arvuti[i]) + ".png"
            kaart = pygame.image.load(kaart)
            ekraani_pind.blit(kaart, (AkoordinaadidX[i], AkoordinaadidY[i]))

    pygame.display.flip()

import  pygame
from time import sleep
from random import shuffle

#Kaardipaki loomine

mast=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
hearts=["H" + mast for mast in mast]
spades=["S" + mast for mast in mast]
diamonds=["D" + mast for mast in mast]
clubs=["C" + mast for mast in mast]
deck=hearts+spades+diamonds+clubs

#Segab kaardipaki ja jagab kaheks


shuffle(deck)
mängija_kaardid=deck[:26]
global arvuti_kaardid
arvuti_kaardid=deck[26:]

global mängija
global arvuti
arvuti=[0,0,0,0]
mängija=[0,0,0,0]
global pakk1
global pakk2
pakk1=[]
pakk2=[]


pygame.init()
#värvime tausta
ekraani_pind = pygame.display.set_mode( (700, 720) )
pygame.display.set_caption("Stress")
ekraani_pind.fill( (224, 192, 224) )

#kaartide asukohad all
alg_koordinaadidX = [80, 230, 380, 530]
alg_koordinaadidY = [540, 540, 540, 540]
koordinaadidX = [80, 230, 380, 530]
koordinaadidY = [540, 540, 540, 540]

sihtX = 230
sihtY = 290

global on_q
global on_w
global on_e
global on_r
on_q = False
on_w = False
on_e = False
on_r = False
done = False

#sissejuhatav ekraan
algus = True

while algus:
    tekst = "Stress"
    tekst2 = "Jätkamiseks vajuta tühikut."
    meie_font = pygame.font.SysFont("Times New Roman", 45)
    meie_font2 = pygame.font.SysFont("Times New Roman", 36)
    teksti_pilt = meie_font.render(tekst, False, (25, 25, 155))
    teksti_pilt2 = meie_font2.render(tekst2, False, (25, 25, 155))
    ekraani_pind.blit(teksti_pilt, (300, 200))
    ekraani_pind.blit(teksti_pilt2, (150, 400))
    pygame.display.flip()
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                algus = False
    
värvi_taust()
pygame.display.flip()


clock = pygame.time.Clock()

sleep(1)
pakkvasak = True
kaartelaual = 0

värvi_taust()

pakk1.append(mängija_kaardid[0])
pakk2.append(arvuti_kaardid[0])
del mängija_kaardid[0]
del arvuti_kaardid[0]

pealmised()
kaarte_alles()

my_event = pygame.USEREVENT + 1
pygame.time.set_timer(my_event, 3000)

while not done:
    ütle_pakk(pakkvasak)
    pygame.display.flip()
    
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        
        if event.type == my_event:
            sleep(0.25)
            arvuti_kaartide_asetamine()
        
        if len(arvuti_kaardid) == 0 and len(mängija_kaardid) == 0:
            vaartus = 0
            for el in arvuti:
                if el != 0 or vaartus != 0:
                    vaartus = 1
            if vaartus == 0:
                sleep(3)
                ekraani_pind.fill( (224, 192, 224) )
                tekst = "Arvuti võit!"
                meie_font = pygame.font.SysFont("Times New Roman", 45)
                teksti_pilt = meie_font.render(tekst, False, (25, 25, 155))
                ekraani_pind.blit(teksti_pilt, (150, 400))
                pygame.display.flip()
                sleep(5)
                done = True
            elif not (on_q or on_w or on_e or on_r):
                sleep(3)
                ekraani_pind.fill( (224, 192, 224) )
                tekst = "Sinu võit!"
                meie_font = pygame.font.SysFont("Times New Roman", 45)
                teksti_pilt = meie_font.render(tekst, False, (25, 25, 155))
                ekraani_pind.blit(teksti_pilt, (150, 400))
                pygame.display.flip()
                sleep(5)
                done = True
            else:
                sleep(3)
                ekraani_pind.fill( (224, 192, 224) )
                tekst = "Viik!"
                meie_font = pygame.font.SysFont("Times New Roman", 45)
                teksti_pilt = meie_font.render(tekst, False, (25, 25, 155))
                ekraani_pind.blit(teksti_pilt, (150, 400))
                pygame.display.flip()
                sleep(5)
                done = True
        
        if event.type == pygame.KEYDOWN:
            #lisame uued kaardid ///ajutine
            if event.key == pygame.K_u:
                uued()
                pealmised()
                nimed()
                kaarte_alles()
            #lisame kaarte lauale
            if kaartelaual < 4 and event.key == pygame.K_SPACE:
                if len(mängija_kaardid) > 0:
                    kaartelaual += 1
                    if not on_q:
                        mängija[0] = mängija_kaardid[0]
                        del mängija_kaardid[0]
                        tõsta_kaart(0)
                        on_q = True
                        nimed()
                        kaarte_alles()
                    elif not on_w:
                        mängija[1] = mängija_kaardid[0]
                        del mängija_kaardid[0]
                        tõsta_kaart(1)
                        on_w = True
                        nimed()
                        kaarte_alles()
                    elif not on_e:
                        mängija[2] = mängija_kaardid[0]
                        del mängija_kaardid[0]
                        tõsta_kaart(2)
                        on_e = True
                        nimed()
                        kaarte_alles()
                    elif not on_r:
                        mängija[3] = mängija_kaardid[0]
                        del mängija_kaardid[0]
                        tõsta_kaart(3)
                        on_r = True
                        nimed()
                        kaarte_alles()
            
            
            if event.key == pygame.K_s:
                pygame.event.set_blocked(my_event)
                if pakk1[-1][1:] == pakk2[-1][1:]:
                    ekraani_pind.fill( (224, 192, 224) )
                    tekst = "Stress!"
                    meie_font = pygame.font.SysFont("Times New Roman", 45)
                    teksti_pilt = meie_font.render(tekst, False, (25, 25, 155))
                    ekraani_pind.blit(teksti_pilt, (150, 400))
                    pygame.display.flip()
                    sleep(3)
                    for el in pakk1:
                        arvuti_kaardid.append(el)
                    for el in pakk2:
                        arvuti_kaardid.append(el)
                    pakk1 = []
                    pakk2 = []
                    
                    värvi_taust()
                    kaarte_alles()
                    uued()
                    ütle_pakk()
                    pealmised()
                    pygame.display.flip()
                pygame.event.set_allowed(my_event)
                
            if event.key == pygame.K_p:
                if(pakkvasak):
                    pakkvasak = False
                    sihtX = 380
                    sihtY = 290
                else:
                    pakkvasak = True
                    sihtX = 230
                    sihtY = 290
                nimed()
            if event.key == pygame.K_q:
                if(pakkvasak):
                    siht = pakk1[-1]
                else:
                    siht = pakk2[-1]
                #kontroll?
                if(mängija[0] != 0):
                    if kontroll(mängija[0], siht):
                        if(pakkvasak):
                            pakk1.append(mängija[0])
                        else:
                            pakk2.append(mängija[0])
                        
                        koordinaadidX[0] = sihtX
                        koordinaadidY[0] = sihtY
                        
                        #prindi vahepealne seis
                        värvi_taust()
                        nimed()
                        nimed_arvuti()
                        kaarte_alles()
                        pealmised()
                        kaartelaual -= 1
                        ütle_pakk(pakkvasak)
                        pygame.display.flip()
                        on_q = False
                        koordinaadidX[0] = alg_koordinaadidX[0]
                        koordinaadidY[0] = alg_koordinaadidY[0]
                        
                        mängija[0] = 0
                    
                
                                
            if event.key == pygame.K_w:
                if(pakkvasak):
                    siht = pakk1[-1]
                else:
                    siht = pakk2[-1]
                #kontroll?
                if(mängija[1] != 0):
                    if kontroll(mängija[1], siht):
                        if(pakkvasak):
                            pakk1.append(mängija[1])
                        else:
                            pakk2.append(mängija[1])
                        
                        koordinaadidX[1] = sihtX
                        koordinaadidY[1] = sihtY
                        #prindi vahepealne seis
                        värvi_taust()
                        nimed()
                        nimed_arvuti()
                        kaarte_alles()
                        pealmised()
                        kaartelaual -= 1
                        ütle_pakk(pakkvasak)
                        pygame.display.flip()
                        on_w = False
                        koordinaadidX[1] = alg_koordinaadidX[1]
                        koordinaadidY[1] = alg_koordinaadidY[1]
                        
                        mängija[1] = 0
                
                
            if event.key == pygame.K_e:
                if(pakkvasak):
                    siht = pakk1[-1]
                else:
                    siht = pakk2[-1]
                #kontroll?
                if(mängija[2] != 0):
                    if kontroll(mängija[2], siht):
                        if(pakkvasak):
                            pakk1.append(mängija[2])
                        else:
                            pakk2.append(mängija[2])
                        
                        koordinaadidX[2] = sihtX
                        koordinaadidY[2] = sihtY
                        #prindi vahepealne seis
                        värvi_taust()
                        nimed()
                        nimed_arvuti()
                        kaarte_alles()
                        pealmised()
                        kaartelaual -= 1
                        ütle_pakk(pakkvasak)
                        pygame.display.flip()
                        on_e = False
                        koordinaadidX[2] = alg_koordinaadidX[2]
                        koordinaadidY[2] = alg_koordinaadidY[2]
                        
                        mängija[2] = 0
                
            
            if event.key == pygame.K_r:
                if(pakkvasak):
                    siht = pakk1[-1]
                else:
                    siht = pakk2[-1]
                #kontroll?
                if(mängija[3] != 0):
                    if kontroll(mängija[3], siht):
                        if(pakkvasak):
                            pakk1.append(mängija[3])
                        else:
                            pakk2.append(mängija[3])
                        
                        koordinaadidX[3] = sihtX
                        koordinaadidY[3] = sihtY
                        #prindi vahepealne seis
                        värvi_taust()
                        nimed()
                        nimed_arvuti()
                        kaarte_alles()
                        pealmised()
                        kaartelaual -= 1
                        ütle_pakk(pakkvasak)
                        pygame.display.flip()
                        on_r = False
                        koordinaadidX[3] = alg_koordinaadidX[3]
                        koordinaadidY[3] = alg_koordinaadidY[3]
                        
                        mängija[3] = 0
                

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
