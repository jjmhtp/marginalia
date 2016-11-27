#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pylast
from os.path import dirname, abspath
import configparser
import re

# get configuration
configfile = dirname(dirname(abspath(__file__))) + '/config'

import configparser

config = configparser.RawConfigParser()
config.read(configfile)

ApiKey = config['lastfm']['ApiKey']
Username = config['lastfm']['Username']

# init last.fm access
network = pylast.LastFMNetwork(api_key = ApiKey,
    username = Username)

user = pylast.User(user_name = Username, network = network)

# get recent tracks
tracks = user.get_recent_tracks(limit = 11)

# process recent tracks
listened = ''
for track in tracks:
    listened += '* ' + str(track.track)
    if track.album: listened += str(track.album)
    listened += '(' + track.playback_date + ')\n'

# insert recent listening in markdown file
# FIXME: markdown syntax should not be interpreted
with open('_includes/index-content.md', 'r') as f:
    oldcontent = f.read()
newcontent = re.sub(
    r'(?<=<!-- recent listening start -->\n).*(?=\n<!-- recent listening end -->)',
    listened, oldcontent, flags=re.DOTALL)
with open('_includes/index-content.md', 'w') as f:
    f.write(newcontent)

