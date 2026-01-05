from moviepy.editor import VideoFileClip

INPUT_VIDEO = "../recursive-bayesian-estimators.mp4"
OUTPUT_GIF = "../recursive-bayesian-estimators.gif"

START_TIME = 0.0
END_TIME = 30

FPS = 12
SCALE = 0.9

clip = VideoFileClip(INPUT_VIDEO)

# MoviePy 1.x uses subclip()
subclip = clip.subclip(START_TIME, END_TIME)

# Resize
subclip = subclip.resize(SCALE)

# Write GIF
subclip.write_gif(OUTPUT_GIF, fps=FPS)

print("GIF created successfully!")
