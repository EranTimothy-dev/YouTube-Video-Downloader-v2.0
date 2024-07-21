import tkinter as tk
from tkinter import ttk
import pytube as yt
from DownloadVideo import DownloadVideo
from DownloadAudio import DownloadAudio




class SearchVideo():
    """
    A class to create a Tkinter-based GUI application for searching and downloading YouTube videos.

    Attributes:
        window (tk.Tk): The main window of the application.
        note (str): A note to display instructions and warnings to the user.
        display_frame (ttk.Frame): The frame for displaying the search bar and notes.
        searchbar_frame (ttk.LabelFrame): The frame containing the search bar.
        searchbar (ttk.Entry): The entry widget for entering the YouTube URL.
        warning_note (ttk.Label): The label displaying the warning note.

    Methods:
        __init__(): Initializes the main window and GUI components.
        create_display_frame(): Creates the main frame for displaying content.
        create_warning_note(): Creates and displays a warning note with instructions.
        create_searchbar(): Creates and displays the search bar for entering YouTube URLs.
        run(): Runs the Tkinter main loop to display the GUI.
        
    Usage Example:
        app = SearchVideo()
        app.run()
    """
    def __init__(self):
       self.window = tk.Tk()
       self.window.title("YouTube Video Downloader")
       self.window.geometry("690x200")
       self.window.iconbitmap("images/icon.ico")
       self.window.resizable(0,0)
       
       self.note = """NOTE: The audio and video files are downloaded separately, therefore kindly wait till your notified 
            that the download has completely finished"""

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
        url_search.grid(row=1,column=1, columnspan=6, padx=10, pady=10)

        # should get url and the time of calling the load_video function else causes regex error.
        def load_video():
            url = url_search.get()
            print(url)
            DownloadVideo(url)
        
        def load_audio():
            url = url_search.get()
            print(url)
            DownloadAudio(url)
        
        get_video_button = ttk.Button(entry_label, text="Download Video", command=lambda: load_video()) 
        get_video_button.grid(row=2, column=3, pady=10)
        
        get_audio_button = ttk.Button(entry_label, text="Download Audio", command=lambda: load_audio()) 
        get_audio_button.grid(row=2, column=4, pady=10)
        
        return entry_label, url_search
   
            
    def run(self):
        self.window.mainloop()


    

if __name__ == "__main__":
    yt = SearchVideo()
    yt.run()