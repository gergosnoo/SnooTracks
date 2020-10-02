import win32gui
import uiautomation as auto
from time import sleep
import datetime
import json
from TimeTracker.activity import *


active_window_name = ""
activity_name = ""
start_time = datetime.datetime.now()
activeList = AcitivyList([])
first_time = True


def url_to_name(url):
    string_list = url
    #print(url)
    return string_list


def get_active_window():
    _active_window_name = None
    window = win32gui.GetForegroundWindow()
    _active_window_name = win32gui.GetWindowText(window)
    return _active_window_name


def get_chrome_tab_name():
    window = win32gui.GetForegroundWindow()

    chrome_control = auto.ControlFromHandle(window)
    edit = chrome_control.EditControl()

    return chrome_control.Name[:chrome_control.Name.find(' - Google')]


try:
    activeList.initialize_me()
except Exception:
    print('No json')

try:
    while True:
        previous_site = ""
        new_window_name = get_active_window()
        if 'Google Chrome' in new_window_name:
            new_window_name = get_chrome_tab_name()

        if active_window_name != new_window_name:
            print(active_window_name)
            activity_name = active_window_name

            if not first_time:
                end_time = datetime.datetime.now()
                time_entry = TimeEntry(start_time, end_time, 0, 0, 0, 0)
                time_entry._get_specific_times()

                exists = False
                for activity in activeList.activities:
                    if activity.name == activity_name:
                        exists = True
                        activity.time_entries.append(time_entry)

                if not exists:
                    activity = Activity(activity_name, [time_entry])
                    activeList.activities.append(activity)
                with open('activities.json', 'w') as json_file:
                    json.dump(activeList.serialize(), json_file,
                              indent=4, sort_keys=True)
                    start_time = datetime.datetime.now()
            first_time = False
            active_window_name = new_window_name

        sleep(1)

except KeyboardInterrupt:
    with open('activities.json', 'w') as json_file:
        json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)