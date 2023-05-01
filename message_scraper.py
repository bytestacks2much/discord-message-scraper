import discord, json

with open('settings.json') as settings:
    settings = json.load(settings)

    token = str(settings['token'])
    channel = str(settings['channel'])

client = discord.Client()

@client.event
async def on_connect():
    channel_cord = client.get_channel(int(channel))
    
    print(f'> Scraping in \"{channel_cord.name}\" as {client.user}')

    messages = []

    async for message in channel_cord.history(limit=None):
        messages.append(message)

    for message in messages:
        with open('new_data.txt', 'a', encoding='utf-8') as data:
            data.write(message.content + '\n')
    

    print(f'> Found {len(messages)} messages in \"{channel_cord.name}\"')

client.run(token)