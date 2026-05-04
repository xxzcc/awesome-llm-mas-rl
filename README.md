# Awesome LLM-MAS RL

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0 + MIT](https://img.shields.io/badge/license-CC0%20%2B%20MIT-blue.svg)](LICENSE)

A GitHub-first curated paper list, paper-pool artifact, and trace schema for:

> Reinforcement Learning for LLM-based Multi-Agent Systems: An Orchestration-Trace Taxonomy

This repository accompanies a survey of reinforcement learning and post-training methods for LLM-based multi-agent systems. The central organizing idea is the **orchestration trace**: a temporal event graph recording orchestrator decisions, sub-agent spawns, inter-agent messages, tool calls, returns, aggregation steps, rewards, and costs.

The README is designed for browsing on GitHub, with the retained papers listed directly below. The CSV files and scripts remain the source of truth for auditability, statistics, and reproducibility.

## Repository Status

- Target GitHub URL: <https://github.com/xxzcc/awesome-llm-mas-rl>
- Retained paper pool: 84 entries
- Exclusion log: 32 screened-but-excluded records
- Audited records total: 116
- Trace artifact: JSON Schema, example trace, and dependency-free validator

This repository supersedes the earlier related credit-assignment list at <https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL> for the LLM-MAS survey artifact.

## Table of Contents

- [Papers by Taxonomy](#papers-by-taxonomy)
- [Artifact Files](#artifact-files)
- [Quick Start](#quick-start)
- [Taxonomy Fields](#taxonomy-fields)
- [Headline Counts](#headline-counts)
- [Orchestration Trace Schema](#orchestration-trace-schema)
- [Update Policy](#update-policy)
- [Citation](#citation)

## Papers by Taxonomy

<!-- BEGIN GENERATED PAPER LIST -->
This section is generated from `papers/papers.csv` by `python scripts/generate_readme_papers.py`. Edit the CSV, not this block.

Retained corpus: **84 entries**.

### RL and Post-Training Methods (42)

1. **LLM Collaboration With Multi-Agent Reinforcement Learning** (2025) `RL` `reward: shared` `credit: agent` `orchestration: centralized` `core`

   *First author: Shuo Liu; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2508.04652) -- Models LLM collaboration as cooperative MARL; proposes MAGRPO.

2. **MARFT: Multi-Agent Reinforcement Fine-Tuning** (2025) `RL` `reward: hybrid` `credit: agent` `orchestration: centralized` `core`

   *First author: Junwei Liao; venue: arXiv (ICLR 2026 submitted).* [[Paper]](https://arxiv.org/abs/2504.16129) -- First systematic LaMAS RFT paradigm.

3. **Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO** (2025) `RL` `reward: hybrid` `credit: role` `orchestration: hierarchical` `scenario: research` `core`

   *First author: Haoyang Hong; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2511.13288) -- Hierarchical GRPO; decoupled planner/sub-agent training.

4. **Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems** (2026) `RL` `reward: shared` `credit: agent` `orchestration: centralized` `core`

   *First author: Lang Feng; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2602.08847) -- Diagnoses GRPO instability in MAS; agent-wise normalization.

5. **Contextual Counterfactual Credit Assignment for Multi-Agent Reinforcement Learning in LLM Collaboration** (2026) `RL` `reward: shared` `credit: message` `orchestration: centralized` `core`

   *First author: Yanjun Chen; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2603.06859) -- Counterfactual causal credit assignment at message level.

6. **Who Deserves the Reward? SHARP: Shapley Credit-based Optimization for Multi-Agent System** (2026) `RL` `reward: hybrid` `credit: agent` `orchestration: hierarchical` `scenario: tool_use` `core`

   *First author: Yanming Li; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2602.08335) -- Shapley-value-based hierarchical credit assignment.

7. **Debate as Reward: A Multi-Agent Reward System for Scientific Ideation via RL Post-Training** (2026) `RL` `reward: debate` `credit: message` `orchestration: debate` `scenario: research` `core`

   *First author: Moein Salimi; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2604.16723) -- Multi-agent debate as reward signal for scientific ideation.

8. **Multi-Agent Tool-Integrated Policy Optimization** (2025) `RL` `reward: role` `credit: role` `orchestration: planner_executor_critic` `scenario: tool_use` `core`

   *First author: Zhanfeng Mo; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2510.04678) -- Single-LLM dual-role (planner+worker) tool-integrated PO.

9. **Multi-Agent Collaboration via Evolving Orchestration** (2025) `RL` `reward: orchestration` `credit: orchestrator` `orchestration: centralized` `core`

   *First author: Yufan Dang; venue: NeurIPS 2025.* [[Paper]](https://arxiv.org/abs/2505.19591) -- Puppeteer central orchestrator; RL-learned dynamic conducting.

10. **HALO: Hierarchical Autonomous Logic-Oriented Orchestration for Multi-Agent LLM Systems** (2025) `partial RL` `reward: orchestration` `credit: role` `orchestration: hierarchical` `supporting`

   *First author: Zhipeng Hou; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2505.13516) -- Three-layer hierarchical MAS with MCTS-based search.

11. **Small Model as Master Orchestrator: Learning Unified Agent-Tool Orchestration with Parallel Subtask Decomposition** (2026) `RL` `reward: orchestration` `credit: orchestrator` `orchestration: centralized` `core`

   *First author: Wenzhen Yuan; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2604.17009) -- Lightweight orchestrator unifies agent-tool action space.

12. **MarsRL: Advancing Multi-Agent Reasoning System via Reinforcement Learning with Agentic Pipeline Parallelism** (2025) `RL` `reward: hybrid` `credit: turn` `orchestration: hierarchical` `scenario: math` `core`

   *First author: Shulin Liu; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2511.11373) -- Agentic pipeline-parallel RL for multi-reasoning agents.

13. **MALT: Improving Reasoning with Multi-Agent LLM Training** (2024) `RL` `reward: role` `credit: role` `orchestration: planner_executor_critic` `scenario: math` `core`

   *First author: Sumeet Ramesh Motwani; venue: COLM 2025.* [[Paper]](https://arxiv.org/abs/2412.01928) -- Multi-role generator-verifier-refiner training with role-PRM.

14. **MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning** (2025) `RL` `reward: shared` `credit: agent` `orchestration: centralized` `core`

   *First author: Chanwoo Park; venue: ACL 2025.* [[Paper]](https://arxiv.org/abs/2502.18439) -- First post-training RL paradigm explicitly training collaboration.

15. **Latent Collaboration in Multi-Agent Systems** (2025) `orchestration: debate` `supporting`

   *First author: Jiaru Zou; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2511.20639) -- Training-free latent-space MAS communication; +14.6% gain.

16. **Multi-Agent Evolve: LLM Self-Improve through Co-evolution** (2025) `RL` `reward: verifier` `credit: role` `orchestration: planner_executor_critic` `supporting`

   *First author: Yixing Chen; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2510.23595) -- Proposer-Solver-Judge tri-role co-evolution self-improvement.

17. **Experience as a Compass: Multi-agent RAG with Evolving Orchestration and Agent Prompts** (2026) `partial RL` `reward: orchestration` `credit: orchestrator` `orchestration: centralized` `scenario: research` `supporting`

   *First author: Sha Li; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2604.00901) -- Experience-evolving orchestration policy and agent prompts for MAS-RAG.

18. **AgentSpawn: Adaptive Multi-Agent Collaboration Through Dynamic Spawning for Long-Horizon Code Generation** (2026) `partial RL` `reward: orchestration` `credit: orchestrator` `orchestration: swarm` `scenario: coding` `supporting`

   *First author: Igor Costa; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2602.07072) -- Runtime dynamic spawn + memory transfer for long-horizon code.

19. **Scaling Long-Horizon LLM Agent via Context-Folding** (2025) `RL` `reward: hybrid` `credit: turn` `orchestration: hierarchical` `scenario: coding` `core`

   *First author: Weiwei Sun; venue: arXiv (ICLR 2026 submitted).* [[Paper]](https://arxiv.org/abs/2510.11967) -- Agent-managed context folding for long-horizon trajectories.

20. **Proximal Policy Optimization Algorithms** (2017) `RL` `core`

   *First author: John Schulman; venue: arXiv.* [[Paper]](https://arxiv.org/abs/1707.06347) -- PPO; clipped surrogate objective; foundation for all LLM-RL methods.

21. **DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models** (2024) `RL` `scenario: math` `core`

   *First author: Zhihong Shao; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2402.03300) -- Introduces GRPO (Group Relative Policy Optimization).

22. **Training Language Models to Follow Instructions with Human Feedback** (2022) `RL` `core`

   *First author: Long Ouyang; venue: NeurIPS 2022.* [[Paper]](https://arxiv.org/abs/2203.02155) -- InstructGPT; canonical RLHF three-stage pipeline.

23. **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (2025) `RL` `reward: verifier` `scenario: math` `core`

   *First author: DeepSeek-AI; venue: Nature 2025.* [[Paper]](https://arxiv.org/abs/2501.12948) -- Rule-based RL unlocks long-CoT reasoning; R1 & R1-Zero.

24. **ReAct: Synergizing Reasoning and Acting in Language Models** (2023) `scenario: tool_use` `core`

   *First author: Shunyu Yao; venue: ICLR 2023.* [[Paper]](https://arxiv.org/abs/2210.03629) -- Interleaved reasoning+acting; agentic origin.

25. **CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization** (2025) `RL` `reward: verifier` `scenario: math` `supporting`

   *First author: Zhongyuan Peng; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2507.06181) -- RL-trained critic scores Lean 4 formalizations; instance of verifier-as-reward.

26. **ReMA: Learning to Meta-Think for LLMs with Multi-agent Reinforcement Learning** (2025) `RL` `reward: hybrid` `credit: role` `orchestration: hierarchical` `scenario: math` `core` `verified: partial`

   *First author: Ziyu Wan; venue: NeurIPS 2025.* [[Paper]](https://openreview.net/forum?id=ur295YVtmt) -- Reinforced meta-thinking agents with high-level meta-thinking and low-level reasoning agents.

27. **Advancing Language Multi-Agent Learning with Credit Re-Assignment for Interactive Environment Generalization** (2025) `RL` `reward: process` `credit: agent` `orchestration: centralized` `scenario: web` `core` `verified: partial`

   *First author: Zhitao He; venue: COLM 2025.* [[Paper]](https://openreview.net/forum?id=SoEmgM1ioC) -- CollabUIAgents uses multi-agent credit re-assignment for interactive UI/web environments.

28. **CoMAS: Co-Evolving Multi-Agent Systems via Interaction Rewards** (2026) `RL` `reward: debate` `credit: agent` `orchestration: debate` `core` `verified: partial`

   *First author: Xiangyuan Xue; venue: ICLR 2026.* [[Paper]](https://openreview.net/forum?id=ihwAzktmWc) -- Co-evolving agents learn from interaction-derived rewards without external supervision.

29. **OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation** (2025) `RL` `reward: hybrid` `credit: orchestrator` `orchestration: hierarchical` `scenario: research` `core` `verified: partial`

   *First author: Mengkang Hu; venue: NeurIPS 2025.* [[Paper]](https://openreview.net/forum?id=MBJ46gd1CT) -- Optimized Workforce Learning trains a domain-agnostic planner for modular multi-agent assistance.

30. **Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains** (2025) `partial RL` `reward: debate` `credit: agent` `orchestration: debate` `scenario: math` `supporting` `verified: partial`

   *First author: Vighnesh Subramaniam; venue: ICLR 2025.* [[Project]](https://llm-multiagent-ft.github.io/) -- Finetunes a multiagent society using interaction-generated diverse reasoning chains.

31. **Learning to Deliberate: Meta-policy Collaboration for Agentic LLMs with Multi-agent Reinforcement Learning** (2025) `RL` `reward: hybrid` `credit: turn` `orchestration: debate` `scenario: math` `core`

   *First author: Wei Yang; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2509.03817) -- MPDF learns decentralized meta-cognitive actions Persist Refine Concede with SoftRankPO.

32. **Learning Decentralized LLM Collaboration with Multi-Agent Actor Critic** (2026) `RL` `reward: shared` `credit: agent` `orchestration: centralized` `core`

   *First author: Shuo Liu; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2601.21972) -- Multi-agent actor-critic methods for decentralized LLM collaboration.

33. **WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning** (2026) `RL` `reward: orchestration` `credit: orchestrator` `orchestration: hierarchical` `scenario: research` `core`

   *First author: Zelai Xu; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2602.04634) -- Lead-agent/subagent MARL for broad information seeking and width scaling.

34. **MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety** (2026) `RL` `reward: debate` `credit: agent` `orchestration: debate` `core`

   *First author: Xiaoyu Wen; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2602.01539) -- Multi-turn attacker-defender MARL for robust LLM safety.

35. **MARTI-MARS2: Scaling Multi-Agent Self-Search via Reinforcement Learning for Code Generation** (2026) `RL` `reward: hybrid` `credit: agent` `orchestration: hierarchical` `scenario: coding` `core`

   *First author: Shijie Wang; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2602.07848) -- Multi-agent reinforced training and self-search scaling for code generation.

36. **SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning** (2026) `RL` `reward: hybrid` `credit: role` `orchestration: debate` `core`

   *First author: Bo Liu; venue: ICLR 2026.* [[Paper]](https://openreview.net/forum?id=7Yayy5fNLg) -- Online multi-turn multi-agent self-play with role-conditioned advantage estimation.

37. **MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs** (2026) `RL` `reward: hybrid` `credit: turn` `orchestration: debate` `core`

   *First author: Huining Yuan; venue: ICLR 2026.* [[Paper]](https://openreview.net/forum?id=GCd5v3ehmr) -- Strategic-game self-play with turn-level advantage estimation and agent-wise normalization.

38. **DEPART: Hierarchical Multi-Agent System for Multi-Turn Interaction** (2026) `RL` `reward: hybrid` `credit: role` `orchestration: hierarchical` `scenario: web` `core` `verified: partial`

   *First author: Hao-Lun Hsu; venue: OpenReview (ICLR 2026 submission).* [[Paper]](https://openreview.net/forum?id=Q4Nk6PlZYH) -- HIMPO alternates planner and executor optimization with dense role rewards.

39. **Agent Q-Mix: Selecting the Right Action for LLM Multi-Agent Systems through Reinforcement Learning** (2026) `RL` `reward: hybrid` `credit: agent` `orchestration: centralized` `core`

   *First author: Eric Hanchen Jiang; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2604.00344) -- QMIX-style CTDE learns decentralized communication/topology decisions.

40. **LangMARL: Natural Language Multi-Agent Reinforcement Learning** (2026) `RL` `reward: hybrid` `credit: agent` `orchestration: centralized` `core`

   *First author: Huaiyuan Yao; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2604.00722) -- Agent-level language credit assignment and policy-gradient evolution.

41. **Towards Scalable Lightweight GUI Agents via Multi-role Orchestration** (2026) `RL` `reward: role` `credit: role` `orchestration: hierarchical` `scenario: web` `core`

   *First author: Ziwei Wang; venue: ACL Findings 2026.* [[Paper]](https://arxiv.org/abs/2604.13488) -- Lightweight GUI agent with multi-role orchestration and cooperative-exploration RL.

42. **SAGE: Multi-Agent Self-Evolution for LLM Reasoning** (2026) `RL` `reward: verifier` `credit: role` `orchestration: planner_executor_critic` `scenario: math` `core` `verified: partial`

   *First author: Anonymous; venue: ACL ARR 2026 January Submission.* [[Paper]](https://openreview.net/forum?id=7sOeRzBzjB) -- Challenger-planner-solver-critic co-evolution with verifier-grounded filtering.

### Frameworks and Systems (3)

1. **Agent Lightning: Train ANY AI Agents with Reinforcement Learning** (2025) `RL` `reward: hybrid` `credit: agent` `orchestration: harness` `core`

   *First author: Xufang Luo; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2508.03680) -- Generic RL training framework decoupling execution and training.

2. **SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning** (2025) `partial RL` `reward: process` `credit: turn` `orchestration: hierarchical` `supporting` `verified: partial`

   *First author: Wanjia Zhao; venue: NeurIPS 2025.* [[Paper]](https://openreview.net/forum?id=IDSTtDw4Cs) -- Self-improving MAS builds and refines an experience library from successful reasoning trajectories.

3. **MAS-Zero: Designing Multi-Agent Systems with Zero Supervision** (2025) `credit: orchestrator` `orchestration: hierarchical` `supporting`

   *First author: Zixuan Ke; venue: arXiv.* [[Project]](https://mas-design.github.io/) -- Inference-time self-evolved MAS design through meta-level design feedback and verification.

### Benchmarks and Evaluation (18)

1. **TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems** (2025) `supporting`

   *First author: Ishan Kavathekar; venue: ICML 2025 MAS Workshop.* [[Paper]](https://arxiv.org/abs/2511.05269) -- First adversarial robustness benchmark for MAS.

2. **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?** (2024) `scenario: coding` `core`

   *First author: Carlos E. Jimenez; venue: ICLR 2024.* [[Paper]](https://arxiv.org/abs/2310.06770) -- Benchmark of 2294 real GitHub issues from 12 Python repos.

3. **WebArena: A Realistic Web Environment for Building Autonomous Agents** (2024) `scenario: web` `core`

   *First author: Shuyan Zhou; venue: ICLR 2024.* [[Paper]](https://arxiv.org/abs/2307.13854) -- Self-hostable realistic web environment across e-commerce/forum/gitea/wiki.

4. **GAIA: a benchmark for General AI Assistants** (2023) `core`

   *First author: Gr\'{e}goire Mialon; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2311.12983) -- 466 real-world questions easy for humans hard for LLMs; tool-use heavy.

5. **BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents** (2025) `scenario: web` `core`

   *First author: Jason Wei; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2504.12516) -- 1266 hard-to-find browsing questions; stress-tests persistent web navigation.

6. **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs** (2023) `scenario: tool_use` `core`

   *First author: Yujia Qin; venue: ICLR 2024 Spotlight.* [[Paper]](https://arxiv.org/abs/2307.16789) -- ToolBench dataset + ToolLLaMA; 16k+ RapidAPI tools.

7. **tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains** (2024) `scenario: tool_use` `core`

   *First author: Shunyu Yao; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2406.12045) -- Agent-user-tool interaction under domain-specific policies (retail/airline).

8. **OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments** (2024) `core`

   *First author: Tianbao Xie; venue: NeurIPS 2024 D&B.* [[Paper]](https://arxiv.org/abs/2404.07972) -- 369 real-computer tasks across Ubuntu/Windows/macOS for multimodal agents.

9. **MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents** (2025) `core`

   *First author: Kunlun Zhu; venue: ACL 2025.* [[Paper]](https://arxiv.org/abs/2503.01935) -- Benchmark + MARBLE framework for LLM-MAS collab/competition.

10. **AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents** (2024) `scenario: tool_use` `supporting`

   *First author: Edoardo Debenedetti; venue: NeurIPS 2024 D&B.* [[Paper]](https://arxiv.org/abs/2406.13352) -- 97 tasks + 629 security cases for prompt-injection eval on tool-using agents.

11. **Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection** (2023) `supporting`

   *First author: Kai Greshake; venue: ACM AISec 2023.* [[Paper]](https://arxiv.org/abs/2302.12173) -- Foundational paper on indirect prompt injection.

12. **InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents** (2024) `scenario: tool_use` `supporting`

   *First author: Qiusi Zhan; venue: Findings of ACL 2024.* [[Paper]](https://arxiv.org/abs/2403.02691) -- 1054 IPI test cases against tool-integrated agents.

13. **Agents Under Siege: Breaking Pragmatic Multi-Agent LLM Systems with Optimized Prompt Attacks** (2025) `supporting`

   *First author: Rana Muhammad Shahroz Khan; venue: ACL 2025.* [[Paper]](https://aclanthology.org/2025.acl-long.476/) -- Permutation-invariant attack on multi-agent topologies under bandwidth/latency constraints.

14. **A Troublemaker with Contagious Jailbreak Makes Chaos in Honest Towns** (2025) `supporting`

   *First author: Tianyi Men; venue: ACL 2025.* [[Paper]](https://arxiv.org/abs/2410.16155) -- Contagious jailbreak propagates through shared memory across agent topologies.

15. **WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks** (2025) `scenario: web` `supporting`

   *First author: Ivan Evtimov; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2504.18575) -- End-to-end web-agent prompt-injection benchmark.

16. **ArtifactsBench: Bridging the Visual-Interactive Gap in LLM Code Generation Evaluation** (2025) `reward: verifier` `scenario: coding` `supporting`

   *First author: Chenchen Zhang; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2507.04952) -- MLLM-as-Judge with temporal screenshots over 1825 tasks.

17. **CodeCriticBench: A Holistic Code Critique Benchmark for Large Language Models** (2025) `reward: verifier` `scenario: coding` `supporting`

   *First author: Alexander Zhang; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2502.16614) -- Two-task multi-difficulty critique benchmark with checklists.

18. **MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models** (2025) `scenario: tool_use` `supporting`

   *First author: Pei Wang; venue: ICLR 2025.* [[Paper]](https://arxiv.org/abs/2410.11710) -- Five-granularity tool-use benchmark.

### Surveys and Overviews (5)

1. **A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application** (2024) `partial RL` `core`

   *First author: Shuaihang Chen; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2412.17481) -- Survey of LLM-MAS architectures and applications.

2. **Multi-Agent Collaboration Mechanisms: A Survey of LLMs** (2025) `core`

   *First author: Khanh-Tung Tran; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2501.06322) -- Taxonomy of MAS collaboration mechanisms.

3. **Agentic Reasoning for Large Language Models** (2026) `partial RL` `supporting`

   *First author: Tianxin Wei; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2601.12538) -- Unified roadmap for agentic reasoning bridging thought and action.

4. **Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle** (2025) `RL` `supporting`

   *First author: Keliang Liu; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2509.16679) -- Survey of RL across LLM full lifecycle.

5. **The Landscape of Agentic Reinforcement Learning for LLMs: A Survey** (2025) `RL` `core`

   *First author: Guibin Zhang; venue: TMLR.* [[Paper]](https://arxiv.org/abs/2509.02547) -- Covers 500+ works on Agentic RL; published in TMLR.

### Industrial Systems and Reports (6)

1. **Kimi K2.5: Visual Agentic Intelligence (Tech Report)** (2026) `RL` `reward: orchestration` `credit: orchestrator` `orchestration: swarm` `scenario: research` `case`

   *First author: Kimi Team; venue: Tech Report.* [[Blog]](https://www.kimi.com/blog/kimi-k2-5.html) -- Native vision + Agent Swarm + PARL training.

2. **Kimi K2.6 Tech Blog** (2026) `partial RL` `orchestration: swarm` `scenario: coding` `case`

   *First author: Kimi Team; venue: Tech Blog.* [[Blog]](https://www.kimi.com/blog/kimi-k2-6) -- Long-horizon coding + 300-agent coordination + Claw Groups.

3. **Introducing Codex** (2025) `partial RL` `orchestration: harness` `scenario: coding` `case`

   *First author: OpenAI; venue: Blog Post.* [[Blog]](https://openai.com/index/introducing-codex/) [[Link 2]](https://openai.com/index/introducing-the-codex-app/) -- Cloud-native parallel software-engineering agent.

4. **Creating Custom Sub-Agents (Claude Code Docs)** (2025) `orchestration: harness` `scenario: coding` `case`

   *First author: Anthropic; venue: Documentation.* [[Docs]](https://docs.anthropic.com/en/docs/claude-code/sub-agents) -- Claude Code built-in and custom sub-agent specification.

5. **Our framework for developing safe and trustworthy agents** (2025) `case`

   *First author: Anthropic; venue: Blog Post.* [[Blog]](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents) -- Safe and trustworthy agent development framework.

6. **Building a C compiler with a team of parallel Claudes** (2026) `orchestration: swarm` `scenario: coding` `case`

   *First author: Anthropic Engineering; venue: Engineering Blog.* [[Blog]](https://www.anthropic.com/engineering/building-c-compiler) -- 16 parallel Claudes building a C compiler.

### Classical MARL Foundations (10)

1. **The Complexity of Decentralized Control of Markov Decision Processes** (2002) `core`

   *First author: Daniel S. Bernstein; venue: Mathematics of Operations Research.* [[Paper]](https://pubsonline.informs.org/doi/10.1287/moor.27.4.819.297) -- Original Dec-POMDP formalism; proves NEXP-complete complexity.

2. **Markov Games as a Framework for Multi-Agent Reinforcement Learning** (1994) `RL` `reward: individual` `credit: agent` `core`

   *First author: Michael L. Littman; venue: ICML.* [[Paper]](https://www.cs.duke.edu/courses/spring07/cps296.3/littman94markov.pdf) -- Foundational formulation of stochastic/Markov games for MARL.

3. **Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments** (2017) `RL` `reward: individual` `credit: agent` `orchestration: centralized` `core`

   *First author: Ryan Lowe; venue: NeurIPS 2017.* [[Paper]](https://arxiv.org/abs/1706.02275) -- MADDPG; canonical CTDE actor-critic for mixed cooperative-competitive MARL.

4. **Value-Decomposition Networks For Cooperative Multi-Agent Learning** (2018) `RL` `reward: shared` `credit: agent` `orchestration: centralized` `core`

   *First author: Peter Sunehag; venue: AAMAS 2018.* [[Paper]](https://arxiv.org/abs/1706.05296) -- VDN; additive value decomposition for joint Q from per-agent Qs.

5. **QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning** (2018) `RL` `reward: shared` `credit: agent` `orchestration: centralized` `core`

   *First author: Tabish Rashid; venue: ICML 2018.* [[Paper]](https://arxiv.org/abs/1803.11485) -- QMIX; monotonic mixing network for value factorisation.

6. **Counterfactual Multi-Agent Policy Gradients** (2018) `RL` `reward: shared` `credit: agent` `orchestration: centralized` `core`

   *First author: Jakob N. Foerster; venue: AAAI 2018.* [[Paper]](https://arxiv.org/abs/1705.08926) -- COMA; counterfactual baseline for per-agent credit assignment.

7. **The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games** (2022) `RL` `reward: shared` `credit: agent` `orchestration: centralized` `core`

   *First author: Chao Yu; venue: NeurIPS 2022 D&B.* [[Paper]](https://arxiv.org/abs/2103.01955) -- MAPPO; PPO with centralized value function for cooperative MARL.

8. **Is Independent Learning All You Need in the StarCraft Multi-Agent Challenge?** (2020) `RL` `reward: individual` `credit: agent` `supporting`

   *First author: Christian Schroeder de Witt; venue: arXiv.* [[Paper]](https://arxiv.org/abs/2011.09533) -- IPPO; independent PPO competitive with CTDE on SMAC.

9. **Shapley Q-value: A Local Reward Approach to Solve Global Reward Games** (2020) `RL` `reward: shared` `credit: agent` `orchestration: centralized` `supporting`

   *First author: Jianhong Wang; venue: AAAI 2020.* [[Paper]](https://arxiv.org/abs/1907.05707) -- Shapley value-based credit assignment in cooperative MARL.

10. **Optimal Payoff Functions for Members of Collectives** (2001) `RL` `reward: individual` `credit: agent` `supporting`

   *First author: David H. Wolpert; venue: Advances in Complex Systems.* [[Paper]](https://doi.org/10.1142/S0219525901000188) -- Difference-rewards / Wonderful Life Utility; foundational credit assignment.
<!-- END GENERATED PAPER LIST -->

## Artifact Files

| Path | Contents |
|---|---|
| `papers/papers.csv` | Retained paper pool with 18 taxonomy fields |
| `papers/excluded.csv` | Screening-decision log for excluded records |
| `papers/papers.bib` | BibTeX database used by the manuscript |
| `scripts/generate_readme_papers.py` | Regenerates the visible paper list in this README |
| `scripts/generate_stats.py` | Recomputes corpus counts and cross-tabs |
| `docs/STATS.md` | Static statistics snapshot used by the paper |
| `docs/claim_ledger.md` | Maps central claims to artifact fields and boundaries |
| `docs/search_protocol_2026-04-26.md` | Search sources, query families, screening rules, and audit hooks |
| `docs/audits/coverage_stress_test_2026-05-03.md` | Stress test for sparse-credit claims under near-miss exclusions |
| `docs/audits/independent_spotcheck_2026-05-03.md` | Independent second-pass spot-check over 32 retained rows |
| `trace-schema/trace_schema.json` | Minimal orchestration-trace JSON Schema |
| `trace-schema/example_trace.json` | Valid illustrative trace |
| `trace-schema/validate_trace.py` | Dependency-free trace validator |

## Quick Start

Regenerate the visible README paper list after editing `papers/papers.csv`:

```bash
python scripts/generate_readme_papers.py
```

Regenerate the corpus statistics:

```bash
python scripts/generate_stats.py
```

Validate the example orchestration trace:

```bash
python trace-schema/validate_trace.py trace-schema/example_trace.json
```

All commands use only the Python standard library.

## Taxonomy Fields

Each retained entry in `papers/papers.csv` is tagged with:

```text
key,title,first_author,affiliation,year,arxiv_id,venue,url,
category,is_rl,reward_type,credit_granularity,orchestration_form,
scenario,is_core,one_liner,verified,notes
```

The main controlled fields are:

| Field | Values |
|---|---|
| `category` | `rl_method`, `survey`, `benchmark`, `framework`, `industry`, `classical_marl` |
| `is_rl` | `yes`, `no`, `partial` |
| `reward_type` | `shared`, `individual`, `role`, `process`, `tool`, `debate`, `verifier`, `orchestration`, `hybrid`, `NA` |
| `credit_granularity` | `token`, `turn`, `message`, `tool`, `agent`, `role`, `orchestrator`, `team`, `NA` |
| `orchestration_form` | `centralized`, `planner_executor_critic`, `debate`, `swarm`, `hierarchical`, `harness`, `NA` |
| `scenario` | `coding`, `web`, `research`, `math`, `tool_use`, `debate`, `general`, `NA` |
| `is_core` | `core`, `supporting`, `case` |
| `verified` | `yes`, `partial`, `no` |

## Headline Counts

Current retained categories:

| Category | Entries |
|---|---:|
| RL methods | 42 |
| Benchmarks | 18 |
| Classical MARL foundations | 10 |
| Industrial systems and reports | 6 |
| Surveys | 5 |
| Frameworks | 3 |

Current sparsity signals:

| Axis | Observation |
|---|---|
| Reward type | `hybrid` appears in 15 retained entries; `shared` in 10; `orchestration` in 7 |
| Credit granularity | `agent` appears in 23 entries; `role` in 10; `orchestrator` in 8; `message` in only 2 |
| Orchestration form | `centralized` appears in 18 entries; `hierarchical` in 13; `debate` in 8 |

These counts are intended to support taxonomy claims, not field-wide prevalence estimates.

## Orchestration Trace Schema

The trace schema records the minimum event graph needed to recompute reward, credit, parallelism, cost, and trace-level safety metrics without forcing authors to expose raw prompt or tool content.

Required top-level fields:

```json
{
  "trace_id": "...",
  "task_id": "...",
  "events": [],
  "edges": [],
  "rewards": {},
  "costs": {}
}
```

Supported event types:

```text
orchestrator_decision, spawn, despawn, message, tool_call,
tool_result, return, aggregate, human_intervention, safety_event
```

Supported edge types:

```text
temporal, causal, spawn, message, tool_dependency, return,
aggregate, safety_flow
```

## Update Policy

Pull requests and issues are most useful when they identify one of:

- A missing LLM-MAS RL or post-training method that changes a reward, credit, or orchestration taxonomy cell.
- A public industrial report with explicit multi-agent training evidence rather than only deployment-shape evidence.
- A benchmark that measures collaboration quality, parallel efficiency, protocol overhead, trace-level safety, or long-trace credit behavior.
- A correction to an existing tag in `papers/papers.csv`, with a citation and short justification.

When adding a paper, update `papers/papers.csv`, regenerate this README with `python scripts/generate_readme_papers.py`, regenerate statistics with `python scripts/generate_stats.py`, and explain which taxonomy claim changes.

## Citation

```bibtex
@misc{zhang2026rl4llmmas,
  title  = {Reinforcement Learning for LLM-based Multi-Agent Systems:
            An Orchestration-Trace Taxonomy},
  author = {Chenchen Zhang},
  year   = {2026},
  note   = {Working draft and artifact repository},
  url    = {https://github.com/xxzcc/awesome-llm-mas-rl}
}
```

## License

Paper-pool metadata and trace examples are released under CC0-1.0. Scripts are released under the MIT License.
