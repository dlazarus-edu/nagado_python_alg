#!/bin/sh
ls *_sort.py | xargs -n1 -I X python3 start.py X benchmark
