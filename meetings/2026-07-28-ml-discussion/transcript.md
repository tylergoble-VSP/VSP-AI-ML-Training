# ML Discussion - Raw Meeting Transcript

**Date:** July 28, 2026

**Meeting:** ML discussion

**Attendees:**
- Vlad Damian
- Dorel Macra
- Marius Mazilu
- Tyler Goble

---

**Tyler Goble:** This kid didn't want to cooperate, so he's gonna have to learn how how to do machine learning. I'll s I'll drop it in psych real quick. Hey hey. Let me add your own to that too.

**Marius Mazilu:** Hello. Sorry for the delay.

**Tyler Goble:** All is well.

**Marius Mazilu:** Hello, how's everybody doing? How's Jet?

**Tyler Goble:** This young man said, You know what, Dad? I'm getting up at 5 30 this morning. There's nothing you can do about

**Marius Mazilu:** it.

**Tyler Goble:** I said. Roger that.

**Dorel Macra:** Oh, is it that he is not sleeping at this hour?

**Tyler Goble:** You would think that he would do that. However, he is uh like his dad very strong-willed.

**Dorel Macra:** Looks like

**Marius Mazilu:** all right. Dearly beloved, we are together here to have a look at the current state of the ML training uh and get Vlad's blessing and his input because because I think he has much bigger plans with us. Is that a fair assumption, Mr. Damian?

**Vlad Damian:** No, I need this group to uh think where we are and where we are going. I will provide my um need as the representative of Deliver.

**Marius Mazilu:** Yes, sir. Alright. Uh Tyler, I think this is your show. Do you have uh your current draft?

**Tyler Goble:** I do. I do. I draft it in a little group chat with all of us. Do you guys think would you like me to run through it right now? Take 10 minutes, do that, and then we can stop. feedback and all those kinds of things.

**Marius Mazilu:** Sounds good to me. Mm-hmm.

**Tyler Goble:** So the idea behind this and the intent is not to get people to even know how to run any of these algorithms. It's more to understand what's available as far as when people say machine learning, what different kinds of things can you do? And to distinguish it from like generative AI was my main intent behind this. And so smart enough to talk with a client, ask the right next question. You do not need to learn to build the robots. It's fine. You don't need to. This is more like the executive slash like EM training. And so when someone says AI, they usually mean one of two things. They either mean like chat GPT or they're talking about like, I want a predictive algorithm. Oftentimes, when they're talking about AI, you'll hear words like, I want to know. Um, like, I want to know is this person going to convert, or what's the actual value of this um this house? That's usually more machine learning. If they're saying I want to. to um like reason about something or I want to have a conversation, that's Chat GPT. And so machine learning inside of machine learning, you have deep learning and you have inside of deep learning the generative AI. And so it's kind of like a nesting doll, but machine learning is the overarching like discipline that contains all this stuff. And so machine learning is is different in that it's not um it's similar to generative AI in that it's not always gonna give you this exact same answer. So there's some inherent randomness inside of that, um, which is why when you're doing machine learning, you need to have a um you need to have an understanding of some basic statistics so that you can know how reliable the answer is. Um there's a saying that goes like all models are useful or all models are wrong, some are useful. That is like a very true statement when you're talking about machine learning. Um some key keywords down here, deterministic, it means if I do two plus two, I know it's always going to equal four. Probabilistic is um a guess with a confidence attached to it. So if I say I'm looking at Vlad and I'm looking at Durrell and understanding a little bit about them, I could say with 95% certainty, they've probably had 24 years worth of school together. Like school years. That is going to be a probabilistic guess because I'm not actually measuring directly what you're doing. I'm like making a guess about how many years of school you guys have. And I'm 95% certain that you actually have that many years of school. Maybe not a great example, but um stochastic is another buzzword. Stochastic is just like randomness. So that means that there's randomness involved. Okay. Machine learning. basically, there's like five different things that I decided to talk through. Um it's really good at finding patterns and numbers. And so it can sort things, it can group things, it can guess a number, it can give the odds, and it can pick the next move. Um and so an example there is like in a sales, a sales world. If you're wanting to understand if this person is going to convert to a buyer, you could make a machine learning algorithm that's going to sort them into buyers or sellers, or buyers or not buyers. You could um guess the amount of money that that person's gonna spend, you could give the the odds of that person being likely to close. Um you could pick the next best move to do with that person in order to try to get them to that preferred outcome. Um and so when you hear sorting it, that's a classification algorithm. When you hear clustering or grouping it, that's a clustering algorithm. If you're guessing a number that's regression. If you're giving the odds propensity and then picking the next move is a recommender algorithm.

**Marius Mazilu:** So can can we uh give a more of a high level on this let's we're going this basically goes through it, right? Grouping uh so let's so I'll

**Tyler Goble:** go a little faster.

**Marius Mazilu:** All right.

**Tyler Goble:** Yeah, so here's the visualization of grouping it. Here's something sorting it. Here's the names of the models for um bunch of different use cases. Modern models that find patterns on their own. The different ways that you could see answers from a model. This is the different ways that you can measure the actual effectiveness. of an algorithm? So like mean absolute error. This is the average miss in real units. Um it's more stuff.

**Marius Mazilu:** So go

**Tyler Goble:** no, yeah, go ahead.

**Marius Mazilu:** No, no, keep keep going. So we have uh this uh the grading, all right. We can have a look of so the purpose here of Vlad, this is the high level one, this is the first stage, right? We go through this as uh training. This this is what I understood through DML literacy, and after this, if we want to go deeper, we can go deeper into each of these uh pieces. Is it what you're expecting?

**Vlad Damian:** No.

**Marius Mazilu:** Well, then I failed.

**Vlad Damian:** Well, try harder.

**Dorel Macra:** Let's uh what about if starting with the agenda?

**Vlad Damian:** Yes.

**Dorel Macra:** To have an overview over the thing.

**Vlad Damian:** Yeah, that is what I want. That's what Bonich wants, and that's why he's keeping my feet to the fire and he's giving me uh headbuts. I need a list of items, I need modules, submodules, tasks, exams, I need a core. course that stands for whatever time period we want or we choose. I need responsibles for each course. I need deadlines to be able to present to the farm team what are we actually going to do to step up our game in being able to talk to the customer about ML and look intelligent. Talk to the customer about LLM based solutions and look intelligent. Talk to the customer about agent systems and look intelligent. Tyler to cross the street. This is how I feel. So we can't hold we cannot stand right, upright right now without the help of Tyler. I need to be able to stand up upright first, then maybe to take a few steps, then maybe walk at a brisk brisk uh pace. I'm not the desire is not necessarily to run a marathon, but to be able to walk at a brisk pace. I would call it a success if we are able to do that. I do not expect it to happen within two or three sessions. I expect this to be a a program um where some of the people that enlist in this this program are in it for the whole program. Or some of them will say, okay, I'm good enough for my level. I know enough to be able to do my job better than I did before. I'm fine. Some others, no, I want to see the echo. Show me the code. Show me the exercise. Teach me how to use it in production. Teach me how more details and so on and so forth. Give me biography, what do I have to read? Test me. It's a program. And it's a recycling program for uh starting with sales engineers and finishing up with technical leads developers.

**Marius Mazilu:** Alright. So that is uh so when I when I talked to Tyler about this, uh I only went for the high level. I'm assuming we can take this, what Tyler has now, and we break this because it has most of the uh individual pieces, we can break this into the course itself. Does that make sense?

**Tyler Goble:** Would you almost consider maybe Vlad this is a table of contents slide deck? Like this is what's going to be covered inside of the the course. I could reframe it in

**Vlad Damian:** that way. This can be a nice uh presentation alongside the table of contents. What I'm expecting is literally. a table, an Excel, where I have uh and it doesn't have to be perfect, we have to work on it. But we have to have the list, uh, it has to be as exhaustive as as possible. We need to have duration to each lesson and responsible for each lesson.

**Tyler Goble:** Do you want me to literally go get my master's coursework and adapt it?

**Vlad Damian:** Whatever you feel uh uh would be appropriate for what I need.

**Tyler Goble:** I

**Vlad Damian:** can give you more details about how I see the need if you want, but yeah. Absolutely. For me it's it's like a course on uh on us being more capable on machine learning, but extremely capable with with that being said, extremely capable on agentic systems development. So I I need to be able to speak intelligently about ML. I need to be able to be uh an expert in a building production grade agency systems. So would you

**Tyler Goble:** would you say the focus should be more on on agents? than it should be on ML.

**Vlad Damian:** Yeah. So the the desire is to have a basic understanding of ML, be able to uh start up a Jupyter notebook and take that uh I always forget how it's called that thing with the numbers, that source data source, do that classical uh exercise, use uh PyTorch as a classical uh uh to do some examples. And if we choose, because we are the group who chooses what the curriculum should be, if we choose, we just paint it uh say for further. uh going deeper go uh use this uh course or look at this jupyter notebook collection of jupiter notebooks etc etc and then you move on to agentic we move on to adjecting systems in production at the end again the point is to be able to when the customer says and they say I don't know about reinforcement learning uh stochastic stuff you just said to be able to have a conversation I do not think that we will be interested in doing ML work uh alone but we need to be able to speak about it I do think we will be tasked to do agentic systems. So the yes, absolutely the uh the lion's share should be agentic system. And by that I mean uh frameworks, uh harnesses, evaluation frameworks. It's an entire space out there that is not just Langchain or Langgraph or LangSmith or Haystack, uh what GCP offers, what Bedrock offers, what Azure offers, etc. etc. All of this stuff has to be here.

**Tyler Goble:** That's a big

**Vlad Damian:** uh

**Tyler Goble:** big L.

**Vlad Damian:** It's a fucking program. And I need to have uh all of this listed. Uh and uh how many hours do we want to spend per item? Use best judgment, of course. I need to have maybe uh, like I said, not maybe for sure, homework, uh study, etc. etc. It doesn't have to be one person. I do not expect it to be one person. No way. Uh I expect it to be uh six months to one year. And of course, you are able to do something after a month, you're able to do a little bit more after two months. So I cannot go to Bonich and say, hey man, uh cool your beer

**Tyler Goble:** for now.

**Vlad Damian:** For yeah, we'll see each other for an Ever. I will be promptly fired. But in order to reach that uh uh level of expertise that I want to reach, uh it doesn't have to be in one single person. Maybe somebody knows Azure, maybe somebody knows Bad Rock. I don't know. All right, WS. We need to have all of this, and it's a journey. Will this include the doctor? That is I I will shut up after this. I'm sorry, Dorel. And I need to have a roadmap which is curated by people who know what we're doing, they're doing because right. now we are in analysis paralysis I am in analysis paralysis and I'm running around headless chicken mode sorry

**Dorel Macra:** I wanted to touch base on the agents in production topic uh if that's separate or is part of this

**Vlad Damian:** it's part of this let me share my screen and let me uh start how I'm seeing it um what the heck am I doing What is it drive? Okay. There you go. So this one

**Tyler Goble:** this that one training like I'm talking back in like January that that one dude came and ran? Do you remember that?

**Vlad Damian:** I do. I absolutely do. That is part of the thing. Absolutely. It is. So I see it ML literacy. LLM literacy. Agentic system. Literacy. These are like this. Can be uh I'm I'm I did not prepare this. This is just to close from my head right now. Um

**Tyler Goble:** Do you have these specific projects where people have asked us to do this stuff that you've been like triggered you of maybe that would be helpful?

**Vlad Damian:** Mm-hmm. Mm-hmm. Yeah, yeah. So these are this is a module, sub module. I don't know, lesson. I have no idea. Uh time responsible.

**Tyler Goble:** Okay. So if you want this can be actually the first. module, and it's called basics. Okay, this one

**Vlad Damian:** takes, I have no idea. Let's say a month. Yeah. Then advanced blah blah blah. Expert. Blah blah blah blah. Now for ML literacy, you start putting in the lessons, or we can break them down as you will. You put in breaking down. Yeah. What is it? Uh para pa para. And then literacy. The same. This is what I'm expecting. So after complete completing any of these modules, you are one step closer to advanced submodules. You are one step closer to the advanced module. Then you start the advanced module. Completing it, you're one step closer to the expert. This this advanced takes three months. This expert takes six months. And it's a lot. So for example, for experts, to be very clear, it's about to self study. Study about evaluation frameworks. Like, I don't know, I see. Yeah.

**Tyler Goble:** Where where my brain's going is Stanford releases really, really good YouTube coursework for all this stuff. Just literally ripping that off and deciding that as companions. I've taught courses at um college here where like I would basically just talk for an hour and then I would say you need to watch this whole thing and do what they're doing here. Does that work?

**Vlad Damian:** Absolutely. Absolutely. So we are not talking about kids. I don't need a lot of hand holding. I need more than uh anything direction. Hey, you motherfucker. This is how this course is gonna be structured. It is structured based on our understanding of uh a good way to ingest all of this. Uh we are going to point you to an inordinate amount of resources that will only increase as you progress from basic to advanced to expert. So, for example, for expert, read book. But we need to it has to be to be curated. So that's the value, you know. So for expertise, just free book, do that, bring it to production, put chaos monkey on it and see what's happening. And then feedback into the advanced or maybe the basic. You know, this shit here feeds. So Tyler, you're maybe doing some of the work here. You know what I mean? Well, I don't know. Stefana is doing some of the work here and is feeding maybe another item that we want to put on the advanced roster. This is education that never stops for the foreseeable future. But for me, these are the things that I want to, and I put it intentionally until here. Like this is my dream that maybe I can reach here. And I have enough until I reach here that I can walk at a brisk pace, as I've said it. I cannot run. I don't want necessarily to run, but I want to be able to discern what is complicated, what is doable, how to approach it, what resources to use. That's what I uh need. need uh like at least 10 people to attend this stuff and to be committed. Right now, the only people I have are Tyler, Stefana, who is I want to say an intermediate, and Loli, who has to stay uh uh in his brevo uh enclosure. That's all I know. That is uh that's my problem, and uh more and more I see, and Tyler, you know this better than than I do, uh all of them require uh this shit. I mean all of them being uh um customers and there's nobody I mean and common who has done a reg system and it's in production for meetings that by the way reg is here somewhere

**Tyler Goble:** yeah that's right

**Vlad Damian:** you know

**Tyler Goble:** no

**Vlad Damian:** it's it it's in basic yeah exactly now rag with uh grasp uh mumbo jumbo maybe you we decide that it is the first one in advance so my my my approach, but this is completely up for debate, guys. My approach is I want to be I would much rather be well rounded, equally well rounded, and then inflate and inflate and inflate than to have spikes. Um so out of the basics, I should be a little deform thier, and then I get more and more bigger and and modular. That's my approach.

**Tyler Goble:** Question my lord. What level of person are we putting through these? Is this like intermediate?

**Vlad Damian:** This

**Tyler Goble:** is juniors.

**Vlad Damian:** No, these are seniors and tiers.

**Tyler Goble:** and TLs. Okay.

**Vlad Damian:** Yes. So this all of this, the purpose is to bring to engineers who are accustomed to bring stuff into production to deliver production ready systems to bring in their hands this capability as well. Out of the basics, for example, they do the first two submodules. Well I'm evaluating with first I don't know maybe however some so they do the first the 30% yeah they should have a better understanding when Stefana talks when you talk. Like okay I know what to expect from a ML guy I know what to expect from a guy who develops an agentic system. I know to ask about observability, I know to ask about reliability, I know to ask about uh whatever KPIs I need to have. I need to ask about the hardware requirements, cost, and to have the conversation with to fill in the gaps, which of course the ML will have, the ML engineer will have in bringing up the uh thing to production. What I've observed, and I've observed it in six map, there is this divide, which is I think it's only natural. Where on one side, you and Stefana would speak a language. and on the other side, these guys would speak another language, and stuff would be lost in translation. You need to close this gap. This is what I'm trying to do. And I cannot ask you to close it. Uh like you guys learn more about bringing shit into production. It's illogical to do that. That's the purpose of basics. And of course, to be able to do three sets and so on. Advanced, it speaks for itself. That's expert again.

**Tyler Goble:** Are we imagining that regardless this is not a um pick and choose menu? You're gonna do everything. in basics if you're getting enrolled in basics.

**Vlad Damian:** I would agree, yes. I I would say yes, yes.

**Tyler Goble:** Oh I think that's the way I think the most important one is basics.

**Vlad Damian:** Yes.

**Tyler Goble:** To get correct. Because once you have basics they can self-educate to advance even if we don't have the

**Vlad Damian:** correct. Exactly. Yes, yes, yes, yes, yes. We may not as correct, exactly. I think that's what you're saying. So let's say I want advanced uh this one. Yeah? For example for me this is advanced. Who the fuck knows about I don't even know how to say it. AISI. Did anybody on this call ever heard exactly? Nobody fucking heard of it. I learned about it literally 10 minutes before this call. The fact this is go and learn it. There is something here. It's clear there is something here. You know? And then maybe some of it, uh what we learned here pickles down into basics. Or the first item on advanced.

**Tyler Goble:** Um talk to me a little bit about what you envisioned as getting delivered by. like like the wave of magic wand and this is how the people are receiving the information and this how we're validating what they're doing.

**Vlad Damian:** Um my stupid idiot

**Tyler Goble:** I don't know if you have enough tabs open. I do I have enough. Um talk to you about family I'm more curious of like medium. Like do you really do you want to literally make a GitHub mono repo that holds all this stuff and we do it that way.

**Marius Mazilu:** I think for now it's just the course, right?

**Vlad Damian:** It should have support. Yeah, so each lesson has support material. Which can be all sorts of multimodal stuff.

**Tyler Goble:** The lesson itself though walking through a PowerPoint? Slide deck.

**Vlad Damian:** Need uh in this world, I need the guide. I am lost without it. So right now, Mr. Tyler, Mr. Co Mr. Goble. Goble.

**Tyler Goble:** Goble.

**Vlad Damian:** No, seriously.

**Tyler Goble:** Goble.

**Vlad Damian:** Goble. Goble. I love him.

**Tyler Goble:** I love it. Mr. Pinkie out. We've got a slight aside. One of my um one of my good buddies is uh his name's David Thomas. But we call him Russell. And when he's being a D.Va, we call him Russell.

**Vlad Damian:** Mr. Goble. This AI and Dorel and Maurice is a piece of shit in a lot of ways. So I spent a couple of hours now discussing about hack the box opportunity with this idiot. And I don't know how yeah, I started from Exploit Gym, which I've heard about in my perusing of the internet. Yeah. And I'm saying how the fuck is would Exploit Gym play into this? And he says, well. really but maybe actually cyberbench side bench would fit better into it, which is by the way, on their freaking. Yeah. Until now, this idiot who say that. And then I reach the moment when I say, why not just take side bench code, make some minor adjustments, and you die blah blah blah. Honestly, and you reach AI SI. Oh, this is the best Marstrong. And I've asked it point blank. How would you uh freaking the uh devise the architecture for this thing? Why didn't why didn't it just say, well, use uh fork uh uh AISI? I don't know, it needs somebody to

**Tyler Goble:** it's not very quick. You need you need to get yes.

**Vlad Damian:** That correct, that's what I need here as well. So these are mature senior people, absolutely, that is the expectation. And they if they do not put in the work, they're out. But that's the discipline. disciplinary part. I mean, I will not we will not waste our time with people who will not put in the work. There will be like 10, 12 spots open. If you want to do it, you're in, you do the work, and you participate. This will be difficult. I think uh it will be difficult, it will be uh hard work. If you don't do it, you're out.

**Tyler Goble:** What um incentive other than being smarter do these folks have to do it?

**Vlad Damian:** To have to have a fucking job in one year.

**Tyler Goble:** Yeah.

**Vlad Damian:** I mean.

**Tyler Goble:** Yeah. I mean, is there anything else that we could we could do for them that makes it makes it the um because I've done this stuff before with with groups and usually the only people who actually latch on to truly doing this stuff. And again, this is like in the US government, so people have infinite job security. But the people who would actually do the work and like benefit from it would only be the people who probably would have just done it on their own if you gave them the time to do it on their own. Without incentives, because we didn't have incentives.

**Vlad Damian:** I hear you. And maybe it transforms the so maybe it's a lot of remote learning. I mean, I should say I think 90% should be remote learning or uh self-study. But I need the guidance. So I need to go to Bonich. Uh we told him that we have this meeting today. I think he's extremely distracted with other stuff. Maybe I can uh uh keeps him uh distracted because of six map Tyler, for example, uh a little bit uh more. Let's get the basics in. And again, it doesn't have to be exhaustive, but there has to there have to be there have to be like like I don't know, twenty lessons, something. And a duration, and at the end. so for the basics, um here something like goals. Yeah. You know what will you when you finish this guy, this module, what would you have learned? Okay, Mr. Dorel, you're uh quiet, and that uh scares me.

**Dorel Macra:** Because I will be or I hope I will be one of the trainees.

**Vlad Damian:** Me too. So our every director has to be part of this training. We are going to be asked more and more by Tyler and his uh friends to join pre-sales. Um for example, HTD. It is inherently a uh systems problem, which in other situations I would have been able to pretty much solve it or discuss very relaxed about it. Now I have to sprinkle on top this AI world. where I am completely assured of myself. I need this training to step on painting.

**Dorel Macra:** And during the training it will be great if um you know we'll connect the the lesson and the the topic to the problem in the real life that this thing will will uh will solve it. For example like we had uh that uh that prospect with uh you know taking a picture or a video of a construction site and decide if it is done or not. What do I need? Uh how how do we resolve that resolve with this and the other thing and the other thing

**Vlad Damian:** yeah you

**Tyler Goble:** know but is the is the nuclear options I literally come to Romania and we lock ourselves in a room for two weeks and we do this

**Vlad Damian:** it's absolutely a possibility to do basics for two weeks intensive training it is and then you give a bunch of uh homework and we revisit for another day or something uh or a couple of days yes it's absolutely a option

**Tyler Goble:** that that's like what I what I would do in my past life was like training people on Power BI and like data modeling, and I would just fly there for a week, and I would take their phones. I would lock their phones in the closet and I would just beat them to death with the computer for a week. And we would get a ton of stuff done. And I wouldn't let them talk to their and this is Marines, so I could do this. I wouldn't let them talk to anybody but me. And we would be locked in a closet for eight hours a day for a week. Um

**Vlad Damian:** it's absolutely an option. So this is the What you m call it the the curriculum. Don't know if it's double L or not. Um now it's the logistics. So there are multiple options. Option A, option A, war room. Tyler flies, flies, flies in um in intensive boot camp. Option B, blah blah blah. Yeah.

**Tyler Goble:** I would feel like we would want to do all the online work and then do like a hackathon.

**Vlad Damian:** I like it.

**Tyler Goble:** Maybe we maybe we couple couple the hackathon. I'm trying to like put dates in my brain to like just give us some goals. And I feel like maybe the week before Christmas or something like that. When things are things are always slow anyways. That's like the graduation ceremony slash we spend four days getting after it and then Friday's the show and tell and we do like a graduation.

**Vlad Damian:** But I really like the fact that we we do online work. I mean online training, individual work, and then we meet. I really like that. So, for example, the training with Andrei Chobanu was a pro was very good, but he was talking about not necessarily advanced stuff, but he was lost 90% of the audience within the first 20% of the course. Because not because he was, I don't know what kind of a genius or whatnot. No, because there was no prior work. put in by the the trainees

**Tyler Goble:** intentional prior work

**Vlad Damian:** you know

**Tyler Goble:** this is what we call scope creep Mozilla

**Marius Mazilu:** well this is actually a complete misunderstanding on my part which which Vlad will uh tell you about later

**Vlad Damian:** is it clear now Mazillo what we have to do

**Marius Mazilu:** yes so let's let's take this in uh

**Vlad Damian:** then take over please I'm popping the share, and you can uh take over.

**Marius Mazilu:** All right. So for now, uh, I think the next step is to have the curricula lay ready, right? Uh uh Tyler, you mentioned you have some uh some of the your old courses.

**Tyler Goble:** So, yeah, let me pull together um

**Marius Mazilu:** but like introduce.

**Tyler Goble:** Yeah,

**Marius Mazilu:** let's do just the Excel because we should go through that curricula together and just uh operate on the Excel at this stage, and then for each of the modules, we'll set up uh uh timeline session, prerequisites, things like that, and out outcome for each of them. Vlad, does that sound like a good plan to you? Do you need that early?

**Vlad Damian:** not deadline. I I'm I'm uh you were all in the call with Banich.

**Marius Mazilu:** Yes, yes. So Mr. Bonich

**Vlad Damian:** on Monday. So yeah. That

**Marius Mazilu:** was

**Vlad Damian:** yesterday. How yes, so how did a lot of things have happened already? How did that conversation between me and Marius go?

**Marius Mazilu:** It ended in the fact that uh after this call we'll give Mr. Banich a plan. So

**Vlad Damian:** no no no no. How did it go?

**Marius Mazilu:** Not well.

**Vlad Damian:** Did I got did I get annoyed?

**Marius Mazilu:** Yes, you did.

**Vlad Damian:** Did he get annoyed?

**Marius Mazilu:** Yes.

**Vlad Damian:** So that's why I'm being annoying right now, because this guy is up out to fuck me. And and he will succeed

**Marius Mazilu:** and the fucking goes uh downstream you know

**Tyler Goble:** i see i see multiple chefs involved or cooks as they say

**Vlad Damian:** he will catch me i i cannot outrun him and outrun him i cannot outlast him

**Marius Mazilu:** yes so uh deadlines uh tyler when can we get the first uh the chap at least the chapters ready i try to i did a small i use claude to do a small extraction right now it got me bait modules on what you have from uh your presentation i can be

**Vlad Damian:** this shed into claude the circle back uh it does it doesn't doesn't have to be perfect. Let's begin.

**Tyler Goble:** You know? I think if I if I'm gonna plan this the way I think it makes the most sense is let me go back to my um my academics. Let me pull their literal courses so they they can give me those those slide decks, those PowerPoints, and let me pull out how they structured it, because obviously like they're literally the professionals. Um and I know that there's a semester long or there's a quarter long course on like introduction to machine learning and like introduction to generative AI. And I may may I may actually know the guy who actually is runs those. So let me get that information together. Hopefully by the the end of today. I think I can get the actual slide decks. And then maybe by tomorrow I can I can give us a more structured look. Um

**Vlad Damian:** okay. So by the end of Wednesday, we should have at least for the basics. Skeleton. Okay. Okay. Maggie Larry taking the note for this?

**Marius Mazilu:** Yes.

**Vlad Damian:** And putting it in the document. Okay. for logistics. Who

**Tyler Goble:** small point of order?

**Vlad Damian:** Go ahead.

**Tyler Goble:** Do we want to cover statistics? Like basic statistics, because so much of this stuff is like you're not gonna really understand what's going on unless you understand some like fundamental math.

**Vlad Damian:** You are you are the expert, I think we should.

**Tyler Goble:** I would say yes.

**Vlad Damian:** Yeah. Then yes. And keep in mind the ML is not it's just enough ML to go through a pre sales. That's like what I want. So I I don't know, five percent of the whole thing, you know. to know what the neural network is, to know what the convolutional neural network is, to know what the fuck deep learning is, to know what reinforcement learning is, to be able to have a mini conversation about this shit and not look completely stupid. Yeah. Okay.

**Dorel Macra:** But still, not enough, at least for my taste, to to get a dictionary definition of it, and that's it.

**Vlad Damian:** No, no. No,

**Dorel Macra:** I will not remember it.

**Vlad Damian:** No. We've backed up by a little exercise. So I I absolutely want to use PyTorch or Teras or whatever you feel is it's the simplest one fire to do something to explain that it's all linear linear algebra to explain that we're doing some shape here to yeah so you know Andre I'm sure you know him Andre Carpassi has if you haven't looked at that uh you have to look at that guys he builds an LLM from scratch in like three or four hours,

**Tyler Goble:** yeah.

**Vlad Damian:** Um he uses a lot of mass, and you have to know you have to be able to follow him, not easy. easy. But he actually does that it's from scratch and he explains if you take your time, you would really understand everything that he's doing. Now I don't want that. But I want the spirit of that. If it makes sense

**Dorel Macra:** how you said he's called Andre.

**Vlad Damian:** Tarpasi. Uh Kappa R Y. Let's tell Luka he worked at uh uh freaking uh I think X anthropic Meta now I don't know where the heck he is

**Marius Mazilu:** all right uh coming back so

**Vlad Damian:** items.

**Marius Mazilu:** Yes. Uh by tomorrow, Tyler, you will have the initial curricula in the basic section. Is that

**Vlad Damian:** we said end of Wednesday?

**Marius Mazilu:** End of Wednesday. That's okay. End of so then uh on the 30th. I will set up a call on the 30th, then to uh uh go to the next uh section. So Vlad, in your right now, what are your priorities? The filling out the basics,

**Vlad Damian:** yes

**Marius Mazilu:** uh entirely with uh okay. So after that we will start scheduling the curricula for each of the lessons, support material and everything else, right? One by one.

**Vlad Damian:** Yeah. So I the the basics has to be fully fleshed out. Who does who uh hold the lessons? I would I don't think it's doable, unless you tell me otherwise, Tyler, that you keep all the lessons.

**Tyler Goble:** Yeah, I mean, I don't know that. Do we have anyone that knows knows this stuff?

**Vlad Damian:** Maybe we can have access to somebody, or we

**Tyler Goble:** I can call my friend and I can pull in some like people I know on my network that would be happy to just chat.

**Vlad Damian:** Okay, that would be interesting. Um, okay, yeah. So let's flesh out the the full content of basics duration for each element is very important. Uh put in the hackathon slash in-person stuff. I really like that. It gives some gravitas to the whole endeavor. Uh logistically speaking. Um yeah, I mean, putting in all these details is uh it will help us to make decisions from a logistical point of view, but let's see first. I would say what are the estimates. Basically, I need an estimate before I can allocate the resources against it. Yeah. And make sure to fill in the goals one will reach when he finishes basics. Good enough shit. Not that you oh I know how to do one plus one, what good is it for me? No, you should know how to add up quantities that are like 50 plus 20. So $50 plus $20 equals $70.

**Tyler Goble:** To me, what a basic would be is I can see the outputs of a model and I can interpret them.

**Vlad Damian:** For example, this

**Tyler Goble:** kind of where my brain goes initially is like I want to see what is each out which what does each model take in? What does it kick out, and how do you interpret?

**Vlad Damian:** Yeah. Yeah. How can I run my model locally? How can I train a model to do a simple task, a labeled task. Basic labeled task. So I know what it's actually possible. I know the limitations. That's also basics. You said that, for example, you said that some point is in and I I wrote it in the I saw you on the document for six map. I wrote it in the document. You said the I need data in order for the model. It was like a a truism, but it's the truth. It can only infer to say. certain point, discussion about that kind of limitation, things of that nature. Yeah, these are all basics. Advanced is like I said, I don't know what sexy hardness. I don't know what advanced, like you said before, advanced should be a lot about self-study.

**Tyler Goble:** Now

**Vlad Damian:** that we have given you the some tools, uh some capabilities, which are the but with you have the bugging means to go forth and flourish. Cool. Three minutes. Wonderful team creation. Yay. Okay. I'm out. Tyler. Uh if you have any any thoughts on that guys, leave me alone with Tyler. I want to talk about six map for a second. You guys. So the purpose of that document.
