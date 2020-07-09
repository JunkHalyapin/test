label day08:

    scene day8 with fade
    "DAY 8"

    scene day8 ev01-01 with fade
    Jes "Mmm."
    "Jessica takes a long, deep breath, feeling Conner's warm body against her own. She is totally relaxed."
    JesT "Ughn. I don't want to get up. I'm too comfortable."

    scene day8 ev01-02
    "Despite her wish to stay in her warm, comfy bed, she's excited about getting back to work."

    if "d04mayorTease" in choices:
        JesT "I've got another visit with the mayor today. Mom was right. Not bad for a week of work."

    else:
        JesT "I need to keep searching for something about the vigilante. Mr. Birch isn't going to wait long."

    JesT "Time to get up."
    "As she rouses, though, Conner does as well. He moans and pulls her close."
    Con "Hey, baby. Sleep well?"

    scene day8 ev01-03
    Jes "I did. You?"
    Con "Really well. I had a good dream."
    Jes "I can tell. You're poking my butt with that thing."
    "Conner chuckles. His hand slips down Jessica's body and onto her leg."
    JesT "Mmm, that's nice. But I don't have time for it."

    scene day8 ev01-04a
    "Jessica rises, Conner still pawing at her."
    Jes "Sorry babe, but I've got to get ready for work."
    Con "Aw, come on. Just a quickie before you run off and get busy all week."

    if "d07firstLesbian" in choices:
        scene day8 ev01-04b with dissolve
        JesT "I'd point out how busy he's been, but I'm the one who came home late after fucking another woman."
        "Thinking about Heather brings up a pang of guilt, and Jessica quickly gets up."

    else:
        scene day8 ev01-04c with dissolve
        Jes "Says the man who drove another guy a hundred miles when we had a date."
        Con "Exactly my point! We're both so busy, so let's spend some time together while we can."
        "Jessica chuckles, patting his hand before getting up."

    Jes "Sorry, sweetie. I've got to go get ready."

    scene day8 ev01-05 with fade
    play sound shower_1 loop
    "Popping into the shower, Jessica begins planning her day."

    if "d04mayorTease" in choices:
        JesT "I need to get my questions together for my meeting with the mayor, and make sure I have my notes on hand."
        "She smiles inwardly."
        JesT "If he's as easy as he was the last time we met, I should be able to get something juicy out of him this time. That'll make Duncan happy."

    else:
        JesT "The mayor let slip something about meeting Senator Harris today. I wonder if there's any way I could get an interview with Mayor Wilson afterward."
        JesT "I could try to speak with his secretary, Shani."
        JesT "She did seem okay if I asked her a few questions. I can drop by for a chat, and see if I can sneak in a talk with the mayor."

    scene day8 ev01-06 with fade
    "Jessica spends a few minutes planning in the shower. Before she finishes, Conner comes in, strolling over to the toilet to pee."
    JesT "Oh, come on. He couldn't wait until I'm done?"
    JesT "Huh. I forgot what it's like living with someone else and only one bathroom."
    "Conner's eyes wander over to her naked body."
    Con "Mind if I jump in with you, babe?"
    Jes "You gonna behave yourself?"
    Con "Probably not."
    JesT "Well, there's no way this doesn't end in sex. I guess I have a little time, though."

    menu:
        "Let him join":
            $ sex += 1
            $ relCon += 2
            JesT "What the hell. I don't have time for this, but I really could use a good bang before the week begins."
            Jes "Come on in."

            jump day08morningsex

        "Not in the mood":
            $ choices.append("d08noMorningSex")
            $ relCon -= 1
            JesT "I'm not in the mood, plus I really have to get ready for work."

            scene day8 ev01-07
            Jes "Sorry, sweetie. I really do need to get going."
            "Conner groans in disappointment, but nods."
            Con "Okay."
            Jes "I'll be out in a minute, then the shower's all yours."
            "He nods again and goes to the sink to brush his teeth."
            stop sound fadeout 1

            jump day08ready

label day08morningsex:

    scene day8 ev01-08 with fade
    "Dropping his shorts to the floor, Conner climbs in with Jessica."
    "She tries to ignore him, continuing to shower while he soaks his body."
    Con "You know, there's something I forgot while I was deployed."
    Jes "What's that?"
    Con "If you're ticklish."
    "His fingers are suddenly on her sides, rapidly stroking her."
    Jes "AGH! Stop! Don't do that!"
    "He just chuckles."
    Con "You used to love playing around like that."
    Jes "No, you used to do it even though I told you to stop. But I have to get ready for work."

    scene day8 ev01-09
    "He turns her around, pushing her up against the wall."
    "They're kissing before she can say anything, both of them moaning together."
    "His hand is pulling her closer while his growing erection begins poking at her leg."
    JesT "Damn, that feels nice. I get so wrapped up in things sometimes I forget how good it feels to have him holding me like this."

    scene day8 ev01-10a
    "Despite her strict schedule, she wants to have some fun with Conner."
    Jes "I told you I have to get ready. I don't have time for this."
    Con "Okay then. I guess I'll just stop."
    Jes "Hey, play along. You're no fun when you won't let me tease you."
    Con "Well, if you're short on time, we shouldn't waste it."

    scene day8 ev01-10b with dissolve
    Jes "I have enough time for a quickie."
    Jes "So you need to get nice and hard already."
    "Her hand begins stroking his cock. Conner sighs, savoring the feeling of her fingers around his manhood."
    Con "That's nice."

    scene day8 ev01-11
    "Once he's fully erect, his hand moves down to pick up her leg."
    "His other takes his dick and places it against her soaking wet cunt."
    "Jessica sighs, eager to feel him inside her. She whispers to him."
    Jes "Come on, sweetie."
    "With a moan he pushes inside her, and she gives a little mewl of delight."
    play voices x_sex_2 fadein 1 loop
    JesT "Oh, that feels wonderful!"

    scene day8 ev01-12ani-00
    "Conner doesn't take his time, and begins thrusting himself forward steadily and swiftly."
    show d08ev01-12ani
    "Jessica is more than happy to feel his powerful body pushing against her, and his thick cock pounding away deep inside."
    "Her hands pull him closer, her moans quickly growing in volume in tandem with her pleasure."
    Jes "Conner, baby, it's so good!"
    "Conner groans in response, continuing to steadily thrust into Jessica."
    "The shower fills with the sounds of pleasure, wet bodies slapping against one another while the pair moan in joy."
    hide d08ev01-12ani
    "In mere moments, both are approaching orgasm."
    stop voices fadeout 1

    scene day8 ev01-13
    play voices x_sex_4 fadein 1
    "Neither says a word, the sounds each of them is making telling the other that they're going to cum."
    "Conner grits his teeth and begins thrusting even faster while Jessica squeals in delight. Her nethers quiver as she climaxes, her pleasure driven even higher by the feeling of Conner's cum splashing deep within."
    stop voices fadeout 1

    scene day8 ev01-14
    Con "Oh, baby. Oh, baby, I love you so much."

    if "d07firstLesbian" in choices:
        Jes "Mmm, that was nice."

    else:
        Jes "Hmm, I love you too, sweetie."

    "The pair share another kiss, softer and gentler than the last."
    Jes "But I really do need to get cleaned up… even more now."
    "He laughs."
    Con "Yeah. Me too."
    stop sound fadeout 1

label day08ready:

    scene day8 ev01-15 with fade
    "After a light breakfast, Jessica gets dressed and ready for work. When she emerges, Conner is dressed and waiting for her."
    Con "I'm ready to head out. You want a ride to work?"
    Jes "That'd be great. It's a little chilly out today."
    Con "Alright. Let's go."

    scene day8 ev02-01 with fade
    play sound car_driving_2_ambient
    "A short ride later, they arrive at the Gazette offices."
    Jes "Thanks, Conner. You have a good day."
    Con "You too. Call me if you want a ride home."
    Jes "I will, sweetie. Bye."
    stop sound fadeout 1

    scene day8 ev02-02 with fade
    "Jessica steps off the elevator at her floor."
    "Duncan is just inside, talking to the receptionist."
    "The conversation seems a little tense."

    scene day8 ev02-03
    Jes "Good morning, Duncan."
    Dun "Jessica, good. I was just about to call you."
    JesT "Oh. I'm not late, am I?"
    Jes "What's going on?"
    Dun "Apparently, there was a big fight at a warehouse in the industrial district last night. A bunch of gangsters got their asses kicked, then were tied up for the police."
    "Jessica feels herself go taut, excitement building in her chest."
    Jes "Our vigilante?"
    Dun "Looks like, unless these nutjobs are multiplying."

    scene day8 ev02-04
    Dun "There was already a reporter on the scene, but he wasn't able to get much. Just the obvious stuff and the police report."
    Dun "Here's the address. I'd like you to head down there and see if you can find something he missed. Anything that could help us with the story and help your case with Birch."
    Jes "I'm on it. Could I get a copy of the police report, though?"
    Dun "I'll head up to my office and e-mail it to you."
    Jes "Thanks. I'll head straight down there."
    Dun "Good luck."

    scene day8 ev02-05 with fade
    "Jessica arrives after a twenty minute cab ride, cursing that she didn't take her scooter."
    JesT "I really need to take Fireball to work. I can't afford to take a cab to every crime scene."
    JesT "Oh well. At least it gave me time to read the police report."
    "It's obvious where the crime scene is located, given the parked patrol car, the officer standing watch, and the police tape blocking the alley."
    JesT "Oh good. The officer's a man. He'll be easier to get past."

    scene day8 ev02-06
    "She greets him with a smile, reading his nametag as she approaches."
    Jes "Hello Officer… Evans."
    OEvan "Miss. I'm afraid this is a crime scene."
    "She gives him a giggle."
    Jes "Yeah, I kinda figured. The tape across the alley was a dead giveaway."
    "Her chuckling doesn't seem to be having the intended effect. The officer's expression remains passive."
    Jes "It's kind of cool out today, isn't it? I wish I'd warn something warmer."

    scene day8 ev02-07
    OEvan  "Miss, was there something you needed? I doubt you're here to talk about the weather."
    JesT "Jesus, this guy needs to pull that rod out of his ass."
    Jes "Just trying to start a conversation, Officer."
    OEvan  "It starts with the weather, and where does it end?"
    Jes "Well, I was hoping you could tell me what happened here last night."
    OEvan  "Ah, you're a journalist."

    scene day8 ev02-08
    Jes "Ah, sorry. I guess I should introduce myself. My name's Jessica O'Neil with the New Port Gazette."
    OEvan "Nice to meet you, and don't worry about forgetting, since it doesn't change anything. I have no comment on this crime scene."
    Jes "Is there anything at all you can tell me? Was this the vigilante?"
    OEvan "..."
    Jes "Was this a gang hideout?"
    OEvan "..."
    Jes "Did you have a nice dinner last night?"
    OEvan "..."
    JesT "Well, he's just a bundle of helpful. Let's see if anyone else noticed anything."

    scene day8 ev02-09
    "Jessica looks around, noticing two men standing nearby."
    JesT "Maybe they know something. They can't possibly be as useless as this \"rock\" I've been talking to."
    "As she strolls away, Officer Evans speaks up."
    OEvan "Be careful who you talk to around here. This isn't the best neighborhood."
    Jes "Thanks, but I'm sure I'll be fine with such an upstanding officer like you here."

    scene day8 ev02-10
    Jes "Excuse me, guys. Do you know what this is all about by any chance? Did someone get killed or something?"
    "The larger guy shakes his head and shrugs."
    GuyA "Nah. No one got killed. That crazy asshole…"

    scene day8 ev02-11
    "Just as Jessica thinks she had found her source of information, the guy with the ponytail butts into the conversation."
    GuyB "We didn't see anything. We just got here."
    JesT "Ah. Thing 2 is the one with the brains, and he doesn't want to talk apparently. Let's see if I can get anything out of the other guy then."
    Jes "You guys live nearby? You must have heard something. Anything at all? Can you help a girl out?"
    "The larger guy is checking her out, a fact that Jessica doesn't miss, but ponytail guy's face is dead serious."
    GuyB "We don't live around here. We were just passing by, thought we'd see what's up."
    JesT "What is with the people around here today? Did someone spray something in the air, or just surgically remove everyone's personalities?"
    "She turns to address the larger guy, since he seems more chatty, but before she can say anything someone calls out to her."

    scene day8 ev02-12
    OSmi "Ms. O'Neil?"
    JesT "I remember him. That's Officer Smith. He let me into the police precinct the other day."
    Jes "Excuse me, guys. I've gotta go. It's a shame you couldn't help me."
    "Jessica can tell the larger guy wants to say something, but he's again interrupted."
    GuyB "Maybe next time."

    scene day8 ev02-13
    Jes "Hello, Officer Smith. It's good to see you."
    Jes "I hope everything went well after my visit the other day. No problems, I trust?"
    OSmi "No problems. No one mentioned anything about your visit."
    Jes "Good. I'd hate for you to get into trouble because of me."
    OSmi "Speaking of that, I've been reading your paper. I'm surprised there's nothing new on this vigilante guy."
    OSmi "Didn't you say you got what you were looking for?"
    "Jessica smiles coyly."
    Jes "Aw, are you my first fan?"
    OSmi "Well, I wanted to see what my help led to."

    scene day8 ev02-14
    Jes "I did get what I was looking for, but I want to get the big story. Not cheap sensation pieces."
    JesT "Although it's not really in my hands what gets published, but that's the way I'd run things."
    OSmi "Right, the big story. I'm guessing that's why you're here."
    Jes "So this WAS the vigilante after all?"
    OSmi "I'm sure you and your people guessed it after reading the official report."
    Jes "We did, but I'm looking for something more. Something that's not in the official report."
    "Smith smiles and nods."

    scene day8 ev02-15
    "He leans into the side of the building, Jessica moving closer. He speaks softly."
    OSmi "I can't give you much, but I can tell you what I know."
    Jes "Okay if I take notes?"
    OSmi "Sure."
    OSmi "The vigilante got into the warehouse last night and just kicked the shit out of these guys."
    Jes "Do you know what time it happened?"
    OSmi "Not sure, but some of the guys got a call just after midnight."
    Jes "The vigilante called them?"
    OSmi "I don't know. A guy called and said he heard some noises from the warehouse. When the units got here, they found a bunch of thugs tied up, just like before."
    Jes "The report said no one was killed."
    OSmi "Right. They were just beaten and bloody."
    Jes "Was this a drug den, like last time?"
    "He hesitates for a moment."
    OSmi "No."
    "When he doesn't say anything for a moment, Jessica shakes her head."
    Jes "Well, what was it?"
    OSmi "Guns."
    Jes "Wow. Like, gun storage?"
    OSmi "We don't know yet, but there were a lot of them, all with the serial numbers scrubbed off."
    Jes "Do you know which gang this was?"
    FV "Officer Smith!"

    scene day8 ev02-16
    "Jessica instinctively hides her notepad, staying behind the corner so she won't be seen."
    OSmi "Uh, Detective Marshall, ma'am? What can I do for you?"
    JesT "Let's just play this cool. Maybe I can convince her I was just flirting with Smith."

    scene day8 ev02-17
    Mar "You can tell me why you're busy chatting, Officer."
    OSmi "Yes, ma'am. I was just… talking with a friend here."
    Mar "Strange place to meet a friend."
    OSmi "Yes, ma'am. I mean, no ma'am. It's just a coincidence."
    Mar "Uh-huh. Where's this friend of yours?"

    scene day8 ev02-18
    "Jessica steps forward, smiling at the detective."
    Jes "Hello. Nice to meet you."
    "Jessica is used to reading people's eyes, and finds a confusing mixture of emotions in the detective. First surprise, then almost recognition."
    "Then she feels as if the detective's sharp, hawklike gaze is ripping out every secret she's ever had."
    Mar "A friend, huh? Does that friend happen to be a journalist?"
    OSmi "Uh… yes sir- MA'AM!"
    Jes "I was just trying to find out when your department would release more info…"
    Mar "Smith, Detective Sanchez has something for you to do. Get to it."
    OSmi "Yes ma'am!"
    "Officer Smith heads off, but the detective's gaze never leaves Jessica."

    scene day8 ev02-19
    Mar "Now, how can the NPPD help you, Ms. O'Neil?"
    "Jessica is taken aback by the statement."
    JesT "I… didn't tell her my name."
    Jes "Do we know each other?"
    Mar "It's my job to know the kind of people who go snooping around police business."
    JesT "But how does she know me personally? I haven't written anything about the vigilante."
    JesT "Does she know about my visit to the precinct?"
    Jes "I was just asking Officer Smith about a few of the details from the previous night's events."
    Jes "He told me your department had its best people on the case. I believe he was talking about you."

    scene day8 ev02-20
    Mar "Ms. O'Neil, you should leave this case alone and let us handle it."
    Mar "Go report on some corrupt politicians, or a bank fraud. This is dangerous."
    Jes "I go where I'm sent. It's my job. I figure you'd appreciate that."
    Jes "And since I'm here, you can either be stubborn and butt heads with me, or we can help each other."
    Mar "Help? And how can you help us, Ms. O'Neil? Do you have any information you want to share?"
    Jes "I just got here. Do you have anything to share with me?"
    Mar "That's not how it works. You have a journalistic obligation to share any details about this case you might have."
    JesT "I could tell her what I've found, about the bike, the warehouse, all that."
    JesT "But I'll reveal all my cards, and then I'll just continue chasing their tails along with everyone else."

    scene day8 ev02-21
    JesT "I can tell her what they already know. That should satisfy her. And it should make them think I found it from somewhere else, not from one of their own."
    Jes "I know he's using a motorcycle to move around.  A black, sports bike."
    Mar "Interesting? And how do you know that?"
    Jes "I have a picture from the last time he showed up. But I cannot reveal my sources, Detective."
    Jes "I can send it to you, of course."
    Mar "You do understand that this is serious criminal activity? Someone is going to get badly hurt sooner or later. Or killed."
    Mar "Sure, that'll sell papers…"
    Jes "But…"
    Mar "Yes, people deserve to know about it. Spare me."
    Mar "The police will be the ones who uncover the truth. You can report it then."
    Mar "Don't mess with something you're not prepared for, Ms. O'Neil. No one wants to see you become the victim in one of your paper's articles."
    Mar "Now I've got work to do. Good day."
    "With that she spins on her heel and walks away."
    JesT "Well that went nowhere."

    scene day8 ev02-22
    "Jessica's mind is already racing as she turns to leave, finding Officer Smith walking back over."
    "He puts down the briefcase he's carrying and smiles a her."
    OSmi "She didn't scare you, did she?"
    Jes "Yeah right, as if I would be scared by some... detective… girl."
    OSmi "Hah, she does scare me at times."
    "The two share an understanding laugh."
    Jes "I'm heading back to the office. Thanks for everything."
    OSmi "No problem. I'm heading out myself."
    Jes "Take care. I'll see you around."
    OSmi "I'm sure you will, Ms. O'Neil."

    scene day8 ev03-01 with fade
    "Back at work, Jessica finds Duncan in his office."
    Dun "Jessica, good. Come in. Did you get anything?"
    Jes "I did. It was our vigilante after all."
    Jes "He beat the tar out of the gang using the warehouse, then someone called the police and said there was a disturbance there."
    Dun "Do I sense an admiration in your voice, Jessica?"
    Jes "Well, he is effective, alright."
    Dun "He is, until he gets killed. Or kills someone else."
    "Jessica just shrugs."
    Dun "Did the vigilante make the call?"
    Jes "They don't know, but the police did find lots of guns on site, with the serial numbers scrubbed."
    Dun "Damn. Anything else?"

    scene day8 ev03-02
    Jes "Yeah. There's two detectives, at least, who were working the scene. Sanchez and Marshall. I spoke to Marshall for a bit. She knew who I was, even before I said anything."
    Dun "That's a little strange, particularly since you just started."
    Jes "I thought so."
    Dun "Anything else?"
    Jes "That's pretty much it. A few other minor details, like a couple of guys who were acting squirrely, but nothing concrete."
    Dun "That's good work, Jessica. Birch should be happy. Write down all the details and send them to me."
    Jes "Will do."

    scene day8 ev03-03 with fade
    "Heading to her desk, Jessica sees Eve and Rosa talking."
    "The sound of Eve's french accent rather pleasant to her ear."
    JesT "Her accent is damn sexy. And fuck me, that outfit is cute."
    JesT "I don't think I could work something like that. I'd feel so stupid, as if I was dressing like a high school girl."
    JesT "She's making it work, though."

    scene day8 ev03-04
    Jes "Good morning, ladies."
    Eve "Good morning."
    Rosa "Hey."
    "Rosa is focused on her work, barely acknowledging Jessica."
    Eve "How was the crime scene?"

    scene day8 ev03-05
    Jes "Interesting. The vigilante kicked a gang's ass, then turned them and their guns over to the police, I think."
    Eve "As I said, the police are sloppy. They need someone like him doing their jobs for them."
    Jes "What are you two working on?"
    Eve "We may have found a good lead for the construction case."
    "Rosa spins about in her chair."
    Rosa "That stadium story. It turns out the piece we ran shook loose a few threads to pull on."
    Jes "Oh? What are the new details?"
    Rosa "Funny you should ask. I was going to ask for your help with this one."

    scene day8 ev03-06
    "Eve takes a seat on the desk while Rosa goes over the details."
    Rosa "So we found a connection between the company that got the contract and a smaller company that closed down a few years ago."
    Rosa "That smaller company worked on a few public projects, one of which was the reconstruction of a local school."
    Rosa "We wanted to see if we could get some details about the job, see if something pops out at us."
    Rosa "The thing is, the public records are superficial and have basically zero details. We'd need to get the full records from the school administration."
    Rosa "And that's where you come in, since the school is Eastwick High."
    Jes "You want me to infiltrate my old high school?"
    Rosa "Not exactly. I was more hoping you knew someone there."
    Jes "Well, it was a while back, and I only went for one year before my family moved."
    Jes "I barely remember anybody. Some teachers, maybe."
    Rosa "How about the principal?"
    Jes "I remember him, but I never really knew him."

    scene day8 ev03-07
    Rosa "Good enough. We're hoping he'll be receptive to a former student asking for those records."
    Jes "I guess it's worth a shot."
    Rosa "Good. We already set up an appointment with him tomorrow morning."
    Jes "Alright. Send me the info. And speaking of info, I was hoping you might be able to help me with some."
    Rosa "Shoot."
    Jes "I was looking into a company for the vigilante story, but I wasn't able to find much since they went out of business."
    Rosa "We have an account for the city registry. Come on. Let's go over to your desk and I'll show you."

    scene day8 ev03-10
    "Rosa guides Jessica to a website, showing her how to login."
    Jes "What's this even for, anyway?"
    Rosa "It's just a public database. The information has to be available to the public, but some parts require special access, for privacy reasons. Thankfully, we have that access, so we can get in whenever we want."
    Rosa "It's one hell of a useful tool. It'll become your best friend soon."

    scene day8 ev03-11
    Rosa "So what's important about this information you're looking for?"
    Jes "Like I said, it's for the vigilante story. Hopefully it'll become another lead, instead of just the dead end it is now."
    "Jessica hesitates before saying anything else."
    JesT "The last time I gave up information on the vigilante, Mr. Birch nearly screwed me."
    JesT "Can I trust Rosa, though? I think I'm being paranoid. She's a good woman."
    JesT "Still, I can just be quiet for now. If this leads to anything, I can tell her."

    scene day8 ev03-12 with fade
    "Jessica spends some time paging through the lists, combing through a disorganized nightmare of a database."
    JesT "Oh, so this is how I die. Of boredom."
    JesT "Wait. There it is. Cellco, a subsidiary of Havinshire Fabrications. Owned by Gerald Udarsh. There's even an address for the parent company."
    JesT "Thank you, Rosa. I'll have to pay this place a visit tomorrow."

    scene day8 ev03-13 with fade
    "Eventually, Rosa reappears at Jessica's desk, the two of them agreeing to head out to lunch."
    Jes "Eve, we're headed out for food. You wanna come?"
    Eve "You two go on ahead. I'll be there shortly."
    Rosa "Okay. See you soon."

    scene day8 ev03-14 with fade
    Rosa "So, is everything going well?"
    Jes "It's not bad, though I need to find something on this vigilante."
    Jes "Birch wants to publish the info I got from the police precinct, even though I promised I wouldn't."
    Rosa "Yeah, he can be stubborn that way."
    Jes "He said if I can find something else to publish, he'd led it slide."
    Rosa "Yeah, that'll work for a while, but he's gonna want to publish it eventually, one way or another."
    Jes "Fuck. Should I have just kept this all to myself?"
    "Rosa sighs, her head bobbing from side to side."
    Rosa "It might be a good idea to keep some things to yourself and off the company server… from time to time."

    scene day8 ev04-01 with fade
    Jes "I suppose. I'll look at this as a learning experience. Maybe next time… huh."
    JesT "Is that…?"
    Jes "Mr. Parker?"

    scene day8 ev04-02
    Parker "Jessica! Good to see you!"
    Rosa "Ben! It's been way too long!"
    Parker "Hello again, Rosie!"

    scene day8 ev04-03
    "Rosa and Mr. Parker share a strong hug, Rosa laughing all the while."
    JesT "Wow. I didn't know they knew each other."
    JesT "I guess they worked together before he left."
    Rosa "It's so good to see you again!"
    Parker "The feeling is mutual. You've only gotten more gorgeous since we worked together, Rosie."

    scene day8 ev04-04
    "Jessica's surprised to see how close the pair are. They won't stop hugging."
    Parker "They don't know what they're missing."
    Rosa "I missed having you around, Ben!"

    scene day8 ev04-05
    Jes "So… I guess you two know each other."
    Rosa "Oh yeah. Ben here taught me everything I know about journalism."
    Parker "Oh come on. You're exaggerating."
    Rosa "No joke. All my experience in this job comes from what this man taught me."
    JesT "These two are awfully close… literally. I wonder if there was something between them once."

    if "d04parkerNoApology" in choices:
        "Jessica feels a pang of jealousy, imagining Parker pushing his dick up against Rosa."
        "She pushes the thought away as soon as it comes to her."
    else:
        "Jessica pushes the thought away."
        JesT "It's not like it would matter."

    scene day8 ev04-06
    Jes "So, Mr. Parker. What brings you here today?"
    Parker "I actually just had a meeting with Birch."
    Rosa "Were the two of you reminiscing about the good old days?"
    Parker "HA! No, it was just about work. I am still in the newspaper business, even if I am at the end of the line."
    Parker "So where are you two off to? Have an interesting story to chase?"
    Rosa "No, just lunch I'm afraid. Nothing exciting."

    scene day8 ev04-07
    "The group heads off toward the exit, chatting as they go."
    Rosa "Did you stop off and see Duncan by any chance."
    Parker "Afraid not. I'm too old to handle both Birch and Duncan in the same day."
    "Rosa and Parker both laugh. Jessica smiles, but it's purely for show."
    "She doesn't like being left out, but doesn't know Rosa or Parker well enough to contribute."
    "Parker seems to notice, though, looking at Jessica out of the corner of his eye."
    Parker "So, Rosie, How is your new colleague working out?"

    if "d02cutAngus" in choices:
        Rosa "She's a natural. She's already doing a wonderful job here."
    else:
        Rosa "I'm confident Jessica's going to do a wonderful job. She's already shown a huge amount of promise."

    "Jessica smiles, a warm feeling springing up in her gut."
    JesT "Not sure if that's pleasure or hunger."
    Jes "Mr. Parker, would you like to join us for lunch?"
    Rosa "You should! It would be great to catch up!"
    Parker "I'd love to, but I have another appointment in twenty minutes."

    scene day8 ev04-08
    play sound city_ambience_siren_1 loop
    Rosa "Alright. Well, it's been wonderful seeing you again, Ben. But you owe us a lunch."
    Parker "Ha! It's a deal! Take care of yourself Rosie. And look after Jess."
    Rosa "I will."
    Parker "Jess, make sure to stop by the newsstand tomorrow. I'm going to talk to my old cop buddy today. Hopefully I'll have something for you."
    Jes "I will. I'll see you tomorrow, Mr. Parker."
    "The pair share a final hug before Parker heads off and the ladies continue on their way."
    stop sound fadeout 1


    if "d03kissBlake" in choices:
        scene day8 ev04-09b with fade
        play sound coffee_shop_1 fadein 1 loop
        "Arriving at the coffee shop, they're greeted by Blake's warm smile."
        "Blake blushes when she sees Jessica, a fact Jessica doesn't miss."
        JesT "Huh. I wonder if that's because of the kiss. She's just as easily flustered as Laura."
        JesT "I hope she doesn't think that was more than it was. I was just trying to fool that kid."
        JesT "Then again, I did kind of get carried away. And kissing Blake was definitely pleasant."
        JesT "Maybe it wasn't quite so innocent after all."
        Blake "Hey Jessica! Hey Rosa!"
        Rosa "Afternoon, Blake."
        Jes "Hey there. How's it going?"
        Blake "I can't complain. What can I get for you?"

    else:
        scene day8 ev04-09a with fade
        play sound coffee_shop_1 fadein 1 loop
        "Arriving at the coffee shop, they're greeted by Blake's warm smile."
        Blake "Hey Jessica! Hey Rosa!"
        Rosa "Afternoon, Blake."
        Jes "Hey there. How's it going?"
        Blake "I can't complain. What can I get for you?"

    "The three women make their orders and Eve heads inside, grabbing a table."

    scene day8 ev04-10
    Jes "So how have things been, Blake?"
    Blake "Not bad. Super busy!"
    Jes "Here or at class?"
    Blake "Both! I barely have any time anymore. I'm exhausted!"
    Jes "Yeah, I remember that feeling. Don't worry. You only have a few years of this left."
    Blake "Oh, don't say that."

    scene day8 ev04-11
    Jes "So that guy that wouldn't leave you alone. What was his name?"
    Blake "The Creep. I mean his name is Derreck, but I think The Creep is better."
    Jes "Right, Derreck. He hasn't come back, has he?"
    Blake "Nope! Thanks to you, he hasn't shown up once! It's been so nice."
    Jes "I'm glad to hear it."

    scene day8 ev04-12 with fade
    "After her brief chat with Blake, Jessica takes a seat with the others."
    Eve "So, you know what we're working on. What have you been doing with your time, Jessica?"
    Jes "Trying to chase down leads for this vigilante."
    Jes "I've got so many small pieces, but I can't seem to put them together."
    Jes "I'll find something soon, though. If I get my way, I'll find out everything about him."

    scene day8 ev04-13
    "Rosa and Eve share a look, but before they can say anything more Blake arrives with their food."
    Jes "Thanks, Blake."
    Blake "You're welcome. Enjoy, everyone."

    scene day8 ev04-14
    "Jessica starts to eat, but the other two seem to have questions for her."
    Rosa "You seem awfully eager to find out about this guy, Jess."
    Jes "I have to. Birch needs something on him from me."
    Rosa "That's not what I mean. You seem very invested in this guy."
    Eve "Oui. The way you talk, I would guess you've made this personal."
    Jes "What? No, I haven't."
    Rosa "What do you think about him? Him, not the story."
    Jes "I mean, he seems like he's doing good work. He's fighting crime, helping out the whole city."
    Rosa "And doing it in style?"
    Jes "I wasn't going to say that, but yeah. I like his style."

    if "d01agreeBirch" not in choices:
        Eve "You've changed your tune from your first day. You didn't think he was that important."
        Jes "Working the case has helped me to understand the situation better is all."

    Rosa "It definitely sounds like you've become invested in him."
    Jes "Huh."
    JesT "Are they right? Do I have a personal interest in this now?"

    scene day8 ev04-15
    Jes "Well, I might have an interest in this, but I'm still a journalist."
    Jes "My first priority is the story."
    Rosa "As it should be."
    "The conversation turns to other topics, but Jessica's mind stays on the vigilante."
    "Far from making her reevaluate her investigation, she's more interested in finding out about him than ever."

    scene day8 ev04-16 with fade
    "With lunch finished, Eve heads off to use the restroom before they leave."
    Jes "So Rosa, you must have had fun working with Mr. Parker when he was at the company."
    Rosa "Oh, he was great! I've never known a more patient man in my life."
    Jes "He's a good man, and you two seemed pretty close."
    "Rosa goes quiet for a moment, her lips almost forming into a smile."
    Rosa "Well, I started working at the Gazette as soon as I graduated. Ben was still a big name in journalism back then."
    Rosa "It was kind of like working with a superstar, only older and able to pry secrets seemingly from nowhere."
    Rosa "Well, one thing led to another and… we kind of had a thing together. Briefly."
    Jes "Wha… really?! You and Mr. Parker?!"
    Rosa "It didn't last long. Working together was complicating things."
    Rosa "And this was twenty or so years ago. He wasn't so old back then."
    Jes "I suppose. He would have been in, what, his late 40s?"
    Jes "You'll have to tell me more sometime. I bet it's one hell of a story."
    Rosa "Maybe one day. Fow now, let's just say it's a shame age caught up with him."
    "The older woman smiles, giving Jessica a playful wink."

    if "d02teaseParker" not in choices:
        Jes "I guess it is."

    else:
        if "d03feelParker" in choices or "d04parkerNoApology" in choices:
            JesT "Well, my teasing brought out one hell of an erection, so age hasn't caught up with him that much."
        else:
            JesT "Well, I don't know if he can get a boner, but he was definitely responding when I teased him. So it hasn't caught up with him that much."

        JesT "But it's a little embarrassing. Should I tell her?"

        menu:
            "Don't mention it":
                JesT "My time with Mr. Parker is fun, but it's just that. My time."
                Jes "It is a pity, but it happens to everyone."

            "Tell Rosa":
                $ choices.append("d08tellRosa")
                Jes "Well, I don't think his age has slowed him down as much as you think."
                Rosa "What do you mean?"
                "Jessica gives her a sly smile."
                Jes "He's… still got a pretty strong libido."

                scene day8 ev04-17
                "Rosa's face lights up."
                Rosa "Wait… are you saying you and Ben…?"
                Jes "It's- it's nothing like that."
                Rosa "Then how…?"
                Jes "I just teased him a couple times and he got a little excited."

                if "d03feelParker" in choices or "d04parkerNoApology" in choices:
                    JesT "VERY excited, and very hard."

                "Surprisingly, Rosa laughs."
                Rosa "That's a very cruel thing to do to an innocent old man."

                scene day8 ev04-18
                Jes "He kind of started it. I caught him checking out my ass while I was helping him move boxes."
                Jes "So he was kind of asking for it."
                Rosa "Ha! That does sound like him."
                Rosa "But you're a little minx, playing with an old man like that."
                "Jessica smiles and shrugs."
                Rosa "Well, we should get going. Looks like Eve's ready to head out."
                Rosa "But I'm gonna want details sometime."
                "Jessica giggles at Rosa's interest."
                Jes "Why don't we swap Mr. Parker stories, then?"
                Rosa "It's a deal."

    scene day8 ev04-20 with fade
    "The group heads to the front counter to pay for their lunch. While Rosa and Eve chat, Jessica goes to speak with Blake."
    Jes "Hey, I was wondering if you wanted to grab that drink we talked about later today."
    Blake "Oh. Uh, sure. That sounds good."
    Jes "I'm not taking you away from anything am I?"
    Blake "Just studying, and I'll do anything to get away from that."
    Jes "Haha! Okay. What time do you get off tonight?"
    Blake "5:30."
    Jes "Okay. I'll swing by and pick you up then."
    Blake "Cool."
    Jes "Ready ladies?"
    "The trio head out on their way back to the Gazette."
    stop sound fadeout 1

    scene day8 ev05-01 with fade
    "The ladies arrive back at the office a short while later, talking about the corruption case."
    Rosa "I'm gonna go make sure Duncan is ready for our meeting with Birch this afternoon."
    Rosa "Catch up with you girls in a bit."
    Jes "Okay."

    scene day8 ev05-02 with fade
    "Heading back into the work area, Jessica sees Tommy staring at his phone."
    Jes "Hey Tommy!"
    Eve "Hello Tommy. Nice to see you today."
    Tom "Hey Jessica, Eve. It's good to see you again."

    scene day8 ev05-03
    Jes "How are you doing?"
    Eve "Doing well, I hope?"
    "His cheeks redden, his eyes briefly moving from Jessica to Eve, and down her legs before turning away."
    Tom "Not bad. I'm just here."
    Eve "I'm glad you are."
    JesT "Eve seems weirdly friendly with Tommy today."
    Tom "Oh yeah?"
    "His voice lifts, surprised, and his cheeks getting even more red."
    Eve "I have something I need to get done, but I just don't have time for it."
    Eve "If you could help me out, I'd be SO thankful."
    Tom "Sure. Happy to."
    JesT "Ah. Now it makes sense."

    scene day8 ev05-04
    "Eve opens up a website, explaining to Tommy what she needs from him - combing through a database and writing down the names of construction companies, along with the work they've done."
    JesT "God, that sounds boring. He's an intern, though. I guess that's kind of the stuff they end up with."
    JesT "Plus, he seems happy to help. I guess any teenage boy would be if asked by a woman that looks like Eve."

    scene day8 ev05-05 with fade
    "After giving Tommy an encouraging pat on the back, Jessica heads to her own desk."
    "She starts doing research on a couple of cases she'd like to work on when she has more time."

    if "d04mayorTease" in choices:
        "She eventually decides to turn her attention to the mayor, doing a bit more research on him."
        JesT "It never hurts to know as much as possible before going into an interview."

    if "d06defendingKevin" in choices:
        scene day8 ev05-06 with fade
        "After a half hour or so her phone beeps."
        JesT "Huh. Unknown caller. I swear, I'm gonna get a new number if it's another solicitation for sex."
        JesT "Oh. It's from that kid who agreed to watch the warehouse for me, Kevin."
        Kev "hey I saw this guy comin out of the building"
        Kev "got a picture of his car but cant follow"
        "Beneath the text is a picture of a surprisingly familiar red car."
        "Kevin mentioning following the car reminds Jessica about advice she got from Mr. Parker, and she doesn't want Kevin getting into trouble or danger on her account."
        "She types in a response, thanking him for his help and telling him not to put himself at risk."
        "After, she scrolls down to find a picture of a surprisingly familiar red car."

        scene day8 ev05-07
        JesT "Huh. That looks just like Conner's car."
        JesT "That can't be his, though. Kevin said he was coming out of the building."
        "She sends a text back to Kevin to confirm that the man was inside, and a minute later Kevin tells her that the driver did come out of the building and get into the car."
        JesT "I have to be imagining things. There's no reason Conner would have been there."

        scene day8 ev05-08
        JesT "Zooming in on the plate doesn't help. It's too blurry."
        JesT "This really does look just like his car, though."
        JesT "Why would he have been there? Does he know something about the vigilante?"
        JesT "I didn't give him that much information. I know I didn't tell him where the warehouse was. I don't even think I told him about the warehouse, did I?"

        scene day8 ev05-09
        JesT "Why don't I just call him. I'm sure I'm just imagining things."
        "The phone doesn't ring long before Conner picks up."
        Con "Hey babe! What's up?"
        Jes "Hey. I just thought I'd call. See what you're up to."
        JesT "He sounds like he's in the car. I think I can hear the engine."
        Con "I'm just workin'."
        Jes "Oh yeah? What are you doing?"
        Con "I drove out to visit a guy, seeing if he can hire some vets."
        Con "Didn't work out, though."
        JesT "Well, there was no one in that warehouse who could hire veterans, so if he went by there he's lying."
        "Jessica does chat for a bit longer, trying to get a few more details out of him."
        "In the end, though, nothing else seems out of the ordinary."

        scene day8 ev05-10
        Jes "Okay. Well, you have a good day, sweetie. I love you."
        Con "I love you, too. Bye."
        "Hanging up, Jessica sighs, her thoughts going back and forth."
        JesT "If that was him in the picture… then he's lying to me."
        JesT "What the fuck was he doing there, and why was he lying about it?!"
        JesT "How the hell did he even know about the warehouse?! Has he been spying on me?!"
        "Jessica's thoughts are interrupted when a voice behind her causes her to jump."
        Dun "Hey, Jessica?"
        Jes "Oh. What's up, Duncan?"

    else:
        scene day8 ev05-11 with fade
        "She keeps at it, working steadily until Duncan walks over."
        Dun "Hey, Jessica?"
        Jes "What's up, Duncan?"

    scene day8 ev05-12
    if "d04mayorTease" in choices:
        "Duncan takes a seat, waving his hand her way."
        Dun "You ready for the interview?"
        Jes "Definitely. And I think he's looking forward to it. I scored some points with him the last time."
        Jes "I think he likes to be the center of attention."
        Dun "Heh. Yeah, I bet he's got lots of articles about himself framed in his home."
        Jes "You think I should push some hard questions, or keep playing the ambitious young journalist?"
        Dun "Keep the act for now. You may impress him, and he'll let something slip. Then we can go from there."
        Dun "So, good luck. Let me know how it goes."
        "He heads off with a smile."

    else:
        "Duncan takes a seat, waving his hand her way."
        Dun "So what did the mayor tell you about meeting Senator Harris?"
        Jes "Not much, unfortunately. It was just a passing mention."
        Dun "Do you think you could pay him a visit and see if he lets something slip?"
        Jes "I'd already been thinking about doing just that."
        Dun "Great minds think alike."
        Jes "I think I can stop by to see if he liked the article I wrote, and see if he has anything else to say."
        Dun "That'll work. Let me know how it goes."
        "He heads off with a smile."

    if "d06defendingKevin" in choices:
        scene day8 ev05-13
        JesT "Okay. Let's think about this. It's definitely possible it's not him."
        JesT "I know his car's make and model. Let me look it up."
        "Jessica begins searching for information on Conner's car."
        JesT "Let's see. According to this, everything in the picture is factory standard. Just like Conner's."
        JesT "So any stock model would look just like his. It could easily be someone else's car."
        JesT "It's still suspicious. I go check there, then soon after a car that looks just like my boyfriend's shows up? It would be a weird coincidence."
        JesT "I need to look into this. It's probably not him, but I need to be sure. This doesn't feel right."
        JesT "But I need more information before I can do anything. Maybe I can compare the photo to his car, or see if I can get him to slip up and say something about it."
        JesT "I'll worry about this later. I need to head to the mayor's office."

    scene day8 ev05-15 with fade
    "While gathering up her things before she heads out, she hears Tommy still working behind her."
    JesT "I should say hi while I've got the chance."
    "Heading over to his workstation, Jessica gives Tommy a big smile."
    Jes "So, how's it going? You enjoying your work?"
    "He shrugs, clearly still very shy."
    Tom "It's interesting. It's cool to learn how all this stuff works."
    Tom "Y'know, searching for leads and stuff."

    scene day8 ev05-18
    JesT "I guess I wouldn't say if I was bored either."
    Jes "I know this sort of stuff isn't very exciting. We'll find something more interesting for you to do tomorrow."
    Jes "I actually have an address I need to check out tomorrow, if you'd like to come with me."
    Tom "Yeah, that'd be great!"
    Jes "Well, I have to go talk to the mayor. I'll see you later, Tommy."
    Tom "Bye, Jessica."

    scene day8 ev05-19 with fade
    "She stops off at Rosa's desk to say goodbye, finding both her and Eve hard at work."
    Rosa "How's Tommy doing?"
    Jes "Oh, he's great! He's learning just how unexciting research can be."
    Eve "Better to learn it now, given that's most of what we do. He doesn't want to dedicate years to a job he'll hate."
    Rosa "I'll make sure to get him something a little more stimulating when he's done with that job."
    Jes "He'll like that. I'm off. I'll see you two tomorrow."
    Rosa "Bye!"
    Eve "Au revoir."

    if "d04mayorTease" in choices:
        jump day08mayor

    else:
        jump day08mayorEarly

label day08mayorEarly:

    scene day8 ev06-01 with fade
    "Jessica arrives at the mayor's office around 5 PM. City Hall seems to be winding down for the day."
    JesT "Oh good. Shani's inside. If nothing else, maybe I can get a good interview out of her."

    scene day8 ev06-02
    Jes "Hey there, Shani."
    Sha "Jessica! Good to see you again. What brings you by?"
    Sha "I don't think you have an appointment today."
    Jes "I don't. I was in the building, so I thought I'd stop by."

    scene day8 ev06-03
    Sha "Mayor's Wilson's in a meeting at the moment, and he has another one soon. I'm not sure he can see you today."
    Jes "It's no problem if he can't. I was hoping to chat with you as well."
    Jes "I'd love to get an interview with the mayor's secretary."

    scene day8 ev06-04
    Sha "Oh. Well, that's a nice thought, but I'm not sure I'd have anything interesting to say. I'm just a receptionist, really."
    Jes "I'm sure that's not the case. You've been with Mayor Wilson a long time, and he spoke very highly of you last time."
    Sha "Sure. Okay. I, uh, do have to ask the mayor first. I need to make sure he's okay with me speaking with the media."
    Jes "Of course. That's no problem at all."

    scene day8 ev06-05
    "A minute later, the mayor exits his office, a well dressed man with silver hair at his side."
    "The pair are laughing together, clearly quite friendly."
    Sha "Oh, they're finished early. He might have some time after all."

    scene day8 ev06-06
    Mayor "Ms. O'Neil! What a pleasant surprise!"
    Jes "Mayor Wilson. A pleasure to see you again."
    Mayor "I wasn't expecting you today. Are you here to see little old me?"
    Jes "I was in the building. I thought I'd stop by and see what you thought of the article."
    "The mayor gives her a huge smile, then turns to the man at his side."

    scene day8 ev06-07
    Mayor "Ms. O'Neil, this is Senator Harris. Senator, this is Jessica O'Neil from the New Port Gazette."
    Har "A pleasure, Ms. O'Neil."
    "The man takes Jessica's extended hand, giving it a firm but not hard squeeze. His eyes are sharp, beaming with intelligence. His voice is regulated, his stance and posture perfect."
    "His eyes seem to be burrowing into Jessica, and she feels the need to wilt, though she resists the urge."
    JesT "I feel like he's seeing right through me."
    Mayor "She's one to keep an eye on, an ambitious young woman."
    Har "A dangerous combination."
    Jes "I'm just a journalist. All I do is report the truth."
    Har "Your truth?"
    Jes "Does everyone have a different one?"
    Har "Well, there's truth, and there's truth. And sometimes it's best to keep one under wraps. For the good of the people? Don't you think?"
    "Jessica shrugs, realizing he's twisting words to suit the game he's playing. She decides to play along."
    Jes "Sometimes. I judge on a case by case basis."

    scene day8 ev06-08
    "The senator seems happy with the response, then steps back and pats the mayor's shoulder."
    Har "Well Bill, it's been fun. Remember what I said. I'll be expecting an answer on the fundraising."
    Mayor "I'll think about it. Take it easy, John."
    "He turns, looking at Jessica."
    Har "It was a pleasure meeting you, Ms. O'Neil."
    Jes "Likewise, Senator Harris."

    scene day8 ev06-09
    "As the senator leaves, the mayor gives Jessica a smile."
    Mayor "Anyway, I did read your article. I thought it was very well written. You're a better writer than many of your colleagues."
    Jes "Well thank you. I'm glad you enjoyed it."
    Mayor "Well, I actually have to get ready for another meeting in a bit. It was a pleasure seeing you again, Ms. O'Neil."
    JesT "Well, if I want to try to get an interview with him, now's the time to ask."
    JesT "I could just see about interview Shani instead. That might be easier to get."

    menu:
        "Just arrange an interview with Shani":
            $ choices.append("d08interviewShani")
            Jes "Before you go, sir, I was actually hoping to get an interview with Shani."
            Mayor "Really?"
            Jes "Yeah. She's such an important member of your staff, but such people rarely get introduced to the public."
            Mayor "Hmm. Shani, what do you think?"
            Sha "I wouldn't mind at all."
            Mayor "Alright then. I've been grooming her for public office for some time now. I think it's a good time to introduce her to the city."
            Mayor "I'll be out the day after tomorrow, so you can use my office for the interview, if Shani has the time."

            scene day8 ev06-10
            Mayor "Well, you have a wonderful day, Ms. O'Neil. I look forward to speaking with you again."
            "He offers his hand, Jessica happily shaking it."
            Jes "Of course. I'm ready to listen if you have anything you'd like to share."
            "The mayor gives her a chuckle, then heads back to his office. Jessica turns back to Shani."
            Sha "Yeah, give me a call sometime tomorrow afternoon. I should know before I leave when I'll have some time the following day."
            Jes "Great! I'll talk to you tomorrow then. Have a nice night."
            Sha "Bye!"

            jump day08blake

        "Ask to talk to him":
            $ choices.append("d08talkMayor")
            $ relMayor += 1
            JesT "Might as well go for it."
            Jes "Actually, sir, if you have some free time, I was hoping you could maybe squeeze in a quick interview."
            Jes "I figured you might have something interesting to share after your meeting with the senator."
            "Jessica is fairly sure she sees a hint of a smile at the corner of his mouth, a mild amusement."
            "He turns his head away briefly, then nods."
            Mayor "Why not? I can't talk for long, but I'd love to speak with you."

            jump day08talkMayor

label day08mayor:
    $ choices.append("d08talkMayor")

    scene day8 ev06-12 with fade
    "Jessica arrives at the mayor's office a little after 5 PM. City Hall seems to be winding down for the day."
    JesT "Damnit. I didn't want to be late, even if it's just a couple of minutes."
    JesT "I definitely need to take my scooter to work. It's so much easier to get around in traffic with it."

    scene day8 ev06-13
    Jes "Hello Shani."
    Sha "Jessica! Good to see you again."
    Jes "Sorry I'm late. I hate to keep the mayor waiting."
    Sha "No worries. Just a sec."
    Sha "Mr. Wilson, Jessica O'Neil is here to see you."
    Mayor "Wonderful. I'll be out in a moment."

    scene day8 ev06-14
    "The ladies exchange a few pleasantries while they wait. A minute later, the office door opens and Mayor Wilson appears."
    Mayor "Ms. O'Neil! Thank you for coming!"
    Jes "Mr. Mayor. Thank you for having me. I'm sorry I'm a little late."
    Mayor "It's not a problem at all."

label day08talkMayor:

    scene day8 ev06-15
    Mayor "Uh, Shani, is that proposal for the trade union ready yet?"
    Sha "It's almost finished. I just need to arrange the wording for the second proposal a bit. The one involving the handling of discrimination lawsuits."
    Sha "I figured that one deserved a little extra time to make sure it pleases the union heads and keeps costs down."
    "Jessica watches them talk, happy to observe just how much the mayor trusts Shani."
    JesT "I had no idea how much he relies on her, or that she was involved with the city business to such a degree."
    JesT "There really is far more to her than it seems."

    scene day8 ev06-16
    Mayor "Alright. Jessica, come on in."
    Jes "Of course. Shani, thank you for your help."
    Sha "No problem, Jessica."

    scene day8 ev06-17
    "The pair head inside, Jessica moving in first. She can feel his gaze on her ass."
    if slut >= 15:
        "She manages to keep a smile off her face, but she does give a bit more sway to her butt."
        JesT "Might as well give him a bit of a show. As long as it brings me closer to a story."
    else:
        "She feels a little uncomfortable, but she ignores the feeling."
        JesT "Maybe I can benefit from his distraction."

    if "d04mayorTease" in choices:
        scene day8 ev06-18a
        "She briefly pauses, considering where to sit. When she does, he puts his hand on her lower back, right at the top of her butt."
        JesT "Of course he wouldn't miss the chance to touch me."
        JesT "I should have expected it."
        Mayor "Please, take a seat on the couch."
        Jes "Thank you."

    else:
        scene day8 ev06-18b
        "She briefly pauses, considering where to sit. When she does, he puts his hand on the small of her back, pushing her toward the couch."
        Mayor "Please, take a seat on the couch."
        Jes "Thank you."

    scene day8 ev06-19
    "She takes her seat, the mayor sitting beside her this time."
    Mayor "Comfortable?"
    Jes "Yes, thank you."

    if "d04mayorTease" in choices:
        Jes "So, did you read the article I wrote?"
        Mayor "I did. It was wonderful. You're a very talented writer."
        Jes "Thank you. I'm glad you enjoyed it."
        Jes "I made sure to keep the part about the deputy mayor out of it."
        Mayor "And I'm very grateful. That's the kind of thing most people in your position would have pounced on."
        Jes "I did promise I won't write about it, and I like to keep my promises."
        "The mayor nods appreciatively."
        Mayor "I can give you all the information on it, but I'd like you to keep it to yourself for two days, until I can hash out all the details."

    else:
        Jes "I'm very glad you enjoyed the article I wrote."
        Jes "I very much wanted to get off to a good start."
        "He gives her a big smile."
        Mayor "I did too. I'm glad we could establish a good working relationship."
        Mayor "Well, since you've been so accommodating, I can return the favor."
        Jes "Oh?"
        Mayor "In regards to a new deputy mayor."
        JesT "This is already going well!"
        Mayor "I do need you to keep this all to yourself for two days, while I hash out all the details."

    scene day8 ev06-20
    Jes "Of course. That won't be a problem."
    Mayor "Well, Deputy Mayor Stratton will be stepping down soon."
    Jes "Why will he be leaving?"
    Mayor "Unsatisfactory results in the fight against the city's crime."
    Mayor "He was directly responsible for that, and his results have been poor to say the least."
    Jes "Crime has been getting worse as of late."
    Jes "Who will be taking up the position?"
    Mayor "I don't have a solid candidate just yet. The police commissioner will take up some of the responsibilities, and other people in his department will help."
    Mayor "The position will be filled after the elections."
    Jes "You don't think the police commissioner bears some responsibility for the rising crime rate?"
    "He shakes his head immediately, as if he expected the question."
    Mayor "The reins were in the deputy mayor's hands. Now the commissioner can run things his way. We'll see how effective he'll be."
    JesT "I sense there was some tension between the commissioner and the deputy mayor, but I'll leave it alone for now."
    "Jessica continues writing notes on her notepad as he's giving her all the details on the story."

    scene day8 ev06-21
    JesT "This is great, I'll be able to write a good article about it in two days. But I'm curious to hear what the senator had to say."
    "Jessica sets aside her notepad."
    Jes "Off the record, anything you want to share with me from your meeting with the senator?"
    Mayor "Off the record?"
    Jes "Absolutely."
    Mayor "Well, there was an interesting proposition. He's thinking of putting in my name as a candidate for governor."
    "Jessica is taken aback for a moment."
    Jes "Wow. That's strange."
    Mayor "Why? Do you think I'm not fit for the job, or that I don't deserve a promotion?"
    Jes "I'm sorry. I didn't mean that you don't deserve it."
    Jes "It's just that your approval rating in the city is good."
    Jes "The people of New Port benefit directly from your good decisions. They drive on good roads, and enjoy a healthy, growing economy."
    Jes "But on a state level, it's all about reputation, and at the moment your reputation isn't in the best place."
    Jes "The latest poll showed your approval rating below 30 percent, and the current governor is most likely going to be reelected."
    Mayor "It seems like you've been doing your homework."
    Jes "I have, and I'm confused. Why would your party want you to exit a race you have a good chance to win, so you can enter one you're probably going to lose?"
    "Jessica stops talking, not sure if saying all of this out loud was the right decision. Guys like him are easily offended, even if what you say is the truth."
    "He's quiet for a moment, then gives her a slight smile."
    Mayor "I like you, Ms. O'Neil. You're a smart girl."
    Jes "Thank you, sir, but what do you think?"
    Mayor "I'm not sure yet. Ask me again in a few days."
    "The two of them continue chatting for a bit about various topics."
    "As they talk, Jessica can see his eyes roaming up and down her legs."
    JesT "Wow. This guy can't seem to control himself. I wonder if it's a defense mechanism."
    JesT "I could play with him a little bit. It could help bring out more information."

    if "d04mayorTease" in choices:
        JesT "It worked out pretty well last time."

    menu:
        "Act professional":
            $ choices.append("d08mayorNoTease")
            JesT "On the other hand, I really shouldn't encourage this kind of behavior."

            jump day08noTease

        "Tease him":
            $ choices.append("d08mayorTease")
            $ relMayor += 1
            $ slut += 1
            JesT "Well, if he wants to play, why don't I give him a better view?"

            jump day08mayorTease

label day08noTease:

    scene day8 ev06-26e
    "They talk a bit more. Jessica getting used to his occasional glances at her legs."
    JesT "He's a horny guy. But as long as he doesn't try to go beyond just looking, I can live with that."
    Mayor "I'll be attending a fundraising event on Thursday evening. There will be various journalists invited."
    Mayor "If the Gazette sends you, I can arrange for you to ask the senator these questions yourself."
    Jes "I'll have to talk to my editor, but if I can make it, I definitely will."

    scene day8 ev06-31e
    "Soon, Mayor Wilson says he needs to wrap it up."
    "Jessica nods, putting away her pad and pen."

    scene day8 ev06-34e
    Jes "Thank you so much for meeting with me, Mr. Mayor."
    Mayor "You're very welcome, Ms. O'Neil. It was a pleasure seeing you again."
    Mayor "I do hope to see you at the fundraiser."
    "The pair shake hands before Jessica heads out of the office."

    jump day08mayorEnd

label day08mayorTease:

    scene day8 ev06-22
    "She reaches for her pen, intentionally pushing it to the ground."
    Jes "Oops. Sorry about that. I can be so clumsy. One sec."

    scene day8 ev06-23
    "Leaning to the side, Jessica makes sure to give him a nice view of her backside."
    JesT "Enjoying the show, Mr. Wilson? I bet you are."
    if persistent.pov == 1:
        scene day8 ev06-23mpov
    "She gives her butt a little wiggle, just enough to look both innocent and titillating."
    JesT "I'll just take my time getting my pen. Give him a few seconds to enjoy the view."
    "Eventually, having given the mayor plenty of time to savor the sight of her ass, she decides that's enough."

    scene day8 ev06-24
    "Sitting back up, Jessica writes a few notes while the mayor talks, but the mood in the room seems to have shifted."
    "The mayor seems looser, a little less restrained."
    Jes "Your receptionist, Shani, is a remarkable young woman. You seem to place a great deal of trust in her."
    Mayor "Well, I'm a busy man, and every bit of help is welcome."

    scene day8 ev06-25
    Jes "Given all your office has to handle, I'm surprised your staff isn't…"
    "She trails off when she realizes she can see the mayor's erection."
    JesT "I shouldn't be surprised, but there's something surreal about sitting in the mayor's office and noticing his erect dick."
    "The mayor gives her a cunning smile when he sees her looking, but makes no attempt to hide it."
    JesT "He's such a horn-dog. It's like he's showing me what he has to offer… or maybe what the price of more information is."

    scene day8 ev06-26
    Jes "Do you think such a capable young woman like Shani deserves a promotion?"
    Jes "Her talents would definitely benefit the city, and you."
    "The mayor laughs, his hand comes to rest on Jessica's back."
    Mayor "Most definitely. I am trying to use all assets as best I can."
    Mayor "I do like to keep talented young women close at hand."
    JesT "My god. It's like you've never heard the word subtle before."
    "She glances down at his erection, thinking he's getting a little too worked up."
    Jes "You always had capable young women helping your campaign. Your wife worked heavily with you during your first election, correct?"
    "She enjoys the heavy sigh he lets out at the mention of his wife."

    scene day8 ev06-27
    "Surprisingly, though, he moves his hand to her knee, almost casually."
    Mayor "My wife and I really do love one another very much, but… as time goes on, people change. The passion fades, and the love matures."
    "His hand is gently rubbing her knee as he speaks."
    JesT "Is he REALLY trying to suggest cheating on his wife is the definition of mature love?"
    JesT "This guy is incredible!"
    JesT "Still, I wonder how many women he's gotten into bed by talking that way about his wife while hitting on them?"

    scene day8 ev06-28
    "Jessica's hand comes down on his own, putting a stop to his fingers stroking her leg."
    Jes "I doubt your wife appreciates your relationships with other women at work, Mr. Mayor, no matter how \"mature\" your love is."
    Mayor "It depends on the kind of work relationship I have with them."
    Jes "And what kind is ours?"
    Mayor "You're holding it in your hand, Ms. O'Neil, so it depends on you."
    JesT "I guess the question falls on me then. What do I want our working relationship to be?"
    JesT "How much do I want what he has to offer?"

    menu:
        "Put his hand on his leg":
            $ choices.append("d08mayorNoTouching")
            JesT "I shouldn't lose control of this situation. Teasing him is one thing, and it would definitely help my career, but this is going too far."

            jump day08noTouching

        "Put his hand on his dick":
            $ choices.append("d08mayorDick")
            $ relMayor += 1
            $ slut += 1
            JesT "I don't want him to get too handsy, but I do like the attention. It's oddly arousing."

            jump day08mayorDick

        "Put his hand higher on your leg":
            $ choices.append("d08mayorGrope")
            $ relMayor += 2
            $ slut += 2
            JesT "Wow, I feel so dirty. Letting this ugly old man feeling me up. He's been open with me, though, and I think he deserves a little reward."

            jump day08mayorGrope

label day08noTouching:

    scene day8 ev06-29a
    "She picks up his hand and puts it on his own leg."
    Jes "I think the most beneficial relationships are the professional ones."
    "The mayor tenses up a bit, his relaxed demeanor fading."
    Mayor "You're probably right. You'll have to forgive me for getting carried away with such a gorgeous young woman by my side."
    Jes "There's nothing to forgive, Mr. Mayor."

    scene day8 ev06-30a
    "He stands, and Jessica can tell he's trying to adjust himself."
    Mayor "Well, time does get away from me. I've got to get ready for my next meeting."
    Mayor "I'm sure you have a tight schedule as well."
    Jes "It's getting late indeed. I should head out."

    scene day8 ev06-31a
    Jes "Let me just get my things together."
    "She turns away, intending to give him time to fix himself."
    "Eventually she hears him exhale sharply, and she realizes that she just gave him a nice view of her ass."
    JesT "Oops. I really didn't mean to tease him this time."
    JesT "One day I'm gonna give him a heart attack if I'm not careful."

    scene day8 ev06-34a
    "Turning back, she shakes his hand, finding it funny how he's trying to cover up his erection with the other one."
    Mayor "Uh, ahem, by the way, there's a fundraising event on Thursday. If the Gazette can send you, I can arrange for you to speak with Senator Harris."
    Jes "That would be wonderful. Thank you. I'll let my editor know."
    Jes "Have a good day, Mr. Mayor."
    Mayor "You too, Ms. O'Neil. I hope to see you Thursday."

    jump day08mayorEnd

label day08mayorDick:

    scene day8 ev06-29b
    "She takes his hand and moves it directly onto his erection, making sure to lightly brush her fingers over as she does so."
    Jes "I do like working with a partner, but I think everyone should keep to their tasks, and use their own tools for maximum efficiency."
    "She keeps her hand on his while she speaks. The mayor seems lost in a world of his own, savoring the feeling of her touch."

    scene day8 ev06-30b
    "She pulls her hand back to her knee, though the mayor is still smirking."
    Mayor "I have to admit that I'm not used to this sort of workflow. I'm old school. I think working closely together is the best solution."
    "His hand is gently stroking his erection as he speaks, Jessica watching in morbid fascination."
    JesT "That bulge seems big. I wonder what it looks like?"
    Jes "Well, the world is changing, and one must adapt."

    scene day8 ev06-31b
    "The mayor unzips his pants and sticks his fingers inside. Jessica is only surprised that she's not shocked in the slightest."
    Mayor "I'm willing to learn, if I have someone younger to help teach me."
    Jes "I could maybe do that, Mr. Mayor, but one step at a time."
    Mayor "Fair enough. Say, there's a fundraising event this Thursday, with various media outlets in attendance."
    Mayor "You should make sure the Gazette sends you. Partners like us should use every opportunity to help one another."
    Jes "I'll definitely be there."
    "Jessica feels a tingling in her nethers at the sight of the man next to her stroking his dick beneath his pants."
    JesT "I really should get out of here before I completely lose control of the situation."

    scene day8 ev06-32b
    Jes "It's late. I should be going."
    "She stands up to collect her things, but can't help giving the mayor another nice view of her backside."
    "For a moment she can imagine him pulling his dick out and taking her as she's bending over in front of the leather couch."
    "The image sending a warm wave through her body, before she dismisses it with a shake of her head."
    JesT "As if I would ever allow this ugly old man go that far."

    scene day8 ev06-34b
    "She picks her bag and turns around, the mayor stands up as well, his body close to Jessica's."
    "She smiles and leans in, giving him a kiss on the cheek, making sure to hold his hand, preventing him from reaching her ass."
    "But there's nothing she can do about his dick rubbing against her thigh."
    "She decides to let him savor the feeling for a moment before pulling away."
    Jes "You have a wonderful day, Mr. Mayor."
    Mayor "You too, Ms. O'Neil. I hope to see you Thursday."

    jump day08mayorEnd

label day08mayorGrope:

    scene day8 ev06-29c
    "She pulls his hand gently up her thigh, giving him a coy smile."
    Jes "You know, some women like it when a man takes the lead in a partnership."
    Jes "You're in charge of this whole city, after all. I'm sure you can take charge of me."
    Mayor "Those are my favorite kind of relationships, Ms. O'Neil. The most productive ones for both parties."

    scene day8 ev06-30c
    "She keeps up the submissive role she's playing while he gently strokes her thigh. His hand moving further along her leg, pushing her skirt up."
    JesT "You dirty old man. You're trying to push my legs apart."
    Jes "Oh, that's a little quick, don't you think? I'm new to this kind of working relationship after all."
    Jes "I'll need to be guided slowly."
    Mayor "You don't seem like someone who gets easily scared, Ms. O'Neil."
    JesT "Ugh, I should find this guy revolting, but… It's like the idea that he's repulsive is making me so damn wet!"
    JesT "I think I should stop this now, before it goes any further."
    Jes "Well, I think it's time I head out. You're a busy man, and I don't want to take up all your time."

    scene day8 ev06-31c
    "She stands, gathering up her things and making sure to give the mayor a nice view of her backside."
    JesT "Might as well give him something to think about until we see each other again."
    JesT "I'm sure he appreciates it."

    scene day8 ev06-32c
    "Standing up, the mayor puts his hand on her hip."
    Mayor "Need some help?"
    if persistent.pov == 1:
        scene day8 ev06-32cmpov
    JesT "Oh man. I can feel his dick pushing into my butt."
    JesT "He's shameless!"

    scene day8 ev06-33c
    Mayor "Let me just get past you here…"
    "His obvious attempt to get physical with Jessica results in the man pushing her onto the sofa."
    Mayor "Oh, I'm sorry. This is such a tiny office, and I'm such a big man."
    JesT "His dick is poking right into my ass! If it was out and I didn't have a skirt on, I bet it would slip right inside."
    JesT "This feels so dirty!"
    if persistent.pov == 2:
        scene day8 ev06-33cfpov
    "Jessica gives a little giggle, and rubs her ass back and forth just a bit."
    Mayor "You know, I'll be at a fundraising event on Thursday. If you have the Gazette send you, I'll make sure it's worth your time."
    Mayor "Especially if you are interested in some… backstage access."
    "A little moan slips from Jessica's lips."
    Jes "Oh, I'll make sure I'm available."

    scene day8 ev06-34c
    "He lets her go, and she turns into his arms. Leaning in, he tries to kiss her on the mouth, but she turns and gives him a peck on the cheek instead."
    JesT "Nice try, Mr. Mayor."
    "Undeterred, his hands grope her ass while he has the chance, making sure to rub his dick between her legs."
    JesT "I really need to go. I'm seriously getting wet here."
    "Pulling away, she gives him a playful smile."
    Jes "I'm gonna head out. Have a good day, Mr. Mayor."
    Mayor "You too, Ms. O'Neil."

    jump day08mayorEnd

label day08mayorEnd:

    scene day8 ev06-35 with fade
    "Heading out of the office, Jessica heads over to Shani's desk."
    Sha "Everything went well?"
    Jes "Very well. It was a very productive meeting."
    Jes "You have a great day, Shani."
    Sha "You too, Jess."

label day08blake:

    scene day8 ev07-01 with fade
    play sound coffee_shop_1 fadein 1 loop
    "Jessica heads back to the coffee shop to pick up Blake for their drink."
    "She's waiting inside, talking with her coworker."
    Blake "Hey Jessica."
    Jes "Hey there, Blake. Sorry I'm late."
    Blake "No problem."
    Jes "You ready?"
    Blake "Yeah. Let's go."
    "They say goodbye to Blake's colleague and leave."
    stop sound fadeout 1

    scene day8 ev07-02 with fade
    play sound city_ambience_siren_1 loop
    "The two of them walk for a little while, chatting as they go."
    Jes "Here we are. Why don't you grab a seat while I get the drinks?"
    Jes "What would you like?"
    Blake "Anything but coffee."
    Jes "Ha! Alright. I'll surprise you."

    scene day8 ev07-03 with fade
    "A minute later, she brings two tall, bright glasses over to Blake."
    Jes "Here you go."
    Jes "Uh… I told the bartender to surprise me as well."
    Blake "Thanks. What is it?"
    Jes "It's… it's… it's green."
    Jes "But there's booze in it, so it's all good."

    scene day8 ev07-04
    Jes "So, how are things going at the university?"
    Blake "Eh. It's alright."
    Blake "I'm working toward a business degree, since my dad wants me to take over the business one day."
    Jes "Is that not what you want?"
    "Blake shrugs."
    Blake "It's fine. It'll help when I'm running the business."
    Jes "Well, if it were up to you, what would you study?"

    scene day8 ev07-05
    Blake "Photography, actually. That or aerospace engineering."
    Jes "Okay. Those are slightly different."
    Blake "I always wanted to design spaceships. I think I was born a little early, though."
    Blake "But I absolutely adore photography."
    Jes "You can at least practice it as a hobby, at least. That's something, right?"
    Blake "Yeah, sure. But with all the studying, and the work, there's not much time left for it."
    Jes "Does your father insist on you working, or it's your idea?"
    "Blake laughs lightly."
    Blake "It's part of my father's education methods, but I also like doing it. It's an interesting experience, something to get my mind off the university."

    scene day8 ev07-06
    Jes "Well, there's the college party life for that, isn't it?"
    "Blake gives a tiny shrug."
    Blake "I'm… not really a party girl."
    Jes "That's funny. I remember you hinting you had lots of fun at school."
    Blake "Oh, right. Yeah, I might have exaggerated."
    Blake "Rosa's always coming up with cool stories and doing awesome things."
    Blake "So I embellished. Just a bit."

    scene day8 ev07-07
    Jes "Well, you're young. You have a whole lifetime for exciting things to happen."
    Blake "Working with my dad, the most exciting thing is when the Dow Jones takes a tumble, and I get to watch him freak."
    Blake "That'll be me one day. Yay."

    scene day8 ev07-08
    Jes "You sound like you've already accepted it."
    Blake "Maybe. Maybe not. I don't know."
    Blake "Maybe I should do something different after college."
    Blake "But for now, my classes take up so much time I don't really think about it."

    scene day8 ev07-09
    Jes "I bet you're a maudlin drunk, aren't you?"
    Blake "Oh my god, yes!"
    Blake "It's one of the reasons I don't drink that often. I get all melancholy and philosophical."
    Blake "And I sing. Apparently, I'm tone deaf."
    "Jessica laughs, putting a smile on Blake's face."
    Jes "I'm dry. You want another drink?"
    Blake "Sure. I'll get the next round."

    scene day8 ev07-10
    "While Jessica's waiting for Blake, she gets a call from Conner."

    if "d06defendingKevin" in choices:
        "She just stares at it for a few seconds, still wondering if he really was the one who went to the warehouse."
        JesT "Don't think about it. Just answer, and pretend nothing's wrong."

    Jes "Hey, sweetie. What's up?"
    Con "Not much. What're you up to?"
    Jes "I'm actually out having a drink with a friend."
    Con "Cool. You gonna want a ride home?"

    menu:
        "Tell him to come pick you up":
            $ choices.append("d08blakeConner")
            Jes "Sure. As long as you don't mind giving my friend a ride home."
            Con "Not a problem. Where you at?"
            Jes "That place across from your gym."
            Con "Awesome. Be there in a bit."

            jump day08blakeConner

        "Tell him you'll meet him home":
            $ choices.append("d08blakeOnly")
            Jes "Don't worry about it. I'll get a car home."
            Con "Alright. In that case, I'm gonna stay a little longer to get some work done. I'll see you at home, babe."
            Jes "Love you."

            jump day08blakeOnly

label day08blakeConner:

    scene day8 ev07-11
    "Blake comes back with two more drinks, almost tripping over her own feet."
    Blake "Here you go. I had no idea what the drink was, but the bartender remembered what he gave you."
    Jes "You okay?"
    Blake "Yeah. Sorry, I'm a bit of a lightweight with booze. Thankfully, these drinks seem light."
    Jes "I imagine you can't drink much before you get drunk. You're so thin."
    Blake "Thank you!"

    scene day8 ev07-12
    "A little while later, Jessica sees Conner's car pull up."

    if "d06defendingKevin" in choices:
        JesT "It really does look just like the one Kevin saw."

    Jes "There's Conner."
    Blake "Conner?"
    Jes "My boyfriend. He's giving us a ride."
    Jes "Hey, sweetie!"
    Con "Hey babe."
    Jes "Conner, this is Blake. Blake, this is Conner."

    scene day8 ev07-13
    Blake "Nice to meet you."
    Con "Likewise. You know, I had a buddy named Blake."
    "Blake sighs audibly."
    Blake "Yeah, I get that alot. Meeting men named Blake, or who know a guy named Blake."
    Con "I wouldn't sweat it. I always thought of Blake as a pretty girl name that guys just have."
    "Blake chuckles and grins, running a hand through her hair."
    Blake "Woo. I'm a little tipsy."
    "Jessica gives Conner a knowing smile."
    JesT "Nice save, sweetie."

    scene day8 ev07-14
    "Conner takes a seat by Jessica, chatting with Blake for a few minutes, while the girls finish their drinks."
    Jes "I think we should get going. Shall we?"
    Blake "Good idea. Another drink or two and I'll end up drunk."
    "Conner grins as Blake gets to her feet, then heads off toward the car."
    stop sound fadeout 1

    scene day8 ev07-15 with fade
    play sound car_driving_2_ambient
    "The conversation keeps going as they drive, Conner taking the time to ask Blake personal questions."
    Con "You live in your dad's old condo? That's pretty cool."
    Blake "Yeah. The house is too small for me and my step-mom."
    Jes "Parents can be difficult."
    Blake "Pfft. Difficult doesn't come near describing that bitch of a slut my dad married."
    Blake "Enough about her, though. I'm having too much fun with you guys."
    Jes "Me too. You want to come out with Conner and I sometime, go to a nightclub?"
    Blake "Yeah! That sounds great!"

    scene day8 ev07-16
    Jes "We'll make sure to get some good stories for you to tell Rosa."
    "Blake laughs, making Conner raise an eyebrow at Jessica."
    Con "Stories?"
    Jes "Blake thinks her life is boring compared to my coworker."
    Con "Oh, well I know we can think of something to get you a good story."
    stop sound fadeout 1

    scene day8 ev07-17 with fade
    play sound neighborhood_1 loop fadein 1
    "When they arrive, Blake and Jessica both get out. Jessica gives Blake a big hug."
    Jes "This was fun. I'm glad we did this."
    Blake "Me too. I had a blast!"
    Jes "You take care now. I'll call you tomorrow, so we can hash out the dinner details."
    Blake "Okay. Buh-bye!"
    stop sound fadeout 1

    scene day8 ev07-18 with fade
    play sound car_driving_2_ambient
    Jes "Alright. Let's head home."

    if "d06defendingKevin" in choices:
        "Now that she's alone with Conner, her mind turns back to the picture Kevin sent her."

    Jes "How was your day?"
    Con "Not bad."
    "He doesn't say anything else. She reaches over to put her hand on his leg, having to bend too far to do it."
    Jes "You know, this car just isn't made for certain activities."
    "Her hand moves up and she gives him a squeeze."
    Con "We should try the back seat. It's great for that sort of thing."
    Jes "And how would you know? We've never done it back there."
    Con "I had to sleep back there a few times in college."
    Jes "Uh-huh. Sure. Come on. Tell me. You don't need to be ashamed of having sex with another woman."
    Con "Nope. I never touched another woman during college, and I won't change that story. Ever."
    "Jessica laughs, and gives him an encouraging squeeze."

    if "d06defendingKevin" in choices:
        "She's happy to have a happy moment with her boyfriend, given how she'd been worrying about that picture all day."
    stop sound fadeout 1

    jump day08backHome

label day08blakeOnly:

    scene day8 ev07-10b
    "After hanging up, Jessica stares at her feet, a dark cloud settling on her thoughts."
    JesT "I don't get it. Why don't I want to spend more time with Conner."
    JesT "During his deployment, all I wanted was him back. Now that he's here, I'm having drinks with Blake instead of spending time with him."
    JesT "I feel like something's changed, and I don't know what."

    if "d07firstLesbian" in choices:
        JesT "And now I'm sneaking around behind his back, and I had sex with another woman."
        JesT "Where is this relationship even going?"

    scene day8 ev07-19
    "Blake returns a moment later with their drinks, almost tripping over her own feet."
    Blake "Here you go. I had no idea what the drink was, but the bartender remembered what he gave you."
    Jes "You okay?"
    Blake "Yeah. Sorry, I'm a bit of a lightweight with booze. Thankfully, these drinks seem light."
    Jes "I imagine you can't drink much before you get drunk. You're so thin."
    Blake "Thank you!"

    scene day8 ev07-20
    "They chat for a little while longer, and after finishing their drinks, the two decide to head home."
    Jes "Why don't we share a car? Give me a minute, and I'll get one."
    Blake "Sounds good. Hey, did you want to go to a club or something sometime?"
    Jes "Definitely! It's been a while since I went clubbing with any of my girlfriends."
    Jes "I'll check my schedule and see when I can get away. I'll call you tomorrow and let you know."
    Blake "Cool."
    stop sound fadeout 1

    scene day8 ev07-21
    play sound car_driving_2_ambient
    "The car arrives a few minutes later. Climbing in, Blake gives the driver directions to her place."
    Blake "You don't have a car, Jess?"
    Jes "I have a scooter, actually. My sweet little Fireball. But my boyfriend took me to work today."
    Blake "Wow. You've got guts. I've always been terrified of motorcycles."
    Jes "It's great once you get over the initial fear. I can teach you how to ride if you like."
    Blake "Ha, my father will be thrilled."

    scene day8 ev07-22
    "As the ride goes on, Blake leans in to Jessica."
    Blake "You know, the driver's spent most of his time checking us out."
    Jes "Yeah, I'm used to it."
    Blake "I bet you are."

    if "d03kissBlake" in choices:
        Blake "You know, we could give him something more interesting to look at."
        Blake "Like we did at the coffee shop to get rid of Derreck."
        JesT "Huh. I didn't expect Blake to suggest something like that. She's a little bolder than I thought."

    else:
        Blake "Maybe we can give him something to look at?"

    menu:
        "Kiss her" if "d03kissBlake" in choices:
            $ choices.append("d08blakeKiss")
            $ relBlake += 2
            $ lesbian += 1
            JesT "Well, I did enjoy kissing her last time. Can't hurt to do it again."
            Jes "Let's do it."

            scene day8 ev07-27
            "Jessica pulls Blake into her embrace, their lips gently pressing together."
            "Blake moans very quietly while Jessica strokes her hand."
            JesT "Geez, I feel like I'm back in college."
            JesT "She's so young, so soft."

            if "d07firstLesbian" in choices:
                JesT "Who knew I liked women this much?"

            scene day8 ev07-28
            "The kiss grows deeper and rougher."
            "Their tongues play together while Blake's fingers caress Heather's leg."
            JesT "Wow, she's actually a really good kisser."

            if "d05heatherFinger" in choices:
                JesT "Maybe even as good as Heather."

            scene day8 ev07-29
            "The kiss is interrupted as the car swerves violently, a horn blaring as another vehicle almost side-swipes the cab."
            Dri "Oh, Jesus! Uh… crazy drivers. Who lets these people drive?"
            "Jessica rolls her eyes."
            Jes "I guess some people can't keep their eyes on the road."

            scene day8 ev07-30
            "Blake is barely holding back a laugh, her eyes gleaming with joy."
            Blake "Oh my god! That was insane! We almost crashed!"
            Jes "Well, now you have a story for Rosa."
            Blake "Yeah, how I almost died while kissing a girl."
            Jes "Well, you wanted an exciting life."
            "The pair share a laugh."
            stop sound fadeout 1

        "Tease him with your legs":
            $ choices.append("d08blakeNoKiss")
            if "d03kissBlake" in choices:
                JesT "I don't want to give Blake the wrong impression. She seems to have taken the kiss the wrong way."
                Jes "I have a better idea."
            else:
                Jes "I have an idea."

            scene day8 ev07-23
            "Jessica opens her legs, rubbing her fingers along her thighs."
            Jes "Oh, my legs get so sore after a long day at work."
            "She can see the driver looking in the mirror, right down her skirt."
            Blake "Uh, yeah. Yeah, and it's really great when you have a guy around to help you rub them afterward."
            Blake "Get ‘em nice and relaxed."

            scene day8 ev07-24
            "A horn blares to the side, and the car swerves back into its own lane."
            "Another vehicle barely avoids side-swiping them."
            Dri "Oh, Jesus! Uh… crazy drivers. Who lets these people drive?"
            Jes "They might have been distracted. Some people can't keep their eyes on the road."

            scene day8 ev07-25
            "Jessica can't keep the grin off her face, and Blake is barely holding back laughter."
            Blake "That was insane! We almost crashed."
            Jes "See? Now you have a story for Rosa."
            stop sound fadeout 1

        "Ignore the guy":
            $ choices.append("d08blakeNoTease")
            Jes "We shouldn't mess with him. We don't want him to crash into someone."

            scene day8 ev07-22b
            Blake "Yeah, you're right."
            "The two continue chatting for a while."
            "They're perfectly aware that the driver is still watching, but they ignore him."
            "A little while later, they stop at Blake's address."
            stop sound fadeout 1

    scene day8 ev07-31 with fade
    play sound neighborhood_1 loop fadein 1
    "When they arrive, Blake and Jessica say their goodbyes."
    Blake "This was so much fun!"
    Jes "It was. Can't wait to do it again. Call to you tomorrow."
    Jes "Bye!"
    "With Blake waving enthusiastically, Jessica gives the driver her address and they head off."

    scene day8 ev07-32 with fade
    "A short time later they arrive at Jessica's."
    Dri "You have a good evening, Miss."
    "His eyes pass over her one last time."
    JesT "This guy needs to learn to keep his eyes to himself, or he's just asking to crash."
    stop sound fadeout 1

label day08backHome:

    scene day8 ev08-01 with fade
    if "d08blakeConner" in choices:
        "When they get home, both of them get cleaned up and changed."
        "Jessica comes out to find Conner on the couch, looking at his phone."

    else:
        "Jessica arrives home a short while later. She can hear Conner moving about."
        "She says hello, gives him a peck on the cheek, then gets cleaned up and changed."
        "She comes out to find him on the couch, looking at his phone."

    Jes "You're not becoming a teenager, are you?"
    Con "Heh. It's just some work stuff."

    scene day8 ev08-02
    Con "So, tell me about your day. Eventful?"

    if "d06defendingKevin" in choices:
        JesT "I might have gotten a picture of your car. I really hope you're not lying to me Conner."

    Jes "Well, it wasn't very busy."

    if "d08talkMayor" in choices:
        Jes "I had a chat with the mayor earlier."
        Con "Oh, cool. You're already mingling with important people."
        Jes "Yeah. It was fruitful talk."
        if "d08mayorTease" in choices:
            JesT "With some big fruit."
        Jes "Oh, by the way. I got invited to a fundraiser the mayor's having on Thursday."
        Jes "I still have to clear it with work, but these things are usually \"plus one\". You want to come?"
        Con "Well, mingling with politicians sound awful, but if you really want I'll go."
        Jes "Come on. You'll have fun."
        Con "Alright. For you, babe."
        Jes "Plus, there will be lots of influential people there. You could maybe get some help for the center."
        Con "That's true."

    else:
        Jes "I have an appointment to talk to the mayor's secretary."
        Jes "Lovely woman, and far more important to the mayor than I thought she was."
        Jes "It should be an interesting conversation."

    "They chat for a bit longer before Jessica gets up."
    Jes "I'm gonna check on Heather. See if we're going for a run tomorrow morning."
    Con "Okay. I'll be here."

    scene day8 ev08-03 with fade
    "Jessica knocks on Heather's door. There's no answer."
    "Used to entering without permission, she heads in anyway."
    Jes "Hello? Heather?"
    "There's no answer."
    Jes "At least I didn't walk in on them having fun in the living room again."

    scene day8 ev08-04
    "Wandering into the bedroom, she calls out for Heather again, and again receives no answer."
    JesT "The door was open. Someone should be home."

    if "d07firstLesbian" in choices:
        "Her eyes fall on the bed, and she tries to block the view of it."
        "Emotions war in her chest, shame and pleasure vying for dominance."
        "I really shouldn't be in here right now."

    scene day8 ev08-05
    "The bathroom door opens, making Jessica jump. Christian emerges, drying his hair."
    Chris "Hey, darling."
    JesT "Oh my god! I really need to stop coming in here uninvited."

    scene day8 ev08-06
    Chris "Oh, Jessica. How's it going?"
    "Jessica turns away, burning with shame."
    JesT "How is he not embarrassed at all?!"
    Chris "Did Heather let you in? Is she home yet?"
    Jes "Oh, no, I'm- I'm sorry. I- I kinda let myself in."
    "He gives a heavy laugh."
    Chris "It's no problem. You're always welcome."
    Jes "Is, uh… is Heather here?"
    Chris "No, she hasn't come from work yet."

    scene day8 ev08-07
    "She hears him come closer, and turns."
    JesT "Okay, he has to have covered himself with that towel OH MY GOD HIS DICK'S STILL OUT!"
    JesT "Don't look at it don't look at it don't look at it!"
    Jes "Arrrre you going to cover yourself?"
    Chris "I don't know why I would. It's my place."
    Jes "Okay. I'll just be leaving now."

    scene day8 ev08-08
    "She moves to leave, but Christian casually puts his hand between her and the door."
    Chris "Before you go, we should talk a bit."
    Jes "Uh… about?"
    Chris "Well, I heard you've been having some fun with my wife."
    Jes "Fun?"
    Chris "Yep. I heard my wife's being giving you some oral advice."

    if "d053some" in choices:
        Chris "And then both you and Conner enjoyed some quality time with her."

    if "d05heatherLesson" in choices and "d053some" not in choices:
        Chris "And then she even went down on you."

    Jes "Yeah. I guess we did."
    Chris "Well, you chose the wrong neighbor, you know?"
    "Jessica suddenly feels worried."
    JesT "Oh my god! Heather said it would be okay! What do I say?!"
    Chris "After all, my wife may have a pussy, but I'm the one who knows how to make it feel good."
    Jes "What?"
    Chris "You should have asked me. I could have shown you how a man should use his tongue."
    "For a brief moment, Jessica is relieved. He's not angry after all."
    "Then the meaning of his words sink in."
    JesT "Is… is he offering what I think he is?"

    menu:
        "Move away from him":
            $ choices.append("d08chrisNoFlirt")
            JesT "Sorry, neighbour, but I'm not interested."

            scene day8 ev08-09
            "Jessica moves away, putting some distance between the two of them."
            JesT "Come on, Jess. Look him in the eyes, not his dick."
            Jes "I think I'm okay. Heather gave me what I needed."

            scene day8 ev08-10
            Chris "You're hurting my feelings, Jessica. But the offer's still on the table."
            JesT "Damnit! I looked at it! Eyes up, Jessica!"
            Jes "That's okay. I'm good. I've made my choice."
            "The sound of the front door opening sends a shiver up Jessica's spine and makes her go stiff. Christian, on the other hand, seems perfectly fine."
            Chris "Well, if you two ever want to learn how to do it properly, you only have to ask."

            scene day8 ev08-11
            Heath "Hey baby. I've had the shittiest… Oh. Jessica. You're here."
            Chris "Yep. She came in looking for you."
            Heath "And you found Christian instead. Were you two having fun without me?"
            JesT "Wow. These two really are perfectly comfortable with their open marriage."
            Jes "Nothing like that. We were just talking… and he just doesn't have any clothes on."
            Chris "Just having a heart-to-heart."
            Heath "Well, it's not fair when one person is clothed."
            Jes "You're right. We should do this again sometime, but with clothes on."
            "Heather nods, then pats her husband on the shoulder."
            Heath "Get dressed, you. Jess, you want to come out into the living room?"
            Jes "Yes please."

        "Stay":
            $ choices.append("d08chrisFlirt")
            $ relChristian += 1
            $ slut += 1
            JesT "This is an awkward way to talk with someone."
            JesT "Still, he's… such a handsome man. And so comfortable with himself."

            scene day8 ev08-17
            "Despite her trepidation, Jessica stays were she is, even as Christian moves a little closer."
            JesT "His dick is right there, hanging behind my ass. I can almost feel it against me."
            JesT "My heart's beating so fast. Having him this close feels so wrong, but so nice too."
            JesT "Of course, he's playing with me. I wonder how he thinks I'm going to react."
            Jes "I didn't know there was another offer on the table."
            "His finger gently brushes along down her bicep, sending a tingle up her arm."
            Chris "My offer was always on display. You only had to ask."
            Jes "Yeah, I can see that you're not one to hide things."

            scene day8 ev08-18
            "He moves even closer, pulling her toward him."
            "She can feel his growing erection pushing into her butt."

            if "d08mayorGrope" in choices:
                JesT "Two men pushing their dicks against my ass in one day. I must be lucky."

            Chris "It's not too late for a proper lesson."
            Jes "I kind of doubt Conner would be okay with me switching teachers."
            Chris "I'm sure you can convince him. I bet you can convince any man of anything."
            "She can feel him getting harder, his cock pressing firmly into her ass."

            scene day8 ev08-19
            "Taking advance to her distraction, Christian reaches around and gropes her breast."
            Chris "What man could resist a body like this?"
            JesT "I should put a stop to this, but damn it feels nice."
            JesT "He's rough, but that good level of rough."
            Chris "And if Conner doesn't like it, I can always give you a private lesson."
            Jes "That's not proper student/teacher behavior."
            "He's already rock-hard, his dick practically assaulting her ass. His hips are moving back and forth, thrusting gently against her."
            "Just as she's about to speak, she hears the front door open. Panic fills her chest, and she quickly pulls away from him."

            scene day8 ev08-20a
            "She turns to face him, just before Heather walks in."
            "Heather's eyes light up with surprise, then amusement, a wry smile playing across her lips."
            Heath "Hey, you two. Having fun?"
            JesT "I guess Heather really doesn't mind Christian fucking other women."
            Jes "Hey. I, uh, came looking for you, actually. Christian's been trying to convince me I need a new teacher."

            scene day8 ev08-20b with dissolve
            "Heather glances down at her husband's dick."
            Heath "He sure has his moments."
            Chris "It doesn't need to be a competition. We can all work together."

            scene day8 ev08-20a with dissolve
            "Heather turns her gaze back to Jessica, giving a quizzical look."
            Jes "I… should go. Conner's waiting for me."
            "Heather nods, then pats her husband on the shoulder."
            Heath "Get dressed, you. I'll walk you out, Jess."

    scene day8 ev08-12
    "The two head out, leaving behind a disappointed Christian."
    Heath "I hope he didn't embarrass you."
    Jes "Well, it was an interesting experience."
    Heath "Anyway, did you want to talk about something?"
    Jes "I just wanted to check in, see if we're still going for our jog tomorrow."

    if "d07firstLesbian" in choices:
        scene day8 ev08-14
        "No sooner have they moved behind the column then Heather pushes Jessica gently against the wall."
        "She leans close, whispering softly."
        Heath "Last night was wonderful."
        Jes "Yes, it was."
        Heath "So… you want to get together like that again?"
        Jes "Maybe."

        scene day8 ev08-15
        "Their lips come together in a passionate embrace."
        "Jessica closes her eyes, once again being drawn into Heather's sensual touch."

        if "d08blakeKiss" in choices:
            JesT "God, I love kissing girls. It's so fucking amazing!"
            JesT "And Heather's so different from Blake. Blake is almost submissive, and wants to be guided."
            JesT "Heather's so domineering, and makes me want to do whatever she says."

        "As they continue, Heather's hand slips onto Jessica's hip and down her pants."
        "Soon Heather's fingers are moving underneath the panties, gently caressing the flesh on the side of Jessica's leg."

        scene day8 ev08-16
        Heath "I can't wait to get you all sweaty tomorrow."
        "Jessica moans at the thought, as well as the feeling of Heather's warm breath and gentle touch on her body."
        Heath "I meant our run."
        Jes "Oh. Right. I can't wait."
        Jes "Well, I should… um, get going."
        Heath "Bye Jess."
        "Jessica heads out, trying to compose herself and wiping any errant lipstick from her mouth."

    else:
        scene day8 ev08-13
        Heath "Definitely. By the way, I had a lot of fun last night. It was nice to have a ladies' night out for once."
        Jes "It was. Um… does Christian know about the guy at the bar?"
        Heath "Yep. I told him about it this morning."
        Jes "That's so… I mean, how do you do that? Just tell your husband, \"by the way, I fucked some guy last night\"?"
        "Heather shrugs."
        Heath "That's how it works. Admittedly, those random hookups aren't as exciting as they used to be."
        Heath "A night with a couple I know, people I trust, that's so much more interesting."
        JesT "Yeah, I get the hint."
        Jes "Alright, I'm gonna head home. I'll see you tomorrow morning. Bye!"
        Heath "Good night, Jess."

    scene day8 ev09-01 with fade
    if "d08chrisNoFlirt" in choices:
        "Jessica strolls back inside, her eyes gazing off into the distance."
        JesT "Those two are something. It turns out Christian is just as brazen as Heather."
        JesT "I guess he's not a fan of subtlety, though."
        JesT "I can't say I blame him, with a dick like that."
        JesT "Oh, stop it, Jess. Get your mind off his dick… and how big and thick it was."
    else:
        "Jessica strolls back inside, a mischievous smile on her face."
        JesT "Those two are something. It turns out Christian is just as brazen as Heather."
        JesT "I guess he's not a fan of subtlety, though. Not that I'm complaining."
        JesT "With a dick like that, why would he be? That beautiful, hard cock."
        JesT "Mmm, maybe I should get Christian and his dick off my mind for now."

    scene day8 ev09-02
    "Conner is in the kitchen, cooking. At the sight of him, she starts thinking about his dick instead."
    JesT "Speaking of big, thick cocks…"
    JesT "I wonder if he's in the mood."

    menu:
        "Have some fun with him":
            $ choices.append("d08connerFun")
            $ relCon += 1
            JesT "Oh, please be in the mood Conner. I really need someone inside me right now."
            jump day08funDinner

        "Maybe after dinner":
            $ relCon -= 1
            JesT "Eh. Now that I think about it, I'm kind of hungry. We can eat, then have fun afterward."

            jump day08casualDinner

label day08funDinner:

    scene day8 ev09-10 with fade
    Jes "Mmm."
    Con "Oh. Hey there."
    Jes "Hey you. How's it going?"
    Con "Good. Just making dinner."
    Jes "So I see. Have I ever told you how attractive it makes you when you cook?"
    "He shrugs."
    Con "Once or twice."

    scene day8 ev09-11
    "She kisses the back of his neck while her hands slips down his pants."
    Jes "I do love a man who can cook."
    Con "Oh, uh, okay. So, you're, uh…"
    Jes "Really in the mood, especially for such a beautiful man like you."
    "Her hand finds his growing erection, gently squeezing and stroking the shaft."

    scene day8 ev09-12
    "Jessica turns him around, getting on her knees and pulling down his pants."
    Jes "Come on, baby. Let me make you feel good."
    Con "Whoa. What's gotten into you?"
    JesT "Should I tell him I saw Christian naked? He might just flip out?"
    JesT "It's not like it's a big deal, though. It was just an accident."

    menu:
        "Tell him":
            $ choices.append("d08tellConner")
            Jes "Well… okay, so, I kind of just walked into Heather and Christian's place, and…"
            Jes "Christian was kind of… in the shower…"
            Con "Uh… okay."

            scene day8 ev09-13
            Jes "He thought I was his wife, and came out… naked."
            Con "Wait… you saw Christian naked?"
            Con "In… cluding his... dick?"

            scene day8 ev09-14
            "Jessica pulls out Conner's cock as he speaking, gently stroking it back and forth."
            Jes "I did. And suddenly I just… couldn't wait to get back here."
            Con "But… Um…"

            scene day8 ev09-15
            "With Jessica's hand going back and forth, he can't really seem to focus."
            Con "You, uh, got turned on by another man's dick?"
            Jes "Kind of, but all it did was make me want the one I have waiting for me at home."
            Jes "I needed to feel it in my fingers, and feel it deep inside me."

            scene day8 ev09-16
            Jes "And, of course, I wanted to taste it."
            "With his dick fully erect, she leans in and puts her lips around the tip, giving the head a big kiss."
            play voices x_bj_1 fadein 1 loop
            if persistent.pov == 1:
                scene day8 ev09-16mpov
            Con "Fuck yeah."
            Jes "Mmm."
            JesT "Too easy."

        "Don't tell him":
            Jes "I just really missed you today."
            "She giggles and brushes her hand over his penis."
            Jes "And this big guy. I wanted to show him how much I love him."

            scene day8 ev09-13
            Con "Well, he loves you too, sweetie."
            "She smiles, and continues to pull down his underwear until his growing erection pops out."

            scene day8 ev09-14
            "Taking it in her hand, she begins stroking it, slow and steady."
            "She looks up at Conner, locking eyes with him."
            Jes "Does that feel good, babe?"
            Con "Oh yeah. That feels really good."

            scene day8 ev09-15
            Jes "I can feel him throbbing in my hand."
            Jes "He's getting nice and big. I know what he wants."
            Con "He wants you to keep doing just what you're doing, baby."
            Jes "I will, then. And I might just start kissing him, too."

            scene day8 ev09-16
            "Seconds later, his cock is fully erect."
            "Jessica licks her lips, enjoying the sight of Conner's dick as hard and as big as it can get."
            if persistent.pov == 1:
                scene day8 ev09-16mpov
            "Leaning in, she puts her lips around the tip, giving the head a big kiss."
            play voices x_bj_1 fadein 1 loop
            Con "Fuck yeah."
            Jes "Mmm."

    scene day8 ev09-17
    "Jessica takes more in, letting his large dick stretch out her lips."
    "Her hand continues to stroke, her mouth sucking at his warm meat."
    "She's moaning loudly, feeling her nethers becoming warm and wet."

    if slut >= 18:
        JesT "I shouldn't be this turned on from seeing another man."
        JesT "But after seeing Christian's big dick, I almost can't help myself."
        "Driven wild by the thought of Christian's cock, she begins to work her head back and forth faster while sucking harder."
    stop voices fadeout 1

    scene day8 ev09-18
    play voices x_bj_3 fadein 1 loop
    "Eventually, Conner responds to her more primal actions. He puts one hand on his erection and the other on the back of her head."
    "He begins pumping into her mouth, meeting her forward thrusts with his own."
    if persistent.pov == 1:
        scene day8 ev09-18mpov
    Con "Fuck, that feel good."
    "Jessica smiles with her eyes, locking her gaze with his and giving him as horny a look as she can manage."

    scene day8 ev09-19
    "The thick member keeps smacking against the back of her throat while Jessica tries to get it as deep as possible."
    "She pulls Conner toward herself, gripping his ass for leverage."
    "It's more than a little rougher than she's used to, and it's getting a little harder to breathe, but she gets a hang of the rhythm quickly enough."
    "She manages to breathe through her nose when the cock is pulling out, allowing her to keep going."

    scene day8 ev09-20ani-00
    Con "Baby, that is so good. You're incredible."
    show d08ev09-20ani
    Jes "Mmm…"
    "Jessica's libido is skyrocketing, her need growing with each passing moment."
    "Seeing Conner's face contorted in pleasure make her want him all the more."
    JesT "I bet he's going to cum in buckets. I wonder if I'll even be able to swallow it all."
    JesT "Let's find out. You wanna give mama all that juice, big boy?"
    JesT "Let's see what you got!"
    hide d08ev09-20ani
    "She can hear Conner's breath going faster, his need to cum growing closer and closer."

    scene day8 ev09-21
    "Her desire to please Conner is tempered, however, by her own need for release."
    JesT "Oh my god, I need to get fucked right now!"
    if persistent.pov == 1:
        scene day8 ev09-21mpov
    JesT "I'm sure he's loving this, but I need a dick in my cunt!"
    "She keeps going for a small while, but as Conner moves toward his orgasm, she finally decides she can't wait any longer."
    stop voices fadeout 1

    scene day8 ev09-22
    "His eyes fly open, surprised when Jessica pulls his dick out of her mouth."
    "She smiles up at him, running the tip of his cock along her lips."
    Jes "I love you so much, baby."
    "She plants a kiss on his dick for emphasis."
    Jes "I want to feel your huge cock in my pussy. Give it to me, baby."
    "She begins furiously licking his dick, showing her aggressive desire."

    scene day8 ev09-23
    Con "Whatever you want, baby."
    "He grabs her, bodily throwing her over her shoulder."
    Jes "WHOA!"
    Con "Or what I want, actually."
    Con "I was about to cum, and you stopped. So now I have to fuck you HARD!"
    Jes "Ooh. Whatever you say, baby."

    scene day8 ev09-24 with fade
    "Conner pushes her against the couch and begins rubbing his cock through her butt."
    Con "You like that, huh? You want this big, thick dick inside you?"
    Jes "Oh yes! Give it to me, baby."
    play voices x_moaning_1 fadein 1 loop
    Con "Say please."
    "He gives her a light slap on her left cheek."
    Jes "Oh! Please, baby!"

    scene day8 ev09-25
    "Pulling down her pants, Conner keeps gently slapping her ass while sliding his dick up and down."
    Jes "Yeah! That feels nice!"
    Con "Yeah? You want more."
    JesT "I want more than that."
    stop voices fadeout 1
    Jes "Only if you do it harder."

    scene day8 ev09-26a
    "Conner pauses for a moment, taken aback by her words."
    "Tentatively, after pulling down her panties, he gives her a harder slap. The sound fills the room as a stinging sensation fills her bottom."
    play sound x_spank_1
    scene day8 ev09-26b with dissolve
    JesT "Oh, that's the stuff!"
    Jes "OOH! Yeah. Harder!"
    if "d08tellConner" in choices:
        Jes "I've been so bad! My ass needs to be punished! Hit it harder!"
    scene day8 ev09-26 with dissolve
    Con "Harder… what?"
    Jes "Harder please!"
    play sound x_spank_3
    scene day8 ev09-26b with dissolve
    "Conner grins and begins bringing his hand down even harder!"
    Jes "AH!"
    scene day8 ev09-26a with dissolve
    play sound x_spanks_1
    "Again and again his hand smacks Jessica’s bottom, stinging her ass with each and every strike."
    "Her body writhes in response to the pain, yet each impact also brings glorious pleasure."
    scene day8 ev09-26b with dissolve
    Jes "Mmm! Yeah! Yes, that's it!"
    if "d08tellConner" in choices:
        Jes "Punish me! I've been so naughty! I need you to punish me!"
    "He chuckles, slapping her harder, drawing louder cries of ecstasy."
    stop sound
    play sound x_spanks_2
    Jes "Yes! More! Slap me then fuck me!"
    stop sound fadeout 1

    scene day8 ev09-27
    Con "You want me to fuck this?"
    play voices x_moaning_1 fadein 1 loop
    "Extending two fingers, he plunges them into Jessica's sopping-wet cunt, drawing a gasp of surprise."
    "She begins squeezing her breast, enjoying how rough the sex is."
    Jes "Yes! Fuck me, baby!"
    Con "You want me to fuck this wet… sloppy… s- slutty pussy?"
    "Jessica is amused by his stumbling, finding it cute how unused to talking dirty he is."
    "She says nothing, though, and decides to play along."
    JesT "It's not like I know much about it either."
    Jes "Yes! Fuck my slutty pussy!"

    scene day8 ev09-28
    "He shoves his fingers deeper inside, drawing a moan of pleasure from Jessica, who bends over the couch to give him easier access."
    Jes "Yes! Oh, yes!"
    "She's practically squealing in delight, her womanhood desperately in need of release."

    if "d08tellConner" in choices:
        scene day8 ev09-29
        "He starts moving his fingers faster, pumping them in while Jessica moans and squeaks."
        Jes "Oh! Oh yes! Oh god!"
        Con "You like that, baby?"
        Jes "Fuck, that's good! Keep going! Just like that!"
        Con "Well, what about this?"
        "He slips his right thumb into her ass, letting it slowly sink in. The resistance of her tight, virgin hole isn't enough to stop the invasion of his finger."
        JesT "Oh my god! He's never done that before! It feels incredible!"

        scene day8 ev09-30
        Jes "AH! What are you doing?!"
        Con "What you asked for!"
        Con "Shut up and take your punishment!"
        "Jessica lets out a shuddering breath, both shocked and aroused by Conner's sudden dominance."
        Jes "Yes, baby! Please, punish me!"
        "He switches thumbs, putting his left in her ass and thrusting it in at the same time his fingers are pushing in below."
        if "d01naughtyVibe" in choices:
            JesT "God, I've done it a few times myself, but it had never felt that good."
        else:
            JesT "God, if I knew it would feel that good I would've tried it myself long ago."

        scene day8 ev09-31
        "With fingers pumping in and out of both her holes, Jessica is barely able to think."
        "Her mind is entirely consumed by pleasure, while the only sounds in the room are those of her moans and fingers thrusting into her soaking cunt."
        JesT "This is too fucking good! I love having him treat me so roughly!"
        JesT "And I can't believe how good having a thumb in my ass feels!"
        JesT "We should experiment a little more often, if it's going to be like this!"

        scene day8 ev09-32
        play sound x_spank_3
        "After a bit more finger-play, Conner gives her ass one more smack."
        "Then he takes his cock and begins rubbing the tip along her warm and wet lips, keeping his thumb in all the while."
        "Jessica keeps mewling, working her hips back and forth, trying to get him to stick it in."
        Jes "Please, baby. I need it."
        play sound x_spank_3
        "He gives her ass a hard smack, making her squeal."
        Con "Beg for it!"
        Jes "Please, Conner. Please, give me your cock! I need you to fuck me! Please!"
        stop voices fadeout 1

        scene day8 ev09-33
        play voices x_sex_1 fadein 1 loop
        "He starts pushing his dick inside, both of them moaning as it goes."
        Jes "Oh yes! Oh yes!"
        Con "Fuck, that's good. Mmm, you're so tight, baby."
        JesT "I feel even tighter since he's got his thumb in there, and it's making his dick rub every inch of me!"
        stop voices fadeout 1

    else:
        scene day8 ev09-29b
        "He starts moving his fingers faster, pumping them in while Jessica moans and squeaks."
        Jes "Oh! Oh yes! Oh god!"
        Con "You like that, baby?"
        Jes "Fuck, that's good! Keep going! Just like that!"

        scene day8 ev09-31
        "With fingers rapidly pumping into her pussy and her ass still stinging from being spanked, Jessica is barely able to think."
        "Her mind is entirely consumed by pleasure, while the only sounds in the room are those of her moans and fingers thrusting into her soaking cunt."
        JesT "This is too fucking good! I love having him treat me so roughly!"
        JesT "We should experiment a little more often, if it's going to be like this!"

        scene day8 ev09-32b
        play sound x_spank_3
        "After a bit more finger-play, Conner gives her ass one more smack."
        "Then he takes his cock and begins rubbing the tip along her warm and wet lips."
        "Jessica keeps mewling, working her hips back and forth, trying to get him to stick it in."
        Jes "Please, baby. I need it."
        play sound x_spank_3
        "He gives her ass a hard smack, making her squeal."
        Con "Beg for it!"
        Jes "Please, Conner. Please, give me your cock! I need you to fuck me! Please!"
        stop voices fadeout 1

        scene day8 ev09-33b
        play voices x_sex_1 fadein 1 loop
        "He starts pushing his dick inside, both of them moaning as it goes."
        Jes "Oh yes! Oh yes!"
        Con "Fuck, that's good. Mmm, you're so tight, baby."
        stop voices fadeout 1

    scene day8 ev09-34
    play voices x_sex_3 fadein 1 loop
    "Conner picks up speed, his body slapping into hers again and again."
    Con "You like that?"
    play sound x_spank_3
    "He gives her ass another slap."
    Con "You like that, little slut?"
    Jes "Yes! Yes, it's good! Harder! Harder!"

    if "d08tellConner" in choices:
        scene day8 ev09-35
        "Putting his leg up on the couch, Conner manages to thrust in with even greater force."
        "His cock begins slamming deep inside her, much to Jessica's continued pleasure."
        if persistent.pov == 1:
            scene day8 ev09-35mpov
        Jes "Yes, yes, yes!"
        "Making it even better, Conner slips his middle finger in her ass again."
        Jes "AH! YES!"

    else:
        scene day8 ev09-35b
        "Putting his leg up on the couch, Conner manages to thrust in with even greater force."
        if persistent.pov == 1:
            scene day8 ev09-35bmpov
        "His cock begins slamming deep inside her, much to Jessica's continued pleasure."
        Jes "Yes, yes, yes!"
    stop voices fadeout 1

    scene day8 ev09-36
    play voices x_sex_4 fadein 1 loop
    "Eventually, Conner leans down over Jessica."
    "He's thrusting into her harder and fast, his breaths coming faster."
    Con "I'm almost there, Jess."
    Jes "Me too! Ah! Keep going!"

    scene day8 ev09-37
    "His hands grip her sides tightly, pulling her back each time he thrusts forward."
    "His balls slap heavily against her clit, bringing Jessica ever closer to her swiftly approaching orgasm."

    scene day8 ev09-38ani-00
    "Jessica's body is going wild. Her cries of utter bliss fill the room."
    show d08ev09-38ani
    Jes "Conner! Ah! Conner, keep going!"
    "He pounds his cock hard into Jessica's tight pussy."
    "The sofa underneath them creaking from his powerful thrusts."
    "Her supple vaginal ring spasming constantly around the pillar of his shaft."
    Con "I'm gonna cum, baby!"
    Jes "Cum with me! Let's cum together!"
    hide d08ev09-38ani
    "Conner groans and Jessica screams as they both approach their inevitable climax."

    stop voices fadeout 1
    play voices x_sex_5 fadein 1
    if "d08tellConner" in choices:
        scene day8 ev09-39
        Con "Nngh!"
        Jes "Agh!"
        "Within moments, Jessica's body tenses and she cries out in ecstasy, the pleasure of her orgasm washing over her."
        "Conner groans, his cock thrusting inside rapidly as he cums as well, filling her with his warm juices."
        "His finger goes back into her ass, pushing in and out while they both experience bliss."

        scene day8 ev09-40
        "With both of them having cum, Jessica sighs and lets her body fall limp, her head collapsing onto the pillow."
        "Conner takes a moment to relax as well, letting his body come down from his orgasm."
        "For a few seconds, he keeps his finger inside Jessica's ass, pulling it out slowly."
        Jes "Ah."
        Con "Whoa. Whew."

    else:
        scene day8 ev09-39b
        Con "Nngh!"
        Jes "Agh!"
        "Within moments, Jessica's body tenses and she cries out in ecstasy, the pleasure of her orgasm washing over her."
        "Conner groans, his cock thrusting inside rapidly as he cums as well, filling her with his warm juices."

        scene day8 ev09-40b
        "With both of them having cum, Jessica sighs and lets her body fall limp, her head collapsing onto the pillow."
        "Conner takes a moment to relax as well, letting his body come down from his orgasm."
        Jes "Ah."
        Con "Whoa. Whew."

    scene day8 ev09-41
    "Both of them moan, taking long, deep breaths."
    stop voices fadeout 1
    Jes "Oh, baby. That was great."
    Con "Holy crap, it was. Whew."

    scene day8 ev09-42
    "Jessica flips around and sits on the edge of the couch."
    "Conner pulls her in, and the pair share a slow, romantic kiss."
    Con "So that wasn't too weird for you?"
    Jes "God no. Well, I mean…"
    Jes "It was a little, at first, but it was SOOO good."
    Jes "I should probably get up, though. Don't want to get stains all over the back of the couch."
    Con "That would make an interesting conversation starter next time your mom comes over."

    scene day8 ev09-43 with fade
    Con "Well, I should actually get back to cooking dinner."
    Jes "That'd be great. I'm starving!"
    "Jessica chuckles, then grabs her panties and pulls them back up."
    "She pauses before she pulls up her pants, though."

    if "d07firstLesbian" in choices:
        JesT "Hmm. I do feel a little bad about having such great sex after I was just kissing Heather, since she was the one who got me going in the first place."
        JesT "Is that weird? Maybe. Fun, though."

    elif slut >= 18:
        JesT "Hmm. I do feel a little bad about having such great sex after seeing another man's dick, since it was Christian that got me going in the first place."
        JesT "Is that weird? Maybe. Fun, though."

    scene day8 ev09-44 with fade
    "Again dressed, she strolls over to the kitchen, thinking as she goes."

    if "d06defendingKevin" in choices:
        JesT "Actually, this is the perfect chance to head to the garage."
        JesT "Conner's distracted with cooking. I have more than enough time to check out his car."
        Jes "Hey, I'm gonna run out to my scooter real quick. I want to make sure I turned the lights off."
        Con "Okay, babe. I'll finish up here."
        "She heads to the door. She hears Conner's phone ringing before she leaves, but pays it no mind."

        jump day08checkingCar

    else:
        JesT "I wonder if I can maybe get him to try some more new things."
        JesT "What, though? Like… whips and leather and stuff?"
        JesT "Not sure if I'd be into that. Ugh. I never did know much about the kinky stuff."
        Con "This won't take long. I just… Oh, hang on."
        "Conner's phone rings, and he heads over to grab it."

        scene day8 ev09-45
        Con "Hello. Mmm-hmm?"
        Con "Really? I'm kind of in the middle of dinner. Can any-?"
        Con "Ugh. Okay. I mean… Okay, fine. Alright. Later."
        Jes "What's going on?"

        scene day8 ev09-46
        Con "Uh… I've got to go for a bit. A friend needs some help. He's working the program, but a guy I know said he's headed to a bar. I'm gonna go get him, hopefully before he has a drink."
        Jes "Are you kidding?! You've been running around doing favors at night since you started working!"
        Con "I'm sorry, but there's no on else who can take care of it."
        Jes "For fuck's sake."

        scene day8 ev09-47
        "Conner heads over to give her a hug and a kiss."
        "She stays still and silent."
        Con "I'm sorry, babe. I'll make it up to you."
        JesT "He's been saying that a lot lately."
        "With a kiss on the cheek, Conner goes to change."
        "A few minutes later he grabs his coat and keys, then heads out."

        jump day08lonelyMeal

label day08casualDinner:

    scene day8 ev09-03 with fade
    "Stepping over to Conner, Jessica slides her hand along his back."
    Jes "I'm back, sweetie."
    Con "I hoped so. If it was a killer I heard come inside, I was going to be very upset."
    Jes "Hehe. You're silly."
    Con "Alright. Food's almost ready. I just need to cook the steaks."

    scene day8 ev09-04 with fade
    "Once their meal is ready, the pair sit down and chat about their day. Conner in particular goes into detail about what he did at work."
    "Jessica nods quietly, but finds it hard to keep pay attention."

    if "d06defendingKevin" in choices:
        JesT "My god, his work sounds boring. It's all paperwork and bureaucracy."
        JesT "Although, I wonder if he's just BSing me. Maybe the reason he can talk about it with such excitement is that he made it all up to hide what he really did today."
    else:
        JesT "My god, his work sounds boring. It's all paperwork and bureaucracy."
        JesT "I'm amazed he can talk about it with such passion."

    scene day8 ev09-05
    Con "So how about your work? How'd things go today?"
    Jes "Well, I stopped by a place the vigilante hit last night."

    if "d06defendingKevin" in choices:
        "Jessica takes careful note of his reaction, wondering if he'll reveal anything."

    Con "Ugh. You're worrying me being around that guy. He's probably pretty fuckin' dangerous."
    Jes "Look…,"
    Con "I know. I know. It's your job, and I know you can take care of yourself."
    Con "I just worry, is all."

    scene day8 ev09-06
    "She takes his hand, giving him a reassuring squeeze."
    Jes "I know, and I appreciate it. Don't worry. I'll stay safe."

    scene day8 ev09-07 with fade

    if "d06defendingKevin" in choices:
        "Conner gets up and gives her a kiss on the forehead. Afterward, he gathers up their plates and brings them over to the sink."
        JesT "While he's occupied with dishes, I could head out and take a look at his car."
        Jes "Hey, I think I may have left something out on Fireball. I'll be right back."
        Con "Sure thing, babe."

        jump day08checkingCar

    else:
        "Conner gets up and gives her a kiss on the forehead. Afterward, he starts to gather up their plates before Jessica stops him."
        Jes "Let me do dishes, sweetie. You cooked, after all."
        Con "Thanks, babe."

        scene day8 ev09-08
        "While Jessica is cleaning their plates, Conner's phone rings. He answers cheerfully."
        Con "Hey, what's up?"
        Con "Uh-huh. Uh-huh."
        Con "Seriously? Alright. I'll be right down."

        scene day8 ev09-09
        Jes "What? Where you going?"
        Con "I'm sorry. A friend of mine needs some help. He's working the program, but a guy I know said he's headed to a bar. I'm gonna go get him, hopefully before he has a drink."
        Jes "Are you kidding?! You've been running around doing favors at night since you started working!"
        Jes "Let someone else do it."
        Con "No one else can help right now. I need to go. Hopefully it won't take long."
        Jes "Oh, for fuck's sake."
        "Jessica throws up her hands while Conner goes to get his things."
        "Angry and frustrated, Jessica turns away and continues to clean up."
        "When Conner comes back out, he gives her a meek goodbye and heads out."

        jump day08lonely


label day08checkingCar:

    scene day8 ev09-49 with fade
    "Jessica's blood is pumping hot when she gets close to Conner's car, her heart hammering in her chest."
    JesT "Am I actually hoping that Conner's involved with all this?"
    JesT "Why would I think that?! That would be awful! So why am I almost expecting it?!"
    JesT "It's just the reporter in me, wanting to confirm my theory. Calm down, inner-sleuth.  You don't want your boyfriend involved."

    scene day8 ev09-50 with fade
    JesT "Okay, let's see. It's the same damn model, alright. Down to the last detail."
    "She holds up the camera, comparing the picture to Conner's car."
    "Strolling around it, she tries various angles, hoping to confirm some similarities or differences."

    scene day8 ev09-51
    JesT "Damnit. The picture's not good enough. I can't really see any of the details."
    JesT "It could be the same car, or not. I don't know. Damnit. Why couldn't the kid have had a better phone."
    JesT "Well, I tried. I'll just need to keep an eye. SOMEONE with this model was at the factory, and it'd be really nice to be able to rule him out."

    scene day8 ev09-52 with fade
    "Jessica heads back up, and finds Conner just inside with his jacket on."
    Jes "Hey. You going somewhere."
    Con "Yeah. A friend of mine just called and needs some help."
    Jes "... Huh. Um… why do you have to go?"
    Con "Sorry. No one else can help right now."
    "She sighs, crossing her arms and pouting."
    Con "I'm sorry, babe. I'll make it up to you."
    "With a peck on the cheek, Conner grabs his keys and heads out."

    if "d08connerFun" in choices:
        jump day08lonelyMeal
    else:
        jump day08lonely

label day08lonelyMeal:

    scene day8 ev09-48 with fade
    if "d06defendingKevin" in choices:
        "Jessica finishes the meal herself, then sits down to eat alone."
        JesT "This is getting to be a habit, and I'm pretty sick of it."
        JesT "I'm really starting to wonder why he's out late so much."
        JesT "And now I get to spend the evening all alone. Lovely."

    else:
        "Jessica finishes the meal herself, then sits down to eat alone."
        JesT "He couldn't at least finish cooking before he left?"
        JesT "And now I get to spend the evening alone. Lovely."

    if "d07firstLesbian" in choices:
        JesT "It's too late to invite Heather over. I wouldn't mind her company tonight."

label day08lonely:

    scene day8 ev09-53 with fade
    "With dinner done and after doing a few house chores, she takes a seat on the couch."
    "The TV is just noise, her thoughts drifting off to Conner and what he's up to."
    "Not to mention her own hurt feelings."
    "After a short while, she decides she just wants to go to sleep."

    scene day8 ev09-54 with fade
    "Lying in bed, her mind tries to put the pieces around the vigilante together."
    JesT "An empty factory making cell-phone parts. Is the company relevant, or did he just use the place since it's empty?"
    JesT "But if he got in, did he break in or does that mean someone gave him access? If so, who?"
    JesT "I know that cop knew more than she was letting on about the vigilante taking down that gang. And those guys watching knew something, too."
    if "d06defendingKevin" in choices:
        JesT "And I really hope Conner's not involved in any of this."
    JesT "Damnit. What they teach about investigative journalism is right. It's like doing a puzzle without the picture, and missing almost all the pieces."
    "She keeps trying to puzzle it all out, but her mind is tired and so she eventually just settles in."

    scene day8 ev09-55 with fade
    "A while later, she briefly wakes when she feels Conner climbs into bed with her, but she doesn't stir."
    "Still upset with him running out, she keeps her eyes closed and does her best to drift off back to sleep."

    jump day09
