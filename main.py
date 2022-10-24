from tkinter import *
from tkinter import messagebox
import subprocess


def search_for_all_wifi_names():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
    profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]
    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('utf-8').split(
            '\n')

        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i][0]
        except IndexError:
            password = None

        with open(file='wifi_passwords_test.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}\n')


def search_for_wifi_name():

    if text_box.get() == " " or len(text_box.get()) == 0:
        messagebox.showerror("Error", "Write any wifi name")
    else:
        profile_info = subprocess.check_output(f'netsh wlan show profile {text_box.get()} key=clear')\
            .decode('utf-8').split('\n')
        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i][0]
        except IndexError:
            password = None

        messagebox.showinfo("Wifi information", password)


window = Tk()
window.title("Get wifi passwords")
window.geometry("580x260")
window.config(bg="light blue")
window.resizable(False, False)
text_box = Entry(font=15)
text_box.pack()
search_for_wifi_name = Button(0, text="Search for wifi", command=search_for_wifi_name)
search_for_wifi_name.pack()
search_for_all_wifi = Button(0, text="Search for all wifi", command=search_for_all_wifi_names)
search_for_all_wifi.pack()
window.mainloop()
