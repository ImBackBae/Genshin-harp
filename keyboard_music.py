from mimetypes import init
import pygame
from pygame import mixer
pygame.init()
pygame.mixer.set_num_channels(50)
display_width = 900
display_height = 500
screen = pygame.display.set_mode((display_width,display_height))
running = True
(x,y) = (30,0)
color = 1
class ColorButton():
    def __init__(self, color_1, color_2):
        self.c1 = color_1
        self.c2 = color_2
        self.color = self.c1
        self.colorful = False

class Bar():
    def __init__(self, bar_img_1, piano_up_1, piano_down_1, guitar_up_1, guitar_down_1, bar_img_2, piano_up_2, piano_down_2, guitar_up_2, guitar_down_2):
        self.bar_c1 = bar_img_1
        self.piano_up_c1 = piano_up_1
        self.piano_down_c1 = piano_down_1
        self.guitar_up_c1 = guitar_up_1
        self.guitar_down_c1 = guitar_down_1

        self.bar_c2 = bar_img_2
        self.piano_up_c2 = piano_up_2
        self.piano_down_c2 = piano_down_2
        self.guitar_up_c2 = guitar_up_2
        self.guitar_down_c2 = guitar_down_2

        self.bar = bar_img_1
        self.piano_up = piano_up_1
        self.piano_down = piano_down_1
        self.guitar_up = guitar_up_1
        self.guitar_down = guitar_down_1
        
class Note():
    current = "guitar"
    def __init__(self, image_up_c1, image_down_c1, image_up_c2, image_down_c2, piano, guitar, name):
        self.img_up_c1 = image_up_c1
        self.img_down_c1 = image_down_c1
        self.img_up_c2 = image_up_c2
        self.img_down_c2 = image_down_c2

        self.image_up = image_up_c1
        self.image_down = image_down_c1

        self.up = True

        self.name = name

        self.piano = piano
        self.guitar = guitar

        self.instrument = guitar

        guitar.set_volume(0.15)
        piano.set_volume(0.15)
    def change_color(self, color):
        if color == 1:
            self.image_up = self.img_up_c1
            self.image_down = self.img_down_c1
        elif color == -1:
            self.image_up = self.img_up_c2
            self.image_down = self.img_down_c2

bar = Bar(pygame.image.load("assets/img/color_1/bar_img/bar.png"), pygame.image.load("assets/img/color_1/bar_img/bar_instrument_1.png"), pygame.image.load("assets/img/color_1/bar_img/bar_instrument_12.png"), pygame.image.load("assets/img/color_1/bar_img/bar_instrument_2.png"), pygame.image.load("assets/img/color_1/bar_img/bar_instrument_22.png"), pygame.image.load("assets/img/color_2/bar_img/bar.png"), pygame.image.load("assets/img/color_2/bar_img/bar_instrument_1.png"), pygame.image.load("assets/img/color_2/bar_img/bar_instrument_12.png"), pygame.image.load("assets/img/color_2/bar_img/bar_instrument_2.png"), pygame.image.load("assets/img/color_2/bar_img/bar_instrument_22.png"))
color_button = ColorButton(pygame.image.load("assets/img/color_1/skin_icon.png"), pygame.image.load("assets/img/color_2/skin_icon.png"))

A5 = Note(pygame.image.load("assets/img/color_1/note_img/up/firstlinei/A5.png"), pygame.image.load("assets/img/color_1/note_img/down/FIRSTLINE2/AA5.png"), pygame.image.load("assets/img/color_2/note_img/up/firstlinei/A5.png"), pygame.image.load("assets/img/color_2/note_img/down/FIRSTLINE2/AA5.png"), pygame.mixer.Sound("assets/piano/treble/A5.wav"), pygame.mixer.Sound("assets/guitar/treble_guitar/A5.mp3"), "A5")
B5 = Note(pygame.image.load("assets/img/color_1/note_img/up/firstlinei/B5.png"), pygame.image.load("assets/img/color_1/note_img/down/FIRSTLINE2/BB5.png"), pygame.image.load("assets/img/color_2/note_img/up/firstlinei/B5.png"), pygame.image.load("assets/img/color_2/note_img/down/FIRSTLINE2/BB5.png"), pygame.mixer.Sound("assets/piano/treble/B5.wav"), pygame.mixer.Sound("assets/guitar/treble_guitar/B5.mp3"), "B5")
C5 = Note(pygame.image.load("assets/img/color_1/note_img/up/firstlinei/C5.png"), pygame.image.load("assets/img/color_1/note_img/down/FIRSTLINE2/CC5.png"), pygame.image.load("assets/img/color_2/note_img/up/firstlinei/C5.png"), pygame.image.load("assets/img/color_2/note_img/down/FIRSTLINE2/CC5.png"), pygame.mixer.Sound("assets/piano/treble/C5.wav"), pygame.mixer.Sound("assets/guitar/treble_guitar/C5.mp3"), "C5")
D5 = Note(pygame.image.load("assets/img/color_1/note_img/up/firstlinei/D5.png"), pygame.image.load("assets/img/color_1/note_img/down/FIRSTLINE2/DD5.png"), pygame.image.load("assets/img/color_2/note_img/up/firstlinei/D5.png"), pygame.image.load("assets/img/color_2/note_img/down/FIRSTLINE2/DD5.png"), pygame.mixer.Sound("assets/piano/treble/D5.wav"), pygame.mixer.Sound("assets/guitar/treble_guitar/D5.mp3"), "D5")
E5 = Note(pygame.image.load("assets/img/color_1/note_img/up/firstlinei/E5.png"), pygame.image.load("assets/img/color_1/note_img/down/FIRSTLINE2/EE5.png"), pygame.image.load("assets/img/color_2/note_img/up/firstlinei/E5.png"), pygame.image.load("assets/img/color_2/note_img/down/FIRSTLINE2/EE5.png"), pygame.mixer.Sound("assets/piano/treble/E5.wav"), pygame.mixer.Sound("assets/guitar/treble_guitar/E5.mp3"), "E5")
F5 = Note(pygame.image.load("assets/img/color_1/note_img/up/firstlinei/F5.png"), pygame.image.load("assets/img/color_1/note_img/down/FIRSTLINE2/FF5.png"), pygame.image.load("assets/img/color_2/note_img/up/firstlinei/F5.png"), pygame.image.load("assets/img/color_2/note_img/down/FIRSTLINE2/FF5.png"), pygame.mixer.Sound("assets/piano/treble/F5.wav"), pygame.mixer.Sound("assets/guitar/treble_guitar/F5.mp3"), "F5")
G5 = Note(pygame.image.load("assets/img/color_1/note_img/up/firstlinei/G5.png"), pygame.image.load("assets/img/color_1/note_img/down/FIRSTLINE2/GG5.png"), pygame.image.load("assets/img/color_2/note_img/up/firstlinei/G5.png"), pygame.image.load("assets/img/color_2/note_img/down/FIRSTLINE2/GG5.png"), pygame.mixer.Sound("assets/piano/treble/G5.wav"), pygame.mixer.Sound("assets/guitar/treble_guitar/G5.mp3"), "G5")

A4 = Note(pygame.image.load("assets/img/color_1/note_img/up/secondline/A4.png"), pygame.image.load("assets/img/color_1/note_img/down/SECONDLINE2/AA4.png"), pygame.image.load("assets/img/color_2/note_img/up/secondline/A4.png"), pygame.image.load("assets/img/color_2/note_img/down/SECONDLINE2/AA4.png"), pygame.mixer.Sound("assets/piano/alto/A4.wav"), pygame.mixer.Sound("assets/guitar/alto_guitar/A4.mp3"), "A4")
B4 = Note(pygame.image.load("assets/img/color_1/note_img/up/secondline/B4.png"), pygame.image.load("assets/img/color_1/note_img/down/SECONDLINE2/BB4.png"), pygame.image.load("assets/img/color_2/note_img/up/secondline/B4.png"), pygame.image.load("assets/img/color_2/note_img/down/SECONDLINE2/BB4.png"), pygame.mixer.Sound("assets/piano/alto/B4.wav"), pygame.mixer.Sound("assets/guitar/alto_guitar/B4.mp3"), "B4")
C4 = Note(pygame.image.load("assets/img/color_1/note_img/up/secondline/C4.png"), pygame.image.load("assets/img/color_1/note_img/down/SECONDLINE2/CC4.png"), pygame.image.load("assets/img/color_2/note_img/up/secondline/C4.png"), pygame.image.load("assets/img/color_2/note_img/down/SECONDLINE2/CC4.png"), pygame.mixer.Sound("assets/piano/alto/C4.wav"), pygame.mixer.Sound("assets/guitar/alto_guitar/C4.mp3"), "C4")
D4 = Note(pygame.image.load("assets/img/color_1/note_img/up/secondline/D4.png"), pygame.image.load("assets/img/color_1/note_img/down/SECONDLINE2/DD4.png"), pygame.image.load("assets/img/color_2/note_img/up/secondline/D4.png"), pygame.image.load("assets/img/color_2/note_img/down/SECONDLINE2/DD4.png"), pygame.mixer.Sound("assets/piano/alto/D4.wav"), pygame.mixer.Sound("assets/guitar/alto_guitar/D4.mp3"), "D4")
E4 = Note(pygame.image.load("assets/img/color_1/note_img/up/secondline/E4.png"), pygame.image.load("assets/img/color_1/note_img/down/SECONDLINE2/EE4.png"), pygame.image.load("assets/img/color_2/note_img/up/secondline/E4.png"), pygame.image.load("assets/img/color_2/note_img/down/SECONDLINE2/EE4.png"), pygame.mixer.Sound("assets/piano/alto/E4.wav"), pygame.mixer.Sound("assets/guitar/alto_guitar/E4.mp3"), "E4")
F4 = Note(pygame.image.load("assets/img/color_1/note_img/up/secondline/F4.png"), pygame.image.load("assets/img/color_1/note_img/down/SECONDLINE2/FF4.png"), pygame.image.load("assets/img/color_2/note_img/up/secondline/F4.png"), pygame.image.load("assets/img/color_2/note_img/down/SECONDLINE2/FF4.png"), pygame.mixer.Sound("assets/piano/alto/F4.wav"), pygame.mixer.Sound("assets/guitar/alto_guitar/F4.mp3"), "F4")
G4 = Note(pygame.image.load("assets/img/color_1/note_img/up/secondline/G4.png"), pygame.image.load("assets/img/color_1/note_img/down/SECONDLINE2/GG4.png"), pygame.image.load("assets/img/color_2/note_img/up/secondline/G4.png"), pygame.image.load("assets/img/color_2/note_img/down/SECONDLINE2/GG4.png"), pygame.mixer.Sound("assets/piano/alto/G4.wav"), pygame.mixer.Sound("assets/guitar/alto_guitar/G4.mp3"), "G4")

A3 = Note(pygame.image.load("assets/img/color_1/note_img/up/THIRDLINEi/A3.png"), pygame.image.load("assets/img/color_1/note_img/down/THIRDLINE2/AA3.png"), pygame.image.load("assets/img/color_2/note_img/up/THIRDLINEi/A3.png"), pygame.image.load("assets/img/color_2/note_img/down/THIRDLINE2/AA3.png"), pygame.mixer.Sound("assets/piano/Bass/A3.wav"), pygame.mixer.Sound("assets/guitar/bass_guitar/A3.mp3"), "A3")
B3 = Note(pygame.image.load("assets/img/color_1/note_img/up/THIRDLINEi/B3.png"), pygame.image.load("assets/img/color_1/note_img/down/THIRDLINE2/BB3.png"), pygame.image.load("assets/img/color_2/note_img/up/THIRDLINEi/B3.png"), pygame.image.load("assets/img/color_2/note_img/down/THIRDLINE2/BB3.png"), pygame.mixer.Sound("assets/piano/Bass/B3.wav"), pygame.mixer.Sound("assets/guitar/bass_guitar/B3.mp3"), "B3")
C3 = Note(pygame.image.load("assets/img/color_1/note_img/up/THIRDLINEi/C3.png"), pygame.image.load("assets/img/color_1/note_img/down/THIRDLINE2/CC3.png"), pygame.image.load("assets/img/color_2/note_img/up/THIRDLINEi/C3.png"), pygame.image.load("assets/img/color_2/note_img/down/THIRDLINE2/CC3.png"), pygame.mixer.Sound("assets/piano/Bass/C3.wav"), pygame.mixer.Sound("assets/guitar/bass_guitar/C3.mp3"), "C3")
D3 = Note(pygame.image.load("assets/img/color_1/note_img/up/THIRDLINEi/D3.png"), pygame.image.load("assets/img/color_1/note_img/down/THIRDLINE2/DD3.png"), pygame.image.load("assets/img/color_2/note_img/up/THIRDLINEi/D3.png"), pygame.image.load("assets/img/color_2/note_img/down/THIRDLINE2/DD3.png"), pygame.mixer.Sound("assets/piano/Bass/D3.wav"), pygame.mixer.Sound("assets/guitar/bass_guitar/D3.mp3"), "D3")
E3 = Note(pygame.image.load("assets/img/color_1/note_img/up/THIRDLINEi/E3.png"), pygame.image.load("assets/img/color_1/note_img/down/THIRDLINE2/EE3.png"), pygame.image.load("assets/img/color_2/note_img/up/THIRDLINEi/E3.png"), pygame.image.load("assets/img/color_2/note_img/down/THIRDLINE2/EE3.png"), pygame.mixer.Sound("assets/piano/Bass/E3.wav"), pygame.mixer.Sound("assets/guitar/bass_guitar/E3.mp3"), "E3")
F3 = Note(pygame.image.load("assets/img/color_1/note_img/up/THIRDLINEi/F3.png"), pygame.image.load("assets/img/color_1/note_img/down/THIRDLINE2/FF3.png"), pygame.image.load("assets/img/color_2/note_img/up/THIRDLINEi/F3.png"), pygame.image.load("assets/img/color_2/note_img/down/THIRDLINE2/FF3.png"), pygame.mixer.Sound("assets/piano/Bass/F3.wav"), pygame.mixer.Sound("assets/guitar/bass_guitar/F3.mp3"), "F3")
G3 = Note(pygame.image.load("assets/img/color_1/note_img/up/THIRDLINEi/G3.png"), pygame.image.load("assets/img/color_1/note_img/down/THIRDLINE2/GG3.png"), pygame.image.load("assets/img/color_2/note_img/up/THIRDLINEi/G3.png"), pygame.image.load("assets/img/color_2/note_img/down/THIRDLINE2/GG3.png"), pygame.mixer.Sound("assets/piano/Bass/G3.wav"), pygame.mixer.Sound("assets/guitar/bass_guitar/G3.mp3"), "G3")

notes = [[C5, D5, E5, F5, G5, A5, B5],
         [C4, D4, E4, F4, G4, A4, B4],
         [C3, D3, E3, F3, G3, A3, B3]]

keys = {113 : C5, 119 : D5, 101 : E5, 114 : F5, 116 : G5, 121 : A5 , 117 : B5,
        97 : C4, 115 : D4, 100 : E4, 102 : F4, 103 : G4, 104 : A4, 106 : B4,
        122 : C3, 120 : D3, 99 : E3, 118 : F3, 98 : G3, 110 : A3, 109 : B3}

def get_location(note):
    for i in range(len(notes)):
        if note in notes[i]:
            return (i, notes[i].index(note))

def key_pressed(key):
    key.instrument.play()
    key.up = False

def switch_instrument(instrument):
    for i in range(len(notes)):
        for note in notes[i]:
            if instrument == "piano":
                note.instrument = note.piano
            elif instrument == "guitar":
                note.instrument = note.guitar
def switch_color(color):
    for i in range(3):
        for note in notes[i]:
            note.change_color(color)
    if color == 1:
        color_button.color = color_button.c1
        color_button.colorful = False
        bar.bar = bar.bar_c1
        bar.guitar_down = bar.guitar_down_c1
        bar.guitar_up = bar.guitar_up_c1
        bar.piano_down = bar.piano_down_c1
        bar.piano_up = bar.piano_up_c1
    elif color == -1:
        color_button.color = color_button.c2
        color_button.colorful = True
        bar.bar = bar.bar_c2
        bar.guitar_down = bar.guitar_down_c2
        bar.guitar_up = bar.guitar_up_c2
        bar.piano_down = bar.piano_down_c2
        bar.piano_up = bar.piano_up_c2                

while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                key_pressed(keys[event.key])
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key].up = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouse_x,mouse_y) = pygame.mouse.get_pos()
            if mouse_x > 40 and mouse_x < 40 + 70 and mouse_y > 400 and mouse_y < 400 + 79:
                Note.current = "guitar"
            elif mouse_x > 40 + 70 and mouse_x < 40 + 2*70 and mouse_y > 400 and mouse_y < 400 + 79:
                Note.current = "piano"
            elif mouse_x > 827-60 and mouse_x < 827-60 + 70 and mouse_y > 400 and mouse_y < 400 +79:
                color = -color
                switch_color(color)
            else:
                for i in range(3):
                    for j in range(7):
                        if mouse_x > x+120*j and mouse_x < x+120*j + 120 and mouse_y > y+120*i and mouse_y < y+120*i + 120:
                            key_pressed(notes[i][j])
                            note = notes[i][j]
        elif event.type == pygame.MOUSEBUTTONUP:
            try:
                note.up = True
            except:
                pass
    for i in range(3):
        for j in range(7):
            if notes[i][j].up:
                screen.blit(notes[i][j].image_up, (x+120*j, y+120*i))
            else:
                screen.blit(notes[i][j].image_down, (x+120*j, y+120*i))

    screen.blit(bar.bar, (30, 380))
    if color_button.colorful:
        screen.blit(color_button.c2, (827-60, 400))
    else:
        screen.blit(color_button.c1, (827-60, 400))

    if Note.current == "guitar":
        switch_instrument("guitar")
        screen.blit(bar.piano_up, (40+70, 400))
        screen.blit(bar.guitar_down, (40, 400))

    elif Note.current == "piano":
        switch_instrument("piano")
        screen.blit(bar.guitar_up, (40, 400))
        screen.blit(bar.piano_down, (40+70, 400))    
    
    pygame.display.update()