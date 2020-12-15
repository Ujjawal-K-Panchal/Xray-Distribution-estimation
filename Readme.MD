# Xray Distribution Estimation.

This repository is supposed to be used for estimating whether the assumption that xray images follow Gaussian/Normal distribution is valid. This will be tested using **Anderson-Darling test.**

# Setup

## 1. Download Seperate Datasets:

### 1.1 CoViD19 Datasets
1. Make directory ```datasets``` in repo.
2. ```cd datasets```
3. Farjan_repo: ```git clone https://github.com/Farjanasumona/covid_chestXray_dataset```
4. ieee8032_repo: ```git clone https://github.com/ieee8023/covid-chestxray-dataset```
5. ahmad_repo: ```git clone https://github.com/ahmadhassan7/Covid-19-Datasets```
6. GeneralBlockchain: ```git clone https://github.com/GeneralBlockchain/covid-19-chest-xray-segmentations-dataset.git```
7. AntonisMakris: ```git clone https://github.com/AntonisMakris/COVID19-XRay-Dataset.git```

### 1.2 Other Xray Datasets
1. NIH Chest X-ray Dataset: https://www.kaggle.com/nih-chest-xrays/data/home
	- Create folder ```datasets/NIH-ChestXray```.
	-  download images_001.zip and images_002.zip
	- extract it inside ```datasets/NIH-ChestXray/images-1``` and ```datasets/NIH-ChestXray/images-2```.

## 2. Make Virtual environment.
1. ```pip install virtualenv```
2. ```python -m venv xray-env```  

## 3. Download requirements:
1. Install requirements: ```pip install -r requirements.txt```

## 4. Preprocess files:
1. Run Collector  to preprocess data and remove duplicates: ```python Collector.py```