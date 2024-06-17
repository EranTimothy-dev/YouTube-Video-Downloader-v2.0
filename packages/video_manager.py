from tkinter import messagebox
from PIL import ImageTk, Image
import urllib.request
import io


def get_resolutions(Stream):
    '''
    Arguments:
        Stream: the stream information of the video url
    
    Returns the resolution of the video based on stream information
    '''
    args = str(Stream)
    start_index = args.find("=",41) + 2
    end_index = args.find('p',41) + 1
    resolution = args[start_index:end_index]
    return resolution


def convert_to_MB(filesize):
    filesize_in_MB = (filesize/1024)/1024
    return round(filesize_in_MB,2)



def get_thumbnail(Thumbnail):
    '''
    Takes Thumbnail url as an argument.
    converts image from url to byte format
    which is then converted to a resized image
    '''
    # Open thumbnail url and load image
    try:
      with urllib.request.urlopen(Thumbnail) as u:
         raw_data = u.read()
    except Exception as e:
        response = messagebox.showerror("Issue loading thumbnail url", "Thumbnail could not be loaded")
        print(f"Error fetching Thumbnail: {e}")
        return

    try:
        image = Image.open(io.BytesIO(raw_data))
        resized_image= image.resize((300,205))
        photo = ImageTk.PhotoImage(resized_image)
        return photo
    except Exception as e:
        response = messagebox.showerror("Issue loading image", "Thumbnail could not be loaded")
        print(f"Error opening Thumbnail: {e}")
        return
     
   
def download_video(resolution,stream, path):
    '''
    takes in 3 arguments:
        resolution: the video resolution to download
        stream: the url stream of the video
        path: the download path 
    '''
    # Option to allow users to select download quality from a selected resolution
    downloading = stream.get_by_resolution(resolution)
    if downloading == None:
        # Display an error message if something unusual happens and destroy top level window
        response = messagebox.showerror("Resolution Unavailable","Something went wrong!")
        print("resolution unavailable")
        #download_section.destroy()
    else:
        downloading.download(path) 



def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%d:%02d:%02d" % (hour, minutes, seconds)
    