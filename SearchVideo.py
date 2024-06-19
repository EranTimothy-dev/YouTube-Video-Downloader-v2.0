import tkinter as tk
from tkinter import ttk
import pytube as yt
# from pytube import YouTube
from DownloadVideo import DownloadVideo




class SearchVideo():
    '''
    Takes 0 positional arguments.
    Instantiates an user friendly interface for user to input the youtube link of the video wished to be downloaded and 
    instantiates an object of the class DownloadVideo to then process the video from the link provided.
    '''
    def __init__(self):
       self.window = tk.Tk()
       self.window.title("YouTube Video Downloader")
       self.window.geometry("690x200")
       self.window.iconbitmap("images/icon.ico")
       self.window.resizable(0,0)
       
       self.note = """NOTE: 1. If the download doesn't start please check if it's already downloaded in the Downloads folder
            2. The audio and video files are downloaded separately, therefore kindly wait till your notified 
                that the download is completely finished"""

       style = ttk.Style()
       style.configure("test.TLabel", foreground= "#e60000")
       self.display_frame = self.create_display_frame()
       self.searchbar_frame, self.searchbar = self.create_searchbar()
       self.warning_note = self.create_warning_note()

           
    def create_display_frame(self):
        url_frame = ttk.Frame(self.window, width=500, height=500)
        url_frame.pack(fill="both", expand=True)
        return url_frame
    
    def create_warning_note(self):
        note_label = ttk.Label(self.display_frame, text=self.note, style="test.TLabel") 
        note_label.grid(row=2, column=1)
        return note_label
      
    
    def create_searchbar(self):
        entry_label = ttk.LabelFrame(self.display_frame, text="Enter Url", padding=10)
        entry_label.grid(row=1, column=1, columnspan=2, padx=20, pady=10)
        
        url_search = ttk.Entry(entry_label, width= 100)
        url_search.pack()

        # should get url and the time of calling the load_video function else causes regex error.
        def load_video():
            url = url_search.get()
            print(url)
            download_window = DownloadVideo(url)
            print(url)
        
        search_button = ttk.Button(entry_label, text="Search", command=lambda: load_video()) 
        search_button.pack(pady=10, padx=10)
        
        return entry_label, url_search
   
            
    def run(self):
        self.window.mainloop()


    

if __name__ == "__main__":
    yt = SearchVideo()
    yt.run()