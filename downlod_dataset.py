from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("3636").project("bunnybots-2023")
dataset = project.version(6).download("yolov8", location="datasets")