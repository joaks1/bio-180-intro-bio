#! /usr/bin/env python

import os
import sys

import matplotlib

from pymsbayes import plotting

matplotlib.rc('text',**{'usetex': True})

x = {1: 0.08,
     11: 0.71,
     16: 0.89}
keys = [1,11,16]

bd = plotting.BarData(
        values = [x[k] for k in keys],
        labels = keys,
        width = 0.5,
        orientation = 'vertical',
        color = '0.5',
        edgecolor = '0.5',
        zorder = 0)
sp = plotting.ScatterPlot(
        bar_data_list = [bd],
        y_label = 'Proportion of HIV particles\nsurviving 0.1 $\mu$M AZT',
        x_label = 'Months of therapy',
        )
sp.set_ylim(bottom=0.0, top=1.0)

p = plotting.PlotGrid(subplots = [sp],
        num_columns = 1,
        label_schema = None,
        share_y = True,
        height = 3,
        width = 3,
        auto_height = False)
sp.savefig('../images/hiv-survival-plot.pdf')

x = {'AA': 0.91,
        'Aa': 0.08,
        'aa': 0.86}
keys = ['AA', 'Aa', 'aa']

bd = plotting.BarData(
        values = [x[k] for k in keys],
        labels = keys,
        width = 0.5,
        orientation = 'vertical',
        color = '0.5',
        edgecolor = '0.5',
        zorder = 0)
sp = plotting.ScatterPlot(
        bar_data_list = [bd],
        y_label = 'Proportion of cells in which\nmalaria reproduced',
        x_label = 'Genotype of cell line',
        )
sp.set_ylim(bottom=0.0, top=1.0)

p = plotting.PlotGrid(subplots = [sp],
        num_columns = 1,
        label_schema = None,
        share_y = True,
        height = 3,
        width = 3,
        auto_height = False)
sp.savefig('../images/malaria-reproduction-plot.png')
