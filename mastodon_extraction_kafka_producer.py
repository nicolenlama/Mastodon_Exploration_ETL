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
from pykafka import KafkaClient
client = KafkaClient("localhost:9092")

import re
from bs4 import BeautifulSoup
print(client.topics)

server_payload = {}
servers = set()
servers.add("https://fosstodon.org")
servers.add("https://techhub.social")
servers.add("https://mstdn.party")
# servers.add("https://astronomy.city")
# servers.add("https://best-friends.chat")
# servers.add("https://pythonist.as")

topics = [client.topics["foss"],
               client.topics["techhub"],
               client.topics["party"]]



def processPosts(posts,h):
    posts_processed = []
    for post in posts:
        soup = BeautifulSoup(post['content'], 'html.parser')
        date = post["created_at"]
        author = post['account']['username']
        content = soup.text
        posts_processed.append({"created":date,"author":author,"content":content, "hashtag":h})
    return posts_processed
          
def processServerData(server_info,name):
    server_processed = {"name":name,
                        "num_users":server_info['stats']['user_count']}
    
    return server_processed
#def extract():

for server,topic in zip(servers,topics):
    
    server_info = json.loads(requests.get("{0}/api/v1/instance".format(server)).text)
    server_info = processServerData(server_info,server)
    
    
    hashtags = set()
    response = requests.get("{0}/api/v1/trends".format(server))
    trends = json.loads(response.text) # this converts the json to a python list of dictionary

    for trend in trends:
        hashtag = trend['name'] # this prints the status text
        hashtags.add(hashtag)
        post_response = requests.get("{0}/api/v1/timelines/tag/{1}?limit=5".format(server,hashtag))
        posts = json.loads(post_response.text)
        
        
        ##Parse posts. I think I want to do this in Flink/Spark
        print(hashtag)
        processed_posts = processPosts(posts,hashtag)
            #print(posts[0]['content'])
        
    
    print(topic)
    producerPost = topic.get_producer()
    producerServer = client.topics["{0}-server".format(topic.name.decode("utf-8"))].get_producer()
    producerPost.produce(bytes(json.JSONEncoder().encode(processed_posts),'utf-8'))
    producerServer.produce(bytes(json.JSONEncoder().encode(server_info),'utf-8'))

    #return server_payload, post_payload
        
#s,p = extract()

print(client.topics) 
        
        
        
        
        
        