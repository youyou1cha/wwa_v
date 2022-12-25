# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : mp4_to_mp3.py
# Time       ：2022/12/23 12:48
# Author     ：wwa
# version    ：python 3.11
# Description：
"""
from moviepy.editor import *
fname = r'D:\media\儿童绘本故事《好饿的小蛇》\1-儿童绘本故事《好饿的小蛇》-480P 清晰-AVC.mp4'
video = VideoFileClip(fname)
audio = video.audio
audio.write_audiofile("好饿的小蛇.wav")
audio.write_audiofile('好饿的小蛇.mp3')
audio.close()
video.close()
