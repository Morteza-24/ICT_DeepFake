import os, json
real = "ICT_DeepFake/DATASET/FF/Real/"
reals = []
for filename in os.listdir(real):
    reals.append(real[13:]+filename)
with open("ICT_DeepFake/DATASET/paths/paths_of_ff_real.json", "wt") as f:
  json.dump(reals, f)
fake = "ICT_DeepFake/DATASET/FF/Fake/"
fakes = []
for filename in os.listdir(fake):
    fakes.append(fake[13:]+filename)
with open("ICT_DeepFake/DATASET/paths/paths_of_ff_fake.json", "wt") as f:
  json.dump(fakes, f)
