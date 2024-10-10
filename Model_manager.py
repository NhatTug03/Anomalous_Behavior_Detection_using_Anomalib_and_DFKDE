import torch
from anomalib.models.image.dfkde.lightning_model import Dfkde
from anomalib.callbacks import GraphLogger
from anomalib.loggers import AnomalibTensorBoardLogger
from anomalib.data.image.folder import TaskType, Folder
from anomalib.engine import Engine
from anomalib.deploy import ExportType


def main():
    # Set up the data module with paths to your dataset and information on how data should be split and prepared
    datamodule = Folder(
        name="dataset2",
        root="./dataset2",
        normal_dir="good",
        abnormal_dir="crack",
        normal_split_ratio=0.2,
        image_size=(256, 256),
        train_batch_size=32,
        eval_batch_size=32,
        task=TaskType.CLASSIFICATION,
    )

    # Initialize the model with the chosen backbone and other hyperparameters
    model = Dfkde(
        backbone="resnet18",
        layers=["layer4"],
        pre_trained=True,
        n_pca_components=16,
        max_training_points=40000,
    )

    # Prepare the data and set up data loaders
    datamodule.setup()
    datamodule.prepare_data()

    # Set up logging and callbacks for model training insights
    logger = AnomalibTensorBoardLogger(save_dir="logs", name="dfkde")
    callbacks = [GraphLogger()]

    # Configure the engine for model training and evaluation
    engine = Engine(
        task="classification",
        max_epochs=10,
        callbacks=callbacks,
        logger=logger,
        image_metrics=["AUROC"],
    )

    # Train the model using the data module and defined model
    try:
        engine.fit(datamodule=datamodule, model=model)
    except Exception as e:
        print(f"An error occurred during training: {e}")

    # Export the trained model to a specified format for deployment
    try:
        engine.export(
            export_type=ExportType.OPENVINO, model=model, export_root="weights"
        )
    except Exception as e:
        print(f"An error occurred during model export: {e}")


if __name__ == "__main__":
    main()
