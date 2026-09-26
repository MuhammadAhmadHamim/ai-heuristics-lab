<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:120a0c,50:1f1114,100:2b171a&height=230&section=header&text=ai-heuristics-lab&fontSize=46&fontColor=d9c9a0&fontAlignY=40&desc=Search%2C%20Reasoning%2C%20and%20Learning&descAlignY=63&descColor=a67f4e&animation=fadeIn&fontFamily=Georgia"/>

<br/>

![Language](https://img.shields.io/badge/Language-Python_3-d9c9a0?style=for-the-badge&logo=python&logoColor=120a0c)
![Focus](https://img.shields.io/badge/Focus-Search%2C_Logic_%26_Learning-a67f4e?style=for-the-badge&logo=buffer&logoColor=white)
![Semester](https://img.shields.io/badge/Semester-4-2b171a?style=for-the-badge&logoColor=d9c9a0)
![Status](https://img.shields.io/badge/Status-🌱_Freshly_Started-a67f4e?style=for-the-badge&logoColor=white)

<br/><br/>

> *"AI won't replace humans, but humans who use AI will replace those who don't"*
> — **Sam Altman, CEO of OpenAI**

<br/>

</div>

---

## ◈ What Lives Here

Semester 4 is where the coursework stopped being about syntax and started being about *thinking machines* — how a search space actually gets explored, how a rule actually gets inferred, how a network learns something nobody explicitly wrote into it.

This is that record, in **Python**, starting **Fall 2026**. No lecture notes, no copied theory, no slide decks pretending to be understanding — a slide never taught anyone to trust an algorithm. Running it did. Every file in here exists because I coded it, not because I was told to remember it.

---

## ◈ Vault Structure

```
ai-concepts-vault/
│
├── 🤖 agents/
|       ├── simple_reflex_agent.py
│       ├── model_based_agent.py
|       └── goal_based_agent.py
│
├── 🧭 search/
│       ├── uninformed/            BFS, DFS, UCS, iterative deepening
│       ├── informed/              greedy best-first, A*, hand-built heuristics
│       ├── local_optimization/    hill-climbing, simulated annealing, beam search
│       ├── evolutionary/          genetic algorithms — encoding, selection, mutation
│       └── adversarial/           minimax, alpha-beta, MCTS
│
├── 🧩 logic_and_reasoning/
│       ├── propositional/         CNF conversion, resolution engine
│       ├── first_order/           unification, inference
│       └── expert_systems/        forward/backward chaining engines
│
├── 🔗 constraint_satisfaction/
│       └── CSP solvers, backtracking, ordering heuristics, min-conflicts
│
├── 🎲 probabilistic_reasoning/
│       └── naive Bayes, Bayesian network inference
│
├── 🗺️ planning/
│       └── STRIPS/PDDL-style planners, planning graphs
│
├── 🧠 learning/
│       ├── neural_networks/       ANNs from scratch, no framework doing the thinking
│       └── deep_learning/         open lane — CNNs, RL, whatever the course opens next
│
└── 🧪 labs/
        └── one-off experiments that don't have a home yet
```

---

## ◈ Chapter Breakdown

<details>
<summary><b>🤖 Agents &nbsp;|&nbsp; Where Everything Starts</b></summary>
<br/>

Before search, before logic, before learning — an agent has to actually perceive an environment and act in it. This is the ground floor.

| Module | What's Queued | Status |
|---|---|:---:|
| **Agent Types** | Simple reflex, model-based, goal-based, utility-based | 3 Done ✅, 1 ⏳ Queued |
| **Environment Design** | PEAS framing, environment properties, small simulated worlds | ⏳ Queued |

> *No agent here gets to be theoretical — if it can't be dropped into an environment and run, it doesn't count as built yet.*

</details>

<details>
<summary><b>🧭 Search &nbsp;|&nbsp; Five Ways to Explore a Space</b></summary>
<br/>

The backbone of the whole course. Everything from "find any path" to "find the *best* path" lives here, in five escalating branches.

| Branch | What's Queued | Status |
|---|---|:---:|
| **Uninformed** | BFS, DFS, uniform-cost search, iterative deepening | 🔨 In progress |
| **Informed** | Greedy best-first, A*, custom heuristic design | ⏳ Queued |
| **Local Optimization** | Hill-climbing, simulated annealing, beam search | ⏳ Queued |
| **Evolutionary** | Genetic algorithms — encodings, selection, crossover, mutation | ⏳ Queued |
| **Adversarial** | Minimax, alpha-beta pruning, Monte Carlo tree search | ⏳ Queued |

> *Uninformed comes first for a reason — you don't get to appreciate a good heuristic until you've felt what it's like without one.*

</details>

<details>
<summary><b>🧩 Logic &amp; Reasoning &nbsp;|&nbsp; Machines That Infer</b></summary>
<br/>

Moving from *searching for* an answer to *deriving* one. This is where an agent starts reasoning instead of just exploring.

| Module | What's Queued | Status |
|---|---|:---:|
| **Propositional Logic** | CNF conversion, resolution-based inference | ⏳ Queued |
| **First-Order Logic** | Unification, knowledge-base inference | ⏳ Queued |
| **Expert Systems** | Forward and backward chaining engines | ⏳ Queued |

> *A resolution engine that can't actually resolve anything is just a flowchart with extra steps — this chapter doesn't count until one runs.*

</details>

<details>
<summary><b>🔗 Constraint Satisfaction &nbsp;|&nbsp; Solving by Elimination</b></summary>
<br/>

Some problems aren't about finding a path — they're about finding an assignment that doesn't break any rules. CSPs are that shift in thinking, in code.

| Module | What's Queued | Status |
|---|---|:---:|
| **CSP Modeling & Backtracking** | Variables, domains, constraints, backtracking search | ⏳ Queued |
| **Ordering Heuristics** | MRV, degree heuristic, least-constraining-value | ⏳ Queued |
| **Local Search for CSPs** | Min-conflicts | ⏳ Queued |

</details>

<details>
<summary><b>🎲 Probabilistic Reasoning &nbsp;|&nbsp; When the Answer Isn't Certain</b></summary>
<br/>

Real environments don't hand you certainty. This chapter is about reasoning well anyway.

| Module | What's Queued | Status |
|---|---|:---:|
| **Bayes' Rule** | Built from scratch, not imported from a stats library | ⏳ Queued |
| **Naive Bayes** | Classification under an independence assumption | ⏳ Queued |
| **Bayesian Networks** | Structured inference over dependent variables | ⏳ Queued |

</details>

<details>
<summary><b>🗺️ Planning &nbsp;|&nbsp; Acting Toward a Goal, Not Just Finding One</b></summary>
<br/>

Search finds a path. Planning figures out what to *do* — a sequence of actions with preconditions and effects.

| Module | What's Queued | Status |
|---|---|:---:|
| **STRIPS / PDDL-Style Representations** | Actions, preconditions, effects | ⏳ Queued |
| **Progression & Regression Planning** | Forward and backward state-space search over plans | ⏳ Queued |
| **Planning Graphs** | Layered representations for plan extraction | ⏳ Queued |

</details>

<details>
<summary><b>🧠 Learning &nbsp;|&nbsp; The Open-Ended Chapter</b></summary>
<br/>

Everything before this chapter is deterministic and hand-traceable. This one is where the course — and this vault — stops having a ceiling.

| Branch | What's Queued | Status |
|---|---|:---:|
| **Neural Networks** | Built from scratch — forward pass, backprop, no framework shortcuts | ⏳ Queued |
| **Deep Learning** | Open lane — CNNs, reinforcement learning, whatever the course opens next | ⏳ Open lane |

> *This is the one chapter without a fixed shape. `deep_learning/` exists specifically so a rabbit hole never has to wait for a restructure.*

</details>

---

## ◈ Concepts at a Glance

```python
# What this vault looks like, expressed in code:

vault = {
    "agents":                   {"status": "queued"},
    "search": {
        "status": "in_progress",
        "branches": ["uninformed", "informed", "local_optimization", "evolutionary", "adversarial"],
    },
    "logic_and_reasoning":       {"status": "queued", "branches": ["propositional", "first_order", "expert_systems"]},
    "constraint_satisfaction":   {"status": "queued"},
    "probabilistic_reasoning":   {"status": "queued"},
    "planning":                  {"status": "queued"},
    "learning":                  {"status": "queued", "branches": ["neural_networks", "deep_learning"]},
}

for concept, meta in vault.items():
    if meta["status"] == "in_progress":
        print(f"{concept} — being traced right now")
# ... the rest fills in one working file at a time.
```

---

## ◈ How to Explore

```bash
# Clone the vault
git clone https://github.com/MuhammadAhmadHamim/ai-heuristics-lab.git

# Navigate to any concept
cd labs

# Run it
python 01_lab.py
```

> **Requirement:** Python 3.10+ &nbsp;|&nbsp; **IDE:** VS Code, PyCharm, or any terminal

---

## ◈ Skills Being Forged

<div align="center">

![](https://img.shields.io/badge/Python-AI_Implementation-d9c9a0?style=flat-square&logo=python&logoColor=120a0c)
![](https://img.shields.io/badge/Search-Uninformed_%26_Informed-d9c9a0?style=flat-square&logoColor=120a0c)
![](https://img.shields.io/badge/Search-Local_Optimization-a67f4e?style=flat-square&logoColor=white)
![](https://img.shields.io/badge/Search-Adversarial_%26_Game_Trees-d9c9a0?style=flat-square&logoColor=120a0c)
![](https://img.shields.io/badge/Probability-Bayesian_Reasoning-2b171a?style=flat-square&logoColor=d9c9a0)
![](https://img.shields.io/badge/Logic-Propositional_%26_Resolution-a67f4e?style=flat-square&logoColor=white)
![](https://img.shields.io/badge/Logic-First_Order_%26_Unification-2b171a?style=flat-square&logoColor=d9c9a0)
![](https://img.shields.io/badge/Search-Evolutionary_Algorithms-2b171a?style=flat-square&logoColor=d9c9a0)
![](https://img.shields.io/badge/CSP-Backtracking_%26_Min_Conflicts-a67f4e?style=flat-square&logoColor=white)
![](https://img.shields.io/badge/Planning-STRIPS_%2F_PDDL-d9c9a0?style=flat-square&logoColor=120a0c)
![](https://img.shields.io/badge/Learning-Neural_Networks_From_Scratch-a67f4e?style=flat-square&logoColor=white)
![](https://img.shields.io/badge/Systems-Expert_Systems-d9c9a0?style=flat-square&logoColor=120a0c)
![](https://img.shields.io/badge/Learning-Deep_Learning_Open_Lane-2b171a?style=flat-square&logoColor=d9c9a0)


</div>

---

## ◈ A Note on This Work


AI has a reputation for feeling like magic until you've built the small, unglamorous version yourself — a search that actually explores, a network that actually learns from three lines of gradient math instead of a library call. This repository is the record of taking that reputation apart, one traced algorithm at a time.

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:2b171a,50:1f1114,100:120a0c&height=120&section=footer&animation=fadeIn"/>

*Understood one trace at a time. Never just memorized.*

</div>