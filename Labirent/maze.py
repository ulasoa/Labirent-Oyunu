from pygame import *


#sprite'lar için ebeveyn sınıfı
class GameSprite(sprite.Sprite):
   #Sınıf kurucusu
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # Her sprite image - resim özelliğini depolamalıdır
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       # Her sprite, içine yazıldığı dikdörtgenin  rect özelliğini saklamalıdır
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#2.hafta
#Oyuncu sprite için sınıf oluşturma.
class Player(GameSprite):
    def update(self):
        keys =key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y +=self.speed
#düşman ve sprite için sınıf oluşturma
class Enemy(GameSprite):
    direction="left"
    def update(self):
        if self.rect.x <=470:
            self.direction="right"
        if self.rect.x >=win_width-85:
            self.direction="left"
        
        if self.direction=="left":
            self.rect.x -=self.speed
        else:
            self.rect.x +=self.speed


#3.hafta
# engel spriteları için sınıf
class Wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
       # duvar resmi - istenilen boyut ve renkte bir dikdörtgen
       self.image = Surface((self.width, self.height))
       self.image.fill((color_1, color_2, color_3))
       # Her sprite rect özelliğini bir dikdörtgen olarak saklamalıdır
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
   def draw_wall(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
       #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))
#--


#Oyun sahnesi
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


#Oyunun karakterleri:
#2.hafta
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
#--
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)


#3.hafta
w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
w4 = Wall(154, 205, 50, 100, 250, 350, 10)
w5 = Wall(154, 205, 50, 100, 150 , 550, 10)
w6 = Wall(154, 205, 50, 100, 300 , 500, 10)
w7 = Wall(154, 205, 50, 100, 190 , 100, 10)
w8 = Wall(154, 205, 50, 100, 400 , 10, 10)
w9 = Wall(154, 205, 50, 100, 100 , 450, 10)
w10 = Wall(154, 205, 50, 100, 380 , 500, 10)

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))



#--


game = True
clock = time.Clock()
FPS = 60
#2.hafta
finish=False
#--


#müzik
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    #2.hafta
    if finish !=True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        
        
        player.reset()
        monster.reset()
        final.reset()


        #--
        #3.hafta
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()

        


        #liste ile yapılış
        duvar=[]
        duvar.append(w1)
        duvar.append(w2)
        duvar.append(w3)
        duvar.append(w4)
        duvar.append(w5)
        duvar.append(w6)
        duvar.append(w7)
        duvar.append(w8)
        duvar.append(w9)
        duvar.append(w10)
        


        #Kaybetme Durumu #liste ile yapılış
        for x in duvar:
            if sprite.collide_rect(player, x):
                finish = True
                window.blit(lose, (200, 200))
                kick.play()


             


       # "Kazanma" durumu
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()


        #--


    display.update()
    clock.tick(FPS)



