import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from yt_dlp import YoutubeDL

class DownloaderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text="Paste YouTube URL below:", size_hint_y=0.2)
        self.layout.add_widget(self.label)
        
        self.url_input = TextInput(multiline=False, size_hint_y=0.2)
        self.layout.add_widget(self.url_input)
        
        self.download_btn = Button(text="Download Video", size_hint_y=0.2)
        self.download_btn.bind(on_press=self.start_download)
        self.layout.add_widget(self.download_btn)
        
        self.status_label = Label(text="Status: Idle", size_hint_y=0.4)
        self.layout.add_widget(self.status_label)
        
        return self.layout

    def start_download(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.status_label.text = "Status: Please enter a valid URL!"
            return
        
        self.status_label.text = "Status: Downloading..."
        # Run download in a background thread to prevent UI freezing
        threading.Thread(target=self.download_video, args=(url,)).start()

    def download_video(self, url):
        # Target the public Downloads directory on Android
        download_path = '/storage/emulated/0/Download/%(title)s.%(ext)s'
        
        ydl_opts = {
            'outtmpl': download_path,
            'format': 'best',  # Gets best pre-merged video/audio stream without needing complex external FFmpeg setups
        }
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.text = "Status: Download Successful! Check your Downloads folder."
        except Exception as e:
            self.status_label.text = f"Status: Error - {str(e)}"

if __name__ == '__main__':
    DownloaderApp().run()
