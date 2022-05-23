import discord, random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # !w 5 p2x7 ls8 b2
    if message.content.startswith('!w'):

        answer = ''

        params = message.content.split()
        dices  = []
        dices_str = []

        for d in range(int(params[1])):
            dice = random.randint(1, 10)
            dices.append(dice)
            dices_str.append(str(dice))

        dices_str.sort(key = int)

        answer += ", ".join(dices_str)


        # optional: probe
        if(len(params) > 2):

            answer += " - "

            check_learning = False
            skill = 0
            learning_threshold = 0

            for p in range(2, len(params)):

                param = params[p]

                if(param[0] == 'p'):
                    test_how_many = int(param[1])
                    test_how_high = int(param[3])

                    if(test_how_high == 0):
                        test_how_high = 10

                    success = 0

                    for d in dices:
                        if d >= test_how_high:
                            success += 1

                    if success >= test_how_many:
                        answer += "**Erfolg** "
                    else:
                        answer += "**Misserfolg** "

                # optional: lernschwelle
                if(param[0] == 'l'):
                    check_learning = True
                    learning_threshold = int(param[2])

                if(param[0] == 'b'):
                    skill = int(param[1])

            if check_learning:
                success = 0
                for d in dices:
                    if d >= learning_threshold:
                        success += 1

                if success >= len(dices) - skill:
                    answer += "__Gesteigert__ "

        answer = answer.strip()
        answer = answer.strip("-")

        await message.channel.send(answer)

client.run('XYZ')
