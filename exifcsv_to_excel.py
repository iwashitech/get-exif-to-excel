# -*- coding: utf-8 -*-
"""

"""

import os
import csv
import re
import pandas as pd

user_name = os.environ['USERPROFILE'].replace('\\', '/')
rows = []

def aspect_ratio(ox, oy):
  x, y = ox, oy
  while y:
    x, y = y, x % y
  return [ox/x, oy/x]

def check_aspect_ratio(x, y):
    w = aspect_ratio(x, y)[0]
    h = aspect_ratio(x, y)[1]
    if str(w) == '4.0' and str(h) == '3.0':
        return True
    return False

def is_rgb(colorspace):
    m = re.search(r'.*rgb.*', colorspace.lower())
    return m
    if m:
        return True
    return False

def is_upper_jpg(path):
    m = re.search(r'.+\.JPG', path)
    return m
    if m:
        return True
    return False

with open(user_name + '/Desktop/exif_img/exif.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

sorted_rows = [sorted(row) for row in rows]
clean_rows = [[re.sub('.+@', '', item) for item in row] for row in sorted_rows]

df = pd.DataFrame(clean_rows)
df.columns = ['作成者', '市区町村', 'RGB/CMYK', '著作権情報', '国', 'カテゴリ', '都道府県', '高さ', '画像パス', '幅']
df = df.loc[:,['画像パス', '幅', '高さ', 'RGB/CMYK', 'カテゴリ', '作成者', '国', '市区町村', '都道府県', '著作権情報']]

df['幅'] = df['幅'].astype(int)
df['高さ'] = df['高さ'].astype(int)

for index, row in df.iterrows():
    if check_aspect_ratio(row['幅'], row['高さ']):
        df.at[index, 'アスペクト比'] = ''
    else:
        df.at[index, 'アスペクト比'] = 'NG'
    
    if is_rgb(row['RGB/CMYK']) is None:
        df.at[index, 'RGBか'] = 'NONE'
    else:
        df.at[index, 'RGBか'] = ''
    
    if is_upper_jpg(row['画像パス']) is None:
        df.at[index, '拡張子が大文字か'] = ''
    else:
        df.at[index, '拡張子が大文字か'] = '大文字'

df.to_excel(user_name + '/Desktop/exif.xlsx', index=False, sheet_name='Exif情報')