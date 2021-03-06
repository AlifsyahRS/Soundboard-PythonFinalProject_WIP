import tkinter as tk
from playsound import playsound
# Used for creating a file explorer to select a file.
from tkinter import filedialog


class Soundboard():

    def __init__(self, button_num, master):
        self.button_num = int(button_num)
        self.file = None
        # Since I can only initialize the main window in the main file, I need a placeholder variable to act as the main window.
        self.master = master
        self.frame = tk.Frame(master)
        self.play_button = tk.Button(self.frame, text=f"Audio {self.button_num}", width=10,
                                     height=5, command=self.playSound)
        self.button_preferences = tk.Button(
            self.frame, text="*", width=3, height=3, command=self.buttonPreferences)
        self.rename_str = tk.StringVar()

    def playSound(self):
        if self.file == None:
            # Nothing happens if no file is chosen.
            pass
        else:
            # playsound() plays the audio file
            playsound(self.file)

    def buttonPreferences(self):
        # Creating a new window
        new_window = tk.Toplevel(self.master)
        new_window.title(f"Preferences for Button {self.button_num}")
        # setfile_button executes the setFile function which opens the file directory
        setfile_button = tk.Button(
            new_window, text="Swap Current\nAudio File", width=10, height=5, command=self.setFile)
        setfile_button.pack()
        # change_buttonlabel initializes setButtonLabel which creates a new window.
        change_buttonlabel = tk.Button(
            new_window, text="Rename Button", width=10, height=5, command=self.setButtonLabel)
        change_buttonlabel.pack()

    def setFile(self):
        self.file = filedialog.askopenfilename(
            filetypes=[("Mp3 Files", "*.mp3"), ("Uncompressed Audio Files", "*.wav")]).replace(" ", "%20")
        # When executed, this function will create a file explorer wherein the user can choose top open the audio files the choose.
        # Replace is needed because the interpreter cannot reach a directory which contains a space character in its name

    def setButtonLabel(self):
        # Toplevel creates a separate window from the main window.
        rename_window = tk.Toplevel(self.master)
        rename_window.title(f"Rename Play Button {self.button_num}")
        rename_entry = tk.Entry(rename_window, bd=5,
                                textvariable=self.rename_str)  # rename_str gets the value of whatever the user specifies in the entry
        rename_button = tk.Button(
            rename_window, bd=5, text="Enter", command=self.getNewButtonText)  # Changes play button label on pressing enter button
        # Changes play button label on hitting enter
        rename_window.bind("<Return>", lambda getText: self.getNewButtonText())
        # .pack() makes the respective object visible and interactable in the GUI
        rename_entry.pack(side=tk.LEFT)
        rename_button.pack(side=tk.RIGHT)

    def getNewButtonText(self):
        # Changes the play button label into the value of rename_str
        self.play_button.configure(text=self.rename_str.get())

    def packButtons(self):
        self.master.bind(
            f"{self.button_num}", lambda play: self.playSound())
        self.play_button.pack(side=tk.LEFT)
        self.button_preferences.pack(side=tk.RIGHT)
        self.frame.pack()
