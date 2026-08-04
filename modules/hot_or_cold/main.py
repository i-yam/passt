"""
Regression Quest — two-player linear regression exploration game.

Each player has their own weight-space panel (side by side).
Players alternate turns clicking in their panel to find the best linear fit.
Dots are coloured red (hot/low error) to blue (cold/high error).
After each guess: WARMER or COLDER vs your own last pick.
10 turns total. Lowest MSE wins.

Deploy with:
    pip install pygbag
    pygbag main.py
Then upload build/web/ to GitHub Pages.
"""

import asyncio, math, colorsys, random
import pygame

def _linspace(a, b, n):
    return [a + (b - a) * i / (n - 1) for i in range(n)]

# ── Layout ─────────────────────────────────────────────────────────────────────
SW, SH   = 960, 600
PANEL_W  = SW // 2      # 480  — each player's panel
TBAR     = 42           # top bar height (title + turn counter)
GS       = 370          # grid size (square)
GML      = 55           # left margin within panel (room for y-axis labels)
GMT      = 78           # y of grid top  (= TBAR + 36 for player header)
# right margin within panel: PANEL_W - GML - GS = 55  ✓
# below-grid space:          SH - (GMT + GS) = 152 px ✓

# ── Game settings ──────────────────────────────────────────────────────────────
WLO, WHI = -5.0, 5.0
WRANGE   = WHI - WLO
TURNS    = 10

# ── Palette ────────────────────────────────────────────────────────────────────
BG     = (12,  12,  22)
GRIDBG = (18,  18,  32)
GRIDLN = (35,  35,  58)
AXCOL  = (70,  70, 115)
TXT    = (220, 220, 240)
DIM    = (110, 110, 148)
DIV    = (45,  45,  78)
WARM   = (255,  90,  60)
COLD   = ( 60, 120, 255)
PCOL   = [(80, 180, 255), (255, 140, 50)]   # P1 cyan-blue, P2 orange

# ── Coordinate helpers (panel-aware) ───────────────────────────────────────────
def w2p(w0, w1, pi):
    """Weight (w0, w1) → screen pixel in player pi's panel."""
    ox = pi * PANEL_W
    x  = ox + GML + (w0 - WLO) / WRANGE * GS
    y  = GMT + (WHI - w1) / WRANGE * GS
    return int(x), int(y)

def p2w(x, y, pi):
    """Screen pixel → (w0, w1) in player pi's panel."""
    ox = pi * PANEL_W
    return (WLO + (x - ox - GML) / GS * WRANGE,
            WHI - (y - GMT) / GS * WRANGE)

def in_grid(x, y, pi):
    ox = pi * PANEL_W
    return ox + GML <= x <= ox + GML + GS and GMT <= y <= GMT + GS

# ── MSE & colour ───────────────────────────────────────────────────────────────
def calc_mse(xs, ys, w1, w0):
    n = len(xs)
    return sum((y - (w1 * x + w0)) ** 2 for x, y in zip(xs, ys)) / n

def heat(val, lo, hi):
    """MSE → colour: blue (cold/high) → red (hot/low), log-scaled."""
    t = (math.log(val + 0.1) - lo) / (hi - lo + 1e-9)
    t = max(0.0, min(1.0, t))
    r, g, b = colorsys.hsv_to_rgb(t * 0.67, 0.92, 1.0)
    return int(r * 255), int(g * 255), int(b * 255)

# ── Game class ─────────────────────────────────────────────────────────────────
class Game:
    def __init__(self):
        self.phase    = "intro"
        self.fb_text  = ["", ""]
        self.fb_timer = [0, 0]
        self._gen_data()

    def _gen_data(self):
        tw1 = random.uniform(-2.5, 2.5)
        tw0 = random.uniform(-2.5, 2.5)
        xs  = [random.uniform(-4.5, 4.5) for _ in range(30)]
        ys  = [tw1 * x + tw0 + random.gauss(0, 0.9) for x in xs]
        self.xs, self.ys = xs, ys
        vals = [calc_mse(xs, ys, v1, v0)
                for v0 in _linspace(WLO, WHI, 20)
                for v1 in _linspace(WLO, WHI, 20)]
        self.log_lo = math.log(min(vals) + 0.1)
        self.log_hi = math.log(max(vals) + 0.1)

    def start(self):
        self._gen_data()
        self.guesses   = []
        self.turn      = 0
        self.player    = 0
        self.last_mse  = [None, None]
        self.best      = [None, None]
        self.fb_text   = ["", ""]
        self.fb_timer  = [0, 0]
        self.phase     = "play"

    def click(self, mx, my):
        p = self.player
        if not in_grid(mx, my, p):
            return
        w0, w1 = p2w(mx, my, p)
        w0 = max(WLO, min(WHI, w0))
        w1 = max(WLO, min(WHI, w1))

        v  = calc_mse(self.xs, self.ys, w1, w0)
        lm = self.last_mse[p]

        if lm is not None:
            self.fb_text[p]  = "WARMER!" if v < lm else "COLDER!"
            self.fb_timer[p] = 150
        else:
            self.fb_text[p] = ""

        self.last_mse[p] = v

        if self.best[p] is None or v < self.best[p]["mse"]:
            self.best[p] = {"w0": w0, "w1": w1, "mse": v}

        self.guesses.append({
            "w0": w0, "w1": w1, "mse": v,
            "col": heat(v, self.log_lo, self.log_hi),
            "p": p,
        })

        self.turn += 1
        if self.turn >= TURNS:
            self.phase = "reveal"
        else:
            self.player = 1 - self.player

    def tick(self):
        for i in range(2):
            if self.fb_timer[i] > 0:
                self.fb_timer[i] -= 1

# ── Top bar ────────────────────────────────────────────────────────────────────
def draw_topbar(s, game, F):
    pygame.draw.rect(s, (20, 20, 36), (0, 0, SW, TBAR))
    pygame.draw.line(s, DIV, (0, TBAR), (SW, TBAR), 1)

    if game.phase == "play":
        label = F["ti"].render(
            f"REGRESSION QUEST          Turn {game.turn + 1} of {TURNS}", True, TXT)
    elif game.phase == "reveal":
        label = F["ti"].render(
            f"REGRESSION QUEST          All {TURNS} turns played!", True, TXT)
    else:
        label = F["ti"].render("REGRESSION QUEST", True, TXT)
    s.blit(label, (SW // 2 - label.get_width() // 2,
                   TBAR // 2 - label.get_height() // 2))

# ── One player's panel ─────────────────────────────────────────────────────────
def draw_panel(s, game, F, pi):
    ox     = pi * PANEL_W
    pc     = PCOL[pi]
    active = (game.phase == "play" and game.player == pi)

    # ── player header (between top bar and grid) ──────────────────────────────
    if active:
        hdr = F["ti"].render(f"> Player {pi + 1}  —  YOUR TURN", True, pc)
    else:
        hdr = F["nm"].render(f"   Player {pi + 1}", True, DIM)
    s.blit(hdr, (ox + GML, TBAR + (36 - hdr.get_height()) // 2))

    # ── grid background ───────────────────────────────────────────────────────
    pygame.draw.rect(s, GRIDBG, (ox + GML, GMT, GS, GS))

    # ── gridlines ─────────────────────────────────────────────────────────────
    for v in range(-5, 6):
        gx = ox + GML + (v - WLO) / WRANGE * GS
        gy = GMT + (WHI - v) / WRANGE * GS
        c  = AXCOL if v == 0 else GRIDLN
        pygame.draw.line(s, c, (int(gx), GMT),        (int(gx), GMT + GS))
        pygame.draw.line(s, c, (ox + GML, int(gy)),   (ox + GML + GS, int(gy)))

    # ── grid border (highlighted for active player) ───────────────────────────
    pygame.draw.rect(s, pc if active else AXCOL,
                     (ox + GML, GMT, GS, GS), 3 if active else 2)

    # ── tick labels ───────────────────────────────────────────────────────────
    sf = F["sm"]
    for v in [-4, -2, 0, 2, 4]:
        gx = ox + GML + (v - WLO) / WRANGE * GS
        gy = GMT + (WHI - v) / WRANGE * GS
        lx = sf.render(str(v), True, DIM)
        ly = sf.render(str(v), True, DIM)
        s.blit(lx, (int(gx) - lx.get_width() // 2,  GMT + GS + 5))
        s.blit(ly, (ox + GML - ly.get_width() - 5,   int(gy) - ly.get_height() // 2))

    # ── axis names ────────────────────────────────────────────────────────────
    xl = F["sm"].render("w_0  (intercept)", True, TXT)
    s.blit(xl, (ox + GML + GS // 2 - xl.get_width() // 2, GMT + GS + 26))
    yl = pygame.transform.rotate(F["sm"].render("w_1  (slope)", True, TXT), 90)
    s.blit(yl, (ox + 3, GMT + GS // 2 - yl.get_height() // 2))

    # ── guesses (only this player's) ─────────────────────────────────────────
    p_guesses = [g for g in game.guesses if g["p"] == pi]
    for i, g in enumerate(p_guesses):
        px, py = w2p(g["w0"], g["w1"], pi)
        pygame.draw.circle(s, g["col"], (px, py), 8)
        pygame.draw.circle(s, pc,       (px, py), 8, 2)
        if i == len(p_guesses) - 1:          # extra ring on most recent dot
            pygame.draw.circle(s, pc, (px, py), 13, 2)

    # ── below-grid: feedback + score ─────────────────────────────────────────
    gy  = GMT + GS
    cx  = ox + GML + GS // 2       # horizontal centre of the grid

    txt, fr = game.fb_text[pi], game.fb_timer[pi]
    if txt and fr > 0:
        fc  = WARM if txt == "WARMER!" else COLD
        fbl = F["bg"].render(txt, True, fc)
        s.blit(fbl, (cx - fbl.get_width() // 2, gy + 22))

    b = game.best[pi]
    if b:
        ml = F["nm"].render(f"Best  MSE = {b['mse']:.2f}", True, pc)
        s.blit(ml, (cx - ml.get_width() // 2, gy + 68))
    else:
        wl = F["sm"].render("no guesses yet", True, DIM)
        s.blit(wl, (cx - wl.get_width() // 2, gy + 72))

    n   = len(p_guesses)
    nl  = F["sm"].render(f"{n} / {TURNS // 2} guesses", True, DIM)
    s.blit(nl, (cx - nl.get_width() // 2, gy + 100))

# ── Reveal overlay (shown after last turn, before results) ────────────────────
def draw_reveal_overlay(s, F):
    bar = pygame.Surface((SW, 100))
    bar.set_alpha(220)
    bar.fill((8, 8, 20))
    s.blit(bar, (0, SH // 2 - 50))
    msg = F["bg"].render("Click to find out who is the winner!", True, (200, 230, 170))
    s.blit(msg, (SW // 2 - msg.get_width() // 2, SH // 2 - msg.get_height() // 2))

# ── End screen: scatter plot (left panel) ─────────────────────────────────────
def draw_scatter(s, game, F):
    ox   = 0
    xs, ys = game.xs, game.ys
    xmin, xmax = -5.0, 5.0
    mg   = 0.8
    ymin = min(ys) - mg
    ymax = max(ys) + mg

    def d2p(x, y):
        px = ox + GML + (x - xmin) / (xmax - xmin) * GS
        py = GMT + (ymax - y) / (ymax - ymin) * GS
        return int(px), int(py)

    pygame.draw.rect(s, GRIDBG, (ox + GML, GMT, GS, GS))
    pygame.draw.rect(s, AXCOL,  (ox + GML, GMT, GS, GS), 2)

    for x, y in zip(xs, ys):
        pygame.draw.circle(s, TXT, d2p(x, y), 4)

    s.set_clip(pygame.Rect(ox + GML, GMT, GS, GS))
    for pi, b in enumerate(game.best):
        if b:
            pygame.draw.line(s, PCOL[pi],
                             d2p(xmin, b["w1"] * xmin + b["w0"]),
                             d2p(xmax, b["w1"] * xmax + b["w0"]), 3)
    s.set_clip(None)

    # legend
    sf = F["sm"]
    for pi, lbl in enumerate(["P1 best", "P2 best"]):
        if game.best[pi]:
            lx = ox + GML + 10 + pi * 100
            ly = GMT + GS - 14
            pygame.draw.line(s, PCOL[pi], (lx, ly), (lx + 28, ly), 3)
            l = sf.render(lbl, True, PCOL[pi])
            s.blit(l, (lx + 32, ly - l.get_height() // 2))

    hdr = F["ti"].render("BEST FITS", True, TXT)
    s.blit(hdr, (ox + GML + GS // 2 - hdr.get_width() // 2, TBAR + 8))

# ── End screen: results (right panel) ─────────────────────────────────────────
def draw_end_right(s, game, F):
    nf, tf, bf, sf = F["nm"], F["ti"], F["bg"], F["sm"]
    x = PANEL_W + 30
    y = TBAR + 20

    s.blit(tf.render("RESULTS", True, TXT), (x, y)); y += 48

    b0, b1 = game.best[0], game.best[1]
    if b0 and b1:
        if   b0["mse"] < b1["mse"]: winner, wc = "Player 1 wins!", PCOL[0]
        elif b1["mse"] < b0["mse"]: winner, wc = "Player 2 wins!", PCOL[1]
        else:                        winner, wc = "It's a tie!",    TXT
    else:
        winner, wc = "—", TXT

    s.blit(bf.render(winner, True, wc), (x, y)); y += 52

    pygame.draw.line(s, DIV, (PANEL_W + 15, y), (SW - 15, y)); y += 18

    for pi in range(2):
        b = game.best[pi]
        s.blit(nf.render(f"Player {pi + 1}:", True, PCOL[pi]), (x, y)); y += 26
        if b:
            s.blit(sf.render(f"  w_0 = {b['w0']:+.2f}", True, PCOL[pi]), (x, y)); y += 20
            s.blit(sf.render(f"  w_1 = {b['w1']:+.2f}", True, PCOL[pi]), (x, y)); y += 20
            s.blit(sf.render(f"  MSE = {b['mse']:.3f}", True, PCOL[pi]), (x, y)); y += 32
        else:
            s.blit(sf.render("  no guesses", True, DIM), (x, y)); y += 32

    pygame.draw.line(s, DIV, (PANEL_W + 15, y), (SW - 15, y)); y += 18
    s.blit(nf.render("Press SPACE or click to play again", True, DIM), (x, y))

# ── Intro screen ───────────────────────────────────────────────────────────────
def draw_intro(s, F):
    nf, bf, sf = F["nm"], F["bg"], F["sm"]
    y = 60

    tt = bf.render("REGRESSION QUEST", True, TXT)
    s.blit(tt, (SW // 2 - tt.get_width() // 2, y)); y += 62

    rows = [
        (nf, "Two players each get their own weight-space panel.", TXT),
        (nf, "Each click tests a slope w_1 and intercept w_0 pair.", TXT),
        (sf, "", DIM),
        (nf, "Dot colour shows how good your guess is:", TXT),
        (nf, "  RED   = low error   (HOT  — you're close!)",  WARM),
        (nf, "  BLUE  = high error  (COLD — keep searching)", COLD),
        (sf, "", DIM),
        (nf, "After each guess you'll see WARMER or COLDER", TXT),
        (nf, "compared to your own previous guess.", DIM),
        (sf, "", DIM),
        (nf, "10 turns total, alternating between players.", TXT),
        (nf, "Lowest MSE at the end wins!", TXT),
        (sf, "", DIM),
        (bf, "Press  SPACE  or click to start", (155, 220, 155)),
    ]
    for font, text, color in rows:
        if text:
            t = font.render(text, True, color)
            s.blit(t, (SW // 2 - t.get_width() // 2, y))
        y += font.get_height() + 6

# ── Main ───────────────────────────────────────────────────────────────────────
async def main():
    pygame.init()
    screen = pygame.display.set_mode((SW, SH))
    pygame.display.set_caption("Regression Quest")
    clock = pygame.time.Clock()

    F = {
        "bg": pygame.font.Font(None, 38),
        "ti": pygame.font.Font(None, 28),
        "nm": pygame.font.Font(None, 22),
        "sm": pygame.font.Font(None, 17),
    }

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                if game.phase in ("intro", "end"):
                    game.start()
                elif game.phase == "reveal":
                    game.phase = "end"
                elif game.phase == "play":
                    game.click(mx, my)

        game.tick()
        screen.fill(BG)

        if game.phase == "intro":
            draw_intro(screen, F)
        elif game.phase in ("play", "reveal"):
            draw_topbar(screen, game, F)
            draw_panel(screen, game, F, 0)
            draw_panel(screen, game, F, 1)
            pygame.draw.line(screen, DIV, (PANEL_W, TBAR), (PANEL_W, SH), 2)
            if game.phase == "reveal":
                draw_reveal_overlay(screen, F)
        else:  # end
            draw_topbar(screen, game, F)
            draw_scatter(screen, game, F)
            draw_end_right(screen, game, F)
            pygame.draw.line(screen, DIV, (PANEL_W, TBAR), (PANEL_W, SH), 2)

        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(60)

asyncio.run(main())
