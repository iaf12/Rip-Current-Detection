# Rip Current Detection

An end-to-end computer vision and object detection pipeline designed to identify, monitor, and track dangerous ocean rip currents from visual data (images and video streams) to enhance beach safety.

https://github.com/user-attachments/assets/42e470bd-d017-4e47-bd2c-2ad78ffdc1f5

## 📌 Project Overview
Rip currents are powerful, narrow channels of fast-moving water flowing away from the shore. They pose a significant hazard to swimmers and beachgoers. This project leverages deep learning object detection algorithms to automate the identification of rip currents in diverse coastal conditions, providing a framework for early warning systems.

## 📁 Repository Structure

* **Models/** — Saved model weights and training checkpoints.
* **Testing/** — Scripts to run validation and performance evaluations.
* **data_custom.yaml** — Configuration mapping dataset paths and class labels.
* **requirements.txt** — List of required Python dependencies.
* **train.py** — Main script to initialize and run model training.
* **sample-rip-output.mp4** — Sample video showing model predictions.

## ⚙️ Quick Setup

1. **Activate Environment:**
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Training:**
   ```bash
   python train.py
   ```

## 📜 License
This project is open-source and licensed under the **MIT License**.

## Note:
Have any query?? contact to istiaqahmmedfahad@gmail.com
