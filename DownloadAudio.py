import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import packages.video_manager as vm
from DownloadVideo import DownloadVideo
from packages.DownloadsPath import get_windows_download_folder, get_non_windows_download_folder
import os
import re



class DownloadAudio(DownloadVideo):
    def __init__(self, link) -> None:
        super().__init__(link)
        
        self.video_resolutions = self.get_resolution()
        
    
    def get_resolution(self):
        audio_files = self.video.streams.filter(adaptive=True, only_audio=True).order_by("abr").desc()
        abr = []
        for i in audio_files:
            bitrate = vm.get_bitrate(i)
            abr.append(bitrate)
        return abr

    def display_resolutions(self):
        # return super().display_resolutions()
        def get_bitrate():
            selected_quality = self.selected_quality.get()
            print(f"Selected quality: {selected_quality}")
            self.download_res = selected_quality
            
            
        
        self.selected_quality = tk.StringVar(self.download_section, "Not selected")
        self.radiobutton_values = dict()
        # num = 1
        for i in self.video_resolutions:
            self.radiobutton_values[i] = f"{i}"
        num = 6
        for (key,value) in self.radiobutton_values.items():
            ttk.Radiobutton(self.video_details, text=key, variable=self.selected_quality, value=value, command=get_bitrate).grid(row=num, column=1, pady=10)
            num += 1
        
        print(f"Initial quality: {self.selected_quality.get()}")


    def download_audio(self):
        if os.name == "nt":
            path = get_windows_download_folder()
        else:
            path = get_non_windows_download_folder()
        
        output = self.video.title.replace(" ","_")
        output_file = re.sub(r'[<>:"/\\|?*]',"_", output)
        
        audio_file = self.video.streams.filter(adaptive=True, only_audio=True,abr=self.download_res).order_by("abr").desc().first()
        audio_file.download(mp3=True, filename=output_file, output_path=path) 
        print("Successfully downloaded audio: ", path)
            
            
    
    def download_button(self):
        def downloader():
            self.downloading_info = ttk.Label(self.video_details, textvariable = "Downloading Audio...", style="Label.TLabel")
            self.downloading_info.grid(row=9, column=2, pady=10)
            self.download_audio()
            messagebox.showinfo("Success", "Download Completed Successfully")
            self.download_section.destroy()
        
        btn2 = ttk.Button(self.download_option, text="Download", command=downloader)
        btn2.grid(row=2, column=2, padx=20, pady=15)










if __name__ == "__main__":
    root = tk.Tk()
    song = "https://youtu.be/O2q59LClA7Q?si=OURcjiDbIvZYFmRs"
    url = "https://youtu.be/Js6H70-eADY?si=fF6a5sRPprlb1MDr"
    downloader = DownloadAudio(song)
    root.mainloop()
    