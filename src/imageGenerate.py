import os
import json

# Assuming you pre-load or list the images manually:
images_dir = "/home/send/images"
image_files = [f for f in os.listdir(images_dir) if f.endswith(".png")]

def generate_title(name):
    name = name.replace("-", " ").replace("_", " ")
    return name.title()

image_data = []

for filename in image_files:
    name, _ = os.path.splitext(filename)
    image_record = {
        "name": name,
        "src": os.path.join(images_dir, filename),
        "title": generate_title(name),
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }
    image_data.append(image_record)

# Output formatted TypeScript-like JSON
print(json.dumps(image_data, indent=4))
