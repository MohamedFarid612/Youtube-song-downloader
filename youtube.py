from pytube import YouTube

link = input("Please enter the link of your Youtube Video : ")

video = YouTube(link)

print(video.title)
print("\nDownloading Audio...")
video.streams.get_audio_only().download(
    output_path="C:\\Users\Mohamed Farid\Desktop\songs")
