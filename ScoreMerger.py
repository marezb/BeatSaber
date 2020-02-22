import json
import os

guest_results_temp_dict = {}

path_host = r'C:\Users\marek\AppData\LocalLow\Hyperbolic Magnetism\Beat Saber'
os.chdir(path_host)
with open("LocalLeaderboards.dat", encoding="UTF-8") as file:
    global host_file
    host_file = json.load(file)
    print('@@@ host file @@@', host_file, '\n')

path_guest = r'C:\BS\guest'
os.chdir(path_guest)
with open("LocalLeaderboards.dat", encoding="UTF-8") as file:
    global guest_file
    guest_file = json.load(file)


def save_to_host(name):  # function to save library to external file
    os.chdir(path_host)
    with open(name, "w", encoding="UTF-8") as file:
        json.dump(host_file, file, ensure_ascii=False)
    return print("saved successfully to dat file")


# dodajemy tytuly piosenek z  host_file jako klucze do tymczasowego slownika: guest_results_temp_dict
for song_host in host_file["_leaderboardsData"]:
    guest_results_temp_dict[song_host['_leaderboardId']] = []

#do temp dict dodajemy najlepszy wynik guesta
for song_guest in guest_file["_leaderboardsData"]:
    for key_song_name_from_host_file in guest_results_temp_dict:
        if key_song_name_from_host_file == song_guest['_leaderboardId']:
            # dodajemy najlepszy wynik guesta do guest_results_temp_dict
            guest_results_temp_dict[key_song_name_from_host_file].append(song_guest['_scores'][0])

print('******* merged file *********', guest_results_temp_dict, '\n')
for song_host in host_file["_leaderboardsData"]:

    print('\n -----------', song_host['_leaderboardId'])
    for key_song_name_from_host_file, item_guest_score in guest_results_temp_dict.items():
        if (len(item_guest_score)) > 0:
            if song_host['_leaderboardId'] == key_song_name_from_host_file:
                print(len(song_host['_scores']), ' amount of results')
                print((song_host['_scores']), ' amount of results')
                index = 0
                for index in range(0, len(song_host['_scores'])):
                    print('index ', index)
                    print(item_guest_score)
                    if song_host['_scores'][index]['_score'] == item_guest_score[0]['_score']:
                        print('wynik rowny nic nie robimy')
                        print('score host: ', song_host['_scores'][0])
                        print('value merged: ', item_guest_score[0])
                        break
                    elif (song_host['_scores'][index]['_score']) < item_guest_score[0]['_score']:
                        print('guest wygral i wstawiamy go na 1 miejscu')
                        print('value merged: ', item_guest_score[0])
                        print('score host:   ', song_host['_scores'][0])
                        (song_host['_scores']).insert(0, item_guest_score[0])
                        print((song_host['_scores']))
                        break

                    elif len(song_host['_scores']) == 1 and (song_host['_scores'][index]['_score']) > \
                            item_guest_score[0]['_score']:
                        print('host wygral dlugosc 1 guesta wstawiamy na drugim miejscu')
                        print('value merged: ', item_guest_score[0])
                        print('score host:   ', song_host['_scores'][0])
                        (song_host['_scores']).insert(1, item_guest_score[0])
                        break

                    elif len(song_host['_scores']) > 1 and index + 1 <= (len(song_host['_scores']) - 1) \
                            and song_host['_scores'][index]['_score'] > item_guest_score[0]['_score'] > \
                            song_host['_scores'][index + 1]['_score']:
                        print(f"wstawiamy item_guest_score[0]['_score'] na miejscu {index+1}")
                        print('score host:   ', song_host['_scores'][0])
                        print('value merged: ', item_guest_score[0])
                        (song_host['_scores']).insert(index+1, item_guest_score[0])

                        break
                    elif index == (len(song_host['_scores']) - 1) and index < 10:
                        print('dodajemy na koncu')
                        (song_host['_scores']).insert(9, item_guest_score[0])

                        break

                    index += 1

print('@@@ host file @@@', host_file, '\n')
save_to_host("LocalLeaderboards.dat")