from gtts import gTTS
import tkinter as tk
from tkinter import Text, Button, filedialog

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Converter")

        self.create_ui()

    def create_ui(self):
        # Text input
        self.text_input = Text(self.root, height=10, width=40)
        self.text_input.pack(pady=10)

        # Save to file button
        self.save_button = Button(self.root, text="Save to File", command=self.save_to_file)
        self.save_button.pack(pady=5)

        # Play button
        self.play_button = Button(self.root, text="Play", command=self.play_text)
        self.play_button.pack(pady=5)

    def save_to_file(self):
        text_to_speak = self.text_input.get("1.0", tk.END).strip()
        if text_to_speak:
            file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
            if file_path:
                tts = gTTS(text=text_to_speak, lang='en')
                tts.save(file_path)
                tk.messagebox.showinfo("Success", "Text saved to file successfully.")

    def play_text(self):
        text_to_speak = self.text_input.get("1.0", tk.END).strip()
        if text_to_speak:
            tts = gTTS(text=text_to_speak, lang='id')
            tts.save("temp.mp3")  # Save a temporary file
            self.play_audio("temp.mp3")

    def play_audio(self, file_path):
        import os
        os.system(f'start {file_path}')

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
