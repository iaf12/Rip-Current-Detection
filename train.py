'''Code V2'''

# # Download the model
# from ultralytics import YOLO

# # This line automatically downloads 'yolo26n.pt' or 'yolo26l.pt' from the cloud on first use
# # model = YOLO("yolo26n.pt")  # Nano (Ultra fast)
# model = YOLO("yolo26l.pt") # Large (High accuracy - great for your 16GB VRAM)
# print("YOLO26 downloaded and loaded successfully!")

from ultralytics import YOLO

# Load the YOLO model with pre-trained weights
model = YOLO("Models\\yolo26l.pt")  # Using YOLOv8 nano for faster training with smaller datasets

if __name__ == "__main__":
    # Train the model with optimized parameters
    model.train(
        data="data_custom.yaml",       # Path to custom dataset configuration
        imgsz=640,                    # Image size (higher size if GPU allows, e.g., 720 or 960)
        batch=16,                     # Increase batch size for better gradient updates
        epochs=300,                   # Train for 300 epochs or until convergence
        optimizer="SGD",            # AdamW optimizer for faster convergence
        lr0=0.001,                    # Initial learning rate
        workers=2,                    # Increase workers for faster data loading
        device=0,                   
          # Use GPU (adjust if multiple GPUs are available)
        patience=20,                  # Early stopping after 20 epochs of no improvement
        augment=True,                 # Enable data augmentation (flip, scale, etc.)
        val=True,                     # Evaluate performance on the validation set after every epoch
        # project="rip_current_model",  # Folder to save training logs and weights
        # name="rip_current_run",       # Name of the training run
        verbose=True                  # Show detailed training output
    )