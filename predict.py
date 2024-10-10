from anomalib import TaskType
from anomalib.deploy import OpenVINOInferencer
from loguru import logger

inferencer = OpenVINOInferencer(
    path="./weights/weights/openvino/model.xml",  # Path to the OpenVINO IR model.
    metadata="./weights/weights/openvino/metadata.json",  # Path to the metadata file.
    device="CPU",  # We would like to run it on an Intel CPU.
    task=TaskType.CLASSIFICATION,
)

image_path = "images/lon_binh_thuong_ngang_rdg_frame_2976_normal.png"
predictions = inferencer.predict(image=image_path)

logger.info(
    "{}: {}, {:.4f}".format(image_path, predictions.pred_label, predictions.pred_score)
)
