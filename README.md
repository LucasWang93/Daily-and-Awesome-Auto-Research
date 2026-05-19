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
- **2026-05-18** [Qumus: Realization of An Embodied AI Quantum Material Experimentalist](https://arxiv.org/abs/2605.18407v1) (Closed-Loop Empirical Science) - card: [2605-18407v1-qumus-realization-of-an-embodied-ai-quantum-material-experimentalist.md](archive/papers/2026-05-19/2605-18407v1-qumus-realization-of-an-embodied-ai-quantum-material-experimentalist.md)
- **2026-05-18** [STRIDE: A Self-Reflective Agent Framework for Reliable Automatic Equation Discovery](https://arxiv.org/abs/2605.17790v1) (Closed-Loop Empirical Science) - card: [2605-17790v1-stride-a-self-reflective-agent-framework-for-reliable-automatic-equation-discovery.md](archive/papers/2026-05-19/2605-17790v1-stride-a-self-reflective-agent-framework-for-reliable-automatic-equation-discovery.md)
- **2026-05-18** [Real-time Multi-instrument Autonomous Discovery of Novel Phase-change Memory Materials](https://arxiv.org/abs/2605.18033v1) (Autonomous Discovery) - card: [2605-18033v1-real-time-multi-instrument-autonomous-discovery-of-novel-phase-change-memory-materials.md](archive/papers/2026-05-19/2605-18033v1-real-time-multi-instrument-autonomous-discovery-of-novel-phase-change-memory-materials.md)
- **2026-05-17** [Evaluating Deep Research Agents on Expert Consulting Work: A Benchmark with Verifiers, Rubrics, and Cognitive Traps](https://arxiv.org/abs/2605.17554v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2605-17554v1-evaluating-deep-research-agents-on-expert-consulting-work-a-benchmark-with-verifiers-rubrics-and-cognitive-traps.md](archive/papers/2026-05-19/2605-17554v1-evaluating-deep-research-agents-on-expert-consulting-work-a-benchmark-with-verifiers-rubrics-and-cognitive-traps.md)
- **2026-05-17** [FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics](https://arxiv.org/abs/2605.17373v1) (End-to-End AI Scientists) - card: [2605-17373v1-fml-bench-a-controlled-study-of-ai-research-agent-strategies-from-the-perspective-of-search-dynamics.md](archive/papers/2026-05-19/2605-17373v1-fml-bench-a-controlled-study-of-ai-research-agent-strategies-from-the-perspective-of-search-dynamics.md)
- **2026-05-15** [Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design](https://huggingface.co/papers/2605.15871) (Autoresearch Loops, Research Infrastructure And Benchmarks) - card: [2605-15871-agentic-discovery-of-neural-architectures-aira-compose-and-aira-design.md](archive/papers/2026-05-18/2605-15871-agentic-discovery-of-neural-architectures-aira-compose-and-aira-design.md)
- **2026-05-15** [Argus: Evidence Assembly for Scalable Deep Research Agents](https://arxiv.org/abs/2605.16217v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2605-16217v1-argus-evidence-assembly-for-scalable-deep-research-agents.md](archive/papers/2026-05-18/2605-16217v1-argus-evidence-assembly-for-scalable-deep-research-agents.md)
- **2026-05-14** [Beyond AI as Assistants: Toward Autonomous Discovery in Cosmology](https://arxiv.org/abs/2605.14791v1) (End-to-End AI Scientists, Autonomous Discovery) - card: [2605-14791v1-beyond-ai-as-assistants-toward-autonomous-discovery-in-cosmology.md](archive/papers/2026-05-15/2605-14791v1-beyond-ai-as-assistants-toward-autonomous-discovery-in-cosmology.md)
- **2026-05-14** [Agentic Design of Compositional Descriptors via Autoresearch for Materials Science Applications](https://arxiv.org/abs/2605.14671v1) (Autoresearch Loops, End-to-End AI Scientists) - card: [2605-14671v1-agentic-design-of-compositional-descriptors-via-autoresearch-for-materials-science-applications.md](archive/papers/2026-05-15/2605-14671v1-agentic-design-of-compositional-descriptors-via-autoresearch-for-materials-science-applications.md)
- **2026-05-13** [EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents](https://arxiv.org/abs/2605.13941v1) (Autoresearch Loops) - card: [2605-13941v1-evolvemem-self-evolving-memory-architecture-via-autoresearch-for-llm-agents.md](archive/papers/2026-05-15/2605-13941v1-evolvemem-self-evolving-memory-architecture-via-autoresearch-for-llm-agents.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [Qumus: Realization of An Embodied AI Quantum Material Experimentalist](https://arxiv.org/abs/2605.18407v1): Qumus represents a groundbreaking step in integrating AI into real-world scientific discovery, particularly in the complex field of quantum materials. By autonomously navigating the entire experimental process, it demonstrates the potential for AI to not only assist but lead in cutting-edge research, reducing human intervention and accelerating innovation in materials science and nanotechnology.
- [STRIDE: A Self-Reflective Agent Framework for Reliable Automatic Equation Discovery](https://arxiv.org/abs/2605.17790v1): STRIDE addresses key limitations in current equation discovery systems by introducing a self-reflective, closed-loop framework that improves reliability and robustness. This innovation has the potential to advance symbolic regression and scientific discovery by enabling more accurate and interpretable models, even in challenging out-of-distribution scenarios.
- [Evaluating Deep Research Agents on Expert Consulting Work: A Benchmark with Verifiers, Rubrics, and Cognitive Traps](https://arxiv.org/abs/2605.17554v1): As deep research agents are rapidly integrated into enterprise workflows, their ability to produce reliable, decision-grade outputs is critical. This study provides a rigorous benchmark to evaluate their performance, uncovering key limitations and failure modes that must be addressed to ensure trust and utility in high-stakes applications like consulting and research synthesis.
- [FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics](https://arxiv.org/abs/2605.17373v1): FML-Bench provides a controlled framework to rigorously evaluate and compare AI research agent strategies, offering insights into how different approaches perform under varying conditions. This helps advance the development of more effective AI systems for automating scientific discovery, a critical step toward scalable and efficient research processes in machine learning and beyond.
- [Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design](https://huggingface.co/papers/2605.15871): This research showcases the potential of AI agents to autonomously design and optimize neural architectures, paving the way for faster, more efficient development of next-generation foundation models. By achieving performance on par with or exceeding human-designed baselines, it highlights a significant step toward recursive self-improvement in AI systems, which could revolutionize how foundational AI technologies are developed and scaled.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[Qumus: Realization of An Embodied AI Quantum Material Experimentalist](https://arxiv.org/abs/2605.18407v1) is the latest archived addition. Themes: Closed-Loop Empirical Science. Why it matters: Qumus represents a groundbreaking step in integrating AI into real-world scientific discovery, particularly in the complex field of quantum materials. By autonomously navigating the entire experimental process, it demonstrates the potential for AI to not only assist but lead in cutting-edge research, reducing human intervention and accelerating innovation in materials science and nanotechnology.
<!-- END: latest-entry -->

## License

MIT
