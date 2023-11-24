# -*- coding: utf-8 -*-
# @Author  : yzc
# @Time    : 2023/10/25 23:56
from utils.google_utils import attempt_download

def download_weights():
    for x in ['s', 'm', 'l', 'x']:
        attempt_download(f'yolov5{x}.pt')

if __name__ == '__main__':
    download_weights()
