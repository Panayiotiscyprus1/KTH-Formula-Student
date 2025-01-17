import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


class Plotter:
    def __init__(self, min=0, max=1, points=1000):
        self.min = min
        self.max = max
        self.points = points
        self.t = np.linspace(self.min, self.max, self.points)

    def calculate(self):
        lambda_v = -5 * np.sin(2 * np.pi * self.t)
        return 3 * np.pi * np.exp(lambda_v)


class SliderPlotter(Plotter):
    def __init__(self, min=0, max=1, points=1000):
        super().__init__(min, max, points)

    def slider_update(self, val):
        new_max = self.slider.val
        self.t = np.linspace(self.min, new_max, self.points)
        y = self.calculate()
        self.plot_line.set_xdata(self.t)
        self.plot_line.set_ydata(y)
        # Re-scale the axis to fit new data
        self.axis.relim()
        self.axis.autoscale_view()
        # Redraw the figure canvas
        plt.draw()

    def plot(self):
        plt.figure(figsize=(12, 8))
        self.plot_line, = plt.plot(
            self.t,
            self.calculate(),
            label=r"$h(t) = 3\pi e^{-5 \sin(2 \pi t)}$",
            color="green"
        )
        plt.xlabel("$t$", fontsize=14)
        plt.ylabel("$h(t)$", fontsize=14)
        plt.grid(True)
        plt.legend(fontsize=14, loc="upper left")
        plt.subplots_adjust(bottom=0.25)
        self.axis = plt.gca()
        axis_slider = plt.axes([0.2, 0.02, 0.65, 0.03])
        self.slider = Slider(axis_slider, 't', self.min, 20, valinit=self.max)
        self.slider.on_changed(self.slider_update)
        plt.show()


#sample
sp = SliderPlotter()
sp.plot()






