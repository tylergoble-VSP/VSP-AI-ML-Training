# ML Discussion - Meeting Notes

**Date:** July 28, 2026

**Attendees:**
- Vlad Damian (vlad.damian@vspartners.us)
- Dorel Macra (dorel.macra@vspartners.us)
- Marius Mazilu (marius.mazilu@vspartners.us)
- Tyler Goble (tyler.goble@vspartners.us)

**Topic:** ML literacy / ML-LLM-agentic training program

---

## Meeting Notes

#### Overview
* The meeting's real outcome: what Tyler had built as a standalone ML literacy deck is actually just the opening module of a much larger, structured training program Vlad needs to present to Marius Banici
* The program covers three pillars — ML literacy, LLM literacy, and agentic systems — with agentic systems as the lion's share; ML is just enough to hold a pre-sales conversation
* Structure is basics → advanced → expert, roughly **1 month / 3 months / 6 months**, mandatory for seniors and TLs (~**10–12** spots), no pick-and-choose — everyone in basics does all of it
* Tyler will pull his academic coursework and slide decks to draft the basics skeleton by end of **Wednesday, July 30th**; Marius will set a follow-up call on **July 30th** to review it
* Preferred delivery format: mostly remote/self-study with intentional pre-work, culminating in an in-person hackathon — tentatively the week before Christmas as a graduation event

#### ML literacy deck walkthrough
* Tyler walked through the current draft deck, framed as "smart enough to talk with a client and ask the right next question" — not how to build models
* The deck covers the five ML jobs (classify, cluster, regress, propensity, recommend), key model types, how to read model outputs, and basic grading metrics like MAE, precision/recall, and AUC
* Vlad confirmed this deck is a good fit as the first module of the basics tier, not a standalone training

#### Full training program vision
* Vlad wants a full structured program — modules, submodules, lessons, durations, responsible owners, and exams — that he can present to Marius Banici as a concrete plan
* The goal is for seniors and TLs to close the translation gap between ML/AI engineers and delivery engineers, particularly in pre-sales and production conversations
* Vlad wants the program to cover ML literacy, LLM literacy, and agentic systems, with the ability to speak intelligently to clients about all three — not to become ML engineers
* ~**10–12** spots, seniors and TLs only; participants who don't do the work are out
* Vlad sees the incentive plainly: having the skills to stay employed as client demand for AI work grows

#### Curriculum structure and levels
* Three tiers: basics (~**1 month**), advanced (~**3 months**), expert (~**6 months**)
* Basics is mandatory and complete — no skipping modules; Tyler and Vlad agree it's the most critical tier to get right because it enables self-directed learning from there
* Advanced is largely self-study once basics gives people the foundation; expert involves deep dives like evaluation frameworks (e.g. AISI) and production-grade work
* Vlad wants basics to include a statistics foundation, hands-on exercises (e.g. running a Jupyter notebook, training a simple labeled model with PyTorch or Keras), and clear learning goals per module — not dictionary definitions
* Tyler suggested using Stanford's publicly available ML and generative AI coursework as companion material and may be able to pull the actual slide decks from contacts there
* Andrei Karpathy's "build an LLM from scratch" series was flagged as a spirit-of-the-thing reference for the hands-on ML section

#### Agentic systems as the core focus
* Agentic systems are the lion's share of the program — Vlad expects VSP will actually be hired to build these, unlike pure ML work
* Coverage needs to include frameworks (LangChain, LangGraph, LangSmith, Haystack), cloud provider offerings (GCP, AWS Bedrock, Azure), evaluation frameworks, observability, reliability, hardware/cost considerations, and harness tooling
* ML literacy is scoped to roughly **5%** of the total program — enough to understand neural nets, CNNs, deep learning, and reinforcement learning at a conversational level
* RAG was called out as a basics-level topic; more advanced RAG patterns (e.g. graph-based retrieval) likely belong in advanced

#### Delivery format and in-person hackathon
* ~**90%** of the program is remote self-study; the in-person component is reserved for a culminating event
* Tyler suggested — and Vlad liked — a model where online work comes first, then an in-person hackathon as a graduation: tentatively the week before Christmas, with a show-and-tell on the final day
* Tyler's past approach (fly in, lock phones, **8** hours/day for a week) was raised as a proven format for intensive boot camps; an in-person basics boot camp is also on the table as Option A in the logistics doc
* Vlad flagged a past training with Andrei Ciobanu where **90%** of the audience was lost early because there was no intentional pre-work — the new program is designed to avoid that

#### Basics skeleton deadline and next steps
* Tyler will pull his academic ML/generative AI coursework and draft the basics skeleton — chapters, durations, responsible owners — by end of **Wednesday, July 30th**
* Marius will set a follow-up call on **July 30th** to review the skeleton together and begin scheduling individual lessons with prerequisites and outcomes
* After basics is fully fleshed out, the team will work through advanced and expert the same way — one module at a time
* Tyler also raised pulling in people from his network to co-teach specific lessons rather than one person holding all of them

---

## Action Items

1. **Schedule curriculum review call for July 30**
   - Assigned to: Marius Mazilu
   - Status: PENDING
   - Description: Schedule a follow-up call on July 30 to review the basics curriculum skeleton Tyler will have ready.

2. **Draft basics curriculum skeleton in the (M)LLM Literacy spreadsheet**
   - Assigned to: Tyler Goble
   - Status: PENDING
   - Description: Pull from your master's coursework and academic contacts to structure the basics module — include topics, duration per lesson, and responsible person for each. Target: end of Wednesday, July 30.
