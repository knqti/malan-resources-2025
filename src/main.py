from datetime import datetime
from utils import get_project_root, get_malan_data, read_write_csv

def main():
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    root_dir = get_project_root()

    raw_file = get_malan_data(root_dir, now)
    read_write_csv(root_dir, raw_file, now)    
    print('Data is ready')

if __name__ == '__main__':
    main()
