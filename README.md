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
- **2026-04-07** [AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery](https://arxiv.org/abs/2604.05550v1) (Research Infrastructure And Benchmarks) - card: [2604-05550v1-autosota-an-end-to-end-automated-research-system-for-state-of-the-art-ai-model-discovery.md](archive/papers/2026-04-08/2604-05550v1-autosota-an-end-to-end-automated-research-system-for-state-of-the-art-ai-model-discovery.md)
- **2026-04-07** [Deep Researcher Agent: An Autonomous Framework for 24/7 Deep Learning Experimentation with Zero-Cost Monitoring](https://arxiv.org/abs/2604.05854v1) (Literature And Survey Agents) - card: [2604-05854v1-deep-researcher-agent-an-autonomous-framework-for-24-7-deep-learning-experimentation-with-zero-cost-monitoring.md](archive/papers/2026-04-08/2604-05854v1-deep-researcher-agent-an-autonomous-framework-for-24-7-deep-learning-experimentation-with-zero-cost-monitoring.md)
- **2026-04-07** [Towards Trustworthy Report Generation: A Deep Research Agent with Progressive Confidence Estimation and Calibration](https://arxiv.org/abs/2604.05952v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-05952v1-towards-trustworthy-report-generation-a-deep-research-agent-with-progressive-confidence-estimation-and-calibration.md](archive/papers/2026-04-08/2604-05952v1-towards-trustworthy-report-generation-a-deep-research-agent-with-progressive-confidence-estimation-and-calibration.md)
- **2026-04-07** [EpiBench: Benchmarking Multi-turn Research Workflows for Multimodal Agents](https://arxiv.org/abs/2604.05557v1) (End-to-End AI Scientists) - card: [2604-05557v1-epibench-benchmarking-multi-turn-research-workflows-for-multimodal-agents.md](archive/papers/2026-04-08/2604-05557v1-epibench-benchmarking-multi-turn-research-workflows-for-multimodal-agents.md)
- **2026-04-06** [Memory Intelligence Agent](https://arxiv.org/abs/2604.04503v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-04503v1-memory-intelligence-agent.md](archive/papers/2026-04-07/2604-04503v1-memory-intelligence-agent.md)
- **2026-04-06** [Memory Intelligence Agent](https://huggingface.co/papers/2604.04503) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-04503-memory-intelligence-agent.md](archive/papers/2026-04-07/2604-04503-memory-intelligence-agent.md)
- **2026-04-06** [RoboPhD: Evolving Diverse Complex Agents Under Tight Evaluation Budgets](https://arxiv.org/abs/2604.04347v1) (Autoresearch Loops) - card: [2604-04347v1-robophd-evolving-diverse-complex-agents-under-tight-evaluation-budgets.md](archive/papers/2026-04-07/2604-04347v1-robophd-evolving-diverse-complex-agents-under-tight-evaluation-budgets.md)
- **2026-04-06** [Memory Intelligence Agent](https://arxiv.org/abs/2604.04503v2) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-04503v2-memory-intelligence-agent.md](archive/papers/2026-04-08/2604-04503v2-memory-intelligence-agent.md)
- **2026-04-05** [GeoBrowse: A Geolocation Benchmark for Agentic Tool Use with Expert-Annotated Reasoning Traces](https://arxiv.org/abs/2604.04017v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-04017v1-geobrowse-a-geolocation-benchmark-for-agentic-tool-use-with-expert-annotated-reasoning-traces.md](archive/papers/2026-04-07/2604-04017v1-geobrowse-a-geolocation-benchmark-for-agentic-tool-use-with-expert-annotated-reasoning-traces.md)
- **2026-04-03** [Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents](https://arxiv.org/abs/2604.03173v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-03173v1-detecting-and-correcting-reference-hallucinations-in-commercial-llms-and-deep-research-agents.md](archive/papers/2026-04-06/2604-03173v1-detecting-and-correcting-reference-hallucinations-in-commercial-llms-and-deep-research-agents.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery](https://arxiv.org/abs/2604.05550v1): AutoSOTA addresses the growing complexity and time demands of AI research by automating the pipeline for reproducing and improving SOTA models. This system not only accelerates innovation but also serves as a foundational infrastructure for researchers, enabling them to focus on creative and high-level scientific tasks rather than repetitive experimentation. Its success across diverse domains highlights its potential to transform how AI research is conducted globally.
- [Deep Researcher Agent: An Autonomous Framework for 24/7 Deep Learning Experimentation with Zero-Cost Monitoring](https://arxiv.org/abs/2604.05854v1): Deep Researcher Agent represents a significant step forward in automating deep learning research, enabling continuous experimentation with minimal costs and resource usage. By addressing challenges like monitoring expenses, memory limitations, and token overhead, it democratizes access to high-efficiency AI research tools, making advanced experimentation feasible for a broader audience of researchers and developers.
- [Memory Intelligence Agent](https://arxiv.org/abs/2604.04503v1): As AI systems increasingly tackle complex reasoning tasks, efficient memory management and autonomous evolution are critical for scalability and adaptability. The MIA framework addresses key limitations in existing memory systems, paving the way for more capable and self-improving AI agents that can operate effectively in dynamic, open-world environments.
- [Memory Intelligence Agent](https://huggingface.co/papers/2604.04503): The MIA framework addresses critical limitations in memory systems for deep research agents, enabling more efficient reasoning, reduced storage costs, and autonomous evolution. By integrating advanced memory management and learning mechanisms, it paves the way for scalable AI systems capable of adapting and improving in real-time, which is crucial for tackling complex, open-world problems in research and beyond.
- [RoboPhD: Evolving Diverse Complex Agents Under Tight Evaluation Budgets](https://arxiv.org/abs/2604.04347v1): As AI systems increasingly rely on iterative optimization under constrained resources, RoboPhD offers a novel, efficient approach to evolving complex agents without splitting resources for validation. This enables breakthroughs in domains where evaluations are costly, such as human-in-the-loop tasks or computationally expensive simulations, driving progress in scalable AI research and applications.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery](https://arxiv.org/abs/2604.05550v1) is the latest archived addition. Themes: Research Infrastructure And Benchmarks. Why it matters: AutoSOTA addresses the growing complexity and time demands of AI research by automating the pipeline for reproducing and improving SOTA models. This system not only accelerates innovation but also serves as a foundational infrastructure for researchers, enabling them to focus on creative and high-level scientific tasks rather than repetitive experimentation. Its success across diverse domains highlights its potential to transform how AI research is conducted globally.
<!-- END: latest-entry -->

## License

MIT
