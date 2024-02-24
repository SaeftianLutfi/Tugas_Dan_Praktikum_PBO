import pygame
from tkinter import Tk, Button, filedialog, Frame, Label

class PemutarAudio:
    def __init__(self, root):
        self.root = root
        self.root.title("Pemutar Audio")
        self.root.geometry("300x200")

        self.path_label = Button(root, text="Pilih File Audio", command=self.cari_audio)
        self.path_label.pack()

        self.play_button = Button(root, text="Play", command=self.putar_audio, state="disabled")
        self.play_button.pack()

        self.stop_button = Button(root, text="Stop", command=self.berhenti_audio, state="disabled")
        self.stop_button.pack()

        self.file_path = None
        
        # Nama, NIM dan Kelas
        frame = Frame(self.root) 
        frame.pack(padx=5, pady=5)

        nametag = Frame(frame, bg="lightblue", height=30)
        nametag.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

        nama = Label(nametag, text="Saeftian Lutfi", bg='lightblue') 
        nama.grid(row=6, column=0, sticky='e', padx=5, pady=5)
        
        nim = Label(nametag, text="220511078", bg='lightblue')
        nim.grid(row=6, column=1, sticky='e', padx=5, pady=5)

        kelas = Label(nametag, text="TIF22E", bg='lightblue') 
        kelas.grid(row=6, column=2, sticky='e', padx=5, pady=5)

    def cari_audio(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])
        self.path_label["text"] = f"File Audio: {self.file_path}"
        self.play_button["state"] = "normal"
        self.stop_button["state"] = "normal"

    def putar_audio(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.file_path)
        pygame.mixer.music.play()

    def berhenti_audio(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = Tk()
    pemutar_audio = PemutarAudio(root)
    root.mainloop()
