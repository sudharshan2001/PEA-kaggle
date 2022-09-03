# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 10:38:21 2022

@author: ROSHAN
"""

import pandas as pd
from datetime import datetime as dt

#Reading Data

df=pd.read_xml('infocept_xml_data_.xml')
sdf=pd.read_csv('infocept_submission.csv')

#Process the "start_time_ts" column to create "time_spec_points" column

dates=[]
for a in df["start_time_ts"]:
    d=dt.strptime(a,'%B %d, %Y %A, %X').hour
    m=dt.strptime(a,'%B %d, %Y %A, %X').minute
    s=dt.strptime(a,'%B %d, %Y %A, %X').second
    if(d>16):
      dates.append(d+5)
    elif(d==16 and ( m>0 or s>0)):
      dates.append(d+5)
    else:
      dates.append(d)
sdf['time_spec_points']=dates
      
#Reduce the "total_duration" round to 2 decimal places

total=[]
for a in df['total_duration']:
    total.append(str(round(a, 2)))
sdf['total_duration']=total

#Add the values of columns  "total_clicks", "total_items", "total_cats" to create a new column: "total_inventory"

inventory1=df["total_clicks"]+df[ "total_items"]+df[ "total_cats"]
inventory=[]

for a in inventory1:
    if(a>10):
        inventory.append(a*2)
    else:
        inventory.append(a)
sdf["total_inventory"]=inventory

#Create a new column "give_big_discount". The value of '"give_big_discount" should be 1 if day_of_week is 0 and is_special_day is 1, otherwise 0.

discount=[]
add=df[['day_of_week','is_special_day']]

for n in range(0,500000):
    if add['day_of_week'][n]==0 and add['is_special_day'][n]==1:
        discount.append(1)
    else:
        discount.append(0)
sdf['give_big_discount']=discount

#Create a new column prod_views_buys_ratio which should be a ratio of prod_views_freqs and prod_buys_freqs

req=df[['prod_views_freqs','prod_buys_freqs']]
ratio=[]
for n in range(0,500000):
    ratio.append(req['prod_views_freqs'][n]/req['prod_buys_freqs'][n])
sdf['prod_views_buys_ratio']=ratio

#Create a new column create loyalty_points which should be calculated based on the following conditions: if a user is spending more than 3 seconds on a Sunday -- and loyalty points score will be 10 multiplied seconds over 3. 
points=[]
requirements=df[['day_of_week','total_duration']]
for n in range(0,500000):
    b=df['total_duration'][n]
    if df['day_of_week'][n]==0 and b>3:
            points.append((b-3)*10)
    else:
        points.append(0)

sdf['loyalty_points']=points


#save to csv

sdf.to_csv('submission.csv',index=False)

    
      
