#! /usr/bin/env python

import os
import sys
import random
import math

import matplotlib

from pymsbayes import plotting

random.seed(48726114)
# matplotlib.rc('text',**{'usetex': True})

def get_normal_samples(mu=0, sigma=1, n=1000):
    samples = []
    for i in range(n):
        samples.append(random.normalvariate(mu, sigma))
    return samples

def get_beta_samples(alpha=1, beta=1, n=1000):
    samples = []
    for i in range(n):
        samples.append(random.betavariate(alpha, beta))
    return samples


patterns = {
        'base': get_normal_samples(20, 2, 10000),
        'directional': get_normal_samples(23, 1, 10000),
        'stabilizing': get_normal_samples(20, 1, 10000),
        'disruptive': get_normal_samples(18, 1, 5000) + get_normal_samples(22, 1, 5000),
        }
all_values = []
for v in patterns.itervalues():
    all_values.extend(v)
maximum=int(math.ceil(max(all_values)))
minimum=int(math.floor(min(all_values)))
bins = range(minimum, maximum)

for p, draws in patterns.iteritems():
    hd = plotting.HistData(
            draws,
            normed = True,
            bins = bins,
            range = None,
            cumulative = False,
            histtype = 'bar',
            align = 'mid',
            orientation = 'vertical',
            rwidth = None,
            log = False,
            color = None,
            edgecolor = '0.5',
            facecolor = '0.5',
            fill = True,
            hatch = None,
            label = None,
            linestyle = None,
            linewidth = None)
    sp = plotting.ScatterPlot(
            hist_data_list = [hd],
            y_label = 'Frequency',
            x_label = 'Trait value',
            xlim = (minimum, maximum),
            ylim = (0.0, 0.4),
            )
    
    pg = plotting.PlotGrid(subplots = [sp],
            num_columns = 1,
            label_schema = None,
            share_y = True,
            height = 3,
            width = 3,
            auto_height = False)
    sp.savefig('../images/generic-trait-histogram-{0}.pdf'.format(p))

beaks = get_normal_samples(9.5, 1.5, 2000)
maximum=int(math.ceil(max(beaks)))
minimum=int(math.floor(min(beaks)))
bins = range(minimum, maximum)

hd = plotting.HistData(
        beaks,
        normed = True,
        bins = 20,
        range = None,
        cumulative = False,
        histtype = 'bar',
        align = 'mid',
        orientation = 'vertical',
        rwidth = None,
        log = False,
        color = None,
        edgecolor = '#FF9900',
        facecolor = '#FF9900',
        fill = True,
        hatch = None,
        label = None,
        linestyle = None,
        linewidth = None,
        zorder=0)
sp = plotting.ScatterPlot(
        hist_data_list = [hd],
        y_label = 'Frequency of finches',
        x_label = 'Beak depth (mm)',
        # xlim = (minimum, maximum),
        # ylim = (0.0, 0.4),
        )

pg = plotting.PlotGrid(subplots = [sp],
        num_columns = 1,
        label_schema = None,
        # share_y = True,
        height = 2.2,
        width = 3.5,
        auto_height = False)
pg.savefig('../images/my-beak-depth-histogram.pdf')



beaks = get_normal_samples(9.5, 1.5, 2000)
maximum=int(math.ceil(max(beaks)))
minimum=int(math.floor(min(beaks)))-1

hd = plotting.HistData(
        beaks,
        normed = True,
        bins = 20,
        range = None,
        cumulative = False,
        histtype = 'bar',
        align = 'mid',
        orientation = 'vertical',
        rwidth = None,
        log = False,
        color = None,
        edgecolor = '0.0',
        facecolor = '0.0',
        fill = True,
        hatch = None,
        label = None,
        linestyle = None,
        linewidth = None,
        zorder=0)
sp = plotting.ScatterPlot(
        hist_data_list = [hd],
        y_label = 'Frequency of lizards',
        x_label = 'Melanin concentration (ng/cell)',
        xlim = (minimum, maximum),
        # ylim = (0.0, 0.4),
        )

pg = plotting.PlotGrid(subplots = [sp],
        num_columns = 1,
        label_schema = None,
        # share_y = True,
        height = 2.2,
        width = 3.5,
        auto_height = False)
pg.savefig('../images/lizard-pigment-histogram-stabilizing.eps')


beaks = get_normal_samples(8, 0.8, 2000) + get_normal_samples(11, 0.8, 2000)
hd = plotting.HistData(
        beaks,
        normed = True,
        bins = 20,
        range = None,
        cumulative = False,
        histtype = 'bar',
        align = 'mid',
        orientation = 'vertical',
        rwidth = None,
        log = False,
        color = None,
        edgecolor = '0.0',
        facecolor = '0.0',
        fill = True,
        hatch = None,
        label = None,
        linestyle = None,
        linewidth = None,
        zorder=0)
sp = plotting.ScatterPlot(
        hist_data_list = [hd],
        y_label = 'Frequency of lizards',
        x_label = 'Melanin concentration (ng/cell)',
        xlim = (minimum, maximum),
        # ylim = (0.0, 0.4),
        )

pg = plotting.PlotGrid(subplots = [sp],
        num_columns = 1,
        label_schema = None,
        # share_y = True,
        height = 2.2,
        width = 3.5,
        auto_height = False)
pg.savefig('../images/lizard-pigment-histogram-disruptive.eps')

beaks = get_normal_samples(7.5, 0.8, 2000)
hd = plotting.HistData(
        beaks,
        normed = True,
        bins = 20,
        range = None,
        cumulative = False,
        histtype = 'bar',
        align = 'mid',
        orientation = 'vertical',
        rwidth = None,
        log = False,
        color = None,
        edgecolor = '0.0',
        facecolor = '0.0',
        fill = True,
        hatch = None,
        label = None,
        linestyle = None,
        linewidth = None,
        zorder=0)
sp = plotting.ScatterPlot(
        hist_data_list = [hd],
        y_label = 'Frequency of lizards',
        x_label = 'Melanin concentration (ng/cell)',
        xlim = (minimum, maximum),
        # ylim = (0.0, 0.4),
        )

pg = plotting.PlotGrid(subplots = [sp],
        num_columns = 1,
        label_schema = None,
        # share_y = True,
        height = 2.2,
        width = 3.5,
        auto_height = False)
pg.savefig('../images/lizard-pigment-histogram-directional.eps')

freqs = [
        (12, get_beta_samples(0.1, 0.1, 100)),
        (12, get_beta_samples(2.5, 2.5, 100)),
        (4, get_beta_samples(20, 1, 100)),
        (4, get_beta_samples(1, 20, 100)),
        ]
maximum = 1.0
minimum = 0.0

splots = []
for nbins, f in freqs:
    hd = plotting.HistData(
            f,
            normed = False,
            bins = nbins,
            range = None,
            cumulative = False,
            histtype = 'bar',
            align = 'mid',
            orientation = 'vertical',
            rwidth = None,
            log = False,
            color = None,
            edgecolor = '#FF9900',
            facecolor = '#FF9900',
            fill = True,
            hatch = None,
            label = None,
            linestyle = None,
            linewidth = None,
            zorder=0)
    sp = plotting.ScatterPlot(
            hist_data_list = [hd],
            x_label = r'Frequency of $A_1$',
            y_label = '# of populations',
            xlim = (minimum, maximum),
            # ylim = (0.0, 0.4),
            )
    splots.append(sp)

pg = plotting.PlotGrid(subplots = splots,
        num_columns = 2,
        label_schema = 'numbers', 
        # share_y = True,
        height = 4.5,
        width = 6,
        auto_height = False)
pg.savefig('../images/allele-freq-clicker-histograms.pdf')
