from anomalib.data.image.folder import TaskType, Folder
from anomalib.models.image.dfkde.lightning_model import Dfkde

from anomalib.engine import Engine
from omegaconf import OmegaConf
import torch

def main():
    # Assuming config and dataset setup
    folder_datamodule = Folder(
        name="dataset2",
        root="./dataset2",
        normal_dir="good",
        abnormal_dir="crack",
        task=TaskType.DETECTION,
        train_batch_size=64,
    )
    folder_datamodule.setup()

    # Initialize the KDEClassifier
    model = Dfkde(backbone='resnet18', layers=('layer4',), pre_trained=True, n_pca_components=16,
                  max_training_points=40000)

 

    # Create engine and train
    engine = Engine(max_epochs=10, task=TaskType.DETECTION)
    engine.fit(datamodule=folder_datamodule, model=model)

    # # Example usage of classifier
    # features = torch.randn(10, 1024)  # Simulated feature tensor
    # classifier.fit(features)  # Fit KDE model to features
    # probabilities = classifier.predict(features)  # Predict anomaly probabilities

if __name__ == '__main__':
    main()
