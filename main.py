# I haven't written alot of code but this is the worst shit I have ever made and for that I am not sorry.

# Versions
# 1.0.0 - Initial release (After like 3 years without versions comments)
# 1.0.1 - Added tits back to fiftyfifty
# 1.0.2 - Added to PC instead of replit.
# 1.0.21 - Removed W I D E
# 1.0.22 - Removed [Calculator as it was a genuine fuck off massive security flaw
# 1.0.23 - Changed [Code link
# 1.0.24 - Added CS or F1
# 1.0.25 - Fixes and comments
# 1.0.26 - Fixed [3
# 1.0.27 - Added [cs that launches cs2 on my pc
# 1.0.28 - Added DM Jake

# ToDo - Stop Praw printing error logs.

import pandas as pd
import os
import sys

import key
from keep_alive import keep_alive
from lists import game_list
from lists import help_list
import random
import praw
from datetime import datetime
from discord.ext import commands
import re
import pytz
import time
import discord
import requests
from bs4 import BeautifulSoup
import webbrowser
import logging
import subprocess

logging.basicConfig(filename='error_log.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)
# import openai

try:
    lost = False  # I don't think this is used
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    client = commands.Bot(command_prefix='[', intents=intents)
    # openai.api_key = os.getenv("chatgpt_API")

    # Records the time the bot started
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)

    word_counter = 1
    # Logs into reddit?
    # These should probably be secret
    # But if you really want to log into the random reddit account I created, go for it
    reddit = praw.Reddit(client_id='lVYaZUjxZFYp-tgY9O7nCA',
                         client_secret='A0OlprUR8a5WGa6EmKByWb0wgSYaSQ',
                         user_agent='PythonPraw')


    # The library 'praw' gives an error evrytime you use it in a function to tell you to not. it still works tho so i'm not sure what it is complaining about
    def img_cute():
        global url_cute
        url_cute = ""
        subreddit = reddit.subreddit("awww")
        all_subs = []
        hot = subreddit.hot(limit=200)
        for submission in hot:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        url_cute = str(random_sub.url)


    # All of theses reddit functions should be put into a singular function which runs with an input
    # and the input defines the subreddit.
    # Fuck that tho too much effort
    def img_chance_1():
        global url_cute
        url_cute = ""
        subreddit = reddit.subreddit("newyorknine")
        all_subs = []
        hot = subreddit.hot(limit=200)
        for submission in hot:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        url_cute = str(random_sub.url)


    def img_chance_2():
        global url_cock
        url_cock = ""
        subreddit = reddit.subreddit("awww")
        all_subs = []
        hot = subreddit.hot(limit=200)
        for submission in hot:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        url_cock = str(random_sub.url)


    # This is bad because I am repeating code, should add an input to the function which decides whether it wants a meme of a cute pic
    def img_meme():
        global url_meme
        url_cute = ""
        subreddit = reddit.subreddit("197")
        all_subs = []
        hot = subreddit.hot(limit=200)
        for submission in hot:
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        url_meme = str(random_sub.url)


    # produces a random number
    def random_num():
        global random_number
        # Pretty sure u don't need int() here but I am scared of removing it
        random_number = int(random.randint(0, int(len(game_list))))


    # This function was made entirely with ChatGPT
    def get_random_population(csv_file):
        day_of_year = datetime.now(london_tz).timetuple().tm_yday  # Get the current day of the year
        random.seed(day_of_year)  # Set the random seed value to the day of the year
        population_csv = pd.read_csv(csv_file, encoding='latin-1')
        num_rows = population_csv.shape[0]
        random_row_index = random.randint(0, num_rows - 1)
        random_row = population_csv.iloc[random_row_index]
        population = "{:,}".format(random_row.iloc[1])
        population_answer = f"{random_row.iloc[0]} has a population of {population}"
        return population_answer


    # This function was made entirely with ChatGPT
    def get_random_country(csv_file):
        day_of_year = datetime.now(london_tz).timetuple().tm_yday  # Get the current day of the year
        random.seed(day_of_year)  # Set the random seed value to the day of the year
        population_csv = pd.read_csv(csv_file, encoding='latin-1')
        num_rows = population_csv.shape[0]
        random_row_index = random.randint(0, num_rows - 1)
        random_row = population_csv.iloc[random_row_index]
        return random_row.iloc[0]


    # This function was made entirely with ChatGPT
    def calculate_score(answer_str, guess_str):
        answer = float(answer_str.replace(',', ''))
        guess = float(guess_str.replace(',', ''))
        difference = abs(guess - answer)
        if difference > answer:
            return 0
        else:
            percentage = (1 - difference / answer) * 100
            return percentage


    london_tz = pytz.timezone('Europe/London')


    # This function was made entirely with ChatGPT
    def get_random_population_only(csv_file):
        day_of_year = datetime.now(london_tz).timetuple().tm_yday  # Get the current day of the year
        random.seed(day_of_year)  # Set the random seed value to the day of the year
        population_csv = pd.read_csv(csv_file, encoding='latin-1')
        num_rows = population_csv.shape[0]
        random_row_index = random.randint(0, num_rows - 1)
        random_row = population_csv.iloc[random_row_index]
        population = "{:,}".format(random_row.iloc[1])
        return population


    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


    # I absoloutlely am coding rock paper scissors
    # in if statements. 100% a better way of doing this.
    def rps_result(player_1, player_2, player_1_result, player_2_result):
        if player_1_result == player_2_result:
            rps_result = "Draw!"

        if player_1_result == "Rock" and player_2_result == "Paper":
            rps_result = player_2 + " wins!"
        if player_1_result == "Rock" and player_2_result == "Scissors":
            rps_result = player_1 + " wins!"

        if player_1_result == "Paper" and player_2_result == "Rock":
            rps_result = player_1 + " wins!"
        if player_1_result == "Paper" and player_2_result == "Scissors":
            rps_result = player_2 + " wins!"

        if player_1_result == "Scissors" and player_2_result == "Rock":
            rps_result = player_2 + " wins!"
        if player_1_result == "Scissors" and player_2_result == "Paper":
            rps_result = player_1 + " wins!"

        return rps_result


    # Define a function that uses the OpenAI API to generate a response
    def generate_response(prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()


    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))


    # Idk if the following bit works
    @client.event
    async def on_member_join(member):
        await client.send_message(discord.Object(id='DISCORD'),
                                  'Welcome! Please read rule 6.1')


    @client.event
    async def on_message(message):
        global hangman, letterinput, replied, alphabet

# Uncomment for the bot to not reply to itself
# This potentially means that the bot could reply to itself in an infinite loop
# But also there is a slight chance that it gives itself the n-word pass.
# The funny outweighs the potential flaws
        #   if message.author == client.user:
        #       return

        # states the truth
        if message.content.startswith("[1"):
            await message.channel.send("This is a very useless bot")

# Random yes no when you ask it if something is gay
# idk is this homophobic?
        if "gay?" in message.content and message.content.startswith("Is"):
            fiftyfifty = int(random.randint(0, 1))
            if fiftyfifty == 0:
                await message.channel.send("Yes")
            if fiftyfifty == 1:
                await message.channel.send("No")

        if "[fiftyfifty" in message.content:
            # await message.channel.send("Y'all been too horny, no more tits.")
            fiftyfifty = int(random.randint(0, 1))
            if fiftyfifty == 0:
                postable = False
                while postable == False:
                    img_chance_1()
                    # Checks if it is a format that discord can embed
                    if ".jpg" in url_cute:
                        postable = True
                    if ".png" in url_cute:
                        postable = True
                    if ".gif" in url_cute:
                        postable = True
                await message.channel.send(url_cute)

            if fiftyfifty == 1:
                postable = False
                while postable == False:
                    img_chance_2()
                    # Checks if it is a format that discord can embed
                    if ".jpg" in url_cock:
                        postable = True
                    if ".png" in url_cock:
                        postable = True
                    if ".gif" in url_cock:
                        postable = True
                await message.channel.send(url_cock)

        if message.content.startswith("@DailySoftPorn") or message.content.startswith(
                "@dailysoftporn") or message.content.startswith("@dailysoftporn"):
            postable = False
            while postable == False:
                img_chance_1()
                # Checks if it is a format that discord can embed
                if ".jpg" in url_cute:
                    postable = True
                if ".png" in url_cute:
                    postable = True
                if ".gif" in url_cute:
                    postable = True
            await message.channel.send(url_cute)

        if "gay?" in message.content and message.content.startswith("is"):
            # Ideally I'd write a function to do capitals but here we are repeating things
            fiftyfifty = int(random.randint(0, 1))
            if fiftyfifty == 0:
                await message.channel.send("Yes")
            if fiftyfifty == 1:
                await message.channel.send("No")

        if message.content.startswith("[2"):
            await message.channel.send("Please mute this channel")

        # Fuck continuity
        if message.content.startswith("[Populationdle") or message.content.startswith("[populationdle"):
            population_country = discord.Embed(
                color=discord.Color.blue(),
                title="Today's Country is **" + get_random_country("population.csv") + "**!",
                description=' \n Use the [Guess command to guess the population.')
            await message.channel.send(embed=population_country)

        if message.content.startswith('[guess') or message.content.startswith('[Guess'):
            guess = message.content.split(' ', 1)[1]  # Get everything after the first space
            message_author = str(message.author)
            # Chatgpt made the next line for me
            new_message_author = re.sub(r'#.*', '', message_author)
            await message.delete()
            answer = get_random_population_only("population.csv")
            populationdle_result = round(float(calculate_score(answer, guess)), 2)
            # The discord library doesn't like concatenated strings so u have to make a variable first then send the variable.
            populationdle_result_message = new_message_author + " scored " + str(populationdle_result)
            if guess == answer:
                cheat_message = new_message_author + " cheated."
                await message.channel.send(cheat_message)
            else:
                await message.channel.send(populationdle_result_message)

        if message.content.startswith("[Answer") or message.content.startswith("[answer"):
            answer = get_random_population_only("population.csv")
            answer_message = "The actual population of " + get_random_country("population.csv") + " is: ||" + str(
                answer) + "||"
            await message.channel.send(answer_message)

        if message.content.startswith("[3"):
            await message.channel.send(
                "Any suggestions for this bot?"
            )

        if message.content.startswith("[4"):
            await message.channel.send(
                "Hello new person. I am not liable for anything posted in the #nsfl chat."
            )

        if message.content.startswith("[5"):
            await message.channel.send(
                "This is a pro Ukrainian bot."
            )

# Possibly makes an infinite messaging loop
        if message.content.startswith('[Repeatafterme'):
            to_repeat = message.content.split(' ', 1)[1]  # Get everything after the first space
            await message.channel.send(to_repeat)

        if "Ukraine" in message.content or "ukraine" in message.content:
            await message.channel.send(
                "Слава Україні!"
            )

        if message.content.startswith('[gpt') or message.content.startswith('[GPT'):
            prompt = message.content[4:]  # remove the question mark from the prompt
            response = generate_response(prompt)
            await message.channel.send(response)

        if message.content.startswith("[Rule34"):
            await message.channel.send("No")
            # Just no
        if message.content.startswith("[help") or message.content.startswith(
                "[Help"):
            mbed = discord.Embed(color=discord.Color.red(),
                                 title='Help',
                                 description=('\n'.join(help_list)))
            await message.channel.send(embed=mbed)

        if message.content.startswith("Which game should we play?"):
            random_num()
            await message.channel.send(game_list[random_number])

        if message.content.startswith("[Game list"):
            await message.channel.send(game_list)

        if message.content.startswith("[bpp"):
            await message.channel.send("https://www.brokenpicturephone.com")

        if message.content.startswith("[Start") or message.content.startswith("[start"):
            global start_time
            start_time = time.time()
            print("Starting Stopwatch")  # Prints in Console

        if message.content.startswith("[Stop") or message.content.startswith("[stop"):
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_lapsed = str(round(time_lapsed)) + " Seconds"
            await message.channel.send(time_lapsed)

        if message.content.startswith("You did a good job, bot."):
            await message.channel.send("Cheers lad!")

        if message.content.startswith("[Test") or message.content.startswith(
                "[test"):
            mbed = discord.Embed(color=discord.Color.magenta(),
                                 title='Testing',
                                 description="Huh, guess I am alive")
            await message.channel.send(embed=mbed)

        if message.content.startswith("Who are you?"):
            await message.channel.send("Farsley away some do")

        if message.content.startswith("[Ping") or message.content.startswith("[ping"):
            mbed = discord.Embed(
                color=discord.Color.magenta(),
                title='Ping',
                description=(f' {round(client.latency * 1000)}ms'))
            await message.channel.send(embed=mbed)
            # await message.channel.send(f'Ping = {round(client.latency * 1000)}ms')

        if message.content.startswith("Is Dan ceeringe?"):
            await message.channel.send("Yes")
        # Why are you reading this?
        if message.content.startswith("[Code") or message.content.startswith("[code"):
            await message.channel.send(
                "https://github.com/GLHF-Goose/Diccy_Bot")

        if message.content.startswith("[RPS") or message.content.startswith("[rps"):
            time.sleep(1)
            await message.channel.send("3")
            time.sleep(1)
            await message.channel.send("2")
            time.sleep(1)
            await message.channel.send("1")
            time.sleep(1)
            await message.channel.send("GO!")

            global rps_goes
            global rps_start_timer
            global player_names
            global player_results
            rps_start_timer = time.time()
            rps_time_lapsed = 0
            rps_goes = 0
            player_names = []
            player_results = []

        # Repeating things because streamlining your code is a sign of being sweaty
        if message.content.startswith("Rock") or message.content.startswith("rock"):
            print("Someone said rock")
            rps_goes = rps_goes + 1
            rps_end_time = time.time()
            time_laps = rps_end_time - rps_start_timer
            if time_laps < 2 and rps_goes < 3:
                message_author = str(message.author)
                new_message_author = re.sub(r'#.*', '', message_author)
                player_names.append(str(new_message_author))
                player_results.append("Rock")
                print(player_names)
                print(player_results)
            if time_laps < 2 and rps_goes == 2:
                # Takes all of the results and sends it to a function which works out the winner
                # ... using a bunch of if statements
                rps_results = rps_result(player_names[0], player_names[1], player_results[0], player_results[1])
                await message.channel.send(rps_results)
            if time_laps > 2:
                await message.channel.send("Too slow idiot.")

        if message.content.startswith("Paper") or message.content.startswith("paper"):
            print("Someone said paper")
            rps_goes = rps_goes + 1
            rps_end_time = time.time()
            time_laps = rps_end_time - rps_start_timer
            if time_laps < 2 and rps_goes < 3:
                message_author = str(message.author)
                new_message_author = re.sub(r'#.*', '', message_author)
                player_names.append(str(new_message_author))
                player_results.append("Paper")
                print(player_names)
                print(player_results)
            if time_laps < 2 and rps_goes == 2:
                rps_results = rps_result(player_names[0], player_names[1], player_results[0], player_results[1])
                await message.channel.send(rps_results)
            if time_laps > 2:
                await message.channel.send("Too slow idiot.")

        if message.content.startswith("Scissors") or message.content.startswith(
                "scissors") or message.content.startswith("Scissor") or message.content.startswith("scissor"):
            print("Someone said scissors")
            rps_goes = rps_goes + 1
            rps_end_time = time.time()
            time_laps = rps_end_time - rps_start_timer
            if time_laps < 2 and rps_goes < 3:
                message_author = str(message.author)
                new_message_author = re.sub(r'#.*', '', message_author)
                player_names.append(str(new_message_author))
                player_results.append("Scissors")
                print(player_names)
                print(player_results)
            if time_laps < 2 and rps_goes == 2:
                rps_results = rps_result(player_names[0], player_names[1], player_results[0], player_results[1])
                await message.channel.send(rps_results)
            if time_laps > 2:
                await message.channel.send("Too slow idiot.")

        if message.content.startswith("RPS Rules"):
            await message.channel.send(
                "After 'Go!' you have two seconds to enter 'Paper', 'Rock' or 'Scissors'. Type [RPS to start a game.")

        if message.content.startswith("I'm not racist but"):
            await message.channel.send("Based!")

        if message.content.startswith("@FIA"):
            fiftyfifty = int(random.randint(0, 2))
            if fiftyfifty == 0:
                await message.channel.send("That was your fault tbh.")
            if fiftyfifty == 1:
                await message.channel.send("What a dickhead, obviously his fault")
            if fiftyfifty == 2:
                await message.channel.send("Racing incident, nobody's fault")

# How do I separate this if statement onto multiple lines?
        if message.content.startswith("F1 or CS") or message.content.startswith("F1 or CS?") or message.content.startswith("F1 or cs?") or message.content.startswith("f1 or cs?") or message.content.startswith("CS or F1?") or message.content.startswith("CS or F1"):
            fiftyfifty = int(random.randint(0, 1))
            if fiftyfifty == 0:
                await message.channel.send("CS")
            if fiftyfifty == 1:
                await message.channel.send("F1")

        if "pepsi" in message.content:
            await message.channel.send("BEPIS")

        # I typed bad words, I am sorry
        if "nigger" in message.content or "nigga" in message.content:
            await message.add_reaction("😬")

        # Best line of the whole thing
        if "farsley" in message.content:
            await message.add_reaction("🍺")

        if "www.tiktok.com" in message.content:
            await message.add_reaction("🤮")

            # Happy little accident
        if "[Myid" in message.content:
            await message.channel.send(message.author.id)

        # This is just to message Jake for a funny
        if message.content.startswith("[DM") or message.content.startswith("[dm"):
            to_send = message.content
            first_space_index = to_send.find(' ')  # Find the index of the first space
            second_space_index = to_send.find(' ', first_space_index + 1)
            user_id = to_send[first_space_index + 1:second_space_index]
            user = await client.fetch_user(user_id)
            dm_message = to_send[second_space_index + 1:]
            await user.send(dm_message)

        # One in a 5 thousand chance that u get an N-word pass
        if "" in message.content:
            n_word_pass = int(random.randint(0, 5000))
            if n_word_pass == 69:
                message2 = "Congratulations " + str(
                    message.author
                ) + " you now have an N-word Pass. This is valid for 12 hours."
                # The discord library doesn't like concatenated strings so u have to make a variable first then send the variable. (message2)
                await message.channel.send(message2)

        if "9 + 10" in message.content:
            await message.channel.send("21")

        if ":Bananashit:" in message.content:
            await message.channel.send("Banana")
            await message.add_reaction("🍌")

        # Posts an embeded post from the top 50 of r/awww
        if message.content.startswith("[Eyebleach") or message.content.startswith(
                "[eyebleach"):
            postable = False
            while postable == False:
                img_cute()
                # Checks if it is a format that discord can embed
                if ".jpg" in url_cute:
                    postable = True
                if ".png" in url_cute:
                    postable = True
                if ".gif" in url_cute:
                    postable = True
            await message.channel.send(url_cute)

        # Posts an embeded post from the top 50 of r/awww
        if message.content.startswith("@dailycute") or message.content.startswith(
                "@Dailycute"):
            postable = False
            while postable == False:
                img_cute()
                # Checks if it is a format that discord can embed
                if ".jpg" in url_cute:
                    postable = True
                if ".png" in url_cute:
                    postable = True
                if ".gif" in url_cute:
                    postable = True
            await message.channel.send(url_cute)

        # Posts an embeded post from the top 50 of r/196
        if message.content.startswith("@dailymeme") or message.content.startswith(
                "@Dailymeme"):
            postable = False
            # Bad because I am repeating the whole loop each time the selected post does not embed / the while loop continues
            # This means it takes a few seconds longer than it should in some cases but this is a god damn meme discord bot, idgaf
            while postable == False:
                img_meme()
                # Checks if it is a format that discord can embed
                if ".jpg" in url_meme:
                    postable = True
                if ".png" in url_meme:
                    postable = True
                if ".gif" in url_meme:
                    postable = True
            await message.channel.send(url_meme)

        if "their" in message.content:
            theirthere = int(random.randint(0, 10))
            if theirthere == 0:
                await message.channel.send("*there")

        if "your" in message.content:
            youryoure = int(random.randint(0, 10))
            if youryoure == 0:
                await message.channel.send("*You're")

        # This bit doesn't work because it crashes occasionally and resets
        # if "W I D E" in message.content:
        #     global word_counter
        #     message1 = "'W I D E' has been sent " + str(word_counter) + " time(s) since " + dt_string
        #     await message.channel.send(message1)
        #     word_counter = word_counter + 1

        if message.content.startswith('[Calculator') or message.content.startswith('[calculator'):
            if "9 + 10" not in message.content:
                await message.channel.send("Yeah nah I removed this function because it was a genuinely scary design flaw.")
                # maths = message.content.split(' ', 1)[1]  # Get everything after the first space
                # try:
                #     # Using eval is frowned upon but its so fucking useful
                #     # People who say you shouldn't use it are just sweats
                #     # Don't use this to inject code into the bot tho
                #     maths_answer = eval(maths)
                #     await message.channel.send(maths_answer)
                # except NameError:
                #     await message.channel.send("Sorry can't figure that one out")
                # except SyntaxError:
                #     await message.channel.send("Sorry can't figure that one out")

        if message.content.startswith('[Wikipedia') or message.content.startswith('[wikipedia'):
            url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
            soup = BeautifulSoup(url.content, "html.parser")
            title = soup.find(class_="firstHeading").text
            url = "https://en.wikipedia.org/wiki/%s" % title
            url = url.replace(' ', '_')
            await message.channel.send(url)

        if message.content.startswith('[Check_Password_Strength'):
            await message.delete()
            await message.channel.send("Password has been logged, cheers for that.")

        if message.content.startswith('[cs2') or message.content.startswith('[CS2') or message.content.startswith('[cs') or message.content.startswith('[CS'):
            await message.channel.send("Launching CS2")
            subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 730")


    # Yeah I gave up
    # if message.content.startswith("[Hangman"):
    # start()

    # for letter in alphabet:
    # if message.content.startswith(letter):
    # letterinput = letter

    # This is a joke, I was never ever selling your information to amazon
    # aws = aws.Send.AllData

    keep_alive()
# Key is in a separate file stored locally so y'all can't steal it from github
    import key
    client.run(key.key)

# This whole ass things runs in a try loop,
# If there is an error the bot just restarts itself
except BaseException as error:
    print('An exception occurred: {}'.format(error))
    python = sys.executable
    os.execl(python, python, *sys.argv)
    logger.error(error)

# I haven't written alot of code but this is the worse shit I have ever made and for that I am not sorry.
