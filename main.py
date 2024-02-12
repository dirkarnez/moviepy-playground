from moviepy.editor import *
import moviepy.video.fx.all as vfx

filename = "mov_bbb"
video = (VideoFileClip(f"{filename}.mp4")
            .fx(vfx.resize, width=1080)
            .set_position(("center","bottom")))#.subclip(0,2))

# Make the text. Many more options are available.
txt_clip = ( TextClip(txt='line 1' + os.linesep + 'line 2', fontsize=50, color='white', font="IMPACT", align="west")
            .set_position((40, 40))
            .set_duration(2)  )

result = CompositeVideoClip([video, txt_clip], size=(video.w, video.h + 200), bg_color=(12, 34, 56)) # Overlay text on video

result.write_videofile(f"{filename}_edited.mp4") # Many options...
