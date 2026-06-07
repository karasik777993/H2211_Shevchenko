import random
import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- CONFIG & THEME ----------------
COLORS = {
    "bg_dark": "#0f172a",  # slate-900
    "bg_panel": "#1e293b",  # slate-800
    "text_primary": "#f8fafc",  # slate-50
    "text_secondary": "#94a3b8",  # slate-400
    "accent": "#38bdf8",  # sky-400
    "danger": "#ef4444",  # red-500
    "success": "#22c55e",  # green-500
    "warning": "#f59e0b",  # amber-500
}

FONTS = {
    "title": ("Segoe UI", 28, "bold"),
    "header": ("Segoe UI", 16, "bold"),
    "body": ("Segoe UI", 11),
    "stat": ("Segoe UI", 10, "bold"),
    "log": ("Consolas", 10),
}

# ---------------- TRANSLATIONS ----------------
TEXTS = {
    "en": {
        "title": "LIFE SIMULATOR Pro",
        "start": "START LIFE",
        "day": "Day",
        "age": "Age",
        "money": "Money",
        "iq": "IQ",
        "health": "Health",
        "satiety": "Hunger",
        "stress": "Stress",
        "gladness": "Happiness",
        "actions": "Actions Remaining",
        "death_age": "Passed away peacefully from old age.",
        "death_hunger": "Died of starvation.",
        "death_stress": "Collapsed from extreme stress.",
        "death_health": "Died from poor health.",
        "work_low": "Junior Work",
        "work_med": "Office Work",
        "work_high": "CEO Duties",
        "study": "Study hard",
        "eat_cheap": "Fast Food",
        "eat_med": "Homemade",
        "eat_exp": "Restaurant",
        "chill": "Relax",
        "clean": "Housework",
        "event_found": "You found $20 on the street!",
        "event_ill": "You caught a cold. Health decreased.",
        "event_bonus": "Performance bonus! Extra cash received.",
    },
    "ua": {
        "title": "СИМУЛЯТОР ЖИТТЯ Pro",
        "start": "ПОЧАТИ ЖИТТЯ",
        "day": "День",
        "age": "Вік",
        "money": "Гроші",
        "iq": "IQ",
        "health": "Здоров'я",
        "satiety": "Голод",
        "stress": "Стрес",
        "gladness": "Щастя",
        "actions": "Залишилось дій",
        "death_age": "Помер від старості.",
        "death_hunger": "Помер від голоду.",
        "death_stress": "Серце зупинилося через стрес.",
        "death_health": "Помер через погане здоров'я.",
        "work_low": "Мала робота",
        "work_med": "Офісна робота",
        "work_high": "Директор",
        "study": "Вчитися",
        "eat_cheap": "Фастфуд",
        "eat_med": "Домашня їжа",
        "eat_exp": "Ресторан",
        "chill": "Відпочинок",
        "clean": "Прибирання",
        "event_found": "Ви знайшли 20$!",
        "event_ill": "Ви захворіли. Здоров'я впало.",
        "event_bonus": "Премія за роботу!",
    }
}


# ---------------- LOGIC ----------------
class Human:
    def __init__(self):
        self.age = 18
        self.money = 100
        self.gladness = 50
        self.satiety = 100
        self.stress = 0
        self.intelligence = 10
        self.health = 100
        self.days_lived = 0

    def study(self):
        self.intelligence += 3
        self.stress += 5
        self.gladness -= 2
        self.satiety -= 10

    def work(self, level):
        if level == "low":
            self.money += 20
            self.stress += 10
            self.satiety -= 15
        elif level == "med":
            if self.intelligence >= 30:
                self.money += 60
                self.stress += 15
                self.satiety -= 20
            else:
                return "Not enough IQ for this job!"
        elif level == "high":
            if self.intelligence >= 80:
                self.money += 200
                self.stress += 25
                self.satiety -= 30
            else:
                return "You need 80 IQ to be a leader!"
        return None

    def eat(self, kind):
        costs = {"cheap": (10, 20), "med": (30, 50), "exp": (80, 100)}
        cost, sat = costs[kind]
        if self.money >= cost:
            self.money -= cost
            self.satiety = min(100, self.satiety + sat)
            self.health = min(100, self.health + 2)
            return None
        return "Not enough money!"

    def chill(self):
        self.gladness = min(100, self.gladness + 15)
        self.stress = max(0, self.stress - 20)
        self.satiety -= 5

    def clean(self):
        self.gladness = min(100, self.gladness + 5)
        self.stress = max(0, self.stress - 5)
        self.health = min(100, self.health + 1)
        self.satiety -= 10

    def process_day(self):
        # Aging logic: 1 day = 1 unit of life progress
        self.days_lived += 1
        if self.days_lived % 30 == 0:
            self.age += 1

        # Passive effects
        self.satiety -= 5
        if self.satiety <= 20:
            self.health -= 5
        if self.stress >= 80:
            self.health -= 5
            self.gladness -= 10
        if self.gladness <= 20:
            self.stress += 5


# ---------------- UI ENGINE ----------------
class GameEngine:
    def __init__(self, root):
        self.root = root
        self.lang = "en"
        self.persona = None
        self.actions_left = 5
        self.setup_styles()
        self.show_menu()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        # Progressbar styles
        style.configure("Health.Horizontal.TProgressbar", foreground=COLORS["success"], background=COLORS["success"],
                        thickness=10)
        style.configure("Satiety.Horizontal.TProgressbar", foreground=COLORS["warning"], background=COLORS["warning"],
                        thickness=10)
        style.configure("Stress.Horizontal.TProgressbar", foreground=COLORS["danger"], background=COLORS["danger"],
                        thickness=10)
        style.configure("Gladness.Horizontal.TProgressbar", foreground=COLORS["accent"], background=COLORS["accent"],
                        thickness=10)

    def t(self, key):
        return TEXTS[self.lang].get(key, key)

    def log(self, message, color="white"):
        self.log_widget.configure(state='normal')
        self.log_widget.insert(tk.END, f"» {message}\n", color)
        self.log_widget.tag_config("red", foreground=COLORS["danger"])
        self.log_widget.tag_config("green", foreground=COLORS["success"])
        self.log_widget.tag_config("blue", foreground=COLORS["accent"])
        self.log_widget.see(tk.END)
        self.log_widget.configure(state='disabled')

    def show_menu(self):
        self.clear_screen()
        frame = tk.Frame(self.root, bg=COLORS["bg_dark"])
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text=self.t("title"), font=("Segoe UI", 48, "bold"),
                 fg=COLORS["accent"], bg=COLORS["bg_dark"]).pack(pady=40)

        btn_style = {"font": ("Segoe UI", 14), "width": 20, "pady": 10, "bd": 0, "cursor": "hand2"}

        tk.Button(frame, text="English Interface", bg=COLORS["bg_panel"], fg="white",
                  command=lambda: self.start_game("en"), **btn_style).pack(pady=10)

        tk.Button(frame, text="Українська мова", bg=COLORS["bg_panel"], fg="white",
                  command=lambda: self.start_game("ua"), **btn_style).pack(pady=10)

    def start_game(self, lang):
        self.lang = lang
        self.persona = Human()
        self.actions_left = 5
        self.clear_screen()
        self.setup_game_ui()
        self.update_stats()
        self.log("Game started! Welcome to your new life.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def setup_game_ui(self):
        self.root.configure(bg=COLORS["bg_dark"])

        # Header
        header = tk.Frame(self.root, bg=COLORS["bg_panel"], height=80)
        header.pack(fill="x", side="top")

        self.day_label = tk.Label(header, text="", font=FONTS["header"], bg=COLORS["bg_panel"], fg=COLORS["accent"])
        self.day_label.pack(side="left", padx=30)

        self.actions_label = tk.Label(header, text="", font=FONTS["header"], bg=COLORS["bg_panel"],
                                      fg=COLORS["text_secondary"])
        self.actions_label.pack(side="right", padx=30)

        # Main Layout
        container = tk.Frame(self.root, bg=COLORS["bg_dark"])
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Left Side: Stats
        stats_panel = tk.Frame(container, bg=COLORS["bg_panel"], padx=20, pady=20)
        stats_panel.place(relx=0, rely=0, relwidth=0.3, relheight=0.6)

        self.create_stat_widget(stats_panel, "money", COLORS["success"])
        self.money_val = tk.Label(stats_panel, text="$0", font=FONTS["title"], bg=COLORS["bg_panel"],
                                  fg=COLORS["success"])
        self.money_val.pack(pady=(0, 20))

        self.create_stat_widget(stats_panel, "iq", COLORS["accent"])
        self.iq_val = tk.Label(stats_panel, text="10", font=FONTS["header"], bg=COLORS["bg_panel"], fg="white")
        self.iq_val.pack(pady=(0, 20))

        # Right Side: Actions
        actions_panel = tk.Frame(container, bg=COLORS["bg_dark"])
        actions_panel.place(relx=0.35, rely=0, relwidth=0.65, relheight=0.6)

        # Progress Bars Column
        bars_frame = tk.Frame(actions_panel, bg=COLORS["bg_dark"])
        bars_frame.pack(fill="x", pady=(0, 30))

        self.health_bar = self.add_labeled_bar(bars_frame, "health", "Health.Horizontal.TProgressbar")
        self.satiety_bar = self.add_labeled_bar(bars_frame, "satiety", "Satiety.Horizontal.TProgressbar")
        self.stress_bar = self.add_labeled_bar(bars_frame, "stress", "Stress.Horizontal.TProgressbar")
        self.gladness_bar = self.add_labeled_bar(bars_frame, "gladness", "Gladness.Horizontal.TProgressbar")

        # Buttons Grid
        btn_grid = tk.Frame(actions_panel, bg=COLORS["bg_dark"])
        btn_grid.pack(fill="both", expand=True)

        self.create_action_btn(btn_grid, "work_low", lambda: self.do_action(lambda: self.persona.work("low")), 0, 0)
        self.create_action_btn(btn_grid, "work_med", lambda: self.do_action(lambda: self.persona.work("med")), 0, 1)
        self.create_action_btn(btn_grid, "work_high", lambda: self.do_action(lambda: self.persona.work("high")), 0, 2)

        self.create_action_btn(btn_grid, "eat_cheap", lambda: self.do_action(lambda: self.persona.eat("cheap")), 1, 0)
        self.create_action_btn(btn_grid, "eat_med", lambda: self.do_action(lambda: self.persona.eat("med")), 1, 1)
        self.create_action_btn(btn_grid, "eat_exp", lambda: self.do_action(lambda: self.persona.eat("exp")), 1, 2)

        self.create_action_btn(btn_grid, "study", lambda: self.do_action(self.persona.study), 2, 0)
        self.create_action_btn(btn_grid, "chill", lambda: self.do_action(self.persona.chill), 2, 1)
        self.create_action_btn(btn_grid, "clean", lambda: self.do_action(self.persona.clean), 2, 2)

        # Log Section
        log_frame = tk.Frame(self.root, bg=COLORS["bg_panel"], height=200)
        log_frame.pack(fill="x", side="bottom", padx=20, pady=(0, 20))

        self.log_widget = tk.Text(log_frame, bg=COLORS["bg_panel"], fg="white", font=FONTS["log"],
                                  height=8, bd=0, padx=10, pady=10)
        self.log_widget.pack(fill="both", expand=True)
        self.log_widget.configure(state='disabled')

    def create_stat_widget(self, parent, key, color):
        tk.Label(parent, text=self.t(key).upper(), font=FONTS["stat"], bg=COLORS["bg_panel"],
                 fg=COLORS["text_secondary"]).pack()

    def add_labeled_bar(self, parent, key, style):
        f = tk.Frame(parent, bg=COLORS["bg_dark"])
        f.pack(fill="x", pady=5)
        tk.Label(f, text=self.t(key), font=FONTS["stat"], bg=COLORS["bg_dark"], fg="white", width=10, anchor="w").pack(
            side="left")
        bar = ttk.Progressbar(f, style=style, length=300, mode='determinate')
        bar.pack(side="left", padx=10, fill="x", expand=True)
        return bar

    def create_action_btn(self, parent, key, cmd, r, c):
        btn = tk.Button(parent, text=self.t(key), bg=COLORS["bg_panel"], fg="white", font=FONTS["body"],
                        command=cmd, bd=1, relief="flat", cursor="hand2", overrelief="solid")
        btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
        parent.grid_columnconfigure(c, weight=1)
        parent.grid_rowconfigure(r, weight=1)

    def do_action(self, func):
        res = func()
        if isinstance(res, str):
            self.log(res, "red")
            return

        self.actions_left -= 1
        self.update_stats()

        if self.actions_left <= 0:
            self.next_day()

    def update_stats(self):
        p = self.persona
        self.day_label.config(text=f"{self.t('day')} {p.days_lived} | {self.t('age')} {p.age}")
        self.actions_label.config(text=f"{self.t('actions')}: {self.actions_left}")
        self.money_val.config(text=f"${p.money}")
        self.iq_val.config(text=str(p.intelligence))

        self.health_bar['value'] = p.health
        self.satiety_bar['value'] = p.satiety
        self.stress_bar['value'] = p.stress
        self.gladness_bar['value'] = p.gladness

    def next_day(self):
        self.actions_left = 5
        self.persona.process_day()
        self.trigger_random_event()
        self.check_death()
        self.update_stats()
        self.log(f"Day {self.persona.days_lived} begins...")

    def trigger_random_event(self):
        if random.random() < 0.3:
            ev = random.choice(["found", "ill", "bonus"])
            if ev == "found":
                self.persona.money += 20
                self.log(self.t("event_found"), "green")
            elif ev == "ill":
                self.persona.health -= 15
                self.log(self.t("event_ill"), "red")
            elif ev == "bonus":
                self.persona.money += 50
                self.log(self.t("event_bonus"), "green")

    def check_death(self):
        p = self.persona
        reason = None
        if p.age >= 100:
            reason = self.t("death_age")
        elif p.health <= 0:
            reason = self.t("death_health")
        elif p.satiety <= 0:
            reason = self.t("death_hunger")
        elif p.stress >= 100:
            reason = self.t("death_stress")

        if reason:
            messagebox.showinfo("Game Over", reason)
            self.show_menu()


# ---------------- START ----------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Life Simulator Pro")
    root.state('zoomed')  # Fullscreen windowed
    root.bind("<Escape>", lambda e: root.destroy())

    app = GameEngine(root)
    root.mainloop()
