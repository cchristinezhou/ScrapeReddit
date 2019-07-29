#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:54:29 2019

@author: christinezhou
"""

import pandas as pd

import praw

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',client_id='GsTWiqwBzl-nHg',client_secret="oo4D3-UC-Xnv3BvNLvXUxFfnvsw",username='Sea_and_Lightning', password='TKZ-b5N-ggy-kVc')
#That's my client id
comm_list = []
header_list = []
i = 0
for submission in reddit.subreddit('opiatesRecovery').hot(limit= 50):
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:]  # Seed with top-level
    while comment_queue:
        header_list.append(submission.title)
        comment = comment_queue.pop(0)
        comm_list.append(comment.body)
        t = []
        t.extend(comment.replies)
        while t:
            header_list.append(submission.title)
            reply = t.pop(0)
            comm_list.append(reply.body)
df = pd.DataFrame(header_list)
df['comm_list'] = comm_list
df.columns = ['header','comments']
df['comments'] = df['comments'].apply(lambda x : x.replace('\n',''))
df.to_csv('OpiatesRecovery_comments.csv',index = False)
