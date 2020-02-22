import json
import os

path_host = r'C:\Users\marek\AppData\LocalLow\Hyperbolic Magnetism\Beat Saber'
os.chdir(path_host)

path_guest = r'C:\BS\guest'
os.chdir(path_guest)

with open("LocalLeaderboards.dat", encoding="UTF-8") as file:
    global host_file
    host_file = json.load(file)

song_number=1
for song_host in host_file["_leaderboardsData"]:
    print(f"\nSong counter: {song_number} \n{song_host['_leaderboardId'][13:]}")

    index = 0
    for index in range(0, len(song_host['_scores'])):
        print(f"{index+1}. {song_host['_scores'][index]['_score']} {song_host['_scores'][index]['_playerName']}")
        index +=1

    song_number += 1