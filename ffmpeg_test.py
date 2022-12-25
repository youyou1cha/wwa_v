# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : ffmpeg_test.py
# Time       ：2022/12/24 21:58
# Author     ：wwa
# version    ：python 3.11
# Description：
"""

import os
import itertools
import typing


def main():
    # 配置环境变量
    ffmpeg_path = 'ffmpeg.exe'
    videos_path = 'videos'
    concat_list_path = videos_path + "\\txt\\"

    L = []

    for root, dirs, files in os.walk(videos_path):
        files.sort()
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                filePath = os.path.join(root, file)
                L.append(filePath)

    concat_file_path = concat_list_path + "concat_list.txt"
    print(concat_file_path)

    total = len(L)
    for i in range(0, total):
        print(L[i])
        with open(concat_file_path, 'a', encoding='utf-8') as f:
            video_file = "file" + "'" + L[i] + "'" + "\n"
            f.write(video_file)
    result_file_path = videos_path + "\\" + "merge.mp4"
    print(result_file_path)

    cmd = ffmpeg_path + "-f concat -safe 0 -i " + concat_file_path + "-c copy" + result_file_path
    print(cmd)

    os.popen(cmd)


# ffmpeg.exe -f concat -safe 0 -i file.txt -c copy out.mp4
# ffmpeg -i "concat:aaa.ts|bb.ts" -c copy outp.mp4

ffmpeg_path = "ffmpeg.exe"


def contact_ts(ts_file: typing.List, file_path=None, outname: typing.AnyStr):
    if file_path is None:
        ffstr = ffmpeg_path + "-i" + "concat:" + "|".join(ts_file) + "-c copy" + outname
        os.popen(ffstr)
    else:
        ffstr = ffmpeg_path + "-f concat -safe 0 -i " + file_path + " -c" + outname
        os.popen(ffstr)


if __name__ == '__main__':
    main()
