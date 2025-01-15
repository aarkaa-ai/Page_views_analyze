import unittest
import time_series_visualizer
import matplotlib as mpl

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        actual = int(time_series_visualizer.df.count()[0])
        expected = 1238  # Update based on your cleaning logic
        self.assertEqual(actual, expected, "Expected DataFrame count after cleaning to be 1238.")

class LinePlotTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fig = time_series_visualizer.draw_line_plot()
        cls.ax = cls.fig.axes[0]

    def test_line_plot_title(self):
        actual = self.ax.get_title()
        expected = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        self.assertEqual(actual, expected, "Expected line plot title to match.")

    def test_line_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Date", "Expected x-axis label to be 'Date'.")
        self.assertEqual(self.ax.get_ylabel(), "Page Views", "Expected y-axis label to be 'Page Views'.")

    def test_line_plot_data_quantity(self):
        actual = len(self.ax.lines[0].get_ydata())
        expected = 1238
        self.assertEqual(actual, expected, "Expected 1238 data points in line plot.")

class BarPlotTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fig = time_series_visualizer.draw_bar_plot()
        cls.ax = cls.fig.axes[0]

    def test_bar_plot_legend_labels(self):
        actual = [label.get_text() for label in self.ax.get_legend().get_texts()]
        expected = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
        self.assertEqual(actual, expected, "Expected legend labels to match months of the year.")

    def test_bar_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Years", "Expected x-axis label to be 'Years'.")
        self.assertEqual(self.ax.get_ylabel(), "Average Page Views", "Expected y-axis label to be 'Average Page Views'.")

    def test_bar_plot_number_of_bars(self):
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        expected = 48  # Update based on logic (12 months × 4 years)
        self.assertEqual(actual, expected, "Expected a different number of bars in bar chart.")

class BoxPlotTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fig = time_series_visualizer.draw_box_plot()
        cls.ax1, cls.ax2 = cls.fig.axes

    def test_box_plot_number(self):
        self.assertEqual(len(self.fig.get_axes()), 2, "Expected two box plots in figure.")

    def test_box_plot_labels(self):
        self.assertEqual(self.ax1.get_xlabel(), "Year", "Expected box plot 1 xlabel to be 'Year'.")
        self.assertEqual(self.ax1.get_ylabel(), "Page Views", "Expected box plot 1 ylabel to be 'Page Views'.")
        self.assertEqual(self.ax2.get_xlabel(), "Month", "Expected box plot 2 xlabel to be 'Month'.")
        self.assertEqual(self.ax2.get_ylabel(), "Page Views", "Expected box plot 2 ylabel to be 'Page Views'.")

    def test_box_plot_titles(self):
        self.assertEqual(self.ax1.get_title(), "Year-wise Box Plot (Trend)", "Expected box plot 1 title to match.")
        self.assertEqual(self.ax2.get_title(), "Month-wise Box Plot (Seasonality)", "Expected box plot 2 title to match.")

    def test_box_plot_number_of_boxes(self):
        self.assertEqual(len(self.ax1.lines) / 6, 4, "Expected 4 boxes in box plot 1.")
        self.assertEqual(len(self.ax2.lines) / 6, 12, "Expected 12 boxes in box plot 2.")

if __name__ == "__main__":
    unittest.main()
