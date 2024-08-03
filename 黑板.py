import os
import pandas as pd
import re

def parse_mapbw_file(mapbw_path):
    with open(mapbw_path, 'r') as file:
        content = file.read()
    
    # Extract SlotNo
    slot_no_search = re.search(r'\[MeasureData\.WaferDataList\],\d+,\(\*Matrix\*\)\n(?:.+\n)*?(\d+),(\d+),', content)
    slot_no = None
    if slot_no_search:
        slot_no = slot_no_search.group(2)
    
    # Extract PointsData
    points_data = {'a': {}, 'b': {}, 'c': {}, 'd': {}}
    
    points_data_searches = re.findall(r'\[MeasureData\.PointsDataList\.PointsData_(\d+)\.LineDataList\.PointDataList_(\w+)\],\d+,\(\*Matrix\*\)\nNo,thickness,lowprofile\n((?:\d+,\d+,\d+\.\d+\n)*)', content)
    
    for points_data_search in points_data_searches:
        dataset_id, data_type, data_lines = points_data_search
        if int(dataset_id) > 1:
            continue  # Skip if not the first two datasets
        
        data_lines = data_lines.strip().split('\n')
        for line in data_lines:
            _, _, lowprofile = line.split(',')
            index = int(line.split(',')[0])
            field_key = chr(ord('a') + int(dataset_id)) + str(index)
            points_data[chr(ord('a') + int(dataset_id))][field_key] = lowprofile
    
    return slot_no, points_data

def process_folder(folder_path):
    data = []
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if not os.path.isdir(subfolder_path):
            continue

        
        # Iterate over all files in the subfolder
        labels = {}
        cnt = 1; name1 = ""; name2 = ""
        for image_file in os.listdir(subfolder_path):
            if cnt == 1: name1 = image_file
            else: name2 = image_file
            if image_file.endswith('.PNG'):
                # Extract the label from the image filename
                label = image_file.split('-')[1].split('.')[0]
                # Store the label in the dictionary with the image file as the key
                labels[image_file] = label
            cnt += 1
        
        print(labels)
    #     # Find mapbw file
    #     mapbw_file = None
    #     for file in os.listdir(subfolder_path):
    #         if file.endswith('.mapbw'):
    #             mapbw_file = os.path.join(subfolder_path, file)
    #             break
        
    #     if not mapbw_file:
    #         continue
        
    #     slot_no, points_data = parse_mapbw_file(mapbw_file)
        

        

    #     if not slot_no or not points_data:
    #         continue
        
    #     # Prepare row
    #     row = {
    #         'folder name': subfolder,
    #         'SlotNo': slot_no,
    #         'label': label
    #     }
        
    #     # Fill in a1 to a73, b1 to b73, etc.
    #     for key in points_data['a']:
    #         row[key] = points_data['a'][key]
    #     for key in points_data['b']:
    #         row[key] = points_data['b'][key]
    #     for key in points_data['c']:
    #         row[key] = points_data['c'][key]
    #     for key in points_data['d']:
    #         row[key] = points_data['d'][key]
        
    #     data.append(row)
    
    # return data

def save_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    folder_path = '/Users/tianqinmeng/Desktop/profile_nano'
    output_file = '/Users/tianqinmeng/Desktop/profile_data.xlsx'
    
    process_folder(folder_path)
    # data = process_folder(folder_path)
    # save_to_excel(data, output_file)
