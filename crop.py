from moviepy import VideoFileClip, vfx

def crop_video(input_video_path, output_video_path, crop_width):
    video = VideoFileClip(input_video_path)

    width, height = video.size
    new_width = width - crop_width

    if new_width <= 0:
        raise ValueError("crop_width is larger than the video width")

    cropped = video.with_effects([
        vfx.Crop(x1=0, y1=0, x2=new_width, y2=height)
    ])

    cropped.write_videofile(
        output_video_path,
        codec="libx264",
        audio_codec="aac"
    )

crop_video(
    "hallway.mp4",
    "final_hallway.mp4",
    crop_width=550
)
