from anomalib.data.image.folder import TaskType, Folder
def main():
    datamodule = Folder( 
        name="./dataset2",

        root='./dataset2', 

        normal_dir="./good", 

        abnormal_dir="./crack", 

        normal_split_ratio=0.2, 

        image_size=(256, 256), 

        train_batch_size=32, 

        eval_batch_size=32, 

        task=TaskType.CLASSIFICATION, 

    ) 

    datamodule.setup()  # Split the data to train/val/test/prediction sets. 

    datamodule.prepare_data()  # Create train/val/test/predic dataloaders 

    i, data = next(enumerate(datamodule.val_dataloader())) 

    print(data.keys())

if __name__ == "__main__":
    main()