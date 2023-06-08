from groundingdino.util.inference import load_model, load_image, predict, annotate
import cv2
import numpy
import difflib

def similarity(file1, file2):
    normalized1 = file1.lower()
    normalized2 = file2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()

model = load_model("/GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py", "/GroundingDINO/weights/groundingdino_swint_ogc.pth")
IMAGE_PATH = "/GroundingDINO/chairs.jpg"
TEXT_PROMPT = "chair . table ."
BOX_TRESHOLD = 0.35
TEXT_TRESHOLD = 0.25

image_source, image = load_image(IMAGE_PATH)

boxes, logits, phrases = predict(
    device="cpu",
    model=model,
    image=image,
    caption=TEXT_PROMPT,
    box_threshold=BOX_TRESHOLD,
    text_threshold=TEXT_TRESHOLD
)

f = open("/GroundingDINO/docker_results.txt", "w+")
docker_result = ""
for i in range(len(phrases)):
    tmp = str(phrases[i]) + " " + str(round(logits[i].item(), 3)) + " " + str(numpy.around(boxes[i].numpy(), decimals = 3)) + '\n'
    f.write(tmp)
    docker_result += tmp
f.close()

local_f = open("/GroundingDINO/local_results.txt", "r")
local_result = local_f.read()

print(f"Similarity: {similarity(docker_result, local_result) * 100}%")