import pygame
import random
import sys
import math
import asyncio

# --- Configuration ---
WIDTH, HEIGHT = 900, 1020
FPS = 60

# Colors
BG_COLOR = (25, 25, 35)
WHITE = (255, 255, 255)
PEG_COLOR = (140, 145, 165)
PEG_HIGHLIGHT = (180, 185, 200)
BIN_BORDER_COLOR = (60, 65, 80)
TEXT_COLOR = WHITE
DIM_TEXT_COLOR = (210, 210, 220)
ACCENT_GAUSS = (80, 180, 120)
ACCENT_PARETO = (220, 120, 80)
ACCENT_COMPETITION = (130, 100, 220)
BTN_BG = (50, 52, 65)
BTN_HOVER = (70, 72, 90)
BTN_BORDER = (90, 92, 110)

# Board layout
NUM_ROWS = 10
PEG_RADIUS = 5
BALL_RADIUS = 5
LANDED_BALL_RADIUS = 3
LANDED_BALL_STEP = 8
PEG_SPACING_X = 48
PEG_SPACING_Y = 42
BOARD_TOP = 120
CENTER_X = WIDTH // 2

# Bins
NUM_BINS = NUM_ROWS + 1
BIN_WIDTH = PEG_SPACING_X
BIN_TOP = BOARD_TOP + NUM_ROWS * PEG_SPACING_Y + 24
BIN_BOTTOM = HEIGHT - 38

# Ball spawning
SPAWN_INTERVAL = 4
MAX_BALLS = 200

# Modes
MODE_GAUSS = "gaussian"
MODE_PARETO = "pareto"
MODE_COMPETITION = "reputation"

# Ball color palettes per mode
PALETTE_GAUSS = [
    (80, 200, 140), (60, 180, 220), (100, 220, 180), (140, 200, 100),
    (80, 160, 240), (120, 230, 160), (70, 190, 200), (160, 220, 80),
    (90, 170, 255), (50, 210, 170),
]

PALETTE_PARETO = [
    (240, 70, 70), (250, 130, 40), (240, 200, 40), (255, 90, 150),
    (230, 160, 50), (255, 60, 100), (240, 110, 80), (250, 180, 70),
    (220, 50, 130), (255, 150, 30),
]

PALETTE_COMPETITION = [
    (150, 100, 255), (180, 80, 230), (120, 130, 255), (200, 100, 200),
    (100, 80, 240), (170, 120, 250), (140, 60, 220), (190, 140, 255),
    (110, 100, 230), (160, 80, 200),
]


def peg_pos(row, col):
    x = CENTER_X + (col - row / 2.0) * PEG_SPACING_X
    y = BOARD_TOP + row * PEG_SPACING_Y
    return (x, y)


def bin_center_x(index):
    return CENTER_X + (index - NUM_ROWS / 2.0) * BIN_WIDTH


def generate_choices(mode, bin_counts=None):
    choices = []
    if mode == MODE_GAUSS:
        for _ in range(NUM_ROWS):
            choices.append(random.randint(0, 1))
    elif mode == MODE_PARETO:
        num_lefts = 0
        for row in range(NUM_ROWS):
            n = max(num_lefts, 1)
            p_right = 0.5 / n
            if random.random() < p_right:
                choices.append(1)
            else:
                choices.append(0)
                num_lefts += 1
    elif mode == MODE_COMPETITION:
        num_rights = 0
        for row in range(NUM_ROWS):
            k = sum(bin_counts[num_rights + 1:]) if bin_counts else 0
            if k > 0:
                p_right = min(0.5 / k, 0.5)
            else:
                p_right = 0.5
            if random.random() < p_right:
                choices.append(1)
                num_rights += 1
            else:
                choices.append(0)
    return choices


class Ball:
    def __init__(self, mode, bin_counts=None):
        self.choices = generate_choices(mode, bin_counts)
        self.final_bin = sum(self.choices)
        self.path = self._build_path()
        self.segment = 0
        self.t = 0.0
        self.speed = random.uniform(0.028, 0.042)
        self.x, self.y = self.path[0]
        self.landed = False
        palettes = {MODE_GAUSS: PALETTE_GAUSS, MODE_PARETO: PALETTE_PARETO, MODE_COMPETITION: PALETTE_COMPETITION}
        palette = palettes[mode]
        self.color = random.choice(palette)
        self.color = tuple(
            max(0, min(255, c + random.randint(-15, 15))) for c in self.color
        )

    def _build_path(self):
        path = [(CENTER_X, BOARD_TOP - 20)]
        col = 0
        for row in range(NUM_ROWS):
            px, py = peg_pos(row, col)
            d = self.choices[row]
            offset_x = (-1 if d == 0 else 1) * (PEG_RADIUS + BALL_RADIUS + 2)
            path.append((px + offset_x, py + PEG_RADIUS + BALL_RADIUS))
            col += d
        bx = bin_center_x(self.final_bin)
        path.append((bx, BIN_TOP + 15))
        return path

    def update(self):
        if self.landed:
            return
        self.t += self.speed
        if self.t >= 1.0:
            self.t -= 1.0
            self.segment += 1
            if self.segment >= len(self.path) - 1:
                self.landed = True
                self.x, self.y = self.path[-1]
                return
        p0 = self.path[self.segment]
        p1 = self.path[self.segment + 1]
        t_ease = self.t * self.t * (3 - 2 * self.t)
        self.x = p0[0] + (p1[0] - p0[0]) * t_ease
        self.y = p0[1] + (p1[1] - p0[1]) * t_ease

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), BALL_RADIUS)


class Button:
    def __init__(self, x, y, w, h, text, font, color=WHITE, accent=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.color = color
        self.accent = accent

    def draw(self, surface, mouse_pos):
        hovered = self.rect.collidepoint(mouse_pos)
        bg = BTN_HOVER if hovered else BTN_BG
        pygame.draw.rect(surface, bg, self.rect, border_radius=8)
        pygame.draw.rect(surface, BTN_BORDER, self.rect, 1, border_radius=8)
        txt_color = self.accent if self.accent else self.color
        txt = self.font.render(self.text, True, txt_color)
        surface.blit(txt, (
            self.rect.centerx - txt.get_width() // 2,
            self.rect.centery - txt.get_height() // 2,
        ))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


def draw_pixel_coin(surface, cx, cy, radius, label, color, border_color, text_color):
    pygame.draw.circle(surface, border_color, (cx, cy), radius)
    pygame.draw.circle(surface, color, (cx, cy), radius - 3)
    pygame.draw.circle(surface, border_color, (cx, cy), radius - 5, 1)
    for angle_deg in range(0, 360, 30):
        rad = math.radians(angle_deg)
        dx = int(math.cos(rad) * (radius - 4))
        dy = int(math.sin(rad) * (radius - 4))
        surface.set_at((cx + dx, cy + dy), border_color)
    coin_font = pygame.font.SysFont("Helvetica", 14, bold=True)
    txt = coin_font.render(label, True, text_color)
    surface.blit(txt, (cx - txt.get_width() // 2, cy - txt.get_height() // 2))


async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Boards of Destiny")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Helvetica", 21)
    title_font = pygame.font.SysFont("Helvetica", 36, bold=True)
    small_font = pygame.font.SysFont("Helvetica", 17)
    btn_font = pygame.font.SysFont("Helvetica", 20, bold=True)

    # Pre-compute peg positions
    pegs = []
    for row in range(NUM_ROWS):
        for col in range(row + 1):
            pegs.append(peg_pos(row, col))

    # Mode selection buttons
    btn_w, btn_h = 690, 90
    btn_x = CENTER_X - btn_w // 2
    base_y = HEIGHT // 2 - 195
    btn_gauss = Button(btn_x, base_y, btn_w, btn_h,
                       "Classical Galton Board", font, accent=ACCENT_GAUSS)
    btn_pareto = Button(btn_x, base_y + 115, btn_w, btn_h,
                        "Memory Board", font, accent=ACCENT_PARETO)
    btn_competition = Button(btn_x, base_y + 230, btn_w, btn_h,
                             "Competition Board", font, accent=ACCENT_COMPETITION)
    mode_buttons = [
        (btn_gauss, MODE_GAUSS),
        (btn_pareto, MODE_PARETO),
        (btn_competition, MODE_COMPETITION),
    ]

    # Description texts for each button
    mode_descs = {
        MODE_GAUSS: "Random events with equal chances of positive or negative outcomes",
        MODE_PARETO: 'Chance of "success" diminishes with the number of "failures"',
        MODE_COMPETITION: 'Chance of "success" depends on being ahead or behind competitors',
    }

    while True:
        # --- Mode selection screen ---
        mode = None
        while mode is None:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for btn, m in mode_buttons:
                        if btn.clicked(event.pos):
                            mode = m
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        mode = MODE_GAUSS
                    elif event.key == pygame.K_2:
                        mode = MODE_PARETO
                    elif event.key == pygame.K_3:
                        mode = MODE_COMPETITION

            screen.fill(BG_COLOR)

            title = title_font.render("Boards of Destiny", True, WHITE)
            screen.blit(title, (CENTER_X - title.get_width() // 2, 60))

            prompt = font.render("Choose a mode:", True, WHITE)
            screen.blit(prompt, (CENTER_X - prompt.get_width() // 2, 120))

            for btn, m in mode_buttons:
                btn.draw(screen, mouse_pos)
                desc = small_font.render(mode_descs[m], True, DIM_TEXT_COLOR)
                screen.blit(desc, (CENTER_X - desc.get_width() // 2, btn.rect.bottom + 6))

            # Pixel art coins
            coin_y = HEIGHT - 90
            coin_r = 42
            draw_pixel_coin(screen, CENTER_X - 80, coin_y, coin_r,
                            "SUCCESS", (220, 190, 60), (170, 140, 30), (100, 75, 10))
            draw_pixel_coin(screen, CENTER_X + 80, coin_y, coin_r,
                            "FAILURE", (160, 170, 185), (100, 110, 125), (50, 55, 65))

            pygame.display.flip()
            clock.tick(FPS)
            await asyncio.sleep(0)

        # --- Board state ---
        active_balls = []
        bin_counts = [0] * NUM_BINS
        landed_positions = []
        spawn_timer = 0
        total_spawned = 0
        paused = False

        mode_labels = {
            MODE_GAUSS: "Classical Galton Board",
            MODE_PARETO: "Memory Board",
            MODE_COMPETITION: "Competition Board",
        }
        mode_accents = {
            MODE_GAUSS: ACCENT_GAUSS,
            MODE_PARETO: ACCENT_PARETO,
            MODE_COMPETITION: ACCENT_COMPETITION,
        }
        mode_label = mode_labels[mode]
        accent = mode_accents[mode]

        # Control buttons during simulation
        ctrl_btn_w, ctrl_btn_h = 120, 39
        btn_pause = Button(CENTER_X - ctrl_btn_w - 15, 78, ctrl_btn_w, ctrl_btn_h,
                           "Pause", btn_font)
        btn_reset = Button(CENTER_X + 15, 78, ctrl_btn_w, ctrl_btn_h,
                           "Reset", btn_font)

        reset = False
        while not reset:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if btn_pause.clicked(event.pos):
                        paused = not paused
                    elif btn_reset.clicked(event.pos):
                        reset = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reset = True
                    elif event.key == pygame.K_SPACE:
                        paused = not paused

            if not paused:
                spawn_timer += 1
                if spawn_timer >= SPAWN_INTERVAL and total_spawned < MAX_BALLS:
                    spawn_timer = 0
                    active_balls.append(Ball(mode, bin_counts))
                    total_spawned += 1

                for ball in active_balls:
                    ball.update()

                still_active = []
                for ball in active_balls:
                    if ball.landed:
                        b = ball.final_bin
                        bin_counts[b] += 1
                        bx = bin_center_x(b)
                        by = BIN_BOTTOM - (bin_counts[b] - 1) * LANDED_BALL_STEP - LANDED_BALL_RADIUS
                        landed_positions.append((bx, by, ball.color))
                    else:
                        still_active.append(ball)
                active_balls = still_active

            # --- Draw ---
            screen.fill(BG_COLOR)

            # Title
            title_surf = title_font.render("Boards of Destiny", True, WHITE)
            screen.blit(title_surf, (CENTER_X - title_surf.get_width() // 2, 10))

            # Mode label
            mode_surf = font.render(f"Mode: {mode_label}", True, accent)
            screen.blit(mode_surf, (CENTER_X - mode_surf.get_width() // 2, 52))

            # Ball counter
            counter = small_font.render(f"Balls: {total_spawned}/{MAX_BALLS}", True, DIM_TEXT_COLOR)
            screen.blit(counter, (15, 84))

            # Control buttons
            btn_pause.text = "Resume" if paused else "Pause"
            btn_pause.draw(screen, mouse_pos)
            btn_reset.draw(screen, mouse_pos)

            # Pegs
            for (px, py) in pegs:
                pygame.draw.circle(screen, PEG_COLOR, (int(px), int(py)), PEG_RADIUS)
                pygame.draw.circle(screen, PEG_HIGHLIGHT, (int(px) - 1, int(py) - 1), max(1, PEG_RADIUS // 2))

            # Bin dividers
            for i in range(NUM_BINS + 1):
                x = int(bin_center_x(0) - BIN_WIDTH / 2 + i * BIN_WIDTH)
                pygame.draw.line(screen, BIN_BORDER_COLOR, (x, BIN_TOP), (x, BIN_BOTTOM), 2)

            # Bin bottom
            left_x = int(bin_center_x(0) - BIN_WIDTH / 2)
            right_x = int(bin_center_x(NUM_BINS - 1) + BIN_WIDTH / 2)
            pygame.draw.line(screen, BIN_BORDER_COLOR, (left_x, BIN_BOTTOM), (right_x, BIN_BOTTOM), 2)

            # Bin labels
            for i in range(NUM_BINS):
                if bin_counts[i] > 0:
                    label = small_font.render(str(bin_counts[i]), True, DIM_TEXT_COLOR)
                    lx = int(bin_center_x(i)) - label.get_width() // 2
                    screen.blit(label, (lx, BIN_BOTTOM + 8))

            # Landed balls
            for (bx, by, color) in landed_positions:
                pygame.draw.circle(screen, color, (int(bx), int(by)), LANDED_BALL_RADIUS)

            # Active balls
            for ball in active_balls:
                ball.draw(screen)

            # Paused indicator
            if paused:
                pause_surf = title_font.render("PAUSED", True, (255, 255, 100))
                screen.blit(pause_surf, (CENTER_X - pause_surf.get_width() // 2, HEIGHT // 2 - 30))

            pygame.display.flip()
            clock.tick(FPS)
            await asyncio.sleep(0)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
