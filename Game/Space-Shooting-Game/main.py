import pygame
import random
import math
from pygame import mixer

# intialize the pygame
pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))

# title and logo
pygame.display.set_caption("Space Game")
icon = pygame.image.load('uranus.png')
pygame.display.set_icon(icon)


# background
bg = pygame.image.load("bg2.jpg")
bg_r = pygame.transform.scale(bg, (1000,1000))

# bg music
mixer.music.load('Fluffing-a-Duck.mp3')
mixer.music.play(-1)



# fighter jet
jet_image = pygame.image.load('jet (2).png')
jet_imageX = 375
jet_imageY = 480
jet_rimage = pygame.transform.scale(jet_image, (50,50))
jet_change = 0

def jet(x,y):
     screen.blit(jet_rimage,(x,y))





# enemy1

enem1 = pygame.image.load('enemy (1).png')
enemy_r1 = pygame.transform.scale(enem1, (50,50))
enemyX1 = random.randint(0,735)
enemyY1 = random.randint(50,150)
enemyx_change1 = 4
enemyy_change1 = 0.1

# enemy2

enem2 = pygame.image.load('enemy (2).png')
enemy_r2 = pygame.transform.scale(enem2, (50,50))
enemyX2 = random.randint(0,735)
enemyY2 = random.randint(50,150)
enemyx_change2 = 4
enemyy_change2 = 0.1

# enemy3

enem3 = pygame.image.load('enemy (3).png')
enemy_r3 = pygame.transform.scale(enem3, (50,50))
enemyX3 = random.randint(0,735)
enemyY3 = random.randint(50,150)
enemyx_change3 = 4
enemyy_change3 = 0.1

# enemy4

enem4 = pygame.image.load('enemy (4).png')
enemy_r4 = pygame.transform.scale(enem4, (50,50))
enemyX4 = random.randint(0,735)
enemyY4 = random.randint(50,150)
enemyx_change4 = 4
enemyy_change4 = 0.1

def enemy1(x,y):
     screen.blit(enemy_r1,(x,y))

def enemy2(x,y):
     screen.blit(enemy_r2,(x,y))

def enemy3(x,y):
     screen.blit(enemy_r3,(x,y))

def enemy4(x,y):
     screen.blit(enemy_r4,(x,y))




# bullet
bullet = pygame.image.load('bullet1.png')
bullet_r = pygame.transform.scale(bullet, (30, 30))
bulletX = 0
bulletY = 480
bulletx_change = 0
bullety_change = 0.8
bullet_stage = "ready"

def fire_bullet(x,y):
     global bullet_stage
     bullet_stage = "fire"
     screen.blit(bullet_r,(x+16,y+10))


def isCollision(enemyX,enemyY,bulletX,bulletY):
     distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
     if distance<27:
          return True
     else:
          False



running = True
score_value = 0
gameOver = 0

# score
font = pygame.font.Font('freesansbold.ttf', 32)

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

fx = 10
fy = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Game loop
while running:
     # Background
     screen.fill((0,0,0))
     # bg image
     screen.blit(bg_r,(0,0))
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    jet_change = -0.4
               if event.key == pygame.K_RIGHT:
                    jet_change = 0.4

               if event.key == pygame.K_SPACE:
                    if bullet_stage is "ready":
                         bullet_sound = mixer.Sound('bullet.mp3')
                         bullet_sound.play()
                         bulletX = jet_imageX
                         fire_bullet(bulletX,bulletY)

          if event.type == pygame.KEYUP:
               if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pass
                    # print("KEY Realesed")




     jet_imageX += jet_change
     if jet_imageX <= 2:
          jet_imageX = 2
     elif jet_imageX >= 748:
          jet_imageX = 748




     # enemy1
     enemyY1 += enemyy_change1
     if enemyX1 <= 2:
          enemyx1_change1 = 0.2
          enemyY1 += enemyy_change1
     elif enemyX1 >= 748:
          enemyx_change1 = -0.2
          enemyY1 += enemyy_change1
     elif enemyY1 >= 550:
          gameOver += 1
          enemyX1 = random.randint(0,735)
          enemyY1 = random.randint(50,150)

     enemyY2 += enemyy_change2
     if enemyX2 <= 2:
          enemyx2_change2 = 0.2
          enemyY2 += enemyy_change2
     elif enemyX2 >= 748:
          enemyx_change2 = -0.2
          enemyY2 += enemyy_change2
     elif enemyY2 >= 550:
          gameOver += 1
          enemyX2 = random.randint(0,735)
          enemyY2 = random.randint(50,150)
     
     enemyY3 += enemyy_change3
     if enemyX3 <= 2:
          enemyx3_change3 = 0.2
          enemyY3 += enemyy_change3
     elif enemyX3 >= 748:
          enemyx_change3 = -0.2
          enemyY3 += enemyy_change3
     elif enemyY3 >= 550:
          gameOver += 1
          enemyX3 = random.randint(0,735)
          enemyY3 = random.randint(50,150)
     
     enemyY4 += enemyy_change4
     if enemyX4 <= 2:
          enemyx4_change4 = 0.2
          enemyY4 += enemyy_change4
     elif enemyX4 >= 748:
          enemyx_change4 = -0.2
          enemyY4 += enemyy_change4
     elif enemyY4 >= 550:
          gameOver += 1
          enemyX4 = random.randint(0,735)
          enemyY4 = random.randint(50,150)
     



     # bullet movement
     if bulletY<=0:
          bulletY = 480
          bullet_stage = "ready"
     if bullet_stage is "fire":
          fire_bullet(bulletX,bulletY)
          bulletY -= bullety_change


     # collision1
     colision1 = isCollision(enemyX1,enemyY1,bulletX,bulletY)
     if colision1:
          explosion_sound = mixer.Sound('explosion.wav')
          explosion_sound.play()
          bulletY  = 480
          bullet_stage = "ready"
          score_value+=1
          print(score_value)
          enemyX1 = random.randint(0,800)
          enemyY1 = random.randint(50,150)

     colision2 = isCollision(enemyX2,enemyY2,bulletX,bulletY)
     if colision2:
          explosion_sound = mixer.Sound('explosion.wav')
          explosion_sound.play()
          bulletY  = 480
          bullet_stage = "ready"
          score_value+=1
          print(score_value)
          enemyX2 = random.randint(0,800)
          enemyY2 = random.randint(50,150)

     colision3 = isCollision(enemyX3,enemyY3,bulletX,bulletY)
     if colision3:
          explosion_sound = mixer.Sound('explosion.wav')
          explosion_sound.play()
          bulletY  = 480
          bullet_stage = "ready"
          score_value+=1
          print(score_value)
          enemyX3 = random.randint(0,800)
          enemyY3 = random.randint(50,150)

     colision4 = isCollision(enemyX4,enemyY4,bulletX,bulletY)
     if colision4:
          explosion_sound = mixer.Sound('explosion.wav')
          explosion_sound.play()
          bulletY  = 480
          bullet_stage = "ready"
          score_value+=1
          print(score_value)
          enemyX4 = random.randint(0,800)
          enemyY4 = random.randint(50,150)


     # gameover
     colision_jet1 = isCollision(enemyX1,enemyY1,jet_imageX,jet_imageY)
     if colision_jet1:
          explosion_sound = mixer.Sound('explosion.wav')
          explosion_sound.play()
          game_over_text()
          score_value = 0
          print("Game Over")
     colision_jet2 = isCollision(enemyX2,enemyY2,jet_imageX,jet_imageY)
     if colision_jet2:
          explosion_sound = mixer.Sound('explosion.wav')
          explosion_sound.play()
          game_over_text()
          score_value = 0
          print("Game Over")
     colision_jet3 = isCollision(enemyX3,enemyY3,jet_imageX,jet_imageY)
     if colision_jet3:
          explosion_sound = mixer.Sound('explosion.wav')
          explosion_sound.play()
          game_over_text()
          score_value = 0
          print("Game Over")
     colision_jet4 = isCollision(enemyX4,enemyY4,jet_imageX,jet_imageY)
     if colision_jet4:
          explosion_sound = mixer.Sound('explosion.wav')
          explosion_sound.play()
          game_over_text()
          score_value = 0
          print("Game Over")

     if gameOver>10:
          game_over_text()
          score_value = 0
          print("Game Over")
          

     jet(jet_imageX,jet_imageY)
     enemy1(enemyX1,enemyY1)
     enemy2(enemyX2,enemyY2)
     enemy3(enemyX3,enemyY3)
     enemy4(enemyX4,enemyY4)
     show_score(fx,fy)
     


     pygame.display.update()


