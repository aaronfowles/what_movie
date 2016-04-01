#!/usr/bin/python

import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql+psycopg2://idunno_db_user:devdevtesttest@localhost:5433/idunno_db')
user_selection = pd.read_sql_query("SELECT * FROM app_userselection", engine)
activity = pd.read_sql_query("SELECT * FROM app_activity", engine)
tag = pd.read_sql_query("SELECT * FROM app_tag", engine)

def calculate_probs_for_activity_tag_pair(df,activity_id,tag):
    # Get activity name
    # activity_name = pd.read_sql_query("SELECT desc * FROM app_activity WHERE id = {}".format(activity_id), engine)
    # let a = activity
    # let b = tag
    #del df['datetime']
    
    this_activity_df = df.loc[df['suggested_activity_id'] == activity_id]

    this_activity_df['tag_in_yes'] = pd.Series()
    for index, row in this_activity_df.iterrows():
        row_no_list = list(row['no_list'].split(','))
        row_yes_list = list(row['yes_list'].split(','))
        if (tag in row_yes_list):
	    this_activity_df['tag_in_yes'][index] = True
        else:
            this_activity_df['tag_in_yes'][index] = False

    a = this_activity_df.loc[(this_activity_df['tag_in_yes'] == True) & (this_activity_df['outcome'] == True)].count()[0]
    b = this_activity_df.loc[(this_activity_df['tag_in_yes'] == True) & (this_activity_df['outcome'] == False)].count()[0]
    c = this_activity_df.loc[(this_activity_df['tag_in_yes'] == False) & (this_activity_df['outcome'] == True)].count()[0]
    d = this_activity_df.loc[(this_activity_df['tag_in_yes'] == False) & (this_activity_df['outcome'] == False)].count()[0]

    if a == 0:
	a = 1
    if b == 0:
        b = 1
    if c == 0:
        c = 1
    if d == 0:
        d = 1
    odds_ratio = float(a*d) / float(b*c)
    return odds_ratio

act_odds_ratios = {}
tag = 'outdoors'
for index, row in activity.iterrows():
    odds_ratio = calculate_probs_for_activity_tag_pair(user_selection, row['id'], tag)
    act_odds_ratios[row['activity_name']] = odds_ratio

likely = {}
unlikely = {}
for k,v in act_odds_ratios.iteritems():
    if (v > 1):
        likely[k] = v
    elif (v < 1):
        unlikely[k] = v
print('Likely to do ' + str(tag) + str(likely))
print('Unlikely to do ' + str(tag) + str(unlikely))
