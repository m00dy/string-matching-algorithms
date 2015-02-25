#!/bin/bash
#2gb genome data
wget -i links.txt
gunzip *.gz
cat *.fa > genome.dat
rm -rf *.fa

