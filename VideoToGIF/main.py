from moviepy.editor import *

video_path = input("视频地址：")
video = VideoFileClip(video_path)
rate = float(input("压缩比例："))
clip = video.resize(rate)
result = input("生成动图路径以及名称：")
clip.write_gif(result,fps=10)