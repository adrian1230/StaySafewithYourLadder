from pytube import YouTube

url = input('enter the youtube video link here >> ')

YouTube(url).streams.filter(progressive=True,
         file_extension='mp4').order_by('resolution').desc(
               ).first().download()

print('Download finished --- ---')
