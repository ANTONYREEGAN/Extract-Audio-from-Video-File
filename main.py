import moviepy.editor
video = moviepy.editor.VideoFileClip("song.mp4")
audio = video.audio
audio.write_audiofile("extracted.mp3")


