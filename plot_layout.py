import matplotlib.pyplot as plt
from matplotlib.patches import Arc


class PitchPlotLayout:
    line_color = 'white'

    @staticmethod
    def draw_half_pitch(axis):
        """
        Construct a half-pitch plot template.
        :param axis: axis to display the half-pitch template on
        :return:
            Stylised plot template for data plotting
        """
        # Pitch size is 60 x 80
        # The pitch ranges from 60 to 120 in the x-axis
        # The pitch ranges from 0 to 80 in the y-axis

        # Pitch Outline & Centre Line
        plt.plot([60, 120], [80, 80], color=PitchPlotLayout.line_color)
        plt.plot([120, 120], [80, 0], color=PitchPlotLayout.line_color)
        plt.plot([120, 60], [0, 0], color=PitchPlotLayout.line_color)
        plt.plot([60, 60], [0, 80], color=PitchPlotLayout.line_color)

        # Right Penalty Area
        plt.plot([120, 105.4], [57.8, 57.8], color=PitchPlotLayout.line_color)
        plt.plot([105.4, 105.4], [57.8, 22.5], color=PitchPlotLayout.line_color)
        plt.plot([120, 105.4], [22.5, 22.5], color=PitchPlotLayout.line_color)

        # Right 6-yard Box
        plt.plot([120, 115.1], [48, 48], color=PitchPlotLayout.line_color)
        plt.plot([115.1, 115.1], [48, 32], color=PitchPlotLayout.line_color)
        plt.plot([120, 115.1], [32, 32], color=PitchPlotLayout.line_color)

        # Prepare Circles
        centre_circle = plt.Circle((60, 40), 8.1, color=PitchPlotLayout.line_color, fill=False)
        centre_spot = plt.Circle((60, 40), 0.71, color=PitchPlotLayout.line_color)
        right_pen_spot = plt.Circle((110.3, 40), 0.71, color=PitchPlotLayout.line_color)

        # Draw Circles
        axis.add_patch(centre_circle)
        axis.add_patch(centre_spot)
        axis.add_patch(right_pen_spot)

        # Prepare Arc
        right_arc = Arc((110.3, 40), height=16.2, width=16.2, angle=0,
                        theta1=130, theta2=230, color=PitchPlotLayout.line_color)

        # Draw Arc
        axis.add_patch(right_arc)


