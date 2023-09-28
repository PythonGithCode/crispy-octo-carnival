from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk
from tkinterweb import HtmlFrame #import the HTML browser

import time, os, keyboard, toml#, webview

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView



from urllib.request import urlopen
from html.parser import HTMLParser

import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)



class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = ""

    def handle_data(self, data):
        self.data += data

## code that runs

# log when this starts
logging.info("Starting")

# keyboard.add_hotkey('ctrl+shift+a', logWithOut, args=("Test", "food"))



director = "C:/windowThing/"

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Main Window")
        self.master.geometry("400x300")

        # create a drop-down menu
        logging.debug("Creating a drop-down menu")
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        # create a "File" dropdown menu
        logging.debug("Creating a \"File\" dropdown menu")
        file_menu = tk.Menu(menu)
        
        logging.debug("Adding cascade to 'file_menu'")
        menu.add_cascade(label="File", menu=file_menu)
        
        logging.debug(f"Adding a command to the 'file_menu' command 'self.save_file'")
        file_menu.add_command(label="Save settings location", command=self.save_file)


        # create a "Settings" dropdown menu
        logging.debug("Creating a settings dropdown menu")
        settings_menu = tk.Menu(menu)
        logging.debug("Adding the settings lable to the 'settings_menu'")
        menu.add_cascade(label="Settings", menu=settings_menu)

        # add a "Advanced settings" submenu to the settings menu
        logging.debug("")
        advanced_menu = tk.Menu(settings_menu)
        logging.debug("")
        settings_menu.add_cascade(label="Advanced settings", menu=advanced_menu)


        # add a "Is Amazing" checkbox to the advanced settings menu
        self.is_amazing_var = tk.BooleanVar()
        self.is_amazing_var.set(False)
        advanced_menu.add_checkbutton(label="Is Amazing", variable=self.is_amazing_var, command=self.save_settings)

        # add a "Is Amazing" checkbox to the advanced settings menu
        self.is_top_var = tk.BooleanVar()
        self.is_top_var.set(False)
        advanced_menu.add_checkbutton(label="Is Top", variable=self.is_top_var, command=self.save_settings)


        # add a radio button group to the advanced settings menu
        self.radio_var = tk.StringVar()
        self.radio_var.set("foo")
        advanced_menu.add_radiobutton(label="Print 'foo'", variable=self.radio_var, value="foo", command=self.save_settings)
        advanced_menu.add_radiobutton(label="Set text size to 24px", variable=self.radio_var, value="size", command=self.save_settings)
        advanced_menu.add_radiobutton(label="Do nothing", variable=self.radio_var, value="nothing", command=self.save_settings)

        # keyboard.add_hotkey('ctrl+shift+c', self.openW3b, args=())

        # add an "All settings" item to the settings menu
        settings_menu.add_command(label="All settings window", command=self.open_all_settings)


        self.makeFileData_button = tk.Button(self.master, text="Make app data", command=self.makeAppDataStuff)
        self.makeFileData_button.pack()

        
        
        # create a "Settings" dropdown menu
        self.project_menu = tk.Menu(menu)
        menu.add_cascade(label="Project Menu", menu=self.project_menu)
        
        self.project_menu.add_command(label="Termoil", command=self.open_terminal)
        self.project_menu.add_command(label="WebPage", command=self.openWeb)
        self.project_menu.add_command(label="Wordle",  command=lambda: self.openWeb("https://wordleespanol.org/"))
        
        keyboard.add_hotkey('ctrl+shift+a', self.openWeb)
        keyboard.add_hotkey('ctrl+shift+b', self.raise_window, args=(self.master))


        # makeing notes
        self.project_menu.add_command(label="Notes", command=self.notesWindow)


        # keep this at the bottem to stop any errors
        try:
            self.load_settings()
            logging.info("Loaded settings")
        except:
            logging.error("Failed to load settings")
        self.web_app = QApplication([])

    def notesWindow(self):
        logging.debug("Running 'openW3b' function")
        pass

    def mocroRecoder(self, deration):
        logging.debug("Running 'openW3b' function")
        pass

    def openWeb(self, site="https://www.google.com/"):
        logging.debug("Running 'openWeb' function")
        try:
            self.web_webview = QWebEngineView()
            self.web_webview.load(QUrl(site))
            self.web_webview.show()
            self.web_app.exec_()
        except:
            loggging.error("Failed to load web page")
    
    def openW3b(self):
        logging.debug("Running 'openW3b' function")
        frame = HtmlFrame(self.master) #create HTML browser
        frame.load_website("https://www.google.com/") #load a website
        frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent windowframe = HtmlFrame(root) #create HTML browser



    # define a function to open a window with a terminal
    def open_terminal(self, n=None):
        logging.debug("Running 'open_terminal' function")
        with open(os.getcwd() + '\\terminalFile.txt', 'w') as f:
            f.write(' ')
        os.startfile(os.getcwd() + '\\terminalFile.txt')


    # define a function to load settings from a TOML file
    def load_settings(self):
        logging.debug("Running 'load_settings' function")
        # read the TOML file
        with open(director + "settings.toml", "r") as f:
            self.settings = toml.load(f)

        # update the widgets with the settings from the file
        self.is_amazing_var.set(self.settings["Is Amazing"])
        self.radio_var.set(self.settings["Radio"])
        self.is_top_var.set(self.settings["topmost"])
        self.master.wm_attributes("-topmost", self.settings["topmost"])
    

    def raise_window(self, window):
        logging.debug("Running 'raise_window' function")
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        window.focus_force()

    def makeAppDataStuff(self):
        logging.debug("Running 'makeAppDataStuff' function")
        try:
            os.mkdir(director)
        except:
            logging.error("Can't make dir")
        
        try:
            with open(director+"settings.toml") as f:
                f.write()
        except:
            logging.error("Can't write to settings")
        
    def open_popup(self, popup_name):
        logging.debug("Running 'open_popup' function")
        # create the pop-up window
        popup = tk.Toplevel(self.master)
        popup.title(popup_name)

        # add some content to the popup window
        popup_label = tk.Label(popup, text=f"This is {popup_name}!")
        popup_label.pack()

    def open_all_settings(self):
        logging.debug("Running 'open_all_settings' function")
        # create the "All settings" window
        self.settings_window = tk.Toplevel(self.master)
        self.settings_window.title("All Settings")
        self.settings_window.geometry("400x300")

        # create a tab control
        tab_control = ttk.Notebook(self.settings_window)
        tab_control.pack(expand=1, fill="both")

        # create the "Settings" tab
        settings_tab = ttk.Frame(tab_control)
        tab_control.add(settings_tab, text="Settings")

        # add the current values of all settings
        self.is_amazing_label = tk.Label(settings_tab, text=f"Is Amazing: {self.is_amazing_var.get()}")
        self.is_amazing_label.pack()
        
        # add the current values of all settings
        self.is_top_label = tk.Label(settings_tab, text=f"Is Top: {self.is_top_var.get()}")
        self.is_top_label.pack()

        
        # create the "Change values" tab
        change_values_tab = ttk.Frame(tab_control)
        tab_control.add(change_values_tab, text="Change Values")


        self.is_amazing_checkbutton = tk.Checkbutton(change_values_tab, text="Is Amazing", variable=self.is_amazing_var)
        self.is_amazing_checkbutton.pack()

        self.is_top_checkbutton = tk.Checkbutton(change_values_tab, text="Is Top", variable=self.is_top_var)
        self.is_top_checkbutton.pack()

        self.radio_label = tk.Label(settings_tab, text=f"Radio2: {self.radio_var.get()}")
        self.radio_label.pack()

        foo_radio = tk.Radiobutton(change_values_tab, text="Print 'foo'", variable=self.radio_var, value="foo")
        foo_radio.pack()

        size_radio = tk.Radiobutton(change_values_tab, text="Set text size to 24px", variable=self.radio_var, value="size")
        size_radio.pack()

        nothing_radio = tk.Radiobutton(change_values_tab, text="Do nothing", variable=self.radio_var, value="nothing")
        nothing_radio.pack()

        self.did_save = tk.Label(change_values_tab, text="")
        self.did_save.pack()

        # add a "Save" button to the "Change Values" tab
        save_button = tk.Button(change_values_tab, text="Save", command=self.save_settings)
        save_button.pack()

        self.settings_window.wm_attributes("-topmost", int(self.settings["topmost"])*29)
    
    def save_settings(self, update=False):
        logging.debug("Running save_settings function")
        # apply the new settings
        is_amazing = self.is_amazing_var.get()
        radio = self.radio_var.get()
        is_top = self.is_top_var.get()

        # save the settings to a TOML file
        self.settings_dict = {
            "Is Amazing": is_amazing,
            "Radio": radio,
            "topmost": is_top
        }
        with open(director+"settings.toml", "w") as f:
            toml.dump(self.settings_dict, f)
        
        if update:
            # update the "All Settings" tab to reflect the new values
            self.is_amazing_label.config(text=f"Is Amazing: {self.is_amazing_var.get()}")
            self.is_top_label.config(text=f"Is Top: {self.is_amazing_var.get()}")
            self.radio_label.config(text=f"Radio: {self.radio_var.get()}")
            self.did_save.config(text="Saved.", fg="green")
        
        try:
            self.load_settings()
            logging.info("reloaded settings")
        except:
            logging.error("Failed to reload settings")

    def save_file(self):
        logging.debug("File dialog")

        # open a file dialog box for saving a file
        file_path = filedialog.asksaveasfilename(initialdir=director, initialfile="settings.toml")
        try:
            logging.info("Saving file to: " + file_path)
        except Eception as e:
            logging.error("Saving to file FAILED, error: " + e)

        # do something with the file path

    # create a button that opens a file dialog box for saving a file
    


if __name__ == "__main__":
    logging.info("Version 0.0.3 - 23.9.27 (3)")
    root = tk.Tk()
    app = MainApplication(master=root)
    app.mainloop()


logging.info("ENDED")