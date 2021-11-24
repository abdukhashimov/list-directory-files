import os
import json

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk('./serials'):
    for filename in filenames:
        dir_name = dirpath.split('/')[-1]
        if dir_name in list_of_files:
            list_of_files[dir_name].append(filename)
        else:
            list_of_files[dir_name]=[filename]

json_output = json.dumps(list_of_files, indent=2)
with open('output.json', 'w') as writer:
    writer.write(json_output)
