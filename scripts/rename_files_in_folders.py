import os

folders = ['Indoor_Run', 'Indoor_Walk', 'Outdoor_Run', 'Outdoor_Walk', 
           'Rowing', 'Symptoms', 'Traditional_Strength_Training', 'Workouts', 'Yoga']

for folder in folders:
    print(folder)
    for files in os.listdir(folder):
        current_path = files
        filename, extension = current_path.split('.')
        if extension != 'csv':
            continue

        filename = filename.replace(" ", "_")
        filename_split = filename.split('-')
        del filename_split[0]

        new_file_path = folder + "/" + "-".join(filename_split) + "." + extension
        current_path = folder + '/' + files

        os.rename(current_path, new_file_path)

    print("==============")
    print()