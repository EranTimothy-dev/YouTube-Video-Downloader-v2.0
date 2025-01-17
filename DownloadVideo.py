import tkinter as tk
from tkinter import ttk
# import pytube as yt
import pytubefix as yt
from tkinter import messagebox
import packages.video_manager as vm
from packages.codecMerger import merge_codecs
import re
from pytubefix.exceptions import RegexMatchError, AgeRestrictedError





class DownloadVideo():
    """
    A class to create a Tkinter-based GUI application for downloading YouTube videos.

    Attributes:
        download_section (tk.Toplevel): The main window for the download section.
        url (str): The URL of the YouTube video to be downloaded.
        video (yt.YouTube): The YouTube object created from the provided URL.
        video_details (ttk.Label): The frame for displaying video details.
        download_option (ttk.Label): The frame for download options.
        download_res (str): The selected video resolution for download.
        video_thumbnail (str): The URL of the video thumbnail.
        video_title (str): The title of the video.
        time_duration (str): The duration of the video.
        published_date (datetime.date): The publish date of the video.
        views (str): The number of views of the video formatted with commas.
        thumbnail (ttk.Label): The label displaying the video thumbnail.
        title (ttk.Label): The label displaying the video title.
        date_published (ttk.Label): The label displaying the publish date.
        duration (ttk.Label): The label displaying the video duration.
        video_views (ttk.Label): The label displaying the number of views.
        download_progress (ttk.Progressbar): The progress bar for download progress.
        selected_quality (tk.StringVar): The selected video quality for download.
        radiobutton_values (dict): Dictionary storing video resolutions for radio buttons.
        selected_stream_size (ttk.Label): The label displaying the selected stream size.

    Methods:
        __init__(link): Initializes the download section with the provided video link.
        create_YouTube_object(): Creates a YouTube object from the provided URL.
        get_video_details(): Retrieves video details like thumbnail, title, duration, publish date, and views.
        create_display_frame(): Creates frames for video details and download options.
        create_video_information_section(): Creates and displays video information section in the GUI.
        download_audio(): Downloads the audio stream of the video.
        get_resolution(): Retrieves available video resolutions.
        display_resolutions(): Displays available video resolutions as radio buttons.
        download_video(): Downloads the video stream based on the selected resolution.
        exit_button(): Creates an exit button to close the download section.
        download_button(): Creates a download button to initiate the download process.

    Usage Example:
        video_downloader = DownloadVideo("https://www.youtube.com/watch?v=example")
        tk.mainloop()
    """
    def __init__(self, link) -> None:
        self.download_section = tk.Toplevel()
        self.download_section.title("Download Video")
        # self.download_section.iconbitmap("images/icon.ico")
        self.download_section.geometry("700x550")
        self.download_section.resizable(0,0)
        self.url = link
        
        try:
            self.video = self.create_YouTube_object()
        except Exception as e:
            print(f"Error creating YouTube object: {e}")
            messagebox.showerror("Error", "Failed to fetch details. Please check the URL and your internet connection.")
            self.download_section.destroy()
            return
        
        self.video_details, self.download_option= self.create_display_frame()
        self.download_res = ""
        self.video_thumbnail, self.video_title, self.time_duration, self.published_date, self.views = self.get_video_details()
        self.thumbnail, self.title, self.date_published, self.duration, self.video_views = self.create_video_information_section()
        self.exit = self.exit_button()
        self.download = self.download_button()
        self.video_resolutions = self.get_resolution()
        self.display_resolutions()
        
        s = ttk.Style()
        s.configure("Label.TLabel", 
                    #background = "#FAF9F6", 
                    font = ('Helvetica', '10'), 
                    padding = (15, 6, 15, 6)
                    )  
        
   
         
    def create_YouTube_object(self):
        def on_progress(stream, chunk, bytes_remaining):
            """Callback function
            Takes 3 positional arguments:
                The youtube video stream
                The chunk of the stream
                Bytes remaining when as download progresses
            """
            # global percentage
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            pct_completed = bytes_downloaded / total_size * 100
            percentage = round(pct_completed)
            print(f"Status: {round(pct_completed, 2)} %")
            
            # Update the progress bar as the video downloads
            self.download_progress['value'] = int(percentage)
            self.download_progress.update_idletasks()
            
        video = yt.YouTube(self.url, on_progress_callback=on_progress)#, use_oauth=True, allow_oauth_cache=True,)
        return video
        
        
    def get_video_details(self):
        from packages.video_manager import convert_seconds
        
        video_thumbnail = self.video.thumbnail_url
        vid_length = self.video.length
        video_duration = convert_seconds(vid_length)
        video_publish_date = self.video.publish_date.date()
        video_views_without_commas = int(self.video.views)
        video_views = (format(video_views_without_commas, ',d'))
        video_title = self.video.title
        return video_thumbnail, video_title, video_duration, video_publish_date, video_views
        
            
    def create_display_frame(self):
        # Video description section
        details_section = ttk.Label(self.download_section)
        details_section.pack(side=tk.TOP)
        # download option section
        download_options_section = ttk.Label(self.download_section)
        download_options_section.pack(side=tk.BOTTOM)
        return details_section, download_options_section
    
    

    def create_video_information_section(self):
        thumbnail = vm.get_thumbnail(self.video_thumbnail)
        self.thumbnail_image = thumbnail
        
        video_thumbnail = ttk.Label(self.video_details, image=self.thumbnail_image)
        video_thumbnail.grid(row=1, column=1,rowspan=5,sticky=tk.W, pady=10, padx=10)
        
        video_title = ttk.Label(self.video_details, text=f"Video Title: {self.video_title}", wraplength=350 ,style="Label.TLabel")
        video_title.grid(row=1, column=2, rowspan=2, pady=10, padx=10)
        
        video_duration = ttk.Label(self.video_details, text=f"Video Duration: {self.time_duration}", style="Label.TLabel")
        video_duration.grid(row=3, column=2)
        
        video_published_date = ttk.Label(self.video_details, text=f"Published Date: {self.published_date}", style="Label.TLabel")
        video_published_date.grid(row=4, column=2)
        
        video_views = ttk.Label(self.video_details, text=f"Views: {self.views}", style="Label.TLabel")
        video_views.grid(row=5,column=2)
        
        self.download_progress = ttk.Progressbar(self.video_details, orient=tk.HORIZONTAL, length=350, mode="determinate")
        self.download_progress.grid(row=8, column=2, pady=10)
        
        return video_thumbnail, video_title, video_published_date, video_duration, video_views
    
    
    def download_audio(self):
        # path_to_download = path_to_downloads()
        # final_path = path_to_download + "\\videos\\"
        final_path = "videos\\"
        audio_file = self.video.streams.filter(adaptive=True, only_audio=True).order_by('abr').desc().first()
        audio_file.download(filename='audio.webm', output_path=final_path)
        print("Audio Downloaded Successfully:", final_path)
        return final_path + "\\audio.webm"

    
    def get_resolution(self):
        try:
            video_files = self.video.streams.filter(adaptive=True, only_video=True, file_extension='mp4').order_by('resolution').desc()
            resolutions = []
            for i in video_files:
                video_resolution = vm.get_resolutions(i)
                resolutions.append(video_resolution)
            return resolutions
        except AgeRestrictedError as e:
            print(f"AgeRestrictedError: {e}")
            messagebox.showerror(f"AgeRestrictedError", "Cannot download age restricted video")
            self.download_section.destroy()
        except RegexMatchError as e:
            print(f"{e}")
            messagebox.showerror("Regex Error!", "Something went wrong") 
    
    def display_resolutions(self):
        def get_selection():
            selected_quality = self.selected_quality.get()
            print(f"Selected quality: {selected_quality}")
            self.download_res = selected_quality
            video_file = self.video.streams.filter(adaptive=True, file_extension='mp4', only_video=True, res=str(self.download_res)).first()
            stream_size = video_file.filesize_mb
            size_text = f"File Size: {round(stream_size,2)} MB"
            self.selected_stream_size = ttk.Label(self.video_details, text=size_text, style="Label.TLabel")
            self.selected_stream_size.grid(row=7, column=2)
            
        self.selected_quality = tk.StringVar(self.download_section,"Not selected")
        self.radiobutton_values = dict()
        # num = 1
        for i in self.video_resolutions:
            self.radiobutton_values[i] = f"{i}"
            # num += 1
        num = 6 
        for (key, val) in self.radiobutton_values.items():
            ttk.Radiobutton(self.video_details, text=key, variable=self.selected_quality, value=val, command=get_selection).grid(row=num, column=1, pady=10)
            num += 1
            
        print(f"Initial quality: {self.selected_quality.get()}")
        
    
    def download_video(self):
        resolution = str(self.download_res)
        video_file = self.video.streams.filter(adaptive=True, file_extension='mp4', only_video=True, res=resolution).first()
        
        print(video_file)
        if video_file is None:
            print(f"No stream found with resolution {resolution}")
            messagebox.showerror("Error", f"No stream found with resolution {resolution}")
            return
        try:
            # path_to_download = path_to_downloads()
            # final_path = path_to_download + "\\videos\\"
            final_path = "videos\\"
            video_file.download(filename='video.mp4', output_path=final_path)
            print("Video Downloaded Successfully:", final_path)
            return final_path + "\\video.mp4"
        except Exception as e:
            print(f"Error downloading video: {e}")
            messagebox.showerror("Error", f"Error downloading video: {e}")
            self.download_section.destroy() 
            
    
    
    def exit_button(self):
        def exit_btn():
            self.download_section.destroy()
            self.download_section.update()
        btn = ttk.Button(self.download_option,text='Cancel',command=exit_btn)
        btn.grid(row=2, column=1, padx=20, pady=15)
        
        
        
    def download_button(self): 
        def downloader():
            download_text = tk.StringVar()
            download_text.set("Getting files ready...")
            self.downloading_info = ttk.Label(self.video_details, textvariable =download_text, style="Label.TLabel")
            self.downloading_info.grid(row=9, column=2, pady=10)
            audio_path = self.download_audio()
            download_text.set("Downloading your video, please wait...")
            self.downloading_info = ttk.Label(self.video_details, textvariable=download_text, style="Label.TLabel")
            self.downloading_info.grid(row=9, column=2, pady=10)
            video_path = self.download_video()
            output = str(f"{self.video.title}.mp4")
            output_file_without_spaces = output.replace(" ","_")
            # output_file1 = output_file_without_spaces.replace("?", "")
            # output_file = output_file1.replace("/","_")
            output_file = re.sub(r'[<>:"/\\|?*]',"_", output_file_without_spaces)
            merge_codecs(video_path,audio_path,output_file)
            download_text.set("Download Completed.")
            self.downloading_info = ttk.Label(self.video_details, textvariable=download_text, style="Label.TLabel")
            self.downloading_info.grid(row=9, column=2, pady=10)
            messagebox.showinfo("Success", "Download Completed Successfully")
            self.download_section.destroy()   
        btn2 = ttk.Button(self.download_option, text="Download", command=downloader)
        btn2.grid(row=2, column=2, padx=20, pady=15)
        
        


if __name__ == "__main__":
    root = tk.Tk()
    url = "https://youtu.be/Js6H70-eADY?si=fF6a5sRPprlb1MDr"
    downloader = DownloadVideo(url)
    root.mainloop()