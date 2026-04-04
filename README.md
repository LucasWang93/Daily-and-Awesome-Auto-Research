# Awesome Auto-Research

An English-first curated knowledge base for autoresearch loops, AI scientist systems, automated discovery frameworks, and research-agent infrastructure.

## What Is Auto-Research?

This repository follows the spirit of [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch): agents run tight research loops, modify code or plans, measure outcomes, keep what works, and accumulate progress. From that baseline, we also track broader AI scientist systems, closed-loop empirical science frameworks, and infrastructure that makes continual machine-driven research possible.

## Workflow

```bash
./run_daily_update.sh run
./run_daily_update.sh install-cron 8 0
python run.py ingest
python run.py build-readme
python run.py sync-index
python run.py curate-report
```

The default daily job is `./run_daily_update.sh run`, which wraps `python run.py ingest`, sends the daily email, stages tracked updates in `README.md`, `data/`, and `reports/`, and pushes the result to GitHub. Use `./run_daily_update.sh install-cron 8 0` to install the daily cron entry through the same script.

## Most Important GitHub Repos

<!-- BEGIN: curated-repos -->
### Reference Loop
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) [landmark]: The cleanest reference loop: an agent edits a single training file, runs a fixed-budget experiment, and keeps only the improvements. Why it matters: This is the conceptual baseline for the field because it reduces autoresearch to a tight modify-run-measure-select loop Relation to auto-research: Defines the smallest serious unit of autonomous ML research Representative reference: karpathy/autoresearch README and program.md design.

### End-to-End AI Scientist Systems
- [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) [landmark]: A widely recognized end-to-end system for idea generation, coding, experimentation, writing, and simulated review. Why it matters: It moved the discussion from isolated research subtasks to complete research-loop automation Relation to auto-research: The key milestone for end-to-end AI scientist systems Representative reference: The AI Scientist paper and project release.
- [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) [active]: A generalized successor that uses agentic tree search for open-ended scientific discovery. Why it matters: It pushes beyond rigid templates and emphasizes exploratory search over research trajectories Relation to auto-research: Represents the shift from scripted pipelines to search-based AI scientist systems Representative reference: The AI Scientist-v2 paper and release.
- [allenai/autodiscovery](https://github.com/allenai/autodiscovery) [active]: A discovery-oriented system for hypothesis search and verification driven by Bayesian surprise and MCTS. Why it matters: It anchors the scientific-discovery branch of autoresearch instead of focusing only on engineering loops Relation to auto-research: Important for open-ended hypothesis generation and validation Representative reference: Autodiscovery NeurIPS 2025 release.
- [HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher) [active]: A production-ready system for literature review, hypothesis generation, implementation, and manuscript preparation. Why it matters: It couples end-to-end automation with Scientist-Bench style evaluation Relation to auto-research: A strong reference for paper-to-implementation scientific workflows Representative reference: AI-Researcher: Autonomous Scientific Innovation.

### Closed-Loop Science Frameworks
- [AutoResearch/autora](https://github.com/AutoResearch/autora) [landmark]: A modular framework for closed-loop empirical research with theorists, experimentalists, and experiment runners. Why it matters: It predates the current AI scientist wave and gives a principled framework for automating empirical science Relation to auto-research: Core foundation for closed-loop science rather than code-only autoresearch Representative reference: AutoRA JOSS 2024.

### Literature And Review Agents
- [eimenhmdt/autoresearcher](https://github.com/eimenhmdt/autoresearcher) [prototype]: An early open-source attempt at automating scientific workflows, currently focused on literature review. Why it matters: Useful as a lightweight prototype for the literature-to-insight side of autoresearch Relation to auto-research: Relevant when research automation starts from retrieval and synthesis Representative reference: AutoResearcher project README.

### Infrastructure And Tools
- [ltjed/freephdlabor](https://github.com/ltjed/freephdlabor) [active]: A customizable multiagent framework for continual and interactive science automation. Why it matters: It emphasizes persistent workflows, modular agents, and domain customization instead of one-shot demos Relation to auto-research: Important for building durable research-agent infrastructure Representative reference: Build Your Personalized Research Group technical report.
- [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) [active]: A practical Claude Code workflow that runs research review, diagnosis, and experiment loops overnight. Why it matters: It turns autoresearch into an operational nightly workflow rather than a one-off showcase Relation to auto-research: Useful as a hands-on automation layer for code-centric research loops Representative reference: ARIS README and Claude Code skills workflow.
<!-- END: curated-repos -->

## Key Papers By Theme

<!-- BEGIN: theme-papers -->
### Autoresearch Loops
- [AutoRA: Automated Research Assistant for Closed-Loop Empirical Research](https://joss.theoj.org/papers/10.21105/joss.06839): A foundational framework for closed-loop empirical research with explicit theorist and experimentalist roles.
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292): The 2024 milestone that made end-to-end AI scientist systems concrete for ML research.

### End-to-End AI Scientists
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292): The 2024 milestone that made end-to-end AI scientist systems concrete for ML research.
- [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066): A search-based follow-up that moves beyond rigid templates toward more open-ended exploration.
- [AI-Researcher: Autonomous Scientific Innovation](https://arxiv.org/abs/2505.18705): An autonomous pipeline from literature review to implementation and manuscript generation, paired with Scientist-Bench.

### Closed-Loop Empirical Science
- [AutoRA: Automated Research Assistant for Closed-Loop Empirical Research](https://joss.theoj.org/papers/10.21105/joss.06839): A foundational framework for closed-loop empirical research with explicit theorist and experimentalist roles.

### Autonomous Discovery
- [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066): A search-based follow-up that moves beyond rigid templates toward more open-ended exploration.
- [Autodiscovery](https://github.com/allenai/autodiscovery): An open-ended discovery system centered on hypothesis search and verification.

### Literature And Survey Agents
- No landmark papers added yet.

### Research Infrastructure And Benchmarks
- [AI-Researcher: Autonomous Scientific Innovation](https://arxiv.org/abs/2505.18705): An autonomous pipeline from literature review to implementation and manuscript generation, paired with Scientist-Bench.
- [Build Your Personalized Research Group: A Multiagent Framework for Continual and Interactive Science Automation](https://arxiv.org/abs/2510.15624): A strong framework paper on persistent, customizable research groups rather than one-shot autonomous runs.
<!-- END: theme-papers -->

## Recent Additions

<!-- BEGIN: recent-papers -->
- **2026-04-02** [CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://huggingface.co/papers/2604.01658) (Autonomous Discovery) - card: [2604-01658-coral-towards-autonomous-multi-agent-evolution-for-open-ended-discovery.md](archive/papers/2026-04-04/2604-01658-coral-towards-autonomous-multi-agent-evolution-for-open-ended-discovery.md)
- **2026-04-02** [Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory](https://huggingface.co/papers/2604.01007) (Autoresearch Loops) - card: [2604-01007-omni-simplemem-autoresearch-guided-discovery-of-lifelong-multimodal-agent-memory.md](archive/papers/2026-04-03/2604-01007-omni-simplemem-autoresearch-guided-discovery-of-lifelong-multimodal-agent-memory.md)
- **2026-04-02** [CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://arxiv.org/abs/2604.01658v1) (Autonomous Discovery) - card: [2604-01658v1-coral-towards-autonomous-multi-agent-evolution-for-open-ended-discovery.md](archive/papers/2026-04-03/2604-01658v1-coral-towards-autonomous-multi-agent-evolution-for-open-ended-discovery.md)
- **2026-04-02** [LLM Agents as Social Scientists: A Human-AI Collaborative Platform for Social Science Automation](https://arxiv.org/abs/2604.01520v1) (Autoresearch Loops) - card: [2604-01520v1-llm-agents-as-social-scientists-a-human-ai-collaborative-platform-for-social-science-automation.md](archive/papers/2026-04-04/2604-01520v1-llm-agents-as-social-scientists-a-human-ai-collaborative-platform-for-social-science-automation.md)
- **2026-04-02** [Symmetry-Informed Term Filtering for Continuum Equation Discovery](https://arxiv.org/abs/2604.01592v1) (Closed-Loop Empirical Science) - card: [2604-01592v1-symmetry-informed-term-filtering-for-continuum-equation-discovery.md](archive/papers/2026-04-04/2604-01592v1-symmetry-informed-term-filtering-for-continuum-equation-discovery.md)
- **2026-04-01** [Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory](https://arxiv.org/abs/2604.01007v2) (Autoresearch Loops) - card: [2604-01007v2-omni-simplemem-autoresearch-guided-discovery-of-lifelong-multimodal-agent-memory.md](archive/papers/2026-04-03/2604-01007v2-omni-simplemem-autoresearch-guided-discovery-of-lifelong-multimodal-agent-memory.md)
- **2026-04-01** [BloClaw: An Omniscient, Multi-Modal Agentic Workspace for Next-Generation Scientific Discovery](https://arxiv.org/abs/2604.00550v1) (End-to-End AI Scientists) - card: [2604-00550v1-bloclaw-an-omniscient-multi-modal-agentic-workspace-for-next-generation-scientific-discovery.md](archive/papers/2026-04-02/2604-00550v1-bloclaw-an-omniscient-multi-modal-agentic-workspace-for-next-generation-scientific-discovery.md)
- **2026-04-01** [Predicting Dynamics of Ultra-Large Complex Systems by Inferring Governing Equations](https://arxiv.org/abs/2604.00599v1) (Closed-Loop Empirical Science) - card: [2604-00599v1-predicting-dynamics-of-ultra-large-complex-systems-by-inferring-governing-equations.md](archive/papers/2026-04-03/2604-00599v1-predicting-dynamics-of-ultra-large-complex-systems-by-inferring-governing-equations.md)
- **2026-04-01** [ORBIT: Scalable and Verifiable Data Generation for Search Agents on a Tight Budget](https://arxiv.org/abs/2604.01195v2) (Literature And Survey Agents) - card: [2604-01195v2-orbit-scalable-and-verifiable-data-generation-for-search-agents-on-a-tight-budget.md](archive/papers/2026-04-03/2604-01195v2-orbit-scalable-and-verifiable-data-generation-for-search-agents-on-a-tight-budget.md)
- **2026-04-01** [ORBIT: Scalable and Verifiable Data Generation for Search Agents on a Tight Budget](https://arxiv.org/abs/2604.01195v1) (Literature And Survey Agents) - card: [2604-01195v1-orbit-scalable-and-verifiable-data-generation-for-search-agents-on-a-tight-budget.md](archive/papers/2026-04-02/2604-01195v1-orbit-scalable-and-verifiable-data-generation-for-search-agents-on-a-tight-budget.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://huggingface.co/papers/2604.01658): CORAL represents a significant step forward in autonomous multi-agent systems, enabling more efficient and effective open-ended discovery. By reducing reliance on fixed heuristics and fostering collaboration among agents, it opens new possibilities for solving complex problems in fields like mathematics, algorithms, and systems optimization. This innovation could accelerate advancements in AI-driven research and development across multiple domains.
- [Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory](https://huggingface.co/papers/2604.01007): As AI systems increasingly operate in complex, long-term environments, their ability to effectively retain and utilize multimodal memory is critical for advancing capabilities in real-world applications. Omni-SimpleMem showcases how autonomous research pipelines can drive innovation in areas too complex for manual or traditional automated exploration, paving the way for more adaptive and intelligent AI systems.
- [CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://arxiv.org/abs/2604.01658v1): CORAL represents a significant step towards autonomous systems capable of sustained, open-ended discovery. By enabling multi-agent collaboration and knowledge reuse, it addresses the limitations of fixed heuristics and rigid exploration rules, paving the way for breakthroughs in complex problem-solving across domains like mathematics, algorithms, and systems optimization.
- [Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory](https://arxiv.org/abs/2604.01007v2): As AI systems increasingly operate over long time horizons, their ability to effectively manage and recall multimodal experiences is critical for real-world applications. Omni-SimpleMem demonstrates how autonomous research pipelines can surpass traditional methods by uncovering impactful design improvements, paving the way for more robust and adaptive lifelong AI systems.
- [BloClaw: An Omniscient, Multi-Modal Agentic Workspace for Next-Generation Scientific Discovery](https://arxiv.org/abs/2604.00550v1): BloClaw addresses critical limitations in deploying AI-driven research environments by introducing robust infrastructural solutions for handling complex scientific workflows. Its innovations in data routing, visualization, and adaptive interfaces pave the way for more reliable and versatile AI research assistants, accelerating scientific discovery in life sciences and beyond.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://huggingface.co/papers/2604.01658) is the latest archived addition. Themes: Autonomous Discovery. Why it matters: CORAL represents a significant step forward in autonomous multi-agent systems, enabling more efficient and effective open-ended discovery. By reducing reliance on fixed heuristics and fostering collaboration among agents, it opens new possibilities for solving complex problems in fields like mathematics, algorithms, and systems optimization. This innovation could accelerate advancements in AI-driven research and development across multiple domains.
<!-- END: latest-entry -->

## License

MIT
