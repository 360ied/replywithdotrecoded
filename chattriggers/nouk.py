import random

import chattrigger


class NouK(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        pastas = []
        pastas.append(
            "Is that all you say to people when they attempt to engage in meaningful conversations? Rather than actually debating with an intellectual, you chose to reply with \"No u\" in order to ridicule their well thought out conversation with such an insensitive message. In fact, the world must have regressed a millenia for people like you to regress meaningful arguments to a mere few letters such as \"k\" or \"no u\". Without a doubt, you are the laziest human being to ever disgrace this world and should thoroughly refrain from ever engaging in a colloqium such as this one.")
        pastas.append(
            "Within the magnitude of 10^63 planck times - the absolute unit of time - have passed in which the universe has existed. For about a quarter of that time, life on Earth has been developing. From simple RNA strands that could reproduce, to archaeans which had evolved dna, to an accident that created eukaryotes - multi-celled organisms. The quantum fluctuations led it to be that a consciousness of your identity was created. Through all the struggles, hardships, and wisdom of your ancestors, you came to be. A miracle it is that such a life form of the species homo sapiens, manages to comprehend the meaning of the English language. And to demonstrate such command over it, that would make infantile children of which have just begun to derive meaning from the English language seem intelligent has managed to live to the age where you can access an electronic device and send information through it. Your thoughts are at such a basic level, it collectively embarasses the entire 14 billion years it took for human life to reach this point. Your rebuttal is like the monkeys at the zoo, randomly flinging around some faeces you found and making mentally challenged noises of triumph to express your excitement in providing a valid argument to debate with me. Should you attempt to express disagreement, please do not debate with such paragon entities such as myself.")
        await message.channel.send(random.choice(pastas))
