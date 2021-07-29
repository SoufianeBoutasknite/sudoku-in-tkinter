from tkinter import *
import numpy as np


class Play:
    def __init__(self):
        self.matrix = np.loadtxt('matrix.txt', delimiter=',', dtype=int)
        self.create_interface()
        self.create_canvas()
        self.create_buttons()
        self.show_matrix()
        self.my_canvas.bind('<Button>', self.select)

    def create_interface(self):
        self.root = Tk()
        self.root.geometry('450x550')
        self.root.title('SUDOKU')
        self.root.config(bg='white')
        delete = Button(self.root, text='delete', bg='white', command=self.delete)
        delete.place(x=300, y=50)
        self.won = Label(self.root, text='', bg='white', font=('arial', 20))
        self.won.place(x=50, y=50)
        self.my_canvas = Canvas(self.root, width=450, height=450, bg='white')
        self.my_canvas.place(x=0, y=100)

    def create_canvas(self):
        for i in range(9):
            if i%3 == 0:
                ep = 2
            else:
                ep = 1
            self.my_canvas.create_line(i*50, 0, i*50, 450, width=ep)
            self.my_canvas.create_line(0, i*50, 450, i*50, width=ep)

    def create_buttons(self):
        for i in range(9):
            button = Button(self.root, text=str(i+1), bg='green', width=2,
                            command=lambda number=i+1:self.button_function(number))
            button.place(x=i*50+15, y=10)

    def show_matrix(self):
        self.labels = []
        for i in range(9):
            sous_list = []
            for j in range(9):
                if self.matrix[j][i] == 0:
                    text = ''
                    color = 'black'
                else:
                    text = str(self.matrix[j][i])
                    color = 'red'
                label = Label(self.my_canvas, text=text, fg=color, bg='white', font=('arial', 25))
                label.place(x=i*50+13, y=j*50+5)
                sous_list.append(label)
            self.labels.append(sous_list)

    def button_function(self, number):
        try:
            number_color = self.labels[self.x_selected][self.y_selected]['fg']
            if number_color != 'red' and not self.is_it(number) and not self.has_won():
                self.my_canvas.delete(self.square)
                self.labels[self.x_selected][self.y_selected]['bg'] = 'white'
                self.labels[self.x_selected][self.y_selected]['text'] = str(number)
                self.matrix[self.y_selected][self.x_selected] = number
                self.has_won()
        except:
            pass

    def has_won(self):
        boul = True
        for x in self.matrix:
            for y in x:
                if y == 0:
                    boul = False
        if boul:
            self.won['text'] = 'You won'
        return boul

    def delete(self):
        if self.labels[self.x_selected][self.y_selected]['fg'] != 'red':
            self.labels[self.x_selected][self.y_selected]['text'] = ''
            self.matrix[self.y_selected][self.x_selected] = 0

    def is_it(self, number):
        line, column, block = False, False, False
        if number in list(self.matrix[self.y_selected, :]):
            line = True
        if number in list(self.matrix[:, self.x_selected]):
            column = True
        a, b = 3*int(self.y_selected/3), 3*int(self.x_selected/3)
        if number in self.matrix[a:a+3, b:b+3]:
            block = True
        return line or column or block

    def select(self, event):
        try:
            self.my_canvas.delete(self.square)
            self.labels[self.x_selected][self.y_selected]['bg'] = 'white'
        except:
            pass
        self.x_selected = event.x//50
        self.y_selected = event.y//50
        self.labels[self.x_selected][self.y_selected]['bg'] = 'blue'
        self.square = self.my_canvas.create_rectangle(self.x_selected*50, self.y_selected*50,
                                (self.x_selected+1)*50, (self.y_selected+1)*50, fill='blue')


obj = Play()
obj.root.mainloop()

