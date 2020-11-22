from datetime import datetime
import codecs
import re
import json

class LearningManager(object):
    def __init__(self, json_data_path, csv_data_path):
        self._json_data_path = json_data_path
        self._json_data = json.loads(codecs.open(self._json_data_path, 'r', encoding='utf-8').read())
        self._started = False
        self._start_time = None
        self._end_time = None
        self._csv_data_path = csv_data_path

    def get(self, json_data_key):
        if json_data_key in self._json_data.keys():
            return self._json_data[json_data_key]
        else:
            return None

    def start_session(self):
        if not self._started:
            self._started = True
            self._start_time = datetime.now()
            return True
        else:
            return False

    def stop_session(self):
        if self._started:
            self._started = False
            self._stop_time = datetime.now()
            return True
        else:
            return False

    def reset_session(self):
        self._started = False
        self._start_time = None
        self._stop_time = None

    def _format_activities(self, activities):
        try:
            return re.subn('\n', ', ', activities, re.MULTILINE | re.DOTALL)[0]
        except Exception as ex:
            print(ex)
            return ''

    def export_session_to_csv(self, course, productivity, difficulty, activities):
        try:
            if course == '' or productivity == '' or difficulty == '':
                return False

            with codecs.open(self._csv_data_path, 'a', encoding='utf-8') as data_file:
                data_file.write(f'{self._json_data["current-session-id"]};{self._start_time};{self._stop_time};{course};{self._format_activities(activities)};{productivity};{difficulty}' + '\n')
            self._json_data["current-session-id"] += 1
            self.reset_session()
            return True
        except Exception as ex:
            print(ex)
            return False

    def export_json_data(self):
        try:
            with codecs.open(self._json_data_path, 'w', encoding='utf-8') as config_file:
                config_file.write(json.dumps(self._json_data))
            return True
        except Exception as ex:
            print(ex)
            return False