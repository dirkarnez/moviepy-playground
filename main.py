from moviepy.editor import *

filename = "mov_bbb"
video = VideoFileClip(f"{filename}.mp4").set_position(("center","bottom")) #.subclip(0,2)

# Make the text. Many more options are available.
txt_clip = ( TextClip("My Holidays 2013", fontsize=15, color='white')
            .set_position(("center","top"))
            .set_duration(2)  )

result = CompositeVideoClip([video, txt_clip], size=(video.w, video.h + 60), bg_color=(12, 34, 56)) # Overlay text on video

result.write_videofile(f"{filename}_edited.mp4") # Many options...
