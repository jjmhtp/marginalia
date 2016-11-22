#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gpxpy
import gpxpy.gpx

infilesdir = 'some-gpx-collection'

# create gpx object for all tracks
outgpx = gpxpy.gpx.GPX()

# get names of existing gpx files
filenames = os.listdir(infilesdir)

# process existing gpx files
for infilename in filenames:
    infile = open(infilesdir + '/' + infilename, 'r')

    ingpx = gpxpy.parse(infile)

    for track in ingpx.tracks:
        outgpx.tracks.append(track)

outfile = open('all.gpx', 'w')
outfile.write(outgpx.to_xml())
outfile.close()

