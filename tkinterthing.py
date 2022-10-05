import tkinter.filedialog as filedialog
import tkinter as tk
import difflib

master = tk.Tk()

def CompareXML(standardxml, XMLPath):

    with open(standardxml, 'r', encoding='utf-8') as y:
        file1 = y.readlines()

    with open(XMLPath, 'r', encoding='utf-8') as fd:
        file2 = fd.readlines()

    diff = list(difflib.context_diff(file1, file2))

    global f

    f = '\n'.join(diff)

def file_save():
    d = filedialog.asksaveasfilename(filetypes=[('Text File', '*.txt')])
    if d is None:
        return
    with open(f'{d}.txt', 'w', encoding='utf-8') as j:
        j.write(f)

def open_popup():
   top= tk.Toplevel()
   top.title(".tds diff overview")
   top.geometry('750x750')
   save = tk.Button(top, text="Save", command=file_save)
   save.pack(side=tk.BOTTOM, pady=10)
   text_widget = tk.Text(top, height=700, width=700)
   scroll_bar = tk.Scrollbar(top)
   scroll_bar.pack(side=tk.RIGHT)
   text_widget.pack(side=tk.LEFT)
   text_widget.insert(tk.END, f)


def begin():
    base_file = input_entry.get()
    comparison_file = output_entry.get()
    CompareXML(base_file, comparison_file)

def input():
    input_path = filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'


def output():
    path = filedialog.askopenfilename()
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, path)  # Insert the 'path'


top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')
master.title('Jonesy\'s .tds diff util')

input_path = tk.Label(top_frame, text="Base File:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)

output_path = tk.Label(bottom_frame, text="Comparison File:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Browse", command=output)

# save_path = tk.Label(bottom_frame, text="Save To:")
# save_entry = tk.Entry(bottom_frame, text="", width=40)
# save = tk.Button(bottom_frame, text="Browse", command=filedialog.asksaveasfile(mode='w', defaultextension='.txt'))

begin_button = tk.Button(bottom_frame, text='Compare', command=lambda:[begin(), open_popup()])

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

# save_path.pack(pady=5)
# save_entry.pack(pady=5)
# save.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)

master.mainloop()
