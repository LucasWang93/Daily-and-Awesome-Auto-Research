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
- **2026-04-10** [DRBENCHER: Can Your Agent Identify the Entity, Retrieve Its Properties and Do the Math?](https://arxiv.org/abs/2604.09251v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-09251v1-drbencher-can-your-agent-identify-the-entity-retrieve-its-properties-and-do-the-math.md](archive/papers/2026-04-13/2604-09251v1-drbencher-can-your-agent-identify-the-entity-retrieve-its-properties-and-do-the-math.md)
- **2026-04-09** [EigentSearch-Q+: Enhancing Deep Research Agents with Structured Reasoning Tools](https://arxiv.org/abs/2604.07927v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-07927v1-eigentsearch-q-enhancing-deep-research-agents-with-structured-reasoning-tools.md](archive/papers/2026-04-10/2604-07927v1-eigentsearch-q-enhancing-deep-research-agents-with-structured-reasoning-tools.md)
- **2026-04-09** [A Model Context Protocol Server for Quantum Execution in Hybrid Quantum-HPC Environments](https://arxiv.org/abs/2604.08318v1) (End-to-End AI Scientists) - card: [2604-08318v1-a-model-context-protocol-server-for-quantum-execution-in-hybrid-quantum-hpc-environments.md](archive/papers/2026-04-10/2604-08318v1-a-model-context-protocol-server-for-quantum-execution-in-hybrid-quantum-hpc-environments.md)
- **2026-04-09** [Towards Knowledgeable Deep Research: Framework and Benchmark](https://arxiv.org/abs/2604.07720v1) (Literature And Survey Agents) - card: [2604-07720v1-towards-knowledgeable-deep-research-framework-and-benchmark.md](archive/papers/2026-04-10/2604-07720v1-towards-knowledgeable-deep-research-framework-and-benchmark.md)
- **2026-04-08** [Rhizome OS-1: Rhizome's Semi-Autonomous Operating System for Small Molecule Drug Discovery](https://arxiv.org/abs/2604.07512v1) (Autonomous Discovery) - card: [2604-07512v1-rhizome-os-1-rhizome-s-semi-autonomous-operating-system-for-small-molecule-drug-discovery.md](archive/papers/2026-04-10/2604-07512v1-rhizome-os-1-rhizome-s-semi-autonomous-operating-system-for-small-molecule-drug-discovery.md)
- **2026-04-07** [AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery](https://arxiv.org/abs/2604.05550v1) (Research Infrastructure And Benchmarks) - card: [2604-05550v1-autosota-an-end-to-end-automated-research-system-for-state-of-the-art-ai-model-discovery.md](archive/papers/2026-04-08/2604-05550v1-autosota-an-end-to-end-automated-research-system-for-state-of-the-art-ai-model-discovery.md)
- **2026-04-07** [Deep Researcher Agent: An Autonomous Framework for 24/7 Deep Learning Experimentation with Zero-Cost Monitoring](https://arxiv.org/abs/2604.05854v1) (Literature And Survey Agents) - card: [2604-05854v1-deep-researcher-agent-an-autonomous-framework-for-24-7-deep-learning-experimentation-with-zero-cost-monitoring.md](archive/papers/2026-04-08/2604-05854v1-deep-researcher-agent-an-autonomous-framework-for-24-7-deep-learning-experimentation-with-zero-cost-monitoring.md)
- **2026-04-07** [DataSTORM: Deep Research on Large-Scale Databases using Exploratory Data Analysis and Data Storytelling](https://arxiv.org/abs/2604.06474v1) (Literature And Survey Agents) - card: [2604-06474v1-datastorm-deep-research-on-large-scale-databases-using-exploratory-data-analysis-and-data-storytelling.md](archive/papers/2026-04-09/2604-06474v1-datastorm-deep-research-on-large-scale-databases-using-exploratory-data-analysis-and-data-storytelling.md)
- **2026-04-07** [Towards Trustworthy Report Generation: A Deep Research Agent with Progressive Confidence Estimation and Calibration](https://arxiv.org/abs/2604.05952v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-05952v1-towards-trustworthy-report-generation-a-deep-research-agent-with-progressive-confidence-estimation-and-calibration.md](archive/papers/2026-04-08/2604-05952v1-towards-trustworthy-report-generation-a-deep-research-agent-with-progressive-confidence-estimation-and-calibration.md)
- **2026-04-07** [EpiBench: Benchmarking Multi-turn Research Workflows for Multimodal Agents](https://arxiv.org/abs/2604.05557v1) (End-to-End AI Scientists) - card: [2604-05557v1-epibench-benchmarking-multi-turn-research-workflows-for-multimodal-agents.md](archive/papers/2026-04-08/2604-05557v1-epibench-benchmarking-multi-turn-research-workflows-for-multimodal-agents.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [DRBENCHER: Can Your Agent Identify the Entity, Retrieve Its Properties and Do the Math?](https://arxiv.org/abs/2604.09251v1): DRBENCHER addresses a critical gap in AI evaluation by combining browsing and computation tasks, reflecting real-world scenarios where agents must synthesize information across domains and perform complex reasoning. This benchmark pushes the boundaries of AI capabilities and highlights limitations in reasoning over dynamic, evolving datasets, paving the way for more robust and adaptable systems in research and decision-making contexts.
- [EigentSearch-Q+: Enhancing Deep Research Agents with Structured Reasoning Tools](https://arxiv.org/abs/2604.07927v1): EigentSearch-Q+ addresses a critical challenge in AI-driven research by introducing structured reasoning tools that enhance the accuracy and efficiency of deep research agents. This advancement not only improves the performance of AI models but also sets a precedent for more deliberate and transparent approaches to information retrieval and reasoning in AI systems.
- [A Model Context Protocol Server for Quantum Execution in Hybrid Quantum-HPC Environments](https://arxiv.org/abs/2604.08318v1): Quantum computing holds immense potential for solving complex scientific problems, but its practical application is hindered by the intricate management of hardware and computational resources. This framework bridges the gap by enabling AI agents to autonomously execute quantum workflows, paving the way for more accessible and scalable quantum research in hybrid environments.
- [Towards Knowledgeable Deep Research: Framework and Benchmark](https://arxiv.org/abs/2604.07720v1): As AI agents increasingly assist in research tasks, integrating structured knowledge alongside unstructured data is crucial for generating reliable, data-driven insights. This work sets a new standard for multimodal reasoning and evaluation, paving the way for more robust and comprehensive autonomous research systems that can tackle complex, expert-level inquiries across diverse domains.
- [Rhizome OS-1: Rhizome's Semi-Autonomous Operating System for Small Molecule Drug Discovery](https://arxiv.org/abs/2604.07512v1): Rhizome OS-1 represents a significant leap in drug discovery by combining AI-driven molecular generation with multi-disciplinary agent collaboration, enabling faster and more innovative approaches to identifying novel therapeutic compounds. This could accelerate the development of treatments for complex diseases like cancer, while reducing costs and increasing efficiency in early-stage research processes.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[DRBENCHER: Can Your Agent Identify the Entity, Retrieve Its Properties and Do the Math?](https://arxiv.org/abs/2604.09251v1) is the latest archived addition. Themes: End-to-End AI Scientists, Literature And Survey Agents. Why it matters: DRBENCHER addresses a critical gap in AI evaluation by combining browsing and computation tasks, reflecting real-world scenarios where agents must synthesize information across domains and perform complex reasoning. This benchmark pushes the boundaries of AI capabilities and highlights limitations in reasoning over dynamic, evolving datasets, paving the way for more robust and adaptable systems in research and decision-making contexts.
<!-- END: latest-entry -->

## License

MIT
