# -*- coding:utf-8 -*-
"""
@file name  : hello pytorch.py
@author     : TingsongYu https://github.com/TingsongYu
@date       : 2020-07-24
@brief      : 问世代码
"""

import torch

print("Hello World, Hello PyTorch Long {}".format(torch.__version__))

print("\nCUDA is available:{}, version is {}".format(torch.cuda.is_available(), torch.version.cuda))

print("MACBOOK PRO")

print("Hope everything will be OK.")

print("Now it is mac again")

print("Again, it is windows")
#print("\ndevice_name: {}".format(torch.cuda.get_device_name(0)))
