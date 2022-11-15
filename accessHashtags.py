# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:13:33 2022

dict_keys(['id', 'created_at', 'in_reply_to_id', 
           'in_reply_to_account_id', 'sensitive', 'spoiler_text', 
           'visibility', 'language', 'uri', 'url', 'replies_count', 
           'reblogs_count', 'favourites_count', 'edited_at', 'content', 
           'reblog', 'account', 'media_attachments', 'mentions', 'tags', 
           'emojis', 'card', 'poll'])

@author: nicol
"""

import json
import requests
# import re
# from bs4 import BeautifulSoup

post_payload = {}
server_payload = {}
servers = set()
servers.add("https://fosstodon.org")
servers.add("https://techhub.social")
servers.add("https://mstdn.party")
servers.add("https://astronomy.city")
# servers.add("https://best-friends.chat")
servers.add("https://pythonist.as")


def extract():

    for server in servers:
        server_info = json.loads(requests.get("{0}/api/v1/instance".format(server)).text)
        server_payload[server] = server_info
        post_payload[server] = {}
        hashtags = set()
        response = requests.get("{0}/api/v1/trends".format(server))
        statuses = json.loads(response.text) # this converts the json to a python list of dictionary
        #assert statuses[0]["visibility"] == "public" # we are reading a public timeline
        for status in statuses:
            hashtag = status['name'] # this prints the status text
            print(hashtag)
            hashtags.add(hashtag)
            post_response = requests.get("{0}/api/v1/timelines/tag/{1}?limit=5".format(server,hashtag))
            posts = json.loads(post_response.text)
            post_payload[server][hashtag] = posts
            
            
            ##Parse posts. I think I want to do this in Flink/Spark
            # for post in posts:
            #     soup = BeautifulSoup(post['content'], 'html.parser')
            #     print(post["created_at"])
        
            #     #tracks = soup.find_all('p')#, attrs=attrs)#, string=re.compile(r'^((?!\().)*$'))
            #     post_text = soup.p.text
            #     print(post_text)
            #     #print(posts[0]['content'])
    return server_payload, post_payload
            
s,p = extract()
            
        
        
        
        
        
        
        
        
        