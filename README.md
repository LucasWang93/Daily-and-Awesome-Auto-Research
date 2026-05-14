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
- **2026-05-13** [ViDR: Grounding Multimodal Deep Research Reports in Source Visual Evidence](https://arxiv.org/abs/2605.13034v1) (Literature And Survey Agents) - card: [2605-13034v1-vidr-grounding-multimodal-deep-research-reports-in-source-visual-evidence.md](archive/papers/2026-05-14/2605-13034v1-vidr-grounding-multimodal-deep-research-reports-in-source-visual-evidence.md)
- **2026-05-12** [AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration -- Learning from Cheap, Optimizing Expensive](https://huggingface.co/papers/2605.11518) (End-to-End AI Scientists) - card: [2605-11518-autollmresearch-training-research-agents-for-automating-llm-experiment-configuration-learning-from-cheap-optimizing-expensive.md](archive/papers/2026-05-13/2605-11518-autollmresearch-training-research-agents-for-automating-llm-experiment-configuration-learning-from-cheap-optimizing-expensive.md)
- **2026-05-12** [AgentDisCo: Towards Disentanglement and Collaboration in Open-ended Deep Research Agents](https://arxiv.org/abs/2605.11732v1) (Autoresearch Loops, End-to-End AI Scientists, Literature And Survey Agents, Research Infrastructure And Benchmarks) - card: [2605-11732v1-agentdisco-towards-disentanglement-and-collaboration-in-open-ended-deep-research-agents.md](archive/papers/2026-05-13/2605-11732v1-agentdisco-towards-disentanglement-and-collaboration-in-open-ended-deep-research-agents.md)
- **2026-05-12** [AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration -- Learning from Cheap, Optimizing Expensive](https://arxiv.org/abs/2605.11518v1) (End-to-End AI Scientists) - card: [2605-11518v1-autollmresearch-training-research-agents-for-automating-llm-experiment-configuration-learning-from-cheap-optimizing-expensive.md](archive/papers/2026-05-13/2605-11518v1-autollmresearch-training-research-agents-for-automating-llm-experiment-configuration-learning-from-cheap-optimizing-expensive.md)
- **2026-05-12** [Automated multiphase identification and refinement in powder diffraction using mismatch-tolerant machine learning](https://arxiv.org/abs/2605.12478v1) (Autonomous Discovery) - card: [2605-12478v1-automated-multiphase-identification-and-refinement-in-powder-diffraction-using-mismatch-tolerant-machine-learning.md](archive/papers/2026-05-13/2605-12478v1-automated-multiphase-identification-and-refinement-in-powder-diffraction-using-mismatch-tolerant-machine-learning.md)
- **2026-05-12** [Deep Reasoning in General Purpose Agents via Structured Meta-Cognition](https://arxiv.org/abs/2605.11388v1) (Literature And Survey Agents) - card: [2605-11388v1-deep-reasoning-in-general-purpose-agents-via-structured-meta-cognition.md](archive/papers/2026-05-13/2605-11388v1-deep-reasoning-in-general-purpose-agents-via-structured-meta-cognition.md)
- **2026-05-12** [PresentAgent-2: Towards Generalist Multimodal Presentation Agents](https://arxiv.org/abs/2605.11363v1) (Literature And Survey Agents) - card: [2605-11363v1-presentagent-2-towards-generalist-multimodal-presentation-agents.md](archive/papers/2026-05-14/2605-11363v1-presentagent-2-towards-generalist-multimodal-presentation-agents.md)
- **2026-05-12** [PresentAgent-2: Towards Generalist Multimodal Presentation Agents](https://huggingface.co/papers/2605.11363) (Literature And Survey Agents) - card: [2605-11363-presentagent-2-towards-generalist-multimodal-presentation-agents.md](archive/papers/2026-05-14/2605-11363-presentagent-2-towards-generalist-multimodal-presentation-agents.md)
- **2026-05-11** [GRAFT-ATHENA: Self-Improving Agentic Teams for Autonomous Discovery and Evolutionary Numerical Algorithms](https://arxiv.org/abs/2605.11117v1) (Autonomous Discovery) - card: [2605-11117v1-graft-athena-self-improving-agentic-teams-for-autonomous-discovery-and-evolutionary-numerical-algorithms.md](archive/papers/2026-05-13/2605-11117v1-graft-athena-self-improving-agentic-teams-for-autonomous-discovery-and-evolutionary-numerical-algorithms.md)
- **2026-05-11** [RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](https://arxiv.org/abs/2605.10899v1) (End-to-End AI Scientists, Literature And Survey Agents, Research Infrastructure And Benchmarks) - card: [2605-10899v1-rubricem-meta-rl-with-rubric-guided-policy-decomposition-beyond-verifiable-rewards.md](archive/papers/2026-05-12/2605-10899v1-rubricem-meta-rl-with-rubric-guided-policy-decomposition-beyond-verifiable-rewards.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration -- Learning from Cheap, Optimizing Expensive](https://huggingface.co/papers/2605.11518): Configuring large language model experiments is a costly and complex process that often relies on expert intuition, making it inaccessible and inefficient. AutoLLMResearch addresses this challenge by automating the process, enabling researchers to optimize configurations with fewer resources and greater accuracy, potentially accelerating advancements in LLM research and reducing computational waste.
- [AgentDisCo: Towards Disentanglement and Collaboration in Open-ended Deep Research Agents](https://arxiv.org/abs/2605.11732v1): AgentDisCo represents a significant step forward in automating deep research workflows, enabling AI systems to independently explore, refine, and synthesize knowledge. By disentangling exploration and exploitation processes, it enhances the quality and relevance of research outputs while reducing human intervention. Its ability to personalize research recommendations based on user behavior could transform how individuals and organizations access and utilize information in real-time contexts.
- [AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration -- Learning from Cheap, Optimizing Expensive](https://arxiv.org/abs/2605.11518v1): Configuring large language model (LLM) experiments is a resource-intensive and complex process that often relies on expert intuition. AutoLLMResearch addresses this challenge by automating the process, enabling researchers to efficiently optimize LLM configurations while reducing computational waste and accelerating innovation in AI research. This framework could democratize access to advanced LLM experimentation by lowering the barrier to entry for non-expert researchers.
- [Automated multiphase identification and refinement in powder diffraction using mismatch-tolerant machine learning](https://arxiv.org/abs/2605.12478v1): Automating phase identification in powder diffraction is critical for accelerating materials discovery and characterization. RADAR-PD bridges a significant gap, particularly in neutron diffraction, by providing a robust, auditable, and instrument-agnostic solution. This advancement enables researchers to streamline workflows and focus on innovation rather than manual analysis bottlenecks.
- [PresentAgent-2: Towards Generalist Multimodal Presentation Agents](https://arxiv.org/abs/2605.11363v1): PresentAgent-2 represents a significant step forward in automating the creation of dynamic, research-grounded presentations, making it easier for users to communicate complex ideas effectively using multimodal media and interactive features. This innovation has potential applications in education, business, and content creation, where engaging presentations are crucial.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[ViDR: Grounding Multimodal Deep Research Reports in Source Visual Evidence](https://arxiv.org/abs/2605.13034v1) is the latest archived addition. Themes: Literature And Survey Agents. Why it matters: ViDR addresses a critical gap in multimodal research systems by leveraging source visual evidence, such as figures and charts, to enhance the grounding, accuracy, and verifiability of long-form research reports. This innovation is crucial for advancing the reliability of AI-generated scientific outputs, particularly in domains where visual data is integral to analysis and communication.
<!-- END: latest-entry -->

## License

MIT
