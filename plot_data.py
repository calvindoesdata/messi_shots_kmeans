import seaborn as sns
import matplotlib.pyplot as plt
from plot_layout import PitchPlotLayout


class Plotter:
    def __init__(self):
        self.fig = plt.figure()
        plt.rcParams['axes.facecolor'] = 'black'
        plt.rcParams['axes.edgecolor'] = 'white'
        plt.rcParams['axes.labelcolor'] = 'white'
        plt.rcParams['xtick.color'] = 'white'
        plt.rcParams['ytick.color'] = 'white'
        plt.rcParams['figure.facecolor'] = 'black'
        plt.rcParams['text.color'] = 'white'

    def plot_inertia(self, x_values, y_values):
        self.fig = plt.figure()
        self.fig.set_size_inches(8, 6)
        plt.xticks(x_values)

        sns.lineplot(x=x_values, y=y_values)
        sns.scatterplot(x=x_values, y=y_values, marker='o')

    def plot_scatter(self, x_coords, y_coords, plot_with_cmap, hue=None, colour_palette=None,
                     marker=None, s=0, edgecolor='black', color=None, legend=False, label='', zorder=1):
        self.fig.set_size_inches(4, 6)
        ax = self.fig.add_subplot(1, 1, 1)
        PitchPlotLayout().draw_half_pitch(axis=ax)
        plt.xlim(60, 120)
        plt.ylim(0, 80)
        plt.axis('off')
        if plot_with_cmap:
            colors = sns.light_palette(colour_palette, as_cmap=True)
            sns.scatterplot(x=x_coords, y=y_coords, hue=hue, palette=colors, marker=marker, s=s,
                            edgecolor=edgecolor, legend=legend, zorder=zorder)
        else:
            sns.scatterplot(x=x_coords, y=y_coords, hue=hue, marker=marker, s=s, edgecolor=edgecolor, color=color,
                            legend=legend, label=label, zorder=zorder)

    @staticmethod
    def save_figure(plots: list, save_location):
        """
        This method saves a single or multiple plots to a single file.
        :param plots: list of Seaborn plots
        :param save_location: file path to save the plot image to
        """
        for plot in plots:
            plot
        plt.savefig(save_location, dpi=500)
