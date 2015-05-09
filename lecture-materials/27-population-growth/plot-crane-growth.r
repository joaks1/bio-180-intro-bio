#!/usr/bin/env Rscript

d = read.delim(file='crane-data.txt', header=T, sep='\t')

pdf('crane-growth.pdf', width=6, height=5)
plot(d$year, d$number_of_cranes, type='l', xlab="Year", ylab="Number of cranes")
dev.off()

