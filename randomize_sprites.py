import json
import random
import yaml

# find a way to read .yml file in python
with open('mod.yml') as file:
    replacements = yaml.full_load(file)

# access keys from json file
with open('sprites.json') as f:
  id_mapping = json.load(f)

# create a copy of the keys that are randomized
vanilla_ids = list(id_mapping.keys())
randomized_ids = vanilla_ids.copy()
random.shuffle(randomized_ids)

# create dict of this pairing
id_replacement_dict = {k: v for k, v in zip(vanilla_ids, randomized_ids)}

# replace all source name attributes in the yml file
assets = replacements['assets']
for k, v in id_replacement_dict.items():
   for asset in assets:
    if k in asset["name"] and "source" in asset:
       for source_asset in asset["source"]:
            if "name" in source_asset:
                source_asset["name"] = source_asset["name"].replace(k, v)

# save the yml file
with open('mod.yml', 'w') as file:
    documents = yaml.dump(replacements, file)