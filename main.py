import sys
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import subprocess  # 用于打开文件

root = tk.Tk()
root.title('SearchTool')
root.geometry('800x300')

search_frame = tk.Frame(root)
search_frame.pack()

tk.Label(search_frame, text='SearchKey').pack(side=tk.LEFT, padx=10, pady=10)
key_entry = tk.Entry(search_frame)
key_entry.pack(side=tk.LEFT, padx=10, pady=10)
tk.Label(search_frame, text='FileType').pack(side=tk.LEFT, padx=10, pady=10)
type_entry = tk.Entry(search_frame)
type_entry.pack(side=tk.LEFT, padx=10, pady=10)

# Button
search_button = tk.Button(search_frame, text='Search')
search_button.pack(side=tk.LEFT, padx=10, pady=10)

list_box = tk.Listbox(root, width=80)
list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar
sb = tk.Scrollbar(root)
sb.pack(side=tk.RIGHT, fill=tk.Y)
list_box.config(yscrollcommand=sb.set)
sb.config(command=list_box.yview)


def search():
    key = key_entry.get()
    file_type = type_entry.get().lstrip('.')  # 移除文件类型前的"."

    if not key:
        messagebox.showinfo(title='Error', message='Please enter a valid search key.')
        return

    if not file_type:
        messagebox.showinfo(title='Error', message='Please enter a file type.')
        return

    # Open directory selection dialog
    fn = filedialog.askdirectory()
    if not fn:
        return  # 如果用户取消选择文件夹，则返回

    list_box.delete(0, tk.END)  # 清空列表框中的现有内容

    fn_list = os.walk(fn)  # 遍历所有文件
    for root_path, dirs, files in fn_list:
        for file in files:
            if file.endswith(file_type) and key in file:
                full_path = os.path.join(root_path, file)
                list_box.insert(tk.END, full_path)


def list_box_click(event):
    try:
        index = list_box.curselection()[0]
        file_path = list_box.get(index)
        if os.name == 'nt':  # 如果是Windows
            os.startfile(file_path)
        elif os.name == 'posix':  # 如果是macOS或Linux
            subprocess.call(('open' if sys.platform == 'darwin' else 'xdg-open', file_path))
    except IndexError:
        messagebox.showinfo(title='Error', message='Please select a file.')


# Set button command to search files
search_button.config(command=search)
# Bind double-click event to list box
list_box.bind('<Double-Button-1>', list_box_click)

root.mainloop()
