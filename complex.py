from tabnanny import check
import tkinter
import tkinter.messagebox
from typing_extensions import Self
import customtkinter
import sys

from numpy import imag

import  triggerbot as tb
import mask_guiviz as mg
import threading 
import cv2 
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 820
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("DUCK AIM")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="DUCK AIM",
                                              text_font=("Roboto Medium", -26))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=20)
        
        

        # self.button_1 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="AI-Aim ",
        #                                         fg_color=("gray75", "gray30"),  # <- custom tuple-color
        #                                         command=self.button_event)
        # self.button_1.grid(row=2, column=0, pady=20, padx=20)

        self.radio_var = tkinter.IntVar(value=0)
        
        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")
        
        
        self.radio_button_5 = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.radio_var,
                                                           value=0,
                                                            width=30,
                                                           height=30,
                                                           text="Trigger-Aim")
        self.radio_button_5.grid(row=2, column=0, pady=30, padx=20 , sticky="w")
        
        self.radio_button_6 = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.radio_var,
                                                           value=1,
                                                           width=30,
                                                           height=30,
                                                           text="STD-Aim")
        self.radio_button_6.grid(row=3, column=0, pady=30, padx=20,sticky="w")
        
        
        
        self.radio_button_7 = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.radio_var,
                                                           value=2,
                                                           width=30,
                                                           height=30,
                                                           text="AI-Aim")
        self.radio_button_7.grid(row=4, column=0, pady=30, padx=20,sticky="w")
        
        
        
        # self.button_2 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Trigger-Aim",
        #                                         fg_color=("gray75", "gray30"),  # <- custom tuple-color
        #                                         command=self.button_event)
        # self.button_2.grid(row=3, column=0, pady=20, padx=20)

        # self.button_3 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="STD-Aim",
        #                                         fg_color=("gray75", "gray30"),  # <- custom tuple-color
        #                                         command=self.button_event)
        # self.button_3.grid(row=4, column=0, pady=20, padx=20)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left,text="Toggle key")
        self.switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        # self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
        #                                         text="Dark Mode",
        #                                         command=self.change_mode)
        # self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkEntry(master=self.frame_info,
                                                   text="closing the gui doesn't meane closing the aimbot\n" ,
                                                   height=100,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT,)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="COLORS: purple is recommended")
        self.label_radio_group.grid(row=0, column=2, columnspan=2, pady=20, padx=10, sticky="ne")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=0,
                                                           text="Purple",
                                                           hover_color=("purple", "purple"),
                                                           fg_color=("purple", "purple"))
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=10, sticky="sw")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=1,
                                                           text="red",
                                                           hover_color=("red", "red"),
                                                           fg_color=("red", "red"))
        self.radio_button_2.grid(row=1, column=3, pady=10, padx=10, sticky="s")

        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
                                                command=self.progressbar.set)
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        # self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
        #                                                height=25,
        #                                                text="CTkButton",
        #                                                command=self.button_event)
        # self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
        #                                                height=25,
        #                                                text="CTkButton",
        #                                                command=self.button_event)
        # self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.checkbox_button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Settings",
                                                         border_width=3,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=self.button_event)
        self.checkbox_button_1.grid(row=6, column=2, columnspan=2, pady=10, padx=20, sticky="we")

        # self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="vizualize",
                                                     command=self.check_event)
        self.check_box_2.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=300,
                                            placeholder_text="enter your toggle-key")
        self.entry.grid(row=4, column=0, columnspan=1, pady=20, padx=100, sticky="se")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Start",
                                                command=self.trigger_start,
                                                fg_color=('#6B8E23'),
                                                text_color=('white', 'white'))
        self.button_5.grid(row=8, column=2, columnspan=2, pady=20, padx=20, sticky="we")
        
        self.button_stop = customtkinter.CTkButton(master=self.frame_right,
                                                text="Stop",
                                                command=self.kill_aim,
                                                fg_color=('#900C3F'),
                                                text_color=('white', 'white'))
        self.button_stop.grid(row=8, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.radio_button_1.select()
        #self.switch_2.select()
        #self.slider_1.set(0.2)
        self.slider_2.set(0.7)
        self.progressbar.set(0.5)
        #self.slider_button_1.configure(state=tkinter.DISABLED, text="Disabled Button")
        #self.radio_button_3.configure(state=tkinter.DISABLED)
        #self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        self.check_box_2.deselect()
        

        
    
    def trigger_start(self):
        t2 = threading.Thread(target=tb.main)
        t2.start()
        
        
    def button_event(self):
        print("Button pressed")
        text = self.entry.get()
        print(text)

            
        
    def kill_aim(self):
        t3 = threading.Thread(target=exiting)
        t3.start()
        exiting = sys.exit(tb.main)
        #print("Killing AIML")
        



    def check_event(self):
        print("CheckBox pressed")
        if self.check_box_2.get():
            t = threading.Thread(target=mg.main)
            t.start()
        

    # def change_mode(self):
    #     if self.switch_2.get() == 1:
    #         customtkinter.set_appearance_mode("dark")
    #     else:
    #         customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    
    t2 = threading.Thread(target=app.start())
    t2.start()
    #app.start()