import json
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox as mb

class ComponentManager(object):
    pass
    # move all the tkinter stuff except window here

    def create_components(self, json_data):
        # create window
        self.window = tk.Tk()
        self.window.title('Learning Tracker')
        # self.window.iconphoto(False, tk.PhotoImage(file=os.path.join(PATH_CURRENT_DIR, '../assets/images/learning-transparent.png')))
        self.window.minsize(600, 400)

        # session
        frame_session = tk.Frame(master=self.window, padx=5)
        frame_session.grid(row=0, column=0, sticky='ew', columnspan=3, pady=(5, 20))
        frame_session.columnconfigure(0, weight=1)
        frame_session.columnconfigure(1, weight=1)
        frame_session.columnconfigure(2, weight=1)
        frame_session.rowconfigure(0, weight=1)
        frame_session.rowconfigure(1, weight=1)

        label_session = tk.Label(text='Session:', master=frame_session, anchor='w')
        label_session.grid(row=0, column=0, sticky='w', padx=20)

        self.label_session_id = tk.Label(text=json_data['current-session-id'], master=frame_session, font=font.Font(size=18, weight='bold'))
        self.label_session_id.grid(row=0, column=1, sticky='ew')


        # self.button_new_session = tk.Button(text='New Session', master=frame_session, anchor='e')
        # self.button_new_session.grid(row=0, column=2, sticky='e')
        
        self.window.columnconfigure(0, weight=1)

        # course        
        frame_course = tk.Frame(master=self.window)
        frame_course.grid(row=1, sticky='ew', columnspan=3, pady=(10, 20), padx=20)
        frame_course.columnconfigure(0, weight=1)
        self.combobox_course = ttk.Combobox(values=json_data['combobox-course'], master=frame_course, justify='center', state='readonly', font=font.Font(size=16, weight='bold'))
        self.combobox_course.grid(row=1, column=0, sticky='ew', pady=9)

        # frame times
        frame_times = tk.Frame(master=self.window, padx=3, pady=5)
        frame_times.grid(row=2, column=0, sticky='ew', columnspan=3, pady=(0, 30))
        frame_times.columnconfigure(0, weight=1)
        frame_times.rowconfigure(0, weight=1)
        frame_times.rowconfigure(1, weight=1)
        frame_times.rowconfigure(2, weight=1)

        label_duration = tk.Label(text='Duration', master=frame_times, font=font.Font(size=14))
        label_duration.grid(row=0, column=0, sticky='ew')

        self.label_duration_time = tk.Label(text='00:00', master=frame_times, font=font.Font(size=16))
        self.label_duration_time.grid(row=1, column=0, sticky='ew', pady=(0, 15))
        
        frame_start = tk.Frame(master=frame_times)
        frame_start.grid(row=2, column=0, sticky='ew')

        label_start = tk.Label(text='Start time: ', master=frame_start, font=font.Font(size=12, weight='bold'))
        label_start.grid(row=2, column=0, sticky='w')

        self.label_start_time = tk.Label(text='', master=frame_start, font=font.Font(size=12))
        self.label_start_time.grid(row=2, column=1, sticky='w')


        # buttons
        frame_buttons = tk.Frame(master=self.window)
        frame_buttons.grid(row=3, column=0, sticky='ew', columnspan=3, pady=(0, 30))
        frame_buttons.columnconfigure(0, weight=1)
        frame_buttons.columnconfigure(1, weight=1)
        frame_buttons.columnconfigure(2, weight=1)

        self.button_start = tk.Button(text='Start', master=frame_buttons)
        self.button_start.grid(row=0, column=0, sticky='ew', padx=20)

        self.button_submit = tk.Button(text='Submit', master=frame_buttons)
        self.button_submit.grid(row=0, column=1, sticky='ew', padx=20)
        self.button_reset = tk.Button(text='Reset Session', master=frame_buttons)
        self.button_reset.grid(row=0, column=2, sticky='ew', padx=20)


        # frame for border
        tk.Frame(master=self.window, borderwidth=2, bg='black').grid(row=4, column=0, sticky='ew', pady=(0, 20))

        # productivity
        frame_lerning_impession = tk.Frame(master=self.window)
        frame_lerning_impession.grid(row=5, column=0, sticky='w', padx=5, pady=(0, 20))

        label_productivity = ttk.Label(text='Productivity:', master=frame_lerning_impession)
        label_productivity.grid(row=0, column=0, sticky='w', padx=(0, 10))

        self.combobox_productivity = ttk.Combobox(values=json_data['combobox-productivity'], master=frame_lerning_impession, state='readonly')
        self.combobox_productivity.grid(row=0, column=1, sticky='w', padx=(0, 30))

        # difficulty
        label_difficulty = ttk.Label(text='Difficulty: ', master=frame_lerning_impession)
        label_difficulty.grid(row=0, column=2, sticky='e', padx=(0, 10))
        self.combobox_difficulty = ttk.Combobox(values=json_data['combobox-difficulty'], master=frame_lerning_impession, state='readonly')
        self.combobox_difficulty.grid(row=0, column=3, sticky='e')

        # activity
        frame_activity = tk.Frame(master=self.window)
        frame_activity.grid(row=6, column=0, sticky='ew', padx=20, pady=20)

        label_activity = ttk.Label(text='Activity: ', master=frame_activity)
        label_activity.grid(row=0, column=0, sticky='ew')
        self.text_activity = tk.Text(master=frame_activity, height=5)
        self.text_activity.grid(row=1, column=0, sticky='ew')

    def __init__(self, json_data):
        self.create_components(json_data)

    def reset_input_data(self):
        self.combobox_course.set('')
        self.combobox_difficulty.set('')
        self.combobox_productivity.set('')
        self.text_activity.delete('0.0', tk.END)
        self.label_start_time['text'] = ''
        self.label_duration_time['text'] = '00:00'

    def data_valid(self):
        if self.combobox_course.get() == '' or self.combobox_productivity.get() == '' or self.combobox_difficulty.get() == '' or self.text_activity.get('0.0', tk.END) == '':
            return False
        else:
            return True