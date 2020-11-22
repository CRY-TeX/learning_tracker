from datetime import datetime, timedelta


import learning_manager as lm
import component_manager as cm



class AppManager(object):
    def __init__(self, json_data_path, csv_data_path):
        self._learning_manager = lm.LearningManager(json_data_path, csv_data_path)
        self._component_manager = cm.ComponentManager(self._learning_manager._json_data)
        self.set_events()

    def set_events(self):
        try:      
            def on_button_start(event):
                try:
                    if self._component_manager.combobox_course.get() == '':
                        cm.mb.Message(message='Choose course!').show()
                        return
                    
                    self._learning_manager.start_session()
                    self._component_manager.label_start_time['text'] = self._learning_manager._start_time.strftime('%H:%M:%S')

                except Exception as ex:
                    print(ex)
            self._component_manager.button_start.bind('<Button-1>', on_button_start)

            def on_button_submit(event):
                try:
                    if not self._learning_manager._started:
                        cm.mb.Message(message='No active session found.').show()
                        return

                    if not self._component_manager.data_valid():
                        cm.mb.Message(message='Configure all data fiels for saving session data').show()
                        return
                    
                    self._learning_manager.stop_session()
                    self._learning_manager.export_session_to_csv(self._component_manager.combobox_course.get(), self._component_manager.combobox_productivity.get(), self._component_manager.combobox_difficulty.get(), self._component_manager.text_activity.get('0.0', cm.tk.END))    
                    self._component_manager.reset_input_data()
                    self._learning_manager.reset_session()
                    self._component_manager.label_session_id['text'] = self._learning_manager.get('current-session-id')
                    cm.mb.Message(message='Current learning session saved.').show()
                        
                except Exception as ex:
                    print(ex)
            self._component_manager.button_submit.bind('<Button-1>', on_button_submit)

            def on_button_reset(event):
                try:
                    self._learning_manager.reset_session()
                    self._component_manager.reset_input_data()
                except Exception as ex:
                    print(ex)
            self._component_manager.button_reset.bind('<Button-1>', on_button_reset)

            def set_duration():
                try:
                    if self._learning_manager._started:
                        duration = (datetime.now() - self._learning_manager._start_time)
                        self._component_manager.label_duration_time['text'] = f'{str(duration.seconds // 60 // 60).rjust(2, "0")}:{str((duration.seconds // 60) % 60).rjust(2, "0")}'
                    self._component_manager.window.after(10000, set_duration)
                except Exception as ex:
                    print(ex)
            self._component_manager.window.after(10000, set_duration)

            def on_closing():
                if self._learning_manager._started:
                    if cm.mb.askokcancel("Quit", "Discard current session?"):
                        self._component_manager.window.destroy()
                        self.close()
                else:
                    self._component_manager.window.destroy()

            self._component_manager.window.protocol("WM_DELETE_WINDOW", on_closing)

        except Exception as ex:
            print(ex)

    def run(self):
        self._component_manager.window.mainloop()

    def close(self):
        self._learning_manager.export_json_data()