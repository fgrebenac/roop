import os
import subprocess

male_images = os.listdir("/Users/fgrebenac/Work/amphr/roop/images/Male")
female_images = os.listdir("/Users/fgrebenac/Work/amphr/roop/images/Female")

for img in male_images:
    # TODO run roop
    subprocess.run(["python3.11", "run.py", "-s", "/Users/fgrebenac/Work/amphr/roop/new_source.jpeg", "-t", "/Users/fgrebenac/Work/amphr/roop/images/Male/" + img, "-o", "/Users/fgrebenac/Work/amphr/roop/images_out/male/out_" + img])
    print(img)
    
for img in female_images:
    # TODO run roop
    subprocess.run(["python3.11", "run.py", "-s", "/Users/fgrebenac/Work/amphr/roop/new_source.jpeg", "-t", "/Users/fgrebenac/Work/amphr/roop/images/Female/" + img, "-o", "/Users/fgrebenac/Work/amphr/roop/images_out/female/out_" + img])
    print(img)