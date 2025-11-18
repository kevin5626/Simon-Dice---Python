import pygame
import random
import time
import mysql.connector
import serial

arduino = serial.Serial('COM3', 9600, timeout=0.01)

# ----------------------------
# MYSQL
# ----------------------------
db_config = {
     'host': 'localhost',
     'user': 'root',
     'password': '1234',
     'database': 'simon_game'
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# ----------------------------
# PYGAME
# ----------------------------
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('MUSICA QUE ESCUCHAS EN EL SUPERMERCADO [jhxOVckpi10].mp3')
pygame.mixer.music.play(-1)

RED = (255, 80, 80)
BLUE = (80, 150, 255)
YELLOW = (255, 230, 80)
GREEN = (80, 255, 140)
WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
CYAN = (0, 255, 255)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

font_big = pygame.font.SysFont(None, 70)
font_small = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()


# ----------------------------
# FUNCIONES
# ----------------------------
def ask_player_name():
    name = ""
    while True:
        screen.fill(BLACK)

        draw_center_text("Ingrese su nombre:", screen_height//3, font_big)
        draw_center_text(name, screen_height//2, font_big, WHITE)
        draw_center_text("Enter para continuar — ESC para salir", screen_height - 100, font_small)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); exit()
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if name != "":
                        return name
                else:
                    if len(name) < 20:
                        name += event.unicode


circle_radius = 140
margin = 200

circle_positions = {
    '0': ((screen_width//2 - margin), (screen_height//2 - margin)),
    '1': ((screen_width//2 + margin), (screen_height//2 - margin)),
    '2': ((screen_width//2 - margin), (screen_height//2 + margin)),
    '3': ((screen_width//2 + margin), (screen_height//2 + margin)),
}

circle_colors = {
    '0': RED,
    '1': BLUE,
    '2': YELLOW,
    '3': GREEN
}

def draw_center_text(text, y, font, color=WHITE):
    msg = font.render(text, True, color)
    screen.blit(msg, (screen_width//2 - msg.get_width()//2, y))


def draw_all_circles(highlight=None):
    for k, (cx, cy) in circle_positions.items():
        pygame.draw.circle(screen, circle_colors[k], (cx, cy), circle_radius)

        if highlight == k:
            pygame.draw.circle(screen, CYAN, (cx, cy), circle_radius + 10, 6)


def animate_glow(key):
    cx, cy = circle_positions[key]
    base_color = circle_colors[key]

    for glow in range(0, 160, 15):
        screen.fill(BLACK)
        draw_all_circles(highlight=key)

        bright = (
            min(base_color[0] + glow, 255),
            min(base_color[1] + glow, 255),
            min(base_color[2] + glow, 255)
        )

        pygame.draw.circle(screen, bright, (cx, cy), circle_radius)
        pygame.display.update()
        pygame.time.delay(30)

    for glow in range(160, 0, -15):
        screen.fill(BLACK)
        draw_all_circles(highlight=key)

        bright = (
            min(base_color[0] + glow, 255),
            min(base_color[1] + glow, 255),
            min(base_color[2] + glow, 255)
        )

        pygame.draw.circle(screen, bright, (cx, cy), circle_radius)
        pygame.display.update()
        pygame.time.delay(30)


# -------------------------------------------------
# LECTURA DE ARDUINO
# -------------------------------------------------
def read_arduino_key():
    try:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode(errors="ignore").strip()
            if data in ["0", "1", "2", "3"]:
                return data
        return None
    except:
        return None


# -------------------------------------------------
# ESPERA HASTA QUE NO HAYA PULSOS (SOLTAR BOTÓN)
# -------------------------------------------------
def wait_button_release(timeout_ms=250):
    release_start = pygame.time.get_ticks()

    while True:

        # ESC para salir
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit(); exit()

        key = read_arduino_key()

        if key is not None:
            release_start = pygame.time.get_ticks()

        if pygame.time.get_ticks() - release_start > timeout_ms:
            return

        clock.tick(60)


# -------------------------------------------------
# ESTADÍSTICAS
# -------------------------------------------------
def show_stats(stats):
    rounds, correct, incorrect, avg_reaction = stats

    while True:
        screen.fill(BLACK)
        draw_center_text("Estadísticas del Juego", 100, font_big, CYAN)
        draw_center_text(f"Rondas jugadas: {rounds}", 250, font_small)
        draw_center_text(f"Aciertos: {correct}", 310, font_small)
        draw_center_text(f"Errores: {incorrect}", 370, font_small)
        draw_center_text(f"Tiempo promedio: {avg_reaction:.3f} s", 430, font_small)
        draw_center_text("ESC para salir — R para reiniciar — E volver a comenzar", screen_height - 120, font_small)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); exit()
                if event.key == pygame.K_e:
                    game()
                if event.key == pygame.K_r:
                    return "RETRY"


# =====================================================
#              JUEGO PRINCIPAL (MODIFICADO)
# =====================================================
def game(player_name=None):

    # ✔ Si NO hay nombre, lo pide
    if player_name is None:
        player_name = ask_player_name()

    round_number = 1
    correct = 0
    incorrect = 0
    reaction_times = []

    while True:
        target = random.choice(['0','1','2','3'])

        animate_glow(target)
        wait_button_release()

        time_limit = max(5, 60 - (round_number - 1) * 2)
        start_time = time.time()

        pressed = None

        while pressed is None:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); exit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit(); exit()

                    # ✔ Reinicio sin pedir nombre
                    if event.key == pygame.K_r:
                        return game(player_name)

            elapsed = time.time() - start_time
            remaining = time_limit - elapsed

            if remaining <= 0:
                avg_reaction = sum(reaction_times) / len(reaction_times) if reaction_times else 0
                show_stats((round_number - 1, correct, incorrect + 1, avg_reaction))
                return

            pressed = read_arduino_key()

            screen.fill(BLACK)
            draw_all_circles(highlight=target)
            draw_center_text(f"Ronda {round_number}", 80, font_big)
            timer_text = f"{int(remaining):02d}"
            draw_center_text(f"Tiempo: {timer_text}s", 160, font_small, WHITE)

            pygame.display.update()
            clock.tick(60)

        reaction = time.time() - start_time

        cursor.execute("""
            INSERT INTO reaction_times
            (player_name, round_number, target_key, pressed_key, reaction_time)
            VALUES (%s, %s, %s, %s, %s)
        """, (player_name, round_number, target, pressed, reaction))
        conn.commit()

        if pressed == target:
            correct += 1
            reaction_times.append(reaction)
            round_number += 1
        else:
            incorrect += 1
            break

    avg_reaction = sum(reaction_times) / len(reaction_times) if reaction_times else 0
    res = show_stats((round_number - 1, correct, incorrect, avg_reaction))

    # ✔ Reinicia sin pedir nombre
    if res == "RETRY":
        return game(player_name)

# INICIO DEL PROGRAMA
game()
