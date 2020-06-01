import random

import chattrigger


class HoesMad(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        pastas = []
        pastas.append(
            "Women, the male counterpart to the only surviving subtribe Hominina, are vital to the survival of the human race due to their reproductive organs. These are made up of the internal and external sex organs that function in reproduction of new offspring. Some of these women are said to be a ‘hoe’, a name for someone, most likely a woman, who has had or continues to have sexual intercourse with someone other than their chosen partner frequently. These women are said to be angered and showing great displeasure in the current situation due to unknown reasons, also known as being ‘mad’. These two words coincide to form the statement in a popular song by American rapper (a form of singing in which they rhyme words to form a story or just music to be enjoyed by listeners) Famous Dex which is said 24 times in his rap “hoes mad” Therefore: hoes mad")
        pastas.append(
            "The current subject, a female - born with two X chromosomes - of the homo sapiens species of the genus homo, of the family great apes, of the order primates, of the grandorder euarchonta, of the mammal class, of the phylum chordata, of the animal kingdom, of the eukaryote domain, of carbon-based life, that is the subject of our conversation, which we shall identify and refer to as a \"hoe\" a derogatory term for an aforementioned female who commonly undergoes sexual experiences with many partners, is experiencing physical reactions it symptoms which includes a number of the following: Production of C8H11NO3 or C9H13NO3; sweating not for the reason of expelling molecular kinetic energy; dilating pupils to increase the awareness of one’s surroundings; increased blood pressure. They may also be experiencing mental reactions when deeming their current situation to be either, caused without a proper reason or originating from a reason that does not lead to an outcome which is at a level that is disarble for the affected parties in which they endorse, or as an annoyance at the level which affects one to a degree that leads to anger.\n∴ hoes mad")
        await message.channel.send(random.choice(pastas))
