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
- **2026-04-14** [Towards grounded autonomous research: an end-to-end LLM mini research loop on published computational physics](https://arxiv.org/abs/2604.12198v1) (Autoresearch Loops) - card: [2604-12198v1-towards-grounded-autonomous-research-an-end-to-end-llm-mini-research-loop-on-published-computational-physics.md](archive/papers/2026-04-15/2604-12198v1-towards-grounded-autonomous-research-an-end-to-end-llm-mini-research-loop-on-published-computational-physics.md)
- **2026-04-13** [PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers](https://arxiv.org/abs/2604.11307v1) (Literature And Survey Agents) - card: [2604-11307v1-paperscope-a-multi-modal-multi-document-benchmark-for-agentic-deep-research-across-massive-scientific-papers.md](archive/papers/2026-04-14/2604-11307v1-paperscope-a-multi-modal-multi-document-benchmark-for-agentic-deep-research-across-massive-scientific-papers.md)
- **2026-04-13** [Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks](https://arxiv.org/abs/2604.11753v1) (Literature And Survey Agents) - card: [2604-11753v1-agentic-aggregation-for-parallel-scaling-of-long-horizon-agentic-tasks.md](archive/papers/2026-04-14/2604-11753v1-agentic-aggregation-for-parallel-scaling-of-long-horizon-agentic-tasks.md)
- **2026-04-13** [CocoaBench: Evaluating Unified Digital Agents in the Wild](https://arxiv.org/abs/2604.11201v1) (Literature And Survey Agents) - card: [2604-11201v1-cocoabench-evaluating-unified-digital-agents-in-the-wild.md](archive/papers/2026-04-14/2604-11201v1-cocoabench-evaluating-unified-digital-agents-in-the-wild.md)
- **2026-04-13** [CocoaBench: Evaluating Unified Digital Agents in the Wild](https://huggingface.co/papers/2604.11201) (Literature And Survey Agents) - card: [2604-11201-cocoabench-evaluating-unified-digital-agents-in-the-wild.md](archive/papers/2026-04-14/2604-11201-cocoabench-evaluating-unified-digital-agents-in-the-wild.md)
- **2026-04-13** [Agentic LLM Reasoning in a Self-Driving Laboratory for Air-Sensitive Lithium Halide Spinel Conductors](https://arxiv.org/abs/2604.11957v1) (Autonomous Discovery) - card: [2604-11957v1-agentic-llm-reasoning-in-a-self-driving-laboratory-for-air-sensitive-lithium-halide-spinel-conductors.md](archive/papers/2026-04-15/2604-11957v1-agentic-llm-reasoning-in-a-self-driving-laboratory-for-air-sensitive-lithium-halide-spinel-conductors.md)
- **2026-04-13** [Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks](https://huggingface.co/papers/2604.11753) (Literature And Survey Agents) - card: [2604-11753-agentic-aggregation-for-parallel-scaling-of-long-horizon-agentic-tasks.md](archive/papers/2026-04-15/2604-11753-agentic-aggregation-for-parallel-scaling-of-long-horizon-agentic-tasks.md)
- **2026-04-13** [Spatial Atlas: Compute-Grounded Reasoning for Spatial-Aware Research Agent Benchmarks](https://arxiv.org/abs/2604.12102v1) (End-to-End AI Scientists) - card: [2604-12102v1-spatial-atlas-compute-grounded-reasoning-for-spatial-aware-research-agent-benchmarks.md](archive/papers/2026-04-15/2604-12102v1-spatial-atlas-compute-grounded-reasoning-for-spatial-aware-research-agent-benchmarks.md)
- **2026-04-13** [AgentWebBench: Benchmarking Multi-Agent Coordination in Agentic Web](https://arxiv.org/abs/2604.10938v1) (Literature And Survey Agents) - card: [2604-10938v1-agentwebbench-benchmarking-multi-agent-coordination-in-agentic-web.md](archive/papers/2026-04-14/2604-10938v1-agentwebbench-benchmarking-multi-agent-coordination-in-agentic-web.md)
- **2026-04-12** [Camyla: Scaling Autonomous Research in Medical Image Segmentation](https://arxiv.org/abs/2604.10696v1) (End-to-End AI Scientists) - card: [2604-10696v1-camyla-scaling-autonomous-research-in-medical-image-segmentation.md](archive/papers/2026-04-14/2604-10696v1-camyla-scaling-autonomous-research-in-medical-image-segmentation.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [Towards grounded autonomous research: an end-to-end LLM mini research loop on published computational physics](https://arxiv.org/abs/2604.12198v1): This work showcases the potential for autonomous AI systems to contribute meaningfully to complex, real-world scientific research by grounding their reasoning in physical truths and existing literature. It represents a step toward scalable, automated scientific discovery, which could accelerate progress in fields like computational physics and beyond.
- [PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers](https://arxiv.org/abs/2604.11307v1): PaperScope addresses a critical gap in evaluating AI systems for scientific research, focusing on multi-modal and multi-document reasoning. By providing a structured benchmark, it enables the development of systems capable of integrating complex evidence across diverse scientific sources, which is essential for advancing AI-driven research workflows and tackling real-world scientific challenges.
- [Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks](https://arxiv.org/abs/2604.11753v1): As AI systems tackle increasingly complex tasks like deep research and agentic search, efficient methods for scaling and synthesizing information are crucial. AggAgent introduces a novel approach to aggregate parallel trajectories, enabling better performance and cost-efficiency in handling long-horizon, multi-turn tasks. This advancement could significantly enhance the capabilities of AI in domains requiring nuanced reasoning and decision-making over extended periods.
- [CocoaBench: Evaluating Unified Digital Agents in the Wild](https://arxiv.org/abs/2604.11201v1): As AI systems increasingly integrate diverse capabilities, evaluating their performance on complex, real-world tasks becomes critical. CocoaBench addresses this by providing a benchmark that tests unified agents on tasks requiring flexible composition of skills, highlighting areas for improvement in reasoning, planning, and execution. This research pushes the boundaries of what AI agents can achieve in practical applications, paving the way for more robust and versatile systems.
- [Agentic LLM Reasoning in a Self-Driving Laboratory for Air-Sensitive Lithium Halide Spinel Conductors](https://arxiv.org/abs/2604.11957v1): This research demonstrates a scalable approach to autonomous materials discovery, addressing the challenge of synthesizing air-sensitive compounds. By combining advanced robotics and agentic AI reasoning, it opens new pathways for accelerating innovation in solid-state materials critical for energy storage and electronics applications.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[Towards grounded autonomous research: an end-to-end LLM mini research loop on published computational physics](https://arxiv.org/abs/2604.12198v1) is the latest archived addition. Themes: Autoresearch Loops. Why it matters: This work showcases the potential for autonomous AI systems to contribute meaningfully to complex, real-world scientific research by grounding their reasoning in physical truths and existing literature. It represents a step toward scalable, automated scientific discovery, which could accelerate progress in fields like computational physics and beyond.
<!-- END: latest-entry -->

## License

MIT
