

https://github.com/user-attachments/assets/42e470bd-d017-4e47-bd2c-2ad78ffdc1f5

# Rip Current Detection

An end-to-end computer vision and object detection pipeline designed to identify, monitor, and track dangerous ocean rip currents from visual data (images and video streams) to enhance beach safety.

## 📌 Project Overview
Rip currents are powerful, narrow channels of fast-moving water flowing away from the shore. They pose a significant hazard to swimmers and beachgoers. This project leverages deep learning object detection algorithms to automate the identification of rip currents in diverse coastal conditions, providing a framework for early warning systems.

## 📁 Repository Structure
Based on the live repository setup, the project is structured as follows:

*   **Models/** — Contains saved model weights (`.pt`, `.onnx`), architecture configurations, and training checkpoints.
*   **Testing/** — Dedicated validation and evaluation scripts to run test images, evaluate performance metrics, and gauge accuracy.
*   **data_custom.yaml** — Configuration file defining paths to training/validation datasets and class label names.
*   **train.py** — Main execution script to initialize, configure, and run the model training pipeline.
*   **sample-rip-output.mp4** — Sample output video demonstrating model inference and prediction visualization on actual footage.
*   **.gitignore** — Configured to exclude heavy files, Python cache files, compressed zip datasets, and virtual environments (`.venv/`).
*   **LICENSE** — Licensed under the open-source MIT License terms.

## ⚙️ Setup & Installation

### 1. Environment Activation
Navigate to your local repository folder and activate your local Python virtual environment:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
```

### 2. Dependencies
Ensure you have your dependencies installed (such as `ultralytics`, `torch`, `opencv-python`, etc.). If you haven't created a requirements file yet, you can initialize your environment with:
```bash
pip install ultralytics opencv-python matplotlib
```

## 🚀 Usage Guide

### 1. Dataset Configuration
Open `data_custom.yaml` and verify that your local absolute or relative paths point to your extracted image dataset:
```yaml
path: ../datasets/rip_current_data  # dataset root dir
train: images/train
val: images/val

names:
  0: rip_current
```
*(Note: Large datasets should be stored locally outside this Git tree to prevent push size errors).*

### 2. Training the Model
To start training the object detection model using your custom scripts, run:
```bash
python train.py
```

### 3. Model Inference & Verification
To test model detection output on video frames or verify the pipeline implementation:
```bash
# Run testing scripts within the dedicated directory
python Testing/predict.py --source path/to/your/video.mp4 --weights Models/best.pt
```
Refer to the included `sample-rip-output.mp4` file in the root directory to see an example of expected visual bounding box outputs.

## 📜 License
This project is open-source and licensed under the terms of the **MIT License**.

