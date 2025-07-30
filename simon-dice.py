# import pygame
# import random
# import time

# # Inicializar pygame
# pygame.init()

# # Definir los colores
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# GREEN = (0, 255, 0)
# CYAN = (0, 255, 255)  # Color del borde
# WHITE = (255, 255, 255)  # Color del texto

# # Crear la pantalla
# screen_width = 600
# screen_height = 400
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Simón Dice")

# # Definir las posiciones de los cuadrados
# square_size = 100
# square_positions = {
#     'w': pygame.Rect(50, 50, square_size, square_size),   # Rojo
#     'a': pygame.Rect(200, 50, square_size, square_size),  # Azul
#     'd': pygame.Rect(50, 200, square_size, square_size),  # Amarillo
#     's': pygame.Rect(200, 200, square_size, square_size)   # Verde
# }

# # Fuentes
# font = pygame.font.SysFont(None, 40)

# # Función para dibujar los cuadrados con el texto correspondiente
# def draw_squares(highlight=None):
#     # Dibujar los cuadrados de colores
#     pygame.draw.rect(screen, RED, square_positions['w'])
#     pygame.draw.rect(screen, BLUE, square_positions['a'])
#     pygame.draw.rect(screen, YELLOW, square_positions['d'])
#     pygame.draw.rect(screen, GREEN, square_positions['s'])
    
#     # Si hay un cuadrado que debe ser destacado, dibujar el borde celeste
#     if highlight:
#         pygame.draw.rect(screen, CYAN, square_positions[highlight], 5)  # Borde de 5 píxeles
    
#     # Mostrar las teclas dentro de cada cuadrado
#     for key, rect in square_positions.items():
#         text = font.render(key.upper(), True, WHITE)  # Usamos el color blanco para el texto
#         screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

# # Función para mostrar el mensaje en pantalla
# def display_message(message):
#     text = font.render(message, True, (0, 0, 0))
#     screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

# # Función principal del juego
# def game():
#     running = True
#     clock = pygame.time.Clock()
#     start_time = time.time()
#     time_limit = 20  # 20 segundos

#     while running:
#         random_square = random.choice(['w', 'a', 'd', 's'])  # Selección aleatoria del cuadrado a tocar
#         display_message(f"Presiona el cuadrado: {random_square.upper()}")
#         round_in_progress = True
#         start_time = time.time()  # Reiniciar el contador de tiempo cada ronda
        
#         while round_in_progress:
#             screen.fill((255, 255, 255))  # Fondo blanco
#             draw_squares(highlight=random_square)  # Resaltar el cuadrado correcto
            
#             # Contador de tiempo
#             elapsed_time = time.time() - start_time
#             remaining_time = time_limit - elapsed_time
#             if remaining_time <= 0:
#                 round_in_progress = False
#                 display_message("¡Tiempo fuera!")
#             else:
#                 time_text = font.render(f"Tiempo: {int(remaining_time)}s", True, (0, 0, 0))
#                 screen.blit(time_text, (10, 10))

#             # Mostrar el mensaje de la secuencia
#             pygame.display.update()

#             # Comprobar los eventos de teclado
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                     round_in_progress = False
#                 if event.type == pygame.KEYDOWN:
#                     # Si presionó la tecla correcta
#                     if event.key == pygame.K_w and random_square == 'w':
#                         display_message("¡Correcto!")
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     elif event.key == pygame.K_a and random_square == 'a':
#                         display_message("¡Correcto!")
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     elif event.key == pygame.K_d and random_square == 'd':
#                         display_message("¡Correcto!")
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     elif event.key == pygame.K_s and random_square == 's':
#                         display_message("¡Correcto!")
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     # Si presionó la tecla incorrecta
#                     elif (event.key == pygame.K_w and random_square != 'w') or \
#                          (event.key == pygame.K_a and random_square != 'a') or \
#                          (event.key == pygame.K_d and random_square != 'd') or \
#                          (event.key == pygame.K_s and random_square != 's'):
#                         display_message("¡Incorrecto! Fin del juego.")
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de terminar
#                         round_in_progress = False  # Terminar la ronda
#                         running = False  # Terminar la ejecución del juego

#             clock.tick(30)  # Limitar FPS

#     pygame.quit()

# if __name__ == "__main__":
#     game()


# import pygame
# import random
# import time

# # Inicializar pygame
# pygame.init()

# # Definir los colores
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# GREEN = (0, 255, 0)
# CYAN = (0, 255, 255)  # Color del borde
# WHITE = (255, 255, 255)  # Color del texto
# BLACK = (0, 0, 0)  # Fondo negro

# # Crear la pantalla
# screen_width = 600
# screen_height = 400
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Simón Dice")

# # Definir el tamaño de los cuadrados
# square_size = 100
# margin = 50  # Margen entre los cuadrados

# # Calcular posiciones de los cuadrados de forma centrada y distribuidos
# square_positions = {
#     'w': pygame.Rect((screen_width // 2) - square_size - margin, (screen_height // 2) - square_size // 2, square_size, square_size),   # Rojo
#     'a': pygame.Rect((screen_width // 2) + margin, (screen_height // 2) - square_size // 2, square_size, square_size),  # Azul
#     'd': pygame.Rect((screen_width // 2) - square_size - margin, (screen_height // 2) + square_size // 2 + margin, square_size, square_size),  # Amarillo
#     's': pygame.Rect((screen_width // 2) + margin, (screen_height // 2) + square_size // 2 + margin, square_size, square_size)   # Verde
# }

# # Fuentes
# font = pygame.font.SysFont(None, 40)

# # Función para dibujar los cuadrados con el texto correspondiente
# def draw_squares(highlight=None):
#     # Dibujar los cuadrados de colores
#     pygame.draw.rect(screen, RED, square_positions['w'])
#     pygame.draw.rect(screen, BLUE, square_positions['a'])
#     pygame.draw.rect(screen, YELLOW, square_positions['d'])
#     pygame.draw.rect(screen, GREEN, square_positions['s'])
    
#     # Si hay un cuadrado que debe ser destacado, dibujar el borde celeste
#     if highlight:
#         pygame.draw.rect(screen, CYAN, square_positions[highlight], 5)  # Borde de 5 píxeles
    
#     # Mostrar las teclas dentro de cada cuadrado
#     for key, rect in square_positions.items():
#         text = font.render(key.upper(), True, WHITE)  # Usamos el color blanco para el texto
#         screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

# # Función para mostrar el mensaje en pantalla
# def display_message(message, y_position):
#     text = font.render(message, True, WHITE)
#     screen.blit(text, (screen_width // 2 - text.get_width() // 2, y_position))

# # Función principal del juego
# def game():
#     running = True
#     clock = pygame.time.Clock()
#     start_time = time.time()
#     time_limit = 20  # 20 segundos

#     while running:
#         random_square = random.choice(['w', 'a', 'd', 's'])  # Selección aleatoria del cuadrado a tocar
#         display_message(f"Presiona el cuadrado: {random_square.upper()}", 50)
#         round_in_progress = True
#         start_time = time.time()  # Reiniciar el contador de tiempo cada ronda
        
#         while round_in_progress:
#             screen.fill(BLACK)  # Fondo negro
#             draw_squares(highlight=random_square)  # Resaltar el cuadrado correcto
            
#             # Contador de tiempo
#             elapsed_time = time.time() - start_time
#             remaining_time = time_limit - elapsed_time
#             if remaining_time <= 0:
#                 round_in_progress = False
#                 display_message("¡Tiempo fuera!", screen_height // 2 + 50)
#                 pygame.display.update()
#                 pygame.time.wait(1000)  # Esperar 1 segundo antes de finalizar el juego
#                 running = False  # Terminar la ejecución del juego
#             else:
#                 time_text = font.render(f"Tiempo: {int(remaining_time)}s", True, WHITE)
#                 screen.blit(time_text, (screen_width // 2 - time_text.get_width() // 2, 20))  # Colocar el tiempo arriba

#             # Mostrar el mensaje de la secuencia
#             pygame.display.update()

#             # Comprobar los eventos de teclado
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                     round_in_progress = False
#                 if event.type == pygame.KEYDOWN:
#                     # Si presionó la tecla correcta
#                     if event.key == pygame.K_w and random_square == 'w':
#                         display_message("¡Correcto!", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     elif event.key == pygame.K_a and random_square == 'a':
#                         display_message("¡Correcto!", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     elif event.key == pygame.K_d and random_square == 'd':
#                         display_message("¡Correcto!", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     elif event.key == pygame.K_s and random_square == 's':
#                         display_message("¡Correcto!", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     # Si presionó la tecla incorrecta
#                     elif (event.key == pygame.K_w and random_square != 'w') or \
#                          (event.key == pygame.K_a and random_square != 'a') or \
#                          (event.key == pygame.K_d and random_square != 'd') or \
#                          (event.key == pygame.K_s and random_square != 's'):
#                         display_message("¡Incorrecto! Fin del juego.", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de terminar
#                         round_in_progress = False  # Terminar la ronda
#                         running = False  # Terminar la ejecución del juego

#             clock.tick(30)  # Limitar FPS

#     pygame.quit()

# if __name__ == "__main__":
#     game()

# import pygame
# import random
# import time

# # Inicializar pygame
# pygame.init()

# # Cargar la música
# pygame.mixer.music.load('MUSICA QUE ESCUCHAS EN EL SUPERMERCADO [jhxOVckpi10].mp3')
# pygame.mixer.music.play(-1, 0.0)  # Reproducir música en bucle (-1 indica bucle infinito)

# # Definir los colores
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# GREEN = (0, 255, 0)
# CYAN = (0, 255, 255)  # Color del borde
# WHITE = (255, 255, 255)  # Color del texto
# BLACK = (0, 0, 0)  # Fondo negro

# # Crear la pantalla
# screen_width = 600
# screen_height = 400
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Simón Dice")

# # Definir el tamaño de los cuadrados
# square_size = 100
# margin = 50  # Margen entre los cuadrados

# # Calcular posiciones de los cuadrados de forma centrada y más arriba
# square_positions = {
#     'w': pygame.Rect((screen_width // 2) - square_size - margin, (screen_height // 2) - square_size - margin, square_size, square_size),   # Rojo
#     'a': pygame.Rect((screen_width // 2) + margin, (screen_height // 2) - square_size - margin, square_size, square_size),  # Azul
#     'd': pygame.Rect((screen_width // 2) - square_size - margin, (screen_height // 2) + square_size // 2, square_size, square_size),  # Amarillo
#     's': pygame.Rect((screen_width // 2) + margin, (screen_height // 2) + square_size // 2, square_size, square_size)   # Verde
# }

# # Fuentes
# font = pygame.font.SysFont(None, 40)

# # Función para dibujar los cuadrados con el texto correspondiente
# def draw_squares(highlight=None):
#     # Dibujar los cuadrados de colores
#     pygame.draw.rect(screen, RED, square_positions['w'])
#     pygame.draw.rect(screen, BLUE, square_positions['a'])
#     pygame.draw.rect(screen, YELLOW, square_positions['d'])
#     pygame.draw.rect(screen, GREEN, square_positions['s'])
    
#     # Si hay un cuadrado que debe ser destacado, dibujar el borde celeste
#     if highlight:
#         pygame.draw.rect(screen, CYAN, square_positions[highlight], 5)  # Borde de 5 píxeles
    
#     # Mostrar las teclas dentro de cada cuadrado
#     for key, rect in square_positions.items():
#         text = font.render(key.upper(), True, WHITE)  # Usamos el color blanco para el texto
#         screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

# # Función para mostrar el mensaje en pantalla
# def display_message(message, y_position):
#     text = font.render(message, True, WHITE)
#     screen.blit(text, (screen_width // 2 - text.get_width() // 2, y_position))

# # Función principal del juego
# def game():
#     running = True
#     clock = pygame.time.Clock()
#     start_time = time.time()
#     time_limit = 20  # 20 segundos

#     while running:
#         random_square = random.choice(['w', 'a', 'd', 's'])  # Selección aleatoria del cuadrado a tocar
#         display_message(f"Presiona el cuadrado: {random_square.upper()}", 50)
#         round_in_progress = True
#         start_time = time.time()  # Reiniciar el contador de tiempo cada ronda
        
#         while round_in_progress:
#             screen.fill(BLACK)  # Fondo negro
#             draw_squares(highlight=random_square)  # Resaltar el cuadrado correcto
            
#             # Contador de tiempo
#             elapsed_time = time.time() - start_time
#             remaining_time = time_limit - elapsed_time
#             if remaining_time <= 0:
#                 round_in_progress = False
#                 display_message("¡Tiempo fuera!", screen_height // 2 + 50)
#                 pygame.display.update()
#                 pygame.time.wait(1000)  # Esperar 1 segundo antes de finalizar el juego
#                 running = False  # Terminar la ejecución del juego
#             else:
#                 time_text = font.render(f"Tiempo: {int(remaining_time)}s", True, WHITE)
#                 screen.blit(time_text, (screen_width // 2 - time_text.get_width() // 2, 20))  # Colocar el tiempo arriba

#             # Mostrar el mensaje de la secuencia
#             pygame.display.update()

#             # Comprobar los eventos de teclado
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                     round_in_progress = False
#                 if event.type == pygame.KEYDOWN:
#                     # Si presionó la tecla correcta
#                     if event.key == pygame.K_w and random_square == 'w':
#                         display_message("¡Correcto!", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     elif event.key == pygame.K_a and random_square == 'a':
#                         display_message("¡Correcto!", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     elif event.key == pygame.K_d and random_square == 'd':
#                         display_message("¡Correcto!", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     elif event.key == pygame.K_s and random_square == 's':
#                         display_message("¡Correcto!", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
#                         round_in_progress = False  # Terminar la ronda
#                     # Si presionó la tecla incorrecta
#                     elif (event.key == pygame.K_w and random_square != 'w') or \
#                          (event.key == pygame.K_a and random_square != 'a') or \
#                          (event.key == pygame.K_d and random_square != 'd') or \
#                          (event.key == pygame.K_s and random_square != 's'):
#                         display_message("¡Incorrecto! Fin del juego.", screen_height // 2 + 50)
#                         pygame.display.update()
#                         pygame.time.wait(1000)  # Esperar 1 segundo antes de terminar
#                         round_in_progress = False  # Terminar la ronda
#                         running = False  # Terminar la ejecución del juego

#             clock.tick(30)  # Limitar FPS

#     pygame.quit()

# if __name__ == "__main__":
#     game()

import pygame
import random
import time

# Inicializar pygame
pygame.init()

# Cargar la música
pygame.mixer.music.load('MUSICA QUE ESCUCHAS EN EL SUPERMERCADO [jhxOVckpi10].mp3')
pygame.mixer.music.play(-1, 0.0)  # Reproducir música en bucle (-1 indica bucle infinito)

# Definir los colores
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)  # Color del borde
WHITE = (255, 255, 255)  # Color del texto
BLACK = (0, 0, 0)  # Fondo negro

# Crear la pantalla
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simón Dice")

# Definir el tamaño de los cuadrados
square_size = 100
margin = 50  # Margen entre los cuadrados

# Calcular posiciones de los cuadrados de forma centrada y más arriba
square_positions = {
    'w': pygame.Rect((screen_width // 2) - square_size - margin, (screen_height // 2) - square_size - margin, square_size, square_size),   # Rojo
    'a': pygame.Rect((screen_width // 2) + margin, (screen_height // 2) - square_size - margin, square_size, square_size),  # Azul
    'd': pygame.Rect((screen_width // 2) - square_size - margin, (screen_height // 2) + square_size // 2, square_size, square_size),  # Amarillo
    's': pygame.Rect((screen_width // 2) + margin, (screen_height // 2) + square_size // 2, square_size, square_size)   # Verde
}

# Fuentes
font = pygame.font.SysFont(None, 40)

# Función para dibujar los cuadrados con borde circular y el texto correspondiente
def draw_squares(highlight=None):
    # Dibujar los cuadrados de colores con borde circular
    pygame.draw.circle(screen, RED, square_positions['w'].center, square_size // 2)  # Rojo
    pygame.draw.circle(screen, BLUE, square_positions['a'].center, square_size // 2)  # Azul
    pygame.draw.circle(screen, YELLOW, square_positions['d'].center, square_size // 2)  # Amarillo
    pygame.draw.circle(screen, GREEN, square_positions['s'].center, square_size // 2)  # Verde
    
    # Si hay un cuadrado que debe ser destacado, dibujar el borde celeste
    if highlight:
        pygame.draw.circle(screen, CYAN, square_positions[highlight].center, square_size // 2, 5)  # Borde de 5 píxeles
    
    # Mostrar las teclas dentro de cada cuadrado
    for key, rect in square_positions.items():
        text = font.render(key.upper(), True, WHITE)  # Usamos el color blanco para el texto
        screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

# Función para mostrar el mensaje en pantalla
def display_message(message, y_position):
    text = font.render(message, True, WHITE)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, y_position))

# Función principal del juego
def game():
    running = True
    clock = pygame.time.Clock()
    start_time = time.time()
    time_limit = 20  # 20 segundos

    while running:
        random_square = random.choice(['w', 'a', 'd', 's'])  # Selección aleatoria del cuadrado a tocar
        display_message(f"Presiona el cuadrado: {random_square.upper()}", 50)
        round_in_progress = True
        start_time = time.time()  # Reiniciar el contador de tiempo cada ronda
        
        while round_in_progress:
            screen.fill(BLACK)  # Fondo negro
            draw_squares(highlight=random_square)  # Resaltar el cuadrado correcto
            
            # Contador de tiempo
            elapsed_time = time.time() - start_time
            remaining_time = time_limit - elapsed_time
            if remaining_time <= 0:
                round_in_progress = False
                display_message("¡Tiempo fuera!", screen_height // 2 + 70)  # Separar un poco más el texto
                pygame.display.update()
                pygame.time.wait(1000)  # Esperar 1 segundo antes de finalizar el juego
                running = False  # Terminar la ejecución del juego
            else:
                time_text = font.render(f"Tiempo: {int(remaining_time)}s", True, WHITE)
                screen.blit(time_text, (screen_width // 2 - time_text.get_width() // 2, 40))  # Separar un poco más el texto

            # Mostrar el mensaje de la secuencia
            pygame.display.update()

            # Comprobar los eventos de teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    round_in_progress = False
                if event.type == pygame.KEYDOWN:
                    # Si presionó la tecla correcta
                    if event.key == pygame.K_w and random_square == 'w':
                        display_message("¡Correcto!", screen_height // 2 + 70)
                        pygame.display.update()
                        pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
                        round_in_progress = False  # Terminar la ronda
                    elif event.key == pygame.K_a and random_square == 'a':
                        display_message("¡Correcto!", screen_height // 2 + 70)
                        pygame.display.update()
                        pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
                        round_in_progress = False  # Terminar la ronda
                    elif event.key == pygame.K_d and random_square == 'd':
                        display_message("¡Correcto!", screen_height // 2 + 70)
                        pygame.display.update()
                        pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
                        round_in_progress = False  # Terminar la ronda
                    elif event.key == pygame.K_s and random_square == 's':
                        display_message("¡Correcto!", screen_height // 2 + 70)
                        pygame.display.update()
                        pygame.time.wait(1000)  # Esperar 1 segundo antes de la siguiente ronda
                        round_in_progress = False  # Terminar la ronda
                    # Si presionó la tecla incorrecta
                    elif (event.key == pygame.K_w and random_square != 'w') or \
                         (event.key == pygame.K_a and random_square != 'a') or \
                         (event.key == pygame.K_d and random_square != 'd') or \
                         (event.key == pygame.K_s and random_square != 's'):
                        display_message("¡Incorrecto! Fin del juego.", screen_height // 2 + 70)
                        pygame.display.update()
                        pygame.time.wait(1000)  # Esperar 1 segundo antes de terminar
                        round_in_progress = False  # Terminar la ronda
                        running = False  # Terminar la ejecución del juego

            clock.tick(30)  # Limitar FPS

    pygame.quit()

if __name__ == "__main__":
    game()
