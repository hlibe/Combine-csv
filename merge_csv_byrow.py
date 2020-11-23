#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 2020

"""
import os #for working directory
import pandas as pd
import numpy as np
import glob
os.getcwd()
os.chdir('/Users/')

path = "/Users/Seperatedcsv/"

all_files = glob.glob(os.path.join(path, "*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['file'] = f.split('/')[-1]
    all_df.append(df)
    
merged_df = pd.concat(all_df, ignore_index=True, sort=True)
merged_df.to_csv( "merged.csv")
