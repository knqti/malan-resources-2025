import csv
import requests
import os
from pathlib import Path

def get_project_root():
    start_path = Path.cwd()
    start_path = start_path.resolve()
    marker = 'requirements.txt'

    for parent in [start_path, *start_path.parents]:
        if (parent / marker).exists():
            return parent
    
    print('ERROR: Could not find project root directory')

def get_malan_data(timestamp: str):
    url = 'https://docs.google.com/spreadsheets/d/1KMk34XY5dsvVJjAoD2mQUVHYU_Ib6COz6jcGH5uJWDY/export?gid=0&format=csv'
    response = requests.get(url)
    root_directory = get_project_root()
    downloaded_file = root_directory / 'data' / 'raw' / f'{timestamp}_downloaded.csv'

    with open(downloaded_file, 'wb') as f:
        f.write(response.content)
    
    print('Google Sheet downloaded')
    return downloaded_file

def read_write_csv(read_file: str, timestamp: str):
    cleaned_data = []

    with open(read_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)[2:] # skip first two rows
        
        for row in data:
            cleaned_row = []

            # Remove line breaks
            for cell in row:
                cleaned_cell = cell.strip().replace('\n', '')        
                cleaned_row.append(cleaned_cell)
            
            cleaned_data.append(cleaned_row)

    root_directory = get_project_root()
    write_file = root_directory / 'data' / 'cleaned' / f'{timestamp}_cleaned.csv'

    with open(write_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_data)
    
    print('CSV file cleaned')

def get_latest_file(directory: object):
    all_files = list(directory.glob(pattern='*'))

    latest_time = 0

    for file in all_files:
        mod_time = os.path.getmtime(file)

        if mod_time > latest_time:
            latest_time = mod_time
            latest_file = file

    print(f'File to display on website: {latest_file}')
    return latest_file
