import tkinter as tk
from tkinter import ttk
import random
import time
from sympy import symbols, solve


class PhysicsChatbot:

    def __init__(self, root):
        self.root = root
        self.root.title("Physics Chatbot for Students")

        # Chat window
        self.chat_frame = tk.Frame(self.root, bg="#1f1f1f")
        self.chat_frame.pack(fill=tk.BOTH, expand=True)
        self.chat_canvas = tk.Canvas(self.chat_frame,
                                     bg="#1f1f1f",
                                     highlightthickness=0)
        self.chat_canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.scrollbar = ttk.Scrollbar(self.chat_frame,
                                       command=self.chat_canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_canvas.config(yscrollcommand=self.scrollbar.set)

        self.chat_window = tk.Frame(self.chat_canvas, bg="#1f1f1f")
        self.chat_canvas.create_window((0, 0),
                                       window=self.chat_window,
                                       anchor="nw")
        self.chat_window.bind(
            "<Configure>", lambda e: self.chat_canvas.configure(
                scrollregion=self.chat_canvas.bbox("all")))

        # Entry field and send button
        self.input_frame = tk.Frame(self.root, bg="#2b2b2b")
        self.input_frame.pack(fill=tk.X, padx=10, pady=10)
        self.input_field = ttk.Entry(self.input_frame, font=("Arial", 14))
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.send_button = ttk.Button(self.input_frame,
                                      text="Send",
                                      command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=5)

        # Bot typing animation
        self.typing_label = tk.Label(self.root,
                                     text="",
                                     font=("Arial", 12),
                                     fg="#ffffff",
                                     bg="#1f1f1f")
        self.typing_label.pack(pady=5)

        # Welcome message
        self.add_message(
            "Bot",
            "Hello! I am your Physics Chatbot. I can assist with Newton's laws, thermodynamics, optics, electromagnetism, and much more. Ask me any physics-related question!"
        )

    def add_message(self, sender, message):
        message_frame = tk.Frame(self.chat_window, bg="#1f1f1f", pady=5)

        if sender == "Bot":
            tk.Label(message_frame,
                     text=sender,
                     font=("Arial", 10, "bold"),
                     fg="#00ff00",
                     bg="#1f1f1f").pack(anchor="w")
            tk.Label(message_frame,
                     text=message,
                     font=("Arial", 12),
                     fg="#ffffff",
                     bg="#1f1f1f",
                     wraplength=500,
                     justify="left").pack(anchor="w")
        else:
            tk.Label(message_frame,
                     text=sender,
                     font=("Arial", 10, "bold"),
                     fg="#ff9800",
                     bg="#1f1f1f").pack(anchor="e")
            tk.Label(message_frame,
                     text=message,
                     font=("Arial", 12),
                     fg="#ffffff",
                     bg="#1f1f1f",
                     wraplength=500,
                     justify="right").pack(anchor="e")

        message_frame.pack(fill=tk.X)
        self.chat_canvas.yview_moveto(1)

    def bot_typing(self):
        self.typing_label.config(text="Bot is typing...")
        self.root.update_idletasks()
        time.sleep(1.5)  # Simulates typing delay
        self.typing_label.config(text="")

    def send_message(self):
        user_message = self.input_field.get()
        if not user_message.strip():
            return

        self.add_message("You", user_message)
        self.input_field.delete(0, tk.END)
        self.respond_to_message(user_message)

    def respond_to_message(self, message):
        try:
            if "newton's law" in message.lower():
                response = (
                    "Newton's Laws of Motion:\n"
                    "1. First Law: An object remains at rest or in motion unless acted upon by a force.\n"
                    "2. Second Law: F = ma (Force equals mass times acceleration).\n"
                    "3. Third Law: For every action, there is an equal and opposite reaction."
                )

            elif "velocity" in message.lower():
                response = "Velocity is the rate of change of displacement. Formula: v = s / t, where s is displacement and t is time."

            elif "gravity" in message.lower():
                response = "Gravity is a force that attracts objects to the center of a planet. Earth's gravity is approximately 9.8 m/s²."

            elif "thermodynamics" in message.lower():
                response = (
                    "Laws of Thermodynamics:\n"
                    "1. Zeroth Law: If two systems are in thermal equilibrium with a third, they are in equilibrium with each other.\n"
                    "2. First Law: Energy cannot be created or destroyed, only transformed (Conservation of Energy).\n"
                    "3. Second Law: Entropy of an isolated system always increases.\n"
                    "4. Third Law: As temperature approaches absolute zero, entropy approaches a constant minimum."
                )

            elif "optics" in message.lower():
                response = (
                    "Optics deals with light behavior:\n"
                    "1. Reflection: Light bounces off a surface.\n"
                    "2. Refraction: Light bends when passing through different media.\n"
                    "3. Diffraction: Light spreads after passing through a narrow aperture."
                )

            elif "kirchhoff's law" in message.lower():
                response = (
                    "Kirchhoff's Laws:\n"
                    "1. Current Law (KCL): Total current entering a junction equals the total current leaving it.\n"
                    "2. Voltage Law (KVL): The sum of all voltages around a closed loop equals zero."
                )

            elif "wave" in message.lower():
                response = ("Wave properties:\n"
                            "1. Frequency (f): Number of waves per second.\n"
                            "2. Wavelength (λ): Distance between wave peaks.\n"
                            "3. Speed (v): v = fλ.")

            elif "solve" in message.lower():
                equation = message.split("solve", 1)[1].strip()
                x = symbols('x')
                solution = solve(equation, x)
                response = f"The solution is: {solution}"

            else:
                response = random.choice([
                    "I'm not sure about that. Could you ask in a different way?",
                    "That's an interesting topic! Let me think...",
                    "Can you provide more details about your question?"
                ])
        except Exception as e:
            response = "I couldn't process your request. Please check your input format."

        self.bot_typing()
        self.add_message("Bot", response)


# Application setup
root = tk.Tk()
app = PhysicsChatbot(root)
root.geometry("600x700")
root.mainloop()
