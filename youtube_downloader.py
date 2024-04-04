from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        status_label.config(text="Video downloaded successfully!")
    except Exception as e:
        status_label.config(text=f"Error: {e}")


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


def download_video_with_url():
    video_url = url_entry.get()
    if video_url:
        save_dir = open_file_dialog()

        if save_dir:
            status_label.config(text="Started downloading...")
            download_video(video_url, save_dir)
        else:
            status_label.config(text="Invalid save location.")
    else:
        status_label.config(text="No URL entered.")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    url_window = tk.Toplevel()
    url_window.title("YouTube Downloader")

    url_label = tk.Label(url_window, text="Please enter a YouTube URL:")
    url_label.pack()

    url_entry = tk.Entry(url_window)
    url_entry.pack()

    url_button = tk.Button(url_window, text="Download", command=download_video_with_url)
    url_button.pack()

    status_label = tk.Label(url_window, text="", fg="blue")
    status_label.pack()

    url_window.mainloop()

