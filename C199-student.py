#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Name : ")
print("We will be learning how to create a application on juipter which has GUI elements and how to manuipulate the output as per the values selected from the GUI components")


# # Code for GUI compenents and manuipulating the output

# In[ ]:


from ipywidgets import widgets
from IPython.display import display, clear_output
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

graph_type = ['Choose one..', 'line', 'bar'] 
df = ' '
def select_files (b):
    clear_output()
    global graph_type
    global df
    root = Tk()
    root.withdraw() # Hide the main window.
    file_name = filedialog.askopenfilename() # List of selected files will be set button's file attribute. df = pd.read_csv(file_name) # Print the list of files selected.
    print(file_name)
    xlabel_widget=widgets.Dropdown (options = df.columns)
    ylabel_widget=widgets.Dropdown (options = df.columns)
    graph_widget=widgets.Dropdown (options = graph_type)
    graph_widgets. interactive (display_plot, xaxis=xlabel_widget, yaxis= ylabel_widget, graph_type = graph_widget)
    display(graph)
fileselect=widgets.Button(description="File select")
fileselect.on_click(select_files)
display (fileselect)


# In[ ]:





# In[ ]:




