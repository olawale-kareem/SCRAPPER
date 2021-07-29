from matplotlib import pyplot as p

class Plot:

    def __init__(self,keys, values):
        self.values = values
        self.keys = keys


    def plot_bar_chart(self):
        p.figure(figsize = (10, 5))
        p.bar(self.keys, self.values, color ='blue',width = 0.4)
        p.show()


    def plot_pie_chart(self):
        p.figure(figsize =(10, 5))
        p.pie(self.values, labels = self.keys, autopct='%.0f%%')
        p.show()








