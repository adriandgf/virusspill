# Filen lager et skall som utgangpunkt for spillprogrammering i IT2
import pygame, math, random#Importerer nødvendige bilblioteker
 
pygame.init()                   # Intialiserer pygame
clock = pygame.time.Clock()     # Lager klokke for å kontrollere
width = 800                     # Bredde på vindu
height = 608                    # Høyde på vindu
screen = pygame.display.set_mode((width, height)) #Setter opp vinduet
running = True                  # Holder spillet i gang helt til running settes til False
gameover = False                # Variabel for å sjekke om spillet er over
levelFerdig = False
levelnr = 0
ferdig = False
 
# Legger til lydeffekter - NB! Kan være hensiktsmessig å bruke .waw-filer
bakgrunnLyd = pygame.mixer.Sound("bakgrunnsmusikk.mp3")
# medkitLyd = pygame.mixer.Sound("medkit.mp3")
# virusLyd = pygame.mxier.Sound(virus.mp3)
 
levels = [
            [       # ***** LEVEL 1 *****
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], # level 1
                [1,8,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"U"],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
                [1,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
                [1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],
                [1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1],
                [1,0,0,2,1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,1,0,0,1,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ],
            [       # ***** LEVEL 2 *****
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                ["U",0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
                [1,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
                [1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,2,0,0,0,0,0,1],
                [1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1],
                [1,0,0,2,1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,1,0,0,1,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
                [1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,8,1,1]
            ],
            [       # ***** LEVEL 3 *****
                [1,1,0,"U",1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
                [1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
                [1,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
                [1,2,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
                [1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],
                [1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1],
                [1,0,0,2,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
                [1,0,0,2,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,1],
                [1,0,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ]
         ]
 
#**************** Plass til variabler som skal benyttes i spillet   ****************
 
virusGruppe = pygame.sprite.Group() # Lager en gruppe for ballene
spillerGruppe = pygame.sprite.Group()
vaksineGruppe = pygame.sprite.Group()
veggGruppe = pygame.sprite.Group()
medkitGruppe = pygame.sprite.Group()
utgangGruppe = pygame.sprite.Group()
 
#font = pygame.font.Font("freesansbold.tbf", 72) # Det trygge valget!
font = pygame.font.SysFont('Comic Sans MS', 72) # Bruk av systemfont. Vær sikker på at den er installert
tekst_gameover = font.render('GAME OVER!', True, (255, 0, 0)) # Lager 'Game over' tekst
gamerover_rect = tekst_gameover.get_rect() # Pakker inn teksten i et rektangel
gamerover_rect.center = (width/2, height/2) # Plasserer teksten midt på skjermen
 
tekst_levelferdig = font.render('LEVEL FULLFØRT!', True, (255, 0, 0)) # Lager 'LEVEL FULLFØRT' tekst
levelFerdig_rect = tekst_levelferdig.get_rect() # Pakker inn teksten i et rektangel
levelFerdig_rect.center = (width/2, height/2) # Plasserer teksten midt på skjermen
 
tekst_fullfort_spill = font.render('GLORIOUS TRIUMPH !!', True, (255, 0, 0)) # Lager 'Glorious triumph' tekst
fullfort_spill_rect = tekst_fullfort_spill.get_rect() # Pakker inn teksten i et rektangel
fullfort_spill_rect.center = (width/2, height/2) # Plasserer teksten midt på skjermen
 
#**************** Plass til klasser vi skal benytte i spillet       ****************
 
class Spiller(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        bilde = pygame.image.load("leonardo.png").convert_alpha() # Laster inn bilde av en spillfigur
        self.image = pygame.transform.scale(bilde, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 45
        self.rect.y = 45
        self.fartx = 0
        self.farty = 0
        self.antall_vaksiner = 0
 
    def reset(self):
        self.fartx = 0
        self.farty = 0
        self.antall_vaksiner = 0
 
 
    def update(self):
        # Flytter høyre og venstre
        self.rect.x += self.fartx  # Oppdaterer pos. i x-retning
        veggTreff_liste = pygame.sprite.spritecollide(self, veggGruppe, False)
        if veggTreff_liste:
            if self.fartx > 0:  # Sjekker om den beveger seg mot høyre
                self.rect.right = veggTreff_liste[0].rect.left
            else:               # Beveger seg mot venstre, siden den ikke beveger seg mot høyre
                self.rect.left = veggTreff_liste[0].rect.right
       
 
        # Flytter opp og ned
        self.rect.y += self.farty  # Oppdaterer pos. i y-retning
        veggTreff_liste = pygame.sprite.spritecollide(self, veggGruppe, False)
        if veggTreff_liste:
            if self.farty > 0: # Beveger seg ned
                self.rect.bottom = veggTreff_liste[0].rect.top
            else: # Beveger seg opp
                self.rect.top = veggTreff_liste[0].rect.bottom
       
 
        # Sjekker om spilleren treffer en medkit
        medkitTreff_liste = pygame.sprite.spritecollide(self, medkitGruppe, False)
        if medkitTreff_liste:
            self.antall_vaksiner += 3
            medkitTreff_liste[0].kill()
       
        # sjekker om spilleren treffer en utgang
        utgangTreff_liste = pygame.sprite.spritecollide(self, utgangGruppe, True)
        if utgangTreff_liste:
            global levelFerdig
            levelFerdig = True
            global levelnr
            levelnr += 1
            restart()
 
class Virus(pygame.sprite.Sprite):
    def __init__(self, x, y, fx, fy):
        pygame.sprite.Sprite.__init__(self)
        bilde = pygame.image.load("spiller.png.png").convert_alpha()
        self.image = pygame.transform.scale(bilde, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fartx = fx
        self.farty = fy
 
    def update(self):
        # Flytter høyre og venstre
        self.rect.x += self.fartx  # Oppdaterer pos. i x-retning
        veggTreff_liste = pygame.sprite.spritecollide(self, veggGruppe, False)
        if veggTreff_liste:
            if self.fartx > 0:  # Sjekker om den beveger seg mot høyre
                self.rect.right = veggTreff_liste[0].rect.left
            else:               # Beveger seg mot venstre, siden den ikke beveger seg mot høyre
                self.rect.left = veggTreff_liste[0].rect.right
 
            self.fartx *= -1
        # Flytter opp og ned
        self.rect.y += self.farty  # Oppdaterer pos. i y-retning
        veggTreff_liste = pygame.sprite.spritecollide(self, veggGruppe, False)
        if veggTreff_liste:
            if self.farty > 0: # Beveger seg ned
                self.rect.bottom = veggTreff_liste[0].rect.top
            else: # Beveger seg opp
                self.rect.top = veggTreff_liste[0].rect.bottom
            self.farty *= -1
   
    def treffVegg(self):
        if self.rect.x + 40 > width or self.rect.x < 0:
            self.fartx = -1 * self.fartx
        if self.rect.y + 40 > height or self.rect.y < 0:
            self.farty = -1 * self.farty
 
class Vaksine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        bilde = pygame.image.load("Filer/vaccines_4.png").convert_alpha()
        self.image = pygame.transform.scale(bilde, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class Vegg(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        bilde = pygame.image.load("brickwall.png").convert_alpha()
        self.image = pygame.transform.scale(bilde, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class Medkit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        bilde = pygame.image.load("medical.png").convert_alpha()
        self.image = pygame.transform.scale(bilde, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class Utgang(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        bilde = pygame.image.load("logout.png")
        self.image = pygame.transform.scale(bilde, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
def restart():
    global gameover
    global levelFerdig
    gameover = False
    levelFerdig = False
 
    for virus in virusGruppe:
        virus.kill()
    for vaksine in vaksineGruppe:
        vaksine.kill()
    for medkit in medkitGruppe:
        medkit.kill()
    for vegg in veggGruppe:
        vegg.kill()
    for utgang in utgangGruppe:
        utgang.kill()
    spiller.reset()
    if spiller not in spillerGruppe:
        spillerGruppe.add(spiller)
   
    if len(levels) > levelnr:
        for i in range (4 + levelnr*3): # Oppretter gitt antall virus i spillet, med bestemte tilfeldige verdier
            virus = Virus(random.randint(0+60, width - 60), random.randint(0+60, height - 60), random.randint(-2, 4), random.randint(-2, 4))
            virus.add(virusGruppe)
 
    # Lager level, medkits og utgang
    if levelnr < len(levels):
        for y, rad in enumerate(levels[levelnr]): # Lager en løkke som løper gjennom alle...
            for x,verdi in enumerate(rad):
                if verdi == 1:
                    vegg = Vegg(x*32,y*32) # Ganger med 32 for å plassere riktig
                    veggGruppe.add(vegg)
                if verdi == 2:
                    medkit = Medkit(x*32, y*32)
                    medkitGruppe.add(medkit)
                if verdi == 8:
                    spiller.rect.x = x * 32
                    spiller.rect.y = y * 32
                if verdi == "U":
                    utgang = Utgang(x*32, y*32)
                    utgangGruppe.add(utgang)
 
    else:
        global ferdig
        ferdig = True
 
 
spiller = Spiller()
spiller.add(spillerGruppe)
restart()
 
#**************** Løkke for selve spillkjøringen                    ****************
while running:
 
    bakgrunnLyd.play()
 
    #Håndterer input fra tastaturet for bevegelse
    tastaturliste = pygame.key.get_pressed()
 
    spiller.fartx = 0
    spiller.farty = 0
    if tastaturliste[pygame.K_w] and not gameover:
        spiller.farty = -7
    if tastaturliste[pygame.K_s] and not gameover:
        spiller.farty = 7
    if tastaturliste[pygame.K_a] and not gameover:
        spiller.fartx = -7
    if tastaturliste[pygame.K_d] and not gameover:
        spiller.fartx = 7
       
    #Håndtering av tastetrykk er ferdig
 
    for virus in virusGruppe:
        virus.treffVegg()
 
    # Lager en liste over alle treff av virusene
    spiller_truffet = pygame.sprite.groupcollide(spillerGruppe, virusGruppe, True, False, pygame.sprite.collide_mask)
        # True og False er knyttet til spiller- og virusGruppe. true gir løsning for å
        # fjerne spilleren i dette tilfellet
        # collide_mask brukes for å knytte kollisjonen til rektangelet.
 
    # Sjekker om listen over treff inneholder noen treff
    if spiller_truffet:
        gameover = True  
 
    # lager en liste over alle treff av vaksinen
    virus_truffet = pygame.sprite.groupcollide(virusGruppe, vaksineGruppe, True, True, pygame.sprite.collide_mask)
 
    virusGruppe.update()
    spillerGruppe.update()
    vaksineGruppe.update()
    veggGruppe.update()
    medkitGruppe.update()
    utgangGruppe.update()
 
    screen.fill((255,255,255))
    utgangGruppe.draw(screen)
    medkitGruppe.draw(screen)
    spillerGruppe.draw(screen)
    vaksineGruppe.draw(screen)
    veggGruppe.draw(screen)
    virusGruppe.draw(screen)
   
   
 
    # Hvis spillet er over, vise 'GAME OVER!' tekst på skjermen
    if not levelFerdig and gameover:
        screen.blit(tekst_gameover, gamerover_rect)
   
    #Hvis man når døra, vis "LEVEL FULLFØRT!"
    if levelFerdig:
        screen.blit(tekst_levelferdig, levelFerdig_rect)
   
    if ferdig:
        screen.blit(tekst_fullfort_spill, fullfort_spill_rect)
 
 
    clock.tick(60)              # Setter bildefrekvensen til 60 bilder per sekund
    pygame.display.update()     # Oppdaterer skjermen
   
    for event in pygame.event.get():    # Henter hendelser fra hendelseskøen
        if event.type == pygame.QUIT:   # Brukeren trykker på lukk knappen
            running = False             # Setter running til false og avslutter løkka
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if spiller.antall_vaksiner > 0:
                    vaksine = Vaksine(spiller.rect.x, spiller.rect.y)
                    vaksineGruppe.add(vaksine)
                    spiller.antall_vaksiner -= 1
 
            if event.key == pygame.K_r:
                restart()
 
       
pygame.quit()               # Avslutter pygame