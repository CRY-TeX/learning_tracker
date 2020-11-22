import time
import os
import json
import codecs

from app_manager import AppManager

def main():
    try:
        # paths
        PATH_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

        app_man = AppManager(os.path.join(PATH_CURRENT_DIR, '../assets/data/config_data.json'),
                             os.path.join(PATH_CURRENT_DIR, '../assets/data/learning_data.csv'))

        app_man.run()

        app_man.close()
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
    print('Mainloop done. Exiting script')