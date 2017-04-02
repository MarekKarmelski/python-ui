#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""BMI UI."""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from src.bmi import BMI
from src.dog_bmi import DogBMI
from src.cat_bmi import CatBMI


class BmiUi:

    def run(self):
        """Run application function."""
        self.display_interface()

    def display_interface(self):
        """Display interface function."""
        app_window = Tk()
        app_window.wm_title('BMI Calculator')
        app_window.resizable(width=False, height=False)
        app_window.minsize(height=400)

        """Top frame."""
        top_frame = Frame(app_window, borderwidth=2, relief='groove', pady=10, padx=10)
        top_frame.pack(fill='x', padx=5, pady=5)

        label1 = Label(top_frame, text='Calculate BMI for: ', width=15, anchor=W)
        label1.grid(row=0, column=0, sticky=W)

        types = ('HUMAN', 'DOG', 'CAT')
        cb_types = ttk.Combobox(top_frame, values=types, width=20)
        cb_types.current(0)
        cb_types.grid(row=0, column=1)

        middle_frame = Frame(app_window, borderwidth=2, relief='groove', pady=10, padx=10)
        middle_frame.pack(fill='x', padx=5, pady=5)

        label2 = Label(middle_frame, text='Weight (kg): ', width=15, anchor=W)
        label2.grid(row=0, column=0, sticky=W)

        weight_entry = Entry(middle_frame, width=10)
        weight_entry.grid(row=0, column=1, sticky=E, pady=3)

        label3 = Label(middle_frame, text='Height (m): ', width=15, anchor=W)
        label3.grid(row=1, column=0, sticky=W)

        height_entry = Entry(middle_frame, width=10)
        height_entry.grid(row=1, column=1, sticky=E, pady=3)

        bottom_frame = Frame(app_window, borderwidth=2, relief='groove', pady=10, padx=10)
        bottom_frame.pack(fill='x', padx=5, pady=5)

        norm_label = Label(bottom_frame, text='', font=("Helvetica", 16), padx=10, pady=10, fg='#ffffff')
        norm_label.pack(fill='x')

        label4 = Label(bottom_frame, text='BMI', font=("Helvetica", 20))
        label4.pack(fill='x')

        bmi_label = Label(bottom_frame, text='?', font=("Helvetica", 25))
        bmi_label.pack(fill='x')

        button_frame = Frame(app_window, borderwidth=2, relief='groove', pady=10, padx=10)
        button_frame.pack(fill='x', padx=5, pady=5)

        calculate_btn = Button(
            button_frame,
            text='Calculate',
            pady=10,
            command=lambda: self.calculate_bmi(cb_types, weight_entry, height_entry, bmi_label, norm_label)
        )
        calculate_btn.pack(fill='x')

        exit_btn = Button(button_frame, text='Close', pady=10, command=app_window.destroy)
        exit_btn.pack(fill='x')

        app_window.mainloop()

    def calculate_bmi(self, cb_type, weight_entry, height_entry, bmi_label, norm_label):
        """Calculate BMI."""
        weight = weight_entry.get()
        height = height_entry.get()

        weight = weight.replace(',', '.')
        height = height.replace(',', '.')

        try:
            try:
                weight = float(weight)
            except ValueError:
                raise Exception('Weight must be an number value!')
            if weight <= 0:
                raise Exception('Weight must be bigger then 0!')
            try:
                height = float(height)
            except ValueError:
                raise Exception('Height must be an number value!')
            if height <= 0:
                raise Exception('Height must be bigger then 0!')
            an_type = cb_type.get()
            if an_type == 'HUMAN':
                bmi_label.configure(text=an_type)
                bmi = BMI(weight, height)
                calculated_bmi = str(round(bmi.get_bmi(), 2))
                bmi_label.configure(text=calculated_bmi)
                bmi_norm = bmi.norm()
                if bmi_norm == -1:
                    norm_label.configure(text='You are underweight!', bg='#ffcc00')
                elif bmi_norm == 0:
                    norm_label.configure(text='You have a healthy weight!', bg='#00cc00')
                elif bmi_norm == 1:
                    norm_label.configure(text='You are overweight!', bg='#e60000')
            elif an_type == 'DOG':
                bmi = DogBMI(weight, height)
                calculated_bmi = str(round(bmi.get_bmi(), 2))
                bmi_label.configure(text=calculated_bmi)
                bmi_norm = bmi.norm()
                if bmi_norm == -1:
                    norm_label.configure(text='You are underweight!', bg='#ffcc00')
                elif bmi_norm == 0:
                    norm_label.configure(text='You have a healthy weight!', bg='#00cc00')
                elif bmi_norm == 1:
                    norm_label.configure(text='You are overweight!', bg='#e60000')
            elif an_type == 'CAT':
                bmi = CatBMI(weight, height)
                calculated_bmi = str(round(bmi.get_bmi(), 2))
                bmi_label.configure(text=calculated_bmi)
                bmi_norm = bmi.norm()
                if bmi_norm == -1:
                    norm_label.configure(text='You are underweight!', bg='#ffcc00')
                elif bmi_norm == 0:
                    norm_label.configure(text='You have a healthy weight!', bg='#00cc00')
                elif bmi_norm == 1:
                    norm_label.configure(text='You are overweight!', bg='#e60000')
        except Exception as e:
            messagebox.showerror('Error', e)

bmi_ui = BmiUi()
bmi_ui.run()
