from time import sleep
from credentials import *
import markovify, random, sys, tweepy

SLEEP_TIME = 1800 # 30 min


# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# given a list of latin words choose 1 or 2 randomly as the new spell name
def generate_spell():
	with open("files/latin.csv") as f:
		lines = f.read()
		spells_list = lines.splitlines()
	k = random.randrange(1,3,1)
	spell = random.sample(spells_list, k)
	return(spell)


# generate a new spell effect from a list of existing HP spells using markovify 
def generate_effect():
	with open("files/spell_effects.csv") as f:
		effects_list = f.read()

	effects_model = markovify.NewlineText(effects_list)
	spell_effect = effects_model.make_sentence(tries=1000).lower()
	return(spell_effect)


# randomly generates a spell type
def generate_type():
	spell_types = ['charm', 'jinx', 'hex', 'curse', 'spell']
	type = random.choice(spell_types)
	return(type)


if __name__ == '__main__':
	while 1:
		spell = " "
		spell_name = generate_spell()
		spell_type = generate_type()
		spell_effect = generate_effect()

		spell = spell.join(spell_name)
		spell = spell + " (" + spell_type + ") " + spell_effect
		print(spell)

		#tweet
		api.update_status(spell)
		sleep(SLEEP_TIME)