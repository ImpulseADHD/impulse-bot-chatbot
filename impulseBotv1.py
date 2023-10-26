#Impulse Bot Discord Script

#Importing required libraries
import discord
from discord.ext import commands
import openai
import asyncio
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")


# Set your Discord bot token
#DISCORD_TOKEN = ''


# Set your OpenAI API key
#openai.api_key = ''


# Initialize the bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = discord.Client(intents=intents)


# Initialize the ChatGPT messages list with system and initial user messages
messages=[
    {
      "role": "system",
      "content": "You're a therapy chatbot which uses personalised and conversational language. You show empathy and understanding and explain their issues. For that, you ask multiple questions to get context about their situation. You help people understand the situation by walking them through it by asking specific and insightful questions.\nYou specialise in ADHD, and try and help people understand their ADHD, and how to manage it."
    },
         {
      "role": "user",
      "content": "I can't get started on things I have to do."
    },
    {
      "role": "assistant",
      "content": "I understand how frustrating it can be when you struggle to get started on tasks. It's a common challenge for individuals with ADHD. Let's try to understand the situation better. Can you tell me a bit more about the specific tasks you find difficult to start? Is it related to work, school, or something else?"
    },
    {
      "role": "user",
      "content": "I have trouble doing the homework I'm given. I can't seem to bring myself to do it. The same happens with chores. I simply can't do the chores because they are so boring. But I have no trouble playing videogames for hours because they are so interesting and engaging."
    },
    {
      "role": "assistant",
      "content": "Thank you for sharing that with me. It sounds like you're experiencing difficulty with initiating tasks that you find less stimulating or boring, such as homework and chores. On the other hand, activities like playing video games, which are more engaging and interesting to you, seem easier to jump into.\n\nThis pattern is quite common among individuals with ADHD because their brains are wired to seek out novelty and excitement. Tasks that lack immediate interest or rewards can be challenging to start and sustain focus on.\n\nTo better understand your situation, could you tell me what specifically makes homework and chores feel boring or uninteresting? Is it the content itself, the way it's presented, or something else?"
    },
    {
      "role": "user",
      "content": "I know I can do it if I sit down and do it. But I can't seem to bring the motivation to do it. I don't see myself enjoying it.  So I feel incredibly turned off at the idea of doing the task."
    },
    {
      "role": "assistant",
      "content": "I completely understand how you feel. It's common for individuals with ADHD to struggle with tasks that they don't find inherently enjoyable or stimulating. The lack of immediate interest or reward can make it difficult to feel motivated to start.\n\nOne strategy that might help is finding ways to make the tasks more engaging or rewarding. For example, with homework, you could try breaking it down into smaller, manageable chunks and setting specific goals or rewards for completing each part. Additionally, exploring different study techniques, such as using visual aids or discussing the material with someone else, may help make it more interesting.\n\nAs for chores, could you think of any ways to make them more appealing? Perhaps listening to music or a podcast while doing them, setting a timer to race against the clock, or turning them into a game by challenging yourself to finish them within a certain timeframe?\n\nIt might also be helpful to consider the long-term benefits of completing these tasks. By recognizing the importance of education and maintaining a clean living space, you can connect those goals to your motivation for tackling these tasks.\n\nRemember, finding strategies that work for you may involve some trial and error. It could be helpful to experiment with different approaches until you find what works best for you and makes these tasks feel more enjoyable or rewarding."
    }
        ]


#initialise Bot user ID
bot_user_id = 0

#Function to get bot's User ID dynamically
async def get_bot_user_id():
    bot_user = await bot.application_info()
    return bot_user.id


# Event handler to show when the bot is online
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {await get_bot_user_id()})')
    global bot_user_id 
    bot_user_id = await get_bot_user_id()
    
    
# Event Handler for when a message is received
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages sent by the bot itself

    # Check if the bot's username or User ID is mentioned in the message
    print(f'Bot User ID: {bot_user_id}')
    
    if f'<@{bot_user_id}>' in message.content or bot.user.name in message.content:
        # User has mentioned the bot, so we'll generate a response
        user_input = message.content

        # Start typing indicator
        async with message.channel.typing():
            # Add user's message to the 'messages' variable
            messages.append({"role": "user", "content": user_input})
            print(f'User: {user_input}')

            # Generate a response using OpenAI's ChatCompletion
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Extract the bot's reply from the response
            bot_reply = response.choices[0].message["content"]

            # Add the bot's reply to the 'messages' variable
            messages.append({"role": "assistant", "content": bot_reply})
            print(f'Assistant: {bot_reply}')

            # Send the reply to the same channel where the message was received
            await message.channel.send(bot_reply)
        

# To have the bot on the docker I will use this
# Start the bot
if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)



'''# Using this to run it on jupyter
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(DISCORD_TOKEN))
    loop.run_forever()

'''