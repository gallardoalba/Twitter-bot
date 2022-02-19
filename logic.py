###########################################
# GET HELP ABOUT DEFAULT METHODS: help(t) #
###########################################

# UI.py functions

def options():
        print("""[X] Options:
        [0] Exit
	[1] Unfavorite tweets!
        [2] Fish new followers
   	[3] Publish new tweet
  	[4] Show number of friends
        [5] Show number of followers
        [6] Options""")

	
def send_tweet(t):
	mssg = raw_input("Introduce the message:\n")
	if len(mssg) < 150:
		t.update_status(status=mssg)
		return 1
	else:
		print "Must be shorter than 160 chars."
		return 0



# FUNCTIONS

def get_usrIDs():
	CONFIG_PARAMS = {}
	with open("/home/nouser/Desktop/scripts/twitter/twitter_bot/twitter_counts.txt") as counts:
        	for i in counts:
        	        l = i.split(" ")
                	l[-1] = l[-1].rstrip('\n')
                	CONFIG_PARAMS[l[1]] = l[2:]
	return CONFIG_PARAMS.keys()

def unfavorite(t,n=100):
        from random import random
        from time import sleep
        def unfav(t,n):
                favorites = t.get_favorites()[:n]
                for f in favorites:
                        st = int(random() * 10)
                        sleep(st + 5)
                        tweet_id = f["id_str"]
                        print("[x] Unfavorite tweet %s" % tweet_id)
                        t.destroy_favorite(id=tweet_id)
        for i in range(10): unfav(t,n)
        
def read_db(db_file):
        user_db = []
        with open(db_file) as db:
                for i in db:
                        user_db.append(int(i[:-1]))
        return user_db




def set_parameters(user,filename = "twitter_counts.txt"):
        
        return t

def show_profiles(users):
	print("\n    AVAILIBLE PROFILES:")
	for i in range(len(users)):
		print "[" + str(i) + "]", users[i]

def set_params(user,twython,filename = "/home/nouser/Desktop/scripts/twitter/twitter_bot/twitter_counts.txt"):
	CONFIG_PARAMS = {}
        with open(filename) as counts:
                for i in counts:
                        l = i.split(" ")
                        if len(l) == 6:
                                l[-1] = l[-1].rstrip('\n')
                                CONFIG_PARAMS[l[1]] = l[2:]
        APP_KEY = CONFIG_PARAMS[user][0]
        APP_SECRET = CONFIG_PARAMS[user][1]
        OAUTH_TOKEN = CONFIG_PARAMS[user][2]
        OAUTH_TOKEN_SECRET = CONFIG_PARAMS[user][3]

        t = twython.Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) #,client_args=client_args) # self hack
	return t

"""
def shuffle(items):  # mutates input list
        i = len(items)
        while i > 1:
                j = random.randrange(i)  # 0 <= j <= i
                items[j], items[i] = items[i], items[j]
                i = i - 1
                return
"""

def show_keys(diccionario):
        print "\n    OPTION KEYS\n"
        for k in diccionario.keys():
                print "[X]", k
        print "\n"

def show_list(list_name):
        print "\n   LIST ELEMENTS"
        n = len(list_name)
        for i in range(n):
                print "[X]", list_name[i]
        print ""
        
def add_friend(t,usr_ID,user_db):
        if  usr_ID not in user_db:
                new_friend = t.create_friendship(user_id = int(usr_ID))
                if new_friend["following"] == "true":
                        print "\tNew friend: ",usr_ID
        
def user_quality_tweet(tweet):
        """
        This function allows to check if a user tend to follow.
        """
        owner = tweet["user"]
        followers = owner["followers_count"]
        friends = owner["friends_count"]
        if int(followers) > 0:
                rr_val = float(friends)/int(followers)
                return rr_val                                        


def user_quality_id(usr_id):
        """
        This function allows to check if a user tend to follow.
        """
        usr = t.show_user(user_id = usr_id)
        followers = usr["followers_count"]
        friends = usr["friends_count"]
        if int(friends) > 0:
                rr_val = float(followers)/int(friends)
                return rr_val 


def get_timeline(t,usr_id, n = 20):
        tl = t.get_user_timeline(user_id = usr_id,count = n)
        return tl


def favorite_tweet(t,tweet):
        if tweet["favorited"] == False:
                fav = t.create_favorite(id = int(tweet["id"]))
                # if tweet["retweet_count"] >= 5000:
                       # t.retweet(id = int(tweet["id"]))
        # else: print "Previously marked as favourite."


def favorite_tl(t,usr_id, n=3): # number of favourites for each user
	import random
        tl = get_timeline(t,usr_id)
        number_tweets = len(tl)
        vals = []
        for i in range(n):
                randomval = int((random.random() * number_tweets) % number_tweets)
                if randomval not in vals:
                        vals.append(randomval)
                        favorite_tweet(t,tl[randomval])
        
def search_term(t, term, n = 300):
        search = t.search(q = term, result_type="recent",count = n)
        return search[search.keys()[1]]



def mark_favorites(t,id_list, usr_db):
	import random,time
        index = random.shuffle([x for x in range(len(id_list))])
        for i in id_list:
                if i not in usr_db:
                        usr_db.append(i)
                        favorite_tl(t,usr_id = i)
                        with open("/home/nouser/Desktop/scripts/twitter/twitter_bot/users_db.txt","a") as db:
                                db.write(str(i) + "\n")
                        print "\t[+]",i
                        
                        st = int(random.random() * 10)
                        time.sleep(st + 5)
                else:
                        print "\t[-]",i,"*"
        return usr_db


def ids_from_search(t,tweets,user_db,thd):
        user_ids = []
        for i in range(len(tweets)):
                qual = user_quality_tweet(tweets[i])
                if qual >= thd:
                        user_ids.append(tweets[i]["user"]["id"])
                #if qual <= 0.2:
                #        add_friend(t,tweets[i]["user"]["id"],user_db)
        return user_ids

def screen_name_from_search(t,tweets):
        names = []
        for i in range(len(tweets)):
                names.append(tweets[i]["user"]["screen_name"])
        return names

def localization_from_search(t,tweets):
        resultado = []
        for i in range(len(tweets)):
                resultado.append(tweets[i]["user"]["location"])
        return resultado
        
def timezone_from_search(t,tweets):
        resultado = []
        for i in range(len(tweets)):
                resultado.append(tweets[i]["user"]["time_zone"])
        return resultado

def name_from_search(t,tweets):
        resultado = []
        for i in range(len(tweets)):
                resultado.append(tweets[i]["user"]["name"])
        return resultado

def language_from_search(t,tweets):
        resultado = []
        for i in range(len(tweets)):
                resultado.append(tweets[i]["user"]["lang"])
        return resultado


def status_from_search(t,tweets):
        resultado = []
        for i in range(len(tweets)):
                resultado.append(tweets[i]["user"]["status"])
        return resultado
        

def statuses_from_search(t,tweets):
        resultado = []
        for i in range(len(tweets)):
                resultado.append(tweets[i]["user"]["statuses_count"])
        return resultado
        
def geo_from_search(t,tweets):
        resultado = []
        for i in range(len(tweets)):
                resultado.append(tweets[i]["user"]["geo_enabled"])
        return resultado

def index_from_search(t,tweets):        
        resultado = []
        for i in range(len(tweets)):
                followers = float(tweets[i]["user"]["followers_count"])
                friends = float(tweets[i]["user"]["friends_count"])
                if friends > 0: r = followers/friends
                else: r = 0
                resultado.append(round(r,3))
        return resultado

def followers_from_search(t,tweets):        
        resultado = []
        for i in range(len(tweets)):
                followers = int(tweets[i]["user"]["followers_count"])
                resultado.append(followers)
        return resultado

def friends_from_search(t,tweets):        
        resultado = []
        for i in range(len(tweets)):
                friends = int(tweets[i]["user"]["friends_count"])
                resultado.append(friends)
        return resultado

def description_from_search(t,tweets):
        resultado = []
        for i in range(len(tweets)):
                friends = tweets[i]["user"]["description"]
                resultado.append(friends)
        return resultado


def wrap_send(t):
	mssg = 0
	while mssg == 0:
        	mssg = send_tweet(t)

def wrap_favs(user_db,user,t,hashtags,thd,n):
	import random
        terms = random.sample(hashtags[user],5) # number of terms for using
        # perform a search and get user ids:
        for termino in terms:
                print "[X] Running:",termino
                tweets = search_term(t, term = termino, n = 600)
                ids = ids_from_search(t,tweets,user_db,thd)
                names = name_from_search(t,tweets)
                lang = language_from_search(t,tweets)
                index = index_from_search(t,tweets)
                #geo = geo_from_search(t,tweets)
                friends = friends_from_search(t,tweets)
                followers = followers_from_search(t,tweets)
                screenames = screen_name_from_search(t,tweets)
                localization = localization_from_search(t,tweets)
                times = timezone_from_search(t,tweets)
		#nstatus = statuses_from_search(t,tweets)
		#status = status_from_search(t,tweets)
		description = description_from_search(t,tweets)

                with open("detailed_info.txt","a") as info:
                        for i in range(len(ids)):
                                info.write(str(ids[i])); info.write("\t")
                                info.write((names[i]).encode('utf-8')); info.write("\t")
                                info.write("@"); info.write((screenames[i]).encode('utf-8')); info.write("\t")
                                info.write(str(friends[i])); info.write("\t")
                                info.write(str(followers[i])); info.write("\t")
                                info.write(str(index[i])); info.write("\t")
                                #info.write((geo[i])); info.write("\t")
                                info.write((lang[i]).encode('utf-8')); info.write("\t")
                                info.write((localization[i]).encode('utf-8')); info.write("\t")
                                #info.write((nstatus[i]).encode('utf-8')); info.write("\t")
                                #info.write((status[i]).encode('utf-8')); info.write("\t")
                                info.write((description[i]).encode('utf-8')); info.write("\t")
                                
                                #info.write((times[i]).encode('utf-8')); info.write("\t")
                                info.write("\n")
                             
                # resort ids:
                ids = set(list(random.sample(ids,len(ids))))
                # print "[x] Recopiled profiles: ", len(ids) # self hack
                # mark favorites:
                user_db = mark_favorites(t,ids ,user_db)
        exit(0)

def show_number_friends(t):
        friends = len(t.get_friends_ids()["ids"])
        print "[X] Number of friends:",friends
        
def show_number_followers(t):
        followers = len(t.get_followers_ids()["ids"])
        print "[X] Number of followers:",followers


