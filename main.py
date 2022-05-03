import pygame # import pygame libary
import random
import os #import OS module

pygame.font.init()
# load images from the image asset folder to be used.
BG = pygame.image.load(os.path.join("assets", "background-black.png")) # background image 
main_char = pygame.image.load(os.path.join("assets", "main_char_edit.png")) #main charecter image
Enemy_laser = pygame.image.load(os.path.join("assets", "enemy_laser.png"))
RedLaser = pygame.image.load(os.path.join("assets", "My lazer.png"))
small_enemy = pygame.image.load(os.path.join("assets", "ball_small_enemy.png"))
WIDTH, HEIGHT = 1000, 600 # this will be used for GUI's size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HIVE MIND") #shows games name
full_BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
boss_face = pygame.image.load(os.path.join("assets", "boss_face.jpg"))
small_vel = 1

def interact(item1, item2): # this function will determine if thier is collison.
    Interact_x = item2.x - item1.x
    Interact_y = item2.y - item1.y
    return item1.mask.overlap(item2.mask, (Interact_x, Interact_y)) != None

class Laser:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

    
    def move(self, x):
        self.x += 6

    def move2(self, y):
        self.x -= 6

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class boss:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        self.boss_img = pygame.transform.scale(boss_face, (80, 160))
        self.mask = pygame.mask.from_surface(self.boss_img) #sets the hitbox
        self.alive = True
        self.L_img = pygame.transform.scale(Enemy_laser, (30, 17))

    def move(self,Evel):
        if self.y << HEIGHT and self.y != 0:
            self.y -= Evel
        elif self.y == 0:
            self.y += 600#makes it move up the screen

    def edraw(self, screen):
        screen.blit(self.boss_img, (self.x, self.y))

    def normal_attack(self):
        boss_laser = Laser(self.x, self.y, self.L_img)
        if len(enemy_attack) <= 20:
            enemy_attack.append(boss_laser)

enemy_attack = []

class Smallenemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Smallenemy_image = pygame.transform.scale(small_enemy, (40, 40))
        self.mask = pygame.mask.from_surface(self.Smallenemy_image)# gets me object hitbox

    def move(self, small_vel):
        self.x -= small_vel # determines how fast the object can move and the direction that they are allowed to move

    def sdraw(self, screen):
        screen.blit(self.Smallenemy_image, (self.x, self.y)) #draws the object

attack = []
player_pos = 100
class Player:
    def __init__(self, x, y, health):
        self.x = x#co-ordinate
        self.y = y
        self.health = health
        self.player_image = pygame.transform.scale(main_char, (400, 200)) # allows me to change shape parameters
        self.Lazer_img = pygame.transform.scale(RedLaser, (30, 17)) # sets the image of laser
        self.mask = pygame.mask.from_surface(self.player_image)

    def get_x(self):
        return self.x

    def fire(self): # allows player to fire laser
            player_laser = Laser(self.x+220, self.y+90, self.Lazer_img)
            if len(attack) <= 10: #limits length of list
                attack.append(player_laser)

    def get_width(self):
        return self.player_image.get_width()

    def get_height(self):
        return self.player_image.get_height()  # these two alrgothims get width and height.

    def draw(self, screen):
        screen.blit(self.player_image, (self.x, self.y)) # allows me to draw the object 

attemps = 0

def main():
    main_font = pygame.font.SysFont("pacifico", 50) # sets font and size
    E_font =  pygame.font.SysFont("pacifico", 25)
    Enemies = [] # enemies will be stored here
    lvel = 3
    Evel = 5
    player_vel = 10
    run = True
    FPS = 60
    player_health = 100
    player = Player(player_pos, 50, player_health)
    Clock = pygame.time.Clock()
    bos = boss(900, 400, 15000)
    kills = 0
    dungeon_level = random.choice([1, 2, 3])

    def redraw(Enemies, no_enemies, small_vel, ):# in this function items will be drawn to the screen
        screen.blit(full_BG, (0, 0))
        if player.health <= 0:
            main()# restarts application
        if dungeon_level == 1:# different dungeon levels that are randomly generated
            no_enemies = 5
            if kills >= 100:# the condition to how many kills the player needs to pass the level
                main()# restarts application
        elif dungeon_level == 2:
            no_enemies = 10
            if kills >= 300:
                main()
        elif dungeon_level == 3:
            if bos.alive:
                bos.edraw(screen)# draws boss to screen
                bos_health_text = E_font.render(f"health:{bos.health}", bool(1), (0, 255, 0))
                screen.blit(bos_health_text, (WIDTH - bos_health_text.get_width() - 20, bos.y + 160))  # shows playe the bosses health
                bos.normal_attack()# calls the function that allows the boss to attack
                for i in enemy_attack:
                    i.draw(screen) #draws enemy laser to screen
                    i.move2(lvel)# moves the item left 
            else:
                winner = main_font.render("You have won.", bool(1), (0, 0, 255))
                screen.blit(winner, (WIDTH - winner.get_width() - 400, 250))

            print(bos.health)
            no_enemies = 0


        player.draw(screen)

        for i in attack:# this will draw and move the lasers
            i.draw(screen)
            i.move(lvel)
        for enemy in Enemies:#draw and move the enemies in this function
            enemy.sdraw(screen)
            enemy.move(small_vel)

            if len(Enemies) > no_enemies:
                print(enemy)
                Enemies.pop()

        intro = main_font.render(f"health:{player.health}", bool(1), (0, 255, 0))
        KD = main_font.render(f"Kills:{kills}", bool(1), (0, 255, 0))
        screen.blit(intro, (WIDTH - intro.get_width() - 20, 20))#show player health
        screen.blit(KD, (WIDTH - KD.get_width() - 850, 20))# show the number of kills the player has
        pygame.display.update()


    while run:
        Clock.tick(FPS)#refreshes 60 times per second
        #if len(Enemies) == 0 or len(Enemies) <= 20:
        if len(Enemies) <= 20:
            enemy = Smallenemy(1500, random.randrange(HEIGHT))
            Enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel + player.get_width() > WIDTH/4:# allows player to go right 
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width()/1.6 < WIDTH:# allows player to go left 
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel + player.get_height() > HEIGHT/4.3:#allows player to go up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height()/1.6 < HEIGHT:#allows player to go down
            player.y += player_vel
        if keys[pygame.K_ESCAPE]:
            pygame.quit()# calls event to allow player to exit game
        if keys[pygame.K_SPACE]: # shoots
            player.fire()

        bos.move(Evel)# moves boss object

        for i in attack[:]:
            if i.x - 1 > 1000:# checks to see if the item is off screen
              attack.remove(i)#removes attack from screen

        for i in enemy_attack[:]:
            if interact(i, player):
                player.health -= 5
                enemy_attack.remove(i)
            if i.x + 1 < 0:
                enemy_attack.remove(i)

        for i in attack[:]:
            for k in enemy_attack[:]:
                if interact(k, i) and len(attack) > 0:
                    attack.pop()
                    enemy_attack.pop()


        if bos.health <= 0:
            bos.alive = False
        for i in attack:
            if interact(bos, i):
                bos.health -= 100
                attack.remove(i)

        for k in Enemies[:]:
            if interact(k, player):
                Enemies.remove(k)# if enemy interacts then its removed
                player.health -= 10#decreases player health
            for i in attack:
                if interact(k, i) and len(Enemies) >> 0:
                    Enemies.pop()# remove enemies from screen
                    kills = kills+1# increases kill counter
            if k.x - 1 < 0:
              Enemies.remove(k)



        redraw(Enemies, 5, 15)


main()
