import pygame
pygame.mixer.pre_init(44100, 16, 2, 4096) 
pygame.init()
class Jogadores:
	def __init__(self,xpos,ypos):
		self.xpos=xpos
		self.ypos=ypos
	
	
#criamos 2 objetos simbolizando cada jogador
jogador1= Jogadores(100,0)
jogador2=Jogadores(890,0)

class Bola:
	def __init__(self,xpos,ypos):
		self.xpos=xpos
		self.ypos=ypos

#criar o objeto da bola		-
bola1=Bola(495,295)
#Sons
def som_tabela():
	game_over = pygame.mixer.Sound("pong1.wav")
	pygame.mixer.Sound.play(game_over)
def som_derrota():
	game_over = pygame.mixer.Sound("Pong_lose.wav")
	pygame.mixer.Sound.play(game_over)
def som_parede():
	game_over = pygame.mixer.Sound("som_parede.wav")
	pygame.mixer.Sound.play(game_over)
	
#definir a estrutura do ecra(dimensoes,titulo,assim como a estrutura dos objetos jogadores(retangulos)
background_colour = (0,0,0)
branco=(250,250,250)
(width, height) = (1000, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')
screen.fill(background_colour)
paddle1=pygame.draw.rect(screen,branco,[jogador1.xpos,jogador1.ypos,10,50])
paddle2=pygame.draw.rect(screen,branco,[jogador2.xpos,jogador2.ypos,10,50])
pygame.display.flip()

#pontuacao,velocidade da bola
margem_sup=0
margem_inf=600
velx=-3
vely=-3
pontuacao1=0
pontuacao2=0
def intro_jogo():
	intro=True
	while intro:
		pygame.time.delay(delay)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		keys=pygame.key.get_pressed()
def jogo():
	global margem_inf,margem_sup,velx,vely,pontuacao1,pontuacao2
	bola1.xpos,bola1.ypos=495,295
	running = True
	delay=15
	while running:
		pygame.time.delay(delay)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		keys=pygame.key.get_pressed()
		#jogador1
		if keys[pygame.K_w] and jogador1.ypos>=0:
				
			jogador1.ypos -=5
		if keys[pygame.K_s] and jogador1.ypos<=550:
			jogador1.ypos +=5
	
		#jogador 2
		if keys[pygame.K_UP] and jogador2.ypos>=0:
				
			jogador2.ypos -=5
		if keys[pygame.K_DOWN] and jogador2.ypos<=550:
			jogador2.ypos +=5
		bola1.xpos+= velx
		bola1.ypos+=vely
		#margemsuperior/etc..
		if bola1.ypos in [-1,0,1]:
			vely=3
			som_parede()
		#paddle1
		if bola1.xpos in [108,109, 110] and jogador1.ypos-2 <= bola1.ypos <=(jogador1.ypos +52):
			som_tabela()
			velx=3
			delay-=1
			
		#margeminferior
		if bola1.ypos in [600,601]:
			vely=-3
			som_parede()
		#paddle2
		if bola1.xpos in [889,890, 891] and jogador2.ypos <= bola1.ypos <=(jogador2.ypos +52):
			som_tabela()
			velx=-3
			delay-=1
		#pontos
		if bola1.xpos in [-1,0,1]:
			pontuacao2+=1
			som_derrota()
			print(pontuacao2)
			if pontuacao2==8:
				print("Vitoria da jogador2!")
				quit()
			jogo()
		if bola1.xpos in [999, 1000, 1001]:
			pontuacao1+=1
			som_derrota()
			print(pontuacao1)
		
			if pontuacao1==8:
				print("Vitoria da jogador1!")
				quit()
			jogo()
		screen.fill((0,0,0))
		paddle1=pygame.draw.rect(screen,branco,[jogador1.xpos,jogador1.ypos,10,50])
		paddle2=pygame.draw.rect(screen,branco,[jogador2.xpos,jogador2.ypos,10,50])
		#movimento bola
		ball=pygame.draw.rect(screen,branco,[bola1.xpos,bola1.ypos,10,10])
		

		pygame.display.update()
jogo()

