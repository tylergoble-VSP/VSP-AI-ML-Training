# **AI interview discussion**

**Date**: Wednesday, January 21, 2026 at 9:00 AM  
 **Duration**: 26:11  
 **People**: Vlad Damian, Andrei Secea, Dorel Macra, Marius Mazilu, and Tyler Goble

#### **Action Items**

* \[ \] Tyler Goble \- **Create sample testing notebooks for AI interviews** Two tracks: one for generative AI, one for machine learning. Notebooks should include question sheets and qualify candidates for both Six Map and Faith Driven roles. Share at next call.

#### **Interview Materials (Anonymized)**

* Traditional ML Interview Section: [Interview/Machine_Learning/Traditional_ML_Interview_Section.md](Interview/Machine_Learning/Traditional_ML_Interview_Section.md)
* Generative AI Implementation Section: [Interview/Generative/Generative_AI_Implementation_Section.md](Interview/Generative/Generative_AI_Implementation_Section.md)

#### **Overview**

* Tyler will create interview materials for AI engineers including question sheets for two tracks (traditional ML and generative AI) and hands-on Jupyter notebooks with answer keys  
* Team identified two types of AI engineers: traditional ML engineers (predictive models, classification, clustering) and generative AI engineers (agents, RAG, chatbots)—candidates could fill one or both roles  
* Six Map project needs embedding models, generative models, and classifier algorithms while FDM needs embedding models, generative models, and clustering  
* Key assessment criteria is adaptability over framework rigidity—team wants candidates who understand fundamentals and logic rather than being locked into specific tools like LangChain  
* Team will share current developer interview questions with Tyler as baseline for creating AI-specific materials

#### **Two types of AI engineers**

* Tyler distinguished traditional ML engineers who build predictive models, classification models, and clustering algorithms from generative AI engineers who build agents and RAG systems  
* Traditional ML engineers are more classically trained and math/statistics heavy while generative AI engineers focus more on logic and business use cases  
* Generative AI engineers don't need to be as technical as ML engineers but need strong curiosity and understanding of fundamentals  
* Both types could be one person or separate people depending on the candidate

#### **Required skills for Six Map and FDM projects**

* Six Map requires embedding models, generative models, and classifier algorithms as the **three** main focus areas  
* FDM requires embedding models, generative models, and clustering algorithms  
* Tyler noted these requirements could expand as projects get deeper into implementation  
* Andrei confirmed both projects involve similar work: embedding stuff into models, orchestration, and ETL processes

#### **Assessing adaptability vs framework rigidity**

* Marius raised concern about candidates who only know recipes from docs versus truly understanding the tools  
* Tyler emphasized hiring people who are curious and understand logic and programming fundamentals regardless of language  
* Team wants to avoid candidates so rigid they only know LangChain and can't adapt when frameworks become irrelevant  
* Mathematics understanding matters significantly because models produce statistics that enable business decisions  
* AI-enabled development tools are getting very good at specific algorithm questions when developers ask the right questions

#### **Current developer interview process**

* Marius outlined the existing process: probe what candidates do in current role, dig into depth of understanding, test critical thinking on their playground, assess problem-solving with out-of-the-box questions, evaluate breadth of experience  
* System design assessment happens for technical leads  
* Interviewers grade each probed area on **one to five** scale to match candidates against job descriptions  
* Hands-on testing uses online code editors where candidates solve small problems while interviewers ask questions about the code being written  
* Marius showed example using Spring framework code to test whether candidates understand how Spring context and proxy work

#### **Proposed AI interview structure**

* Tyler will create **two** tracks: one for generative AI and one for machine learning, with question sheets for each  
* Hands-on portion will use premade Google Colab notebooks where candidates write code and make it run  
* Team will have answer keys that candidates don't see  
* Tyler's educational repo covers Python, ML (supervised/unsupervised/survival/reinforcement learning), and GenAI (embedding models and generative models)  
* Interview approach will walk through notebooks asking candidates to explain concepts in regular business terms  
* ML fundamentals to assess: knowing when to apply model types, what tests to run for accuracy, how to monitor models for drift over time  
* Tyler noted all models produce output but candidates need to know mathematical tests to verify models are actually appropriate to use  
* Team will hold follow-up meeting to review Tyler's materials before using them in actual interviews

# **AI interview discussion**

**Date**: Wednesday, January 21, 2026 at 9:00 AM  
 **Duration**: 26:11  
 **People**: Vlad Damian, Andrei Secea, Dorel Macra, Marius Mazilu, and Tyler Goble

\[0:01\] **Tyler Goble**: Right.

\[0:04\] **Marius Mazilu**: So I think

\[0:05\] **Dorel Macra**: I've sent in the the circle back because I think it's good to remember

\[0:09\] **Andrei Secea**: Oh, yeah.

\[0:10\] **Dorel Macra**: To have a summary.

\[0:12\] **Tyler Goble**: Alright. Perfect. Alright. So, guys, any thoughts on this? What outcomes are we wanting to get out of the AI people? That's the real question, I think. In the outcomes, in my mind, to maybe start that conversation is we need somebody who understands how to do models. And when I say models, I mean predictive models, classification models, association models, like clustering. That lives in the traditional machine learning realm, which is still part of AI.

\[0:47\] **Tyler Goble**: Then you have all the buzzword stuff, which is where I think most people talk a big game of generative AI, and that is talking about actually building agents, actually building those kinds of frameworks, and understanding the things that go into why you would do certain things there. To me, those could be two separate people. The person doing the machine learning stuff is more of your traditional AI engineer, which is, like, they've always existed since before, like, ChatGPT launched and became super popular.

\[1:25\] **Tyler Goble**: The generative AI person could be someone who's not necessarily as classically trained, but is just really curious and understands how to, like, build stuff. And those could be all one person as well, but that's kinda how I think about it.

\[1:43\] **Marius Mazilu**: I'm assuming we may need to assess both aspects of somebody. And depending on what we need them on, we should focus our questions and direct our tests towards that direction. Would it make sense, Tyler, maybe to since you're the leading expert here, to maybe start building a small spreadsheet with what we're looking for these two types of people and have maybe some thoughts there on how to how we get these what type of questions we put, what kind of tests we want to run, and how we drive those tests.

\[2:21\] **Tyler Goble**: Yeah. So I threw it in the chat. I'll share my screen real quick.

\[2:26\] **Andrei Secea**: To me, I I mean, I I know we need to start from somewhere, but also maybe not try to find the best. I think to me, we have FDM. We have six map. What it would need? What someone would need to be able to do this type of work? Because I'm looking I'm looking I'm I'm I'm thinking what's coming ahead of us. I think this type of work embedding stuff into a model, do some orchestration, right, that ETL part. I mean, those two projects are somehow similar. Right?

\[3:04\] **Tyler Goble**: They are.

\[3:05\] **Andrei Secea**: This is, I think, the type of work we would need to do mostly. And I think this would be a start. At least, that's how I'm seeing it.

\[3:15\] **Tyler Goble**: Mhmm. What I just kinda broke down in this foundations portion of this this repo, these are the different skills that in my mind if you if you say you're an AI engineer, you fall somewhere on the spectrum of understanding this stuff right here. Really not analytics performance, more like 11 through one here. So you're usually writing code in Python. You understand machine learning. And inside of machine learning, you know what supervised is, classifiers, unsupervised clustering, survival. And then on the generative side, you understand how to work with embedding models and generative models.

\[3:59\] **Tyler Goble**: And these are kinda built to walk you through what those skill sets are. And so maybe going through these, we could tease out questions as interview things to to identify competencies. Does that make sense?

\[4:13\] **Andrei Secea**: So one to three is programming. What we do? Four to nine is machine learning. Yep. And ten, eleven is GenAI? Yes. Okay.

\[4:27\] **Tyler Goble**: And then inside of that, I broke out more sections of specific types of algorithms inside of that.

\[4:38\] **Andrei Secea**: Okay. How much I I would go on the first. I think that that gives us a bit easy. How much of this unit, for example, for six map?

\[4:56\] **Tyler Goble**: So six map, these two things

\[5:00\] **Andrei Secea**: Mhmm.

\[5:01\] **Tyler Goble**: And classifier algorithms, I think, are gonna be the two or the three main

\[5:07\] **Andrei Secea**: Mhmm.

\[5:07\] **Tyler Goble**: Things that we're doing. Mhmm. However, that could explode as we get deeper into what they're doing.

\[5:14\] **Andrei Secea**: Of course.

\[5:15\] **Tyler Goble**: But I think from your first perspective, that's where I think we're gonna spend most of our time.

\[5:20\] **Andrei Secea**: Don't don't

\[5:23\] **Dorel Macra**: have the oh, is it on FDM side?

\[5:26\] **Tyler Goble**: FDM, I would say here and clustering.

\[5:31\] **Andrei Secea**: And clustering. Okay.

\[5:35\] **Tyler Goble**: Which clustering algorithms and classifier algorithms are kinda like cousins.

\[5:41\] **Andrei Secea**: Okay. And the others, like, I mean, unsupervised learning, survival analytics. I mean, even their naming, it looks it it to me, it sounds like there are some deep stuff over there, which I think is the next level. Right?

\[5:58\] **Tyler Goble**: Survival analysis, that's like I'm looking at churn for a SaaS company. I'm looking at what are the odds that this person's gonna cancel their subscription. Survival analysis is make making models to help predict, hey. We should be at a 5% churn according to our past data. If we go to 7%, we need to intervene as a business. Or if we're at 3%, we're doing better than we should be doing. We need to double down on whatever it is we're done. And you pull out reasons for why that stuff's happening inside those models.

\[6:30\] **Andrei Secea**: Alright. Got it. So it's actually okay. It's not about the necessarily the the the depth or the the an additional layer. It's it's more like a different business case. That's why I'm

\[6:43\] **Tyler Goble**: solve it. That's a really good way to frame it. So, like Right. Reinforcement learning, the way I structured these. And I'm still working on these as well. But, basically see if this is a good one. Yeah. Good to use when Mazilu's simple games. Mhmm. Like, each one of these breaks down for, like, why would you use it? When would you not use it?

\[7:18\] **Tyler Goble**: And I think that's kind of a key skill set for an AI engineer is you should have all these tools in your toolbox, and then you should be using your discretion to work with AI enabled coding environments. And so all this stuff was developed inside of Cursor.

\[7:34\] **Tyler Goble**: But the secret sauce is I know that you need to go through now and verify these reasons you would do certain things

\[7:44\] **Dorel Macra**: Mhmm.

\[7:45\] **Tyler Goble**: If that makes sense. Like unsupervised learning.

\[7:51\] **Andrei Secea**: I don't want to necessarily to to to blow this out of more promotions. What about seniorities here? I mean, is there less than a senior AI engineer here?

\[8:11\] **Tyler Goble**: I don't know.

\[8:12\] **Marius Mazilu**: So I think that's one of the issues. The other issue is what if they work with something else? How easy would it be for them to transition to what we need? Just like just like encoding. Right? They're working with the particular framework. We have a different framework, but I can't ask them to always be experts.

\[8:32\] **Marius Mazilu**: But if they're smart enough, they're good enough, we need to may be able to have the proper questions so we can figure that out, that they understand the tools that they're working with currently, and that they can move towards with what we need.

\[8:47\] **Tyler Goble**: I think the thing that's the most important is people that are curious and that are really understand logic and understand, like, fundamentals of of programming regardless of the language because these tools are so they're getting so good when you're actually the thing that these these AI enabled development tools are really good at is when you're asking them the real specific questions about these types of algorithms, they're nailing the actual logic that you should have and the test that you should run to make sure that those models are valid.

\[9:24\] **Tyler Goble**: And so maybe a little bit of a sidetrack, but, like, a mathematics understanding matters a lot for for these different models because that's really the fundamental thing that comes out of these models oftentimes is some sort of statistic that's enabling a decision for the business. And so to your question of, like, we need to just know that they're capable in the frameworks that they're working in and adaptable to take on the new frameworks that are coming out because they're coming out really, really fast as well. Mhmm. Yep. And so that's a that's a key component.

\[10:04\] **Tyler Goble**: We don't wanna hire somebody that's gonna be so rigid that all they're doing is lang chain. And now all of a sudden, lang chain is completely irrelevant, and we can adapt. So Yeah.

\[10:15\] **Tyler Goble**: That's that's the so if they come in,

\[10:17\] **Marius Mazilu**: they let's let's be back in one year example. They only use the line chain. They learn that, but they're very rigid and they they don't truly understand. They just understand some recipes. They read the docs. Everything is good. How do we gauge that within an interview to see how do we test that out? Because it's it will be good to have some hands on testing to see. So we need to prepare some some test bed for them, probably.

\[10:43\] **Andrei Secea**: And what's the level? Let's say we

\[10:46\] **Marius Mazilu**: And and what's the level? Yes.

\[10:51\] **Tyler Goble**: What would be helpful for me? Could you guys provide me what we're doing currently for other types of devs?

\[10:59\] **Marius Mazilu**: So in our current interviews for other types of devs, basically, we start with, okay, what what did they do? Right? What's what's your current what what are you doing on your current job? Ideally, we dig through we dig deeper into what they do so we can see how deep of an understanding they they they have on their current usage. We find the we ask them to see whether they thought about that when they use their own tools. We we go on their playground Mhmm.

\[11:30\] **Marius Mazilu**: To see how how deep understanding, how how critical how good of a critical thinking thinker they are. Mhmm. And we try to play around with them in that area. After that, we we go to some basics on languages or whatever, and we try to have some problems to see if they can think out of the box. Mhmm. And then we probe to see how big their breadth is for for the for all the experience.

\[11:59\] **Andrei Secea**: System design.

\[12:01\] **Marius Mazilu**: System design, that's mostly on technical leads. Well, as you you you will realize during the conversation during the first part if they really understood the technology because that's their best part. Right? You go on to their expertise level. You figure out then and there if they actually know how to use it. In certain points, there's no point in going to system design because they barely know their own tools or their own Mhmm. Their own thing.

\[12:25\] **Marius Mazilu**: And when you do a test with them, you make sure that you're close to their environment or whatever we need them to do. So we're not we're not we're not asking them to build something that's completely new. We need to make sure that it's very it's approachable. But it also proves the fact that they are comfortable in writing the code, in thinking about the problem, and in debugging or whatever they're doing at the time.

\[12:54\] **Tyler Goble**: Mhmm. Do you guys have any of those recorded? The interviews?

\[12:59\] **Andrei Secea**: We cannot.

\[13:00\] **Dorel Macra**: We can always think.

\[13:04\] **Tyler Goble**: When's the next interview for anyone regardless of job?

\[13:10\] **Andrei Secea**: I think it should be a technical one.

\[13:13\] **Tyler Goble**: Yeah. I

\[13:14\] **Andrei Secea**: But I don't know. I do not have any.

\[13:18\] **Tyler Goble**: Let me check. I know me me, Vlad, and Lupu are meeting on Friday.

\[13:28\] **Dorel Macra**: Mhmm. Yeah. But Lupu is an internal employee. Correct.

\[13:33\] **Tyler Goble**: Does it make sense to workshop that thought of, like, what an interview would be structured like even though that's an internal person? It would.

\[13:44\] **Marius Mazilu**: I think it would be

\[13:46\] **Tyler Goble**: Not like saying, like, hey. We're gonna fire you. You don't do well in this interview, but, like, walk through the motions of, this is kind of what we're thinking for an interview. How does how does a known quantity like Lupu understand and and operate through these things?

\[14:04\] **Marius Mazilu**: I don't know if loop Lupo has experience with some of these things. If he did actually worked on these. Did he?

\[14:12\] **Dorel Macra**: Probably, this is why they are Tyler, we are having this conversation because, you know, it's a big confusion for us

\[14:19\] **Andrei Secea**: Mhmm.

\[14:20\] **Dorel Macra**: When we are talking about AI related engineering.

\[14:26\] **Tyler Goble**: Actually What yeah.

\[14:27\] **Dorel Macra**: What does it mean? What kind of skills are needed and so on? Somebody just using an AI as a coding assistant is already saying, I I am working with AI. Well, actually, you are not.

\[14:38\] **Tyler Goble**: Yeah. Yeah. That's like the conversation, Dorel, me and you had, I think, with Faith Driven at one point is, like, you say AI, but when you say AI, what do you mean? Do you mean Exactly. We need a classification model, or do you mean we need a chatbot, or we need a Rag database? There's a lot of different flavors of what you can mean when you say AI engineer. And what I think AI engineer, I do think in two major branches. And somebody could occupy both branches, But there's two distinctions.

\[15:10\] **Tyler Goble**: There's the math and statistics heavy AI engineer who's really more classical machine learning algorithm builder. And then there's a generative AI engineer who's more of a logic business use case person, which that person doesn't need to be as technical as the machine learning person.

\[15:30\] **Marius Mazilu**: Well, in in the assessment, we usually write these things down. We we write each of the things that we probed. We will write a level on them, like, between one and five. And then this is a three, this is a five, this is a four, this is a zero completely out of that there. Because after that, we need to mix and match and make sure that they actually fit their job description.

\[15:50\] **Tyler Goble**: Mhmm. Okay.

\[15:53\] **Marius Mazilu**: So we could split out the that's why it's good to have these two separations so we can actually put these two with their sub items for each of them.

\[16:04\] **Tyler Goble**: Okay.

\[16:13\] **Marius Mazilu**: Alright. So next steps, can you compile let's assume I guess, we probably need to start with a set of we we need to start with questions and maybe how to do some hands on something hands on so we can actually probe and see whether they truly worked on something or not.

\[16:34\] **Marius Mazilu**: And if we are to start from what they already did, we should probably start with we should have multiple hands on test beds where we if you work with that, try this and let's let's walk them through those scenarios, see if they truly understand if it truly works, and then we can go to others. Does that make sense for everyone, Omar?

\[17:01\] **Andrei Secea**: I think before the list of questions, what's the skill set? Like, a list of skills. Right?

\[17:08\] **Marius Mazilu**: Yeah. Python should be there as well. Mhmm.

\[17:11\] **Andrei Secea**: Python, Genovive AI, on the ML, I don't know. Maybe it needs it doesn't need I know. Maybe it's a separate role or is this role. I don't know.

\[17:23\] **Marius Mazilu**: I think I think those

\[17:25\] **Andrei Secea**: are skills that as you said, you we would grade them. Okay. He knows that. One zero five five zero five, whatever. Right?

\[17:33\] **Marius Mazilu**: Yeah. And I think Tyler kind of touched on that. So this Python and the two other types. Right? I'm assuming those are the main ones, and that we may have subsections on each of them.

\[17:46\] **Tyler Goble**: Yeah. Could you send me a list of questions that you ask? Or, like like, give me, like, the full end to end for somebody that got hired inside Victory Square, like, those artifacts. And then I could review those and mold and form them, and maybe that's our next step is I produce that for

\[18:06\] **Marius Mazilu**: you guys. So let me let me show you exactly let me show you a few things that I have here. Yeah. I don't think there's a few classic questions that I that we ask or used to ask. We changed tabs in normally, we start normally, we start with the so when when doing the for example, we we have this project we we have this problem in. Right? We give them this as a hands on. So this is a service. I'm showing them this, and I'm asking them, hey. Can you do this?

\[18:43\] **Marius Mazilu**: We you have this code. Can you actually do this? Does this code compile? Yes. What does it do? Because you have a database sensor, sorry, throwing a new runtime exception. What will it do? If you do if you look at the so first question, how the what do you think this does? Well, it should try to insert, but because you throw runtime, it should roll back because it's annotated with transaction. Okay. Great. Can I do this in the code? Well, yes, you can. And if I call the function, can I call it? Yes, you can.

\[19:13\] **Marius Mazilu**: What will it do? Well, the catch here is that it won't roll back because if you initiate it like this without going through spring context, it will basically not work the way you expect it. So I want to understand whether he understands how spring Mhmm. Works that he needs to proxy five, things like that.

\[19:31\] **Tyler Goble**: Got it. So then let me let me steal screen real quick and see if I'm on the same page with you. So, like, in that if that sort of workflow is what makes sense, let's just go to a go to a notebook, go to supervised learning, go to linear regression. We're walking through this notebook and say, explain to me in regular words what homoscedasticity means. Like, what does that mean to the business customer?

\[20:11\] **Tyler Goble**: And this might look like Chinese to you guys, but if you know math and you know statistics and you've been working with this kind of stuff, constant variance of residuals across all feature values. What that means is that when I run the model, I'm seeing the error term be relatively stable over time across all the different things. And so the model's not wrong. Like, when you're looking at how wrong your model is, the it doesn't blow up as you get deeper into the dataset. That would be a way to describe that kind of a function.

\[20:45\] **Tyler Goble**: So with the interview process kinda go through something like that where we're we're walking through a notebook? Because Python, Jupyter Notebooks would probably be how I would I would go about it. Would be.

\[20:56\] **Tyler Goble**: So this this would be

\[20:57\] **Marius Mazilu**: how you would pull the questions out. Yes. And as for hands on, however, what we do is we let them open whatever in our case, we let them open a terminal, for example, Java or or JavaScript. Usually, they open a an online code editor, and we ask them to do a small problem, like, make me a promise that resolves itself in five minutes or something like that. Mhmm. And then I ask them questions on the code they're writing because I want to see their promise of writing the code, and this is what we're gauging. Right?

\[21:27\] **Marius Mazilu**: Their promise of interacting with the tools. And then you go into small questions deeper to okay.

\[21:34\] **Marius Mazilu**: Now make it do that or make it do the

\[21:36\] **Andrei Secea**: other. Mhmm.

\[21:38\] **Tyler Goble**: Okay. So then

\[21:40\] **Marius Mazilu**: Python. Yeah. Ideally. Okay. And if we have something for AI, it would be good for that as well.

\[21:47\] **Andrei Secea**: Mhmm. Okay.

\[21:48\] **Tyler Goble**: So Then I think I could use this as a baseline to maybe give them code that's not commented out the way I comment this stuff out. This is like an educational repo that we're probably gonna end up using inside Victory Square to, like, get us all baselined. But

\[22:08\] **Marius Mazilu**: yeah. Okay.

\[22:11\] **Tyler Goble**: Okay. I think that makes a lot of sense. And so we would put basically, for the hands on portion, the interview part of just, like, talking through what these different things work, what would these different things mean is one step. Then the next step hands on, that can be a pre premade Google Colab notebook that they're able to then write some code, make it run, and do that kind of a thing. And we have, an answer key that's expected that we have that we're looking at that they don't see.

\[22:46\] **Marius Mazilu**: Yep. I think we can we can try that. And then then I we could potentially try to have some see if we have someone who has done something like that and see how they feel about that kind of test. I mean, imagine somebody's interviewing you. Oh, yeah. And they would put you for the for this. What how would that look like?

\[23:07\] **Tyler Goble**: Mhmm. No. I hear you on that. Yeah. You don't wanna, like, wire brush somebody, like, brutally, but you do wanna find out what they can do and Yeah. And some things as we all know, Google's our best friend for everything, but now it's like ChatGPT is our best friend for everything. And so whether or not they remember the exact syntax of how this thing works is kind of irrelevant at this day and age. It's more like the logic and stuff that matters. So okay.

\[23:38\] **Marius Mazilu**: Cool. Alright. I think we're good. We may need to set up a follow-up for this to actually discuss some

\[23:45\] **Tyler Goble**: of these. Yeah. I think next steps, shoot me over examples of questions that you guys are asking. How many questions, that kind of thing. I will make a couple sample testing notebooks, share those without share with us on the next call there, and we'll have, like, a question sheet, two tracks, one for generative AI, one for machine learning. That person could fill both roles or they maybe fill one of them. Generative AI notebook, machine learning notebook with concepts like that.

\[24:23\] **Tyler Goble**: And, Secea, I I will work to make sure that those notebooks would qualify somebody to be able to fill those roles inside of six map and inside of Faith Driven at the same time.

\[24:35\] **Andrei Secea**: I only have those as a reference right now. I don't know. Mhmm. Right. Oh, oh, the question. So between those ML sections, let's say, if someone knows one, it's easy to grab the other one to learn the other other ones.

\[24:56\] **Tyler Goble**: For machine learning, I would say yes.

\[24:58\] **Andrei Secea**: Yeah. So if he has the fundamentals and at least one of those things, then we know we can leverage him further. Right?

\[25:05\] **Tyler Goble**: The fundamentals for machine learning is knowing when is it okay to apply that type of model, know what tests you need to run to see how accurate the model is, and then know how to monitor that model for Drift. So over time, is your relationships changing in that model? And if you can do those three things, that's kind of the fundamental blocking and tackling for any sort of machine learning model.

\[25:28\] **Tyler Goble**: And you now know the right questions to ask, the right the right test to run to make sure that this model is good to go on your stuff. Because the danger is all the models will produce an output, and you may think that that output is correct if you don't actually run tests on it. Mhmm. And not test in a way, like, software development life cycle, like, unit tests. Tests as in, like, mathematical fundamentals that this model is actually appropriate to be used.

\[25:52\] **Andrei Secea**: Yeah. I've seen your tests. You've done so for six months. I understand. Yeah. Over time, it's some data size or some somewhere it breaks. Right? Or the speed is not enough or Yeah.

\[26:05\] **Tyler Goble**: Alright. We gotta jump for six map.

\[26:07\] **Andrei Secea**: Yeah. Same. Thank you. Yeah. \+1 04\. Talk to you guys. Bye.

