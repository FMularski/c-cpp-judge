import tkinter as tk
from tkinter import filedialog


class Judge():
    def __init__(self):
        self.window = tk.Tk()
        self.bg = '#FFF982'
        self.filename = None
        self.test_data = None
        self.width = 500
        self.height = 600

        self.set_window(title='C/C++ Judge', size=f'{self.width}x{self.height}')
        self.set_widgets()
        self.show()

    def set_window(self, title, size):
        self.window.title(title)
        self.window.geometry(size)
        self.window.configure(bg=self.bg)
        self.window.iconbitmap('judge.ico')

    def set_widgets(self):
        self.choose_file_btn = tk.Button(self.window, text='<< Choose source file >>', width=20, bg='white', command=self.choose_source_file)
        self.filename_label = tk.Label(self.window, text=self.filename, width=50, bg='white')
        self.choose_test_data_btn = tk.Button(self.window, text='<< Choose test data >>', width=20, bg='white', command=self.choose_test_data_file)
        self.test_data_label = tk.Label(self.window, text=self.test_data, width=50, bg='white')
        self.exp_output_label = tk.Label(self.window, text='Expected output:', bg=self.bg)
        self.exp_output = tk.Text(self.window, height=4, width=50)
        self.judge_btn = tk.Button(self.window, text='Judge', width=20, bg='white', command=self.judge)
        self.output_label = tk.Label(self.window, text='Output:', bg=self.bg)
        self.output = tk.Label(self.window, height=4, width=50, bg='white')
        self.time_label = tk.Label(self.window, text='Execution time:', bg=self.bg)
        self.time = tk.Label(self.window, text='', width=50, bg='white')
        self.result_label = tk.Label(self.window, text='Result:', bg=self.bg)
        self.result = tk.Label(self.window, text='', width=50, bg='white')

        self.choose_file_btn.place(anchor='n', x=self.width / 2, y=10)
        self.filename_label.place(anchor='n', x=self.width / 2, y=45)

        self.choose_test_data_btn.place(anchor='n', x=self.width / 2, y=75)
        self.test_data_label.place(anchor='n', x=self.width / 2, y=110)



        self.exp_output_label.place(anchor='n', x=self.width / 2, y=140)
        self.exp_output.place(anchor='n', x=self.width / 2, y=160)

        self.judge_btn.place(anchor='n', x=self.width / 2, y=240)
        self.output_label.place(anchor='n', x=self.width / 2, y=300)

        self.output.place(anchor='n', x=self.width / 2, y=340)


        self.time_label.place(anchor='n', x=self.width / 2, y=420)
        self.time.place(anchor='n', x=self.width / 2, y=450)

        self.result_label.place(anchor='n', x=self.width / 2, y=480)
        self.result.place(anchor='n', x=self.width / 2, y=510)

    def choose_source_file(self):
        self.filename = filedialog.askopenfilename(initialdir='/', title='Select file', 
        filetypes=(('c source code', '*.c'), ('cpp source code', '*.cpp' )))
        self.filename_label['text'] = self.filename

    def choose_test_data_file(self):
        self.test_data = filedialog.askopenfilename(initialdir='/', title='Select file', 
        filetypes=(('text file', '*.txt'), ('csv file', '*.csv' )))
        self.test_data_label['text'] = self.test_data

    def judge(self):
        if not self.filename:
            self.filename_label['text'] = 'You have to choose a file!'
            return

        # tu kompilacja, uruchomienie i odczytanie wyjscia w programu C/Cpp

        # zapis do boxów
        self.output['text'] = '>> output of the c/cpp code here <<'
        self.result['text'] = 'Correct / Incorrect'
        self.time['text'] = '0ms'

        raise NotImplementedError('No work with c/cpp files yet.')

    def show(self):
        self.window.mainloop()


judge = Judge()
