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
- **2026-03-26** [From Intent to Evidence: A Categorical Approach for Structural Evaluation of Deep Research Agents](https://arxiv.org/abs/2603.25342v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2603-25342v1-from-intent-to-evidence-a-categorical-approach-for-structural-evaluation-of-deep-research-agents.md](archive/papers/2026-03-27/2603-25342v1-from-intent-to-evidence-a-categorical-approach-for-structural-evaluation-of-deep-research-agents.md)
- **2026-03-25** [Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs](https://arxiv.org/abs/2603.24511v1) (Autoresearch Loops) - card: [2603-24511v1-claudini-autoresearch-discovers-state-of-the-art-adversarial-attack-algorithms-for-llms.md](archive/papers/2026-03-26/2603-24511v1-claudini-autoresearch-discovers-state-of-the-art-adversarial-attack-algorithms-for-llms.md)
- **2026-03-25** [From AI Assistant to AI Scientist: Autonomous Discovery of LLM-RL Algorithms with LLM Agents](https://arxiv.org/abs/2603.23951v1) (End-to-End AI Scientists, Autonomous Discovery) - card: [2603-23951v1-from-ai-assistant-to-ai-scientist-autonomous-discovery-of-llm-rl-algorithms-with-llm-agents.md](archive/papers/2026-03-26/2603-23951v1-from-ai-assistant-to-ai-scientist-autonomous-discovery-of-llm-rl-algorithms-with-llm-agents.md)
- **2026-03-25** [Can LLMs Beat Classical Hyperparameter Optimization Algorithms? A Study on autoresearch](https://arxiv.org/abs/2603.24647v1) (Autoresearch Loops) - card: [2603-24647v1-can-llms-beat-classical-hyperparameter-optimization-algorithms-a-study-on-autoresearch.md](archive/papers/2026-03-27/2603-24647v1-can-llms-beat-classical-hyperparameter-optimization-algorithms-a-study-on-autoresearch.md)
- **2026-03-24** [Bilevel Autoresearch: Meta-Autoresearching Itself](https://arxiv.org/abs/2603.23420v1) (Autoresearch Loops) - card: [2603-23420v1-bilevel-autoresearch-meta-autoresearching-itself.md](archive/papers/2026-03-26/2603-23420v1-bilevel-autoresearch-meta-autoresearching-itself.md)
- **2026-03-23** [Neural Structure Embedding for Symbolic Regression via Continuous Structure Search and Coefficient Optimization](https://arxiv.org/abs/2603.22429v1) (Closed-Loop Empirical Science) - card: [2603-22429v1-neural-structure-embedding-for-symbolic-regression-via-continuous-structure-search-and-coefficient-optimization.md](archive/papers/2026-03-25/2603-22429v1-neural-structure-embedding-for-symbolic-regression-via-continuous-structure-search-and-coefficient-optimization.md)
- **2026-03-23** [AwesomeLit: Towards Hypothesis Generation with Agent-Supported Literature Research](https://arxiv.org/abs/2603.22648v1) (Literature And Survey Agents) - card: [2603-22648v1-awesomelit-towards-hypothesis-generation-with-agent-supported-literature-research.md](archive/papers/2026-03-25/2603-22648v1-awesomelit-towards-hypothesis-generation-with-agent-supported-literature-research.md)
- **2026-03-22** [ARYA: A Physics-Constrained Composable & Deterministic World Model Architecture](https://arxiv.org/abs/2603.21340v1) (End-to-End AI Scientists) - card: [2603-21340v1-arya-a-physics-constrained-composable-deterministic-world-model-architecture.md](archive/papers/2026-03-24/2603-21340v1-arya-a-physics-constrained-composable-deterministic-world-model-architecture.md)
- **2026-03-22** [TRACE: A Multi-Agent System for Autonomous Physical Reasoning in Seismological Science](https://arxiv.org/abs/2603.21152v1) (Autonomous Discovery) - card: [2603-21152v1-trace-a-multi-agent-system-for-autonomous-physical-reasoning-in-seismological-science.md](archive/papers/2026-03-24/2603-21152v1-trace-a-multi-agent-system-for-autonomous-physical-reasoning-in-seismological-science.md)
- **2026-03-21** [LLM-ODE: Data-driven Discovery of Dynamical Systems with Large Language Models](https://arxiv.org/abs/2603.20910v1) (Closed-Loop Empirical Science) - card: [2603-20910v1-llm-ode-data-driven-discovery-of-dynamical-systems-with-large-language-models.md](archive/papers/2026-03-24/2603-20910v1-llm-ode-data-driven-discovery-of-dynamical-systems-with-large-language-models.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs](https://arxiv.org/abs/2603.24511v1): Claudini showcases the transformative potential of autoresearch pipelines powered by LLMs, enabling rapid discovery of advanced adversarial attack algorithms. This highlights both the promise and risks of autonomous AI research in critical areas like security, emphasizing the need for robust safeguards as AI systems evolve.
- [From AI Assistant to AI Scientist: Autonomous Discovery of LLM-RL Algorithms with LLM Agents](https://arxiv.org/abs/2603.23951v1): Automating the discovery of optimization algorithms for language models could significantly accelerate advancements in AI research, reducing manual effort and enabling more efficient exploration of novel mechanisms. This approach has the potential to democratize AI innovation and improve the performance of language models in practical applications.
- [Can LLMs Beat Classical Hyperparameter Optimization Algorithms? A Study on autoresearch](https://arxiv.org/abs/2603.24647v1): This research highlights the potential of combining LLMs with classical optimization techniques to improve hyperparameter tuning, a critical task in machine learning. By leveraging the strengths of both approaches, it opens up new possibilities for efficient and reliable optimization, even with smaller, cost-effective models.
- [Bilevel Autoresearch: Meta-Autoresearching Itself](https://arxiv.org/abs/2603.23420v1): Bilevel Autoresearch demonstrates the potential of AI systems to autonomously improve their own research processes, reducing reliance on human intervention and accelerating innovation. By enabling meta-optimization, this framework could revolutionize how we approach complex problems across domains, leveraging AI's ability to explore solutions beyond human intuition.
- [Neural Structure Embedding for Symbolic Regression via Continuous Structure Search and Coefficient Optimization](https://arxiv.org/abs/2603.22429v1): Symbolic regression is a cornerstone of interpretable machine learning, enabling the discovery of human-readable equations from data. By introducing continuous embeddings and optimization techniques, SRCO addresses computational inefficiencies and scalability issues in traditional methods, paving the way for faster and more robust equation discovery across diverse applications in science and engineering.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[From Intent to Evidence: A Categorical Approach for Structural Evaluation of Deep Research Agents](https://arxiv.org/abs/2603.25342v1) is the latest archived addition. Themes: End-to-End AI Scientists, Literature And Survey Agents. Why it matters: As AI systems increasingly take on roles in research and knowledge synthesis, robust evaluation methods are critical to ensure their reliability and effectiveness. This work provides a formalized, rigorous approach to stress-test deep research agents, exposing their current limitations and guiding future advancements in AI-driven research workflows.
<!-- END: latest-entry -->

## License

MIT
