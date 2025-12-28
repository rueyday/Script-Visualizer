from moviepy import VideoFileClip

INPUT_VIDEO = "../../final_hallway.mp4"     # path to your MP4
OUTPUT_GIF = "../../hallway.gif"

START_TIME = 0.0
END_TIME = 16.5

FPS = 15
SCALE = 3.0

clip = VideoFileClip(INPUT_VIDEO)

# MoviePy 2.x uses subclipped()
subclip = clip.subclipped(START_TIME, END_TIME)

# Resize
subclip = subclip.resized(SCALE)

# Write GIF
subclip.write_gif(OUTPUT_GIF, fps=FPS)

print("GIF created successfully!")
