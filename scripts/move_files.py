import os

files_dir = ''

for files in os.listdir():
    current_path = files
    # get names and extensions
    try:
        splits = files.split('.')
        extension = splits[1]
    except:
        continue
    
    if extension != 'csv':
        continue

    filename_with_date = splits[0]
    foldername = filename_with_date.split('-')[0]
    new_file_path = foldername + '/' + current_path
    
    # print(foldername)
    print(extension)
    # print(files)
    # print(new_file_path)

    if not os.path.exists(foldername):
        os.makedirs(foldername)

    # move file
    os.rename(current_path, new_file_path)

