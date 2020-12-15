# -*- coding: utf-8 -*-
"""
Title: Xray Dataset Collector.
    
Created on Mon Dec 14 23:00:47 2020

@author: Ujjawal.K.Panchal, @Email: ujjawalpanchal32@gmail.com

Copyright (C) Ujjawal K. Panchal - All Rights Reserved.
Unauthorized copying of this file, via any medium is strictly prohibited.
Proprietary and confidential.
"""
#TODO.
#std. libs.
from PIL import Image
import os
from pathlib import Path
import multiprocessing as mp
#custom libs.
import imagehash


#global variables.
dataroot = "datasets"
merge_name = "combined-dsets"
image_extensions = {"jpg", "jpeg", "png", "svg", "dicom"}
outpath = "combined"

covid_datasets = [
	"covid-chestxray-dataset/images/",
	"covid_chestXray_dataset/covid_19 dataset/covid19/",
	"covid_chestXray_dataset/covid_19 dataset/normal/",
	"covid-19-chest-xray-segmentations-dataset/images/",
	"COVID19-XRay-Dataset/test",
	"COVID19-XRay-Dataset/train"
]

noncovid_datasets = [
	"NIH-ChestXray/images-1/",
	"NIH-ChestXray/images-2/"
]

all_datasets = covid_datasets + noncovid_datasets


def ProcessImages(dataset):
	"""
	Take relative intermediate path and return all image files present inside.
	---
	1. dataset: relative path to the dataset in question. (path str).
	"""
	#1. Traverse and find files in dataset.
	for root, dirs, files in os.walk(Path(dataroot, dataset)):
		for file in files:
			#1. Check whether the file is an image file.
			f_ext = file.split(".")[1]
			if f_ext in image_extensions:
				#1.1. get gray image.
				path = Path(root, file)
				print(path)
				img = Image.open(Path(root, file)).convert('L')
				SaveImg(img, hash(img))
				img.close()
	return True

def hash(img, size = 8):
	"""
	Take path and compute average hash value using DCT.
	---
	1. img = The image. (PIL.Image obj).
	2. size = hash size. (int).
	"""
	return imagehash.average_hash(img, hash_size = size)

def SaveImg(img, hash):
	img.save(Path(outpath, f"{hash}.png"), "PNG")

if __name__ == "__main__":
	pool = mp.Pool(4)
	content = []
	#1. extract all images in dataset.
	mapResult = pool.map_async(ProcessImages, all_datasets).get()
	pool.close()