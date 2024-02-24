import tkinter as tk
from tkinter import filedialog
import cv2
import PIL.Image, PIL.ImageTk

class VideoPlayerApp:
    def __init__(self, window, window_title, video_source):
        self.window = window
        self.window.title(window_title)
        self.window.geometry("500x300")
        self.video_source = video_source

        # Membuat frame untuk menampilkan video
        self.vid_frame = tk.Label(window)
        self.vid_frame.pack()

        # Tombol untuk memilih video
        self.btn_open = tk.Button(window, text="Pilih Video", width=20, command=self.open_video)
        self.btn_open.pack(pady=10)

        # Tombol untuk memutar video
        self.btn_play = tk.Button(window, text="Putar", width=10, command=self.play_video)
        self.btn_play.pack(pady=10)

        # Tombol untuk menghentikan video
        self.btn_stop = tk.Button(window, text="Stop", width=10, command=self.stop_video)
        self.btn_stop.pack(pady=10)

        # Inisialisasi video
        self.vid = cv2.VideoCapture(self.video_source)
        self.vid_player()

        self.window.mainloop()

    def vid_player(self):
        ret, frame = self.vid.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.vid_frame.config(image=self.photo)
            self.vid_frame.image = self.photo
            self.window.after(10, self.vid_player)

    def open_video(self):
        self.stop_video()
        self.video_source = filedialog.askopenfilename()
        self.vid = cv2.VideoCapture(self.video_source)
        self.vid_player()

    def play_video(self):
        self.vid_player()

    def stop_video(self):
        if self.vid:
            self.vid.release()
            self.vid_frame.config(image="")
            self.vid_frame.image = None

# Menjalankan aplikasi
app = VideoPlayerApp(tk.Tk(), "Aplikasi Pemutar Video", "sample_video.mp4")
