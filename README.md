
# Converting the Video File to Audio File

```diff

+ import moviepy.editor

+ video = moviepy.editor.VideoFileClip("song.mp4")
! #If your videos is in same folder then you can name them directly
! #Else you need to give path of the video file

+ audio = video.audio

+ audio.write_audiofile("extracted.mp3")
```
