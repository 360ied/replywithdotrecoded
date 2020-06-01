import random

import discord

import chattrigger


class YandevQuotes(chattrigger.ChatTrigger):

    async def run(self, message: discord.Message, trigger: str, client: discord.Client):
        # print("hi")
        # async with aiohttp.ClientSession() as session:
        #	get = await session.get("https://twitch.center/customapi/quote/list?token=64801a3d")
        # returnedtext = await get.text()
        returnedtext = '''1. "Cuck a mother duck!" ~ YandereDev
2. "There's only two bears left in Korea? What's the problem? Just make 'em fuck!" ~ YandereDev
3. "Wow. She did the ninja run while she was leaving. What a turbo weeb." ~ YandereDev
4. "I am not a cinnamon roll. I am a SIN-amon roll." ~ YandereDev
5. "Jesus Christ, it sounds like a bunch of balloon animals are having an orgy." ~ YandereDev
6. "Does she have big boobies? No? Then why do I care?" ~ YandereDev
7. "A micropenis could still pleasure a woman, if it was vibrating very rapidly." ~ YandereDev
8. "Do I look like a guy who has time for horsecock? I have no time for it! NO TIME!" ~ YandereDev
9. "Just imagine you've got a really, really long dick that's so long, it drags behind you. And then, it gets stuck in a door. Wouldn't that suck ass?" ~ YandereDev
10. "I'll fuck your dick to death, you damn piece of shit!" ~ YandereDev
11. "I was really worried that I was inside of his rectum just now. It was a legitimate fear." ~ YandereDev
12. "If I could be any item, what would I be? Maybe a dildo. But what if it's a dildo owned by a fat gay man who constantly wants to fuck his own ass? That would be a bad thing..." ~ YandereDev
13. "I've been sucking and choking all night long." ~ YandereDev
14. "I might be a dumbfuck supercuck...but I'm YOUR dumbfuck supercuck." ~ YandereDev
15. "She was a tsundere bitch! She grew a nice pair of fish titties, that was it!" ~ YandereDev
16. "Fuck that little fuccboi cuccboi piece of shit!" ~ YandereDev
17. "No, I was not TRYING to take a picture of its butt! Its butt just so happened to be facing me!" ~ YandereDev
18. "You're not a butter-ass-fly! You're a dragon-ass-fly! Nobody asked for you! Fuck off!" ~ YandereDev
19. "Did you just fucking sneeze on me? That's disgusting, you bitch!" ~ YandereDev
20. "I am not the one who gets cucked! I AM THE ONE WHO CUCKS!" ~ YandereDev
21. "Solve world hunger? I dunno. Think about it. Do we really need all those people surviving? The world's population is already high enough." ~ YandereDev
22. "I don't know if I would want a pet cockroach. I don't want to pet anything that has ''cock'' in the name." ~ YandereDev
23. "I dunno. How cucked are ya? I mean, are you still as cucked as you were last time I called you a cucklord?" ~ YandereDev
24. "I'm a little cuckyyyyy rubber duckyyyyy~" ~ YandereDev
25. "You're not allowed to do things that put you on equal footing with me! THAT'S CHEATING!" ~ YandereDev
26. "I'm glad that What's-Her-Face, The Pyro Bitch, is gone." ~ YandereDev
27. "He just came out of the ground and started fuckin' me and cuckin' me!" ~ YandereDev
28. "They're covering my dick in shit and eating it like a lollipop right now!" ~ YandereDev
29. "Rusty dusty tainted vagina lips." ~ YandereDev
30. "You think your vagina is broken? Have you tried turning it off and on again?" ~ YandereDev
31. "You know the inside of a car wash? That's what it looks like inside a vagina. It's self-cleaning, you guys." ~ YandereDev
32. "If I don't fuck this guy to death, he's going to be a pain in my ass." ~ YandereDev
33. "Is your cat a stuck-up sassy bitch?" ~ YandereDev
34. "Who the fuck do you think I am? Some little bitch-tit with time to waste?" ~ YandereDev
35. "I got 40 more of these fuckers to fuck." ~ YandereDev
36. "I don't appreciate getting a fuckload of shit in my dick, you know." ~ YandereDev
37. "When life gives you lemons...stick 'em in your bra. Cuz you got tiny little mosquito bites for boobs." ~ YandereDev
38. "Fuck 'em to death fuck 'em to death fuck 'em to death fuck 'em to death fuck 'em to death, does it look like I give a SHIIIIIIIIIIT? I'm YandereDev." ~ YandereDev
39. "I headbutted him in the dick, cuz he deserved it!" ~ YandereDev
40. "His controller is a life-sized doll of Chun-li, and he has to stick his thumbs into her vagina and her pooper in order to play." ~ YandereDev
41. "We'll be putting their backs to the wall! No - we'll be putting their FRONTS to the wall! And pulling down their pants! And fucking them in the aaaaassssssssss!"~ YandereDev
42. "There are some sexy butts on that lion's face..." ~ YandereDev
43. "Awwwww, the penis is limp and saaaaad!" ~ YandereDev
44. "This guy has, like, six titties." ~ YandereDev
45. "I'm good at two things - makin' penises limp, and makin' vaginas dry!" ~ YandereDev
46. "I'm not gonna call you daddy. You're gonna call ME daddy." ~ YandereDev
47. "You prefer your panties black? I prefer your panties...off. ( ͡° ͜ʖ ͡°)" ~ YandereDev
48. "NO! You can't stop me, you FASCIST! I'll stare at the booty all I want!" ~ YandereDev
49. "God, the music is so good! If this game's soundtrack was a woman, I would FUCK HER SO HARD!" ~ YandereDev
50. "You know how a monkey can swing on tree branches with its tail? That's what my penis is like. I can swing on tree branches with my penis." ~ YandereDev
51. "Then I killed her." ~ YandereDev
52. "I don't wanna play as any protagonist that's not wearing a thong!" ~ YandereDev
53. "What flavor? Booty flavor." ~ YandereDev
54. "I got fucked in the ass, like an ass with an ass for an ass!" ~ YandereDev
55. "A girl's breasts are like water balloons full of milk. If you stab a girl in the breast, milk spills out." ~ YandereDev
56. "Oh god, that was scary! I almost got fucked in the ass by my own shit!" ~ YandereDev
57. "My penis cried tears of joy." ~ YandereDev
58. "Look at my big ol' fat titties jigglin'. That's such a beautiful sight." ~ YandereDev
59. "You never shoulda been born, so crawl back into your momma's vagina!" ~ YandereDev
60. "Sleepfuck? That's like sleepwalking or sleeptalking, except with your dick?" ~ YandereDev
61. "I was really good at 'The Floor Is Lava' when I was a kid. Except, the floor was social interactions." ~ YandereDev
62. "Ahh, I didn't mean to click it! The 'Kick' button and the 'Talk To Black Man' button are the same button!" ~ YandereDev
63. "Why in the world are these girls wearing clothing? This is stupid." ~ YandereDev
64. "What, is there just a giant vagina in the background, constantly giving birth to more Nazis?!" ~ YandereDev
65. "I just randomly mashed buttons until I found the 'Get Rid Of That Shit' button." ~ YandereDev
66. "Half of her pants is missing. I want to make the other half go missing, too." ~ YandereDev
67. "It's like a vagina that just keeps giving birth to new fuccbois for me to kill." ~ YandereDev
68. "I hope he didn't slap me with the same hand that he jerked off with." ~ YandereDev
69. "My penis was cringing for the entirety of that scene." ~ YandereDev
70. "It was kinda like a giant space sperm headed towards a giant space vagina." ~ YandereDev
71. "The real question is, what's inside of Cuphead's cup? It's a white liquid, so that shit is either milk, or cum." ~ YandereDev
72. "I hope your mother chokes to death on her own dick." ~ YandereDev
73. "That thing has a vagina for a face." ~ YandereDev
74. "Is there an ass hanging out the back of the wagon? There might be too many butts in the wagon. I might need to take some butts out." ~ YandereDev
75. "Oh, god. I thought he was going to climb on top of the trash can, then climb on top of the poop, then sit on top of the poop, then poop on top of the poop." ~ YandereDev
76. "Fucky shit dick nipple farts!" ~ YandereDev
77. "Among the five cacti, my dick did get stuck. It fucking hurts like hell, holy shit, holy fuck." ~ YandereDev
78. "I can't believe that actually worked. SHIT! It's not working, it's not working, it's not working, it's not working! ...it worked." ~ YandereDev
79. "Uhhhhh, no. My stream is not child-friendly. We talk about cucks, ducks, and sweaty bear balls." ~ YandereDev
80. "It's a penis car! Ohhhhh, why did I build a penis car?" ~ YandereDev
81. "I would genocide every fucking kitten on the face of the fucking planet if it meant I would get to cuddle with Zero Suit Samus." ~ YandereDev
82. "Oh my fucking GOD! The camera just went STRAIGHT UP HER ASS! It was FUCKING MAGICAL! Oh, god bless you, Japan! God BLESS you!" ~ YandereDev
83. "That's a bunch of dead children! ...ooh, they make nice squishy noises when you step on them." ~ YandereDev
84. "I'm glad that giant mechanical penis is finally dead." ~ YandereDev
85. "I would never put my lips on anything that came from the inside of a car. Unless Zero Suit Samus came out of a car. Then I'd put my lips all over her." ~ YandereDev
86. "Do you have something against hot sexy steamy lesbian SEX?" ~ YandereDev
87. "What? Like a dick? I don't need your dick. I got that sweet tight pussy." ~ YandereDev
88. "A fuck kitten is the baby version of a fuck cat." ~ YandereDev
89. "She's violently farting on him hard enough to melt his face off." ~ YandereDev
90. "Blanka's dick is green. Probably...probably surrounded by orange pubic hair." ~ YandereDev
91. "After all she's been through today, I think the loli's entire body is sore." ~ YandereDev
92. "Girls don't pee. Their vaginas just...whisper liquid dreams into the toilet." ~ YandereDev
93. "Ooh ooh ooh ooh ooh! See this right here? This is an android girl's vagina. Watch how I fist it. ...and that was a demonstration of how to properly fist an android girl." ~ YandereDev
94. "I wonder if the jizz is still inside Dorothy" ~ YandereDev
95. "Wee woo, wee woo! Potential new waifu spotted! All hands on dick!" ~ YandereDev
96. "SHE hates me. SHE hates me. HE hates me. HE'S dead. HE'S just some random fuccboi." ~ YandereDev
97. "I don't want you to take no shits on my dick. My dick ain't there to be your personal toilet, okay?" ~ YandereDev
98. "Okay, come on! Give me your nine thousand penises! Give me ALL nine thousands of the penises, come on!" ~ YandereDev
99. "Chest, pelvic area, and posterior? That's a funny way to say BOOBS, VAGINA, AND ASS." ~ YandereDev
100. "You have tuned in to twitch.tv/yanderedev, the number one hentai channel on Twitch!" ~ YandereDev
101. "Are all the babies aborted? I hope I aborted all the babies." ~ YandereDev
102. "Now, look at the eggplant. That doesn't look like a dick at all! If that's what your dick looks like, you need to see the fucking dick doctor!" ~ YandereDev
103. "It's fine if somebody farts on me. That's better than all the other stuff that could happen." ~ YandereDev
104. "So, from now on, a boy will always fart on me. Every single time. It will always be fartboi." ~ YandereDev
105. "I dunno if that works. I dunno if you can use a dead fat Mexican midget as a boat." ~ YandereDev
106. "Are you dicking my dick right now? Fuck you!" ~ YandereDev
107. "Why do you need his consent to touch him? You should be able to touch him without his consent!" ~ YandereDev
108. "I fisted that big boy up the ass." ~ YandereDev
109. "That bastard Cody. He's always punching women in the vagina. So rude." ~ YandereDev
110. "What's the point of playing the video game...if you don't need to play the video game, in order to play the video game?" ~ YandereDev
111. "Everything has to be about fat tits. If your game's not about fat tits, what the fuck are you doing?" ~ YandereDev
112. "An ass is just...boobs without nipples. That you sit on." ~ YandereDev
113. "Green is the color of the busty girl. Blue is the color of the shitty flat-chested tsundere BITCH. So I'll go with green." ~ YandereDev
114. "No, you dummy! You're not the one blow-jobbing the mermaid! The mermaid is the one blow-jobbing YOU!" ~ YandereDev
115. "If you become sexually aroused, then my nose grows longer, like Pinocchio." ~ YandereDev
116. "Why is Lisa Simpson...it's like she's twerking with her vagina instead of her ass." ~ YandereDev
117. "I want to run outside, grab that coyote by the dick, and say, SHUT THE FUCK UP!" ~ YandereDev
118. "I can't stop touching her. I just want to touch her. Can I just sit here all day, touching her?" ~ YandereDev
119. "Do I have a dirty mind, or is that a giant golden penis?" ~ YandereDev
120. "Just fuck me in the ass with a big old golden dildo." ~ YandereDev
121. "Have you ever heard of a film called FUCK YOUUUUU, STUPID HORSE! STUPID HORSE! STUPID GODDAMN HORSE PIECE OF SHIT!" ~ YandereDev
122. "Are you serious?! You want me to stick my hand in a horse's vagina?!" ~ YandereDev
123. "Either that, or there's an unlimited supply of hippos that come outta there. Like a vagina that just gives birth to hippos." ~ YandereDev
124. "The male crotch has armor. The female crotch is fully exposed." ~ YandereDev
125. "My horse has a shiny ass. Look at that ass." ~ YandereDev
126. "How do you know that a clown car is not a vagina that gives birth to clowns?" ~ YandereDev
127. "You can fuck everything. There's never anything that you're not fucking." ~ YandereDev
128. "Bada bing, bada boom, bada fuck you in the ass, grandpa." ~ YandereDev
129. "Oh,onii-chan, I'm hurt...please...kiss it better..." ~ YandereDev
130. "I'm attacking him in the butt, and it's kinda working. SHIT, IT'S NOT WORKING ANYMORE!" ~ YandereDev
131. "Surely, I've touched the girls at least two billion times..." ~ YandereDev
132. "I know this, because I've looked up every one of their skirts." ~ YandereDev
133. "Boobs aren't handles to grab? I've had it wrong this entire time." ~ YandereDev
134. "Blonde lady is really hot. I'm about to tear off all her clothes." ~ YandereDev
135. "Damn, son! You wearin' some lewd panties. Only covers the front, doesn't cover the taint and asshole. Das sum lewd panties." ~ YandereDev
136. "🎵 I'm a girl 🎵 With a butt 🎵 I run around with a butt 🎵 Attached to my butt 🎵 " ~ YandereDev
137. "I'm just glad there's no birds here. Birds totally ruined the last mission - GOD DAMN IT, THERE'S BIRDS HERE!" ~ YandereDev
138. "What the shit is this shit? How do I unfuck this fuckery?" ~ YandereDev
139. "Like Icarus with his wings of wax, flying too close to the sun, I flew too close to the boobies, and was enveloped in the milk storm." ~ YandereDev
140. "Is it warm up there in that tight wet warm hole?" ~ YandereDev
141. "That's as bad as 100 Hitlers!" ~ YandereDev
142. "Go stick a Senpai up your ass. You don't know what you're talking about." ~ YandereDev
143. "I had to fuck her unconscious. That's the only way I could get out of there." ~ YandereDev
144. "My favorite part was when the praying mantis opened up her dick-sucking mouth and I slobbered all over it." ~ YandereDev
145. "He side-stepped my lesbian!" ~ YandereDev
146. "Jesus, we just saw diarrhea erupt out of that volcano's asshole!" ~ YandereDev
147. "I'm trying to have an all-girl party, but all these penises keep getting in my way. It's very frustrating." ~ YandereDev
148. "He's sneezing. Or he's orgasming. It's one or the other." ~ YandereDev
149. "Her fart is so powerful, it's casting a shadow." ~ YandereDev
150. "Sticking your hand up their ass is so effective, there's no point in doing anything else." ~ YandereDev
151. "Grab her by the boobs and drag her. They're like handles." ~ YandereDev
152. "Did you give it a picture of Minnie Mouse, and it started masturbating?" ~ YandereDev
153. "I may as well have a cat boyfriend to have gay adventures with on this island." ~ YandereDev
154. "I want to get a stick to beat up those annoying blind girls." ~ YandereDev
155. "Gaze too long into the vagina, the vagina gazes back at you." ~ YandereDev
156. "A ladder is an anti-gravity device that temporarily grants humans flight." ~ YandereDev
157. "Awwwww, the penis got snapped in half immediately." ~ YandereDev'''
        # print(returnedtext)
        quotes = returnedtext.splitlines()
        # print(quotes)
        '''for c, i in enumerate(quotes):
            a = ".".split(i)
            b = ".".join(a[1:])
            quotes[c] = b
            print(b)'''
        # eeeee = random.choice(quotes)
        # print(eeeee)
        # print(eeeee.split("."))
        await message.channel.send(".".join(random.choice(quotes).split(".")[1:]))
