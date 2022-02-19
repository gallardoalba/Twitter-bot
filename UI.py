#!/usr/bin/python

from logic import *
import twython
import argparse
import pickle
import random,time

# BASIC CONFIG:

random.seed(long(time.time()*256))
tcounts = get_usrIDs() # availibre Twitter counts 
regis = read_db("/home/nouser/Desktop/scripts/twitter/twitter_bot/users_db.txt") # registered users id
thd = 1.5 # threshold value for selecting users
uname = tcounts[0] # user name
t = set_params(uname,twython)
nfavs = 100 # number of tweets selected

with open("/home/nouser/Desktop/scripts/twitter/twitter_bot/hashtags.pickle","rb") as handle:
	htags = pickle.load(handle) # hashtag lists

# PARSER

parser = argparse.ArgumentParser(description="Select an option")
parser.add_argument('-o',"--option", 
                    action="store",
                    help="Choose an option",
                    type=str)
params = parser.parse_args()


#################
# MAIN FUNCTION #
#################

def main():
	try:
                while not params.option: 
                        options()
			params.option = raw_input("\n[X] Select an option: ") # self hack
		if params.option == "0": exit(0)
	        elif params.option == "1": unfavorite(t)
                elif params.option == "2": wrap_favs(regis,uname,t,htags,thd,nfavs)
                elif params.option == "3": wrap_send(t)
                elif params.option == "4": show_number_frieds(t)
                elif params.option == "5": show_number_followers(t)
	        else: print("[x] Wrong option!")
	except twython.TwythonError as e: 
                print (e)


if __name__ == "__main__":
	main()
