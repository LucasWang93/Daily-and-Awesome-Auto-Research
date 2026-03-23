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
- **2026-03-20** [Pitfalls in Evaluating Interpretability Agents](https://arxiv.org/abs/2603.20101v1) (End-to-End AI Scientists) - card: [2603-20101v1-pitfalls-in-evaluating-interpretability-agents.md](archive/papers/2026-03-23/2603-20101v1-pitfalls-in-evaluating-interpretability-agents.md)
- **2026-03-20** [Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States](https://arxiv.org/abs/2603.19987v1) (Autonomous Discovery) - card: [2603-19987v1-breaking-the-capability-ceiling-of-llm-post-training-by-reintroducing-markov-states.md](archive/papers/2026-03-23/2603-19987v1-breaking-the-capability-ceiling-of-llm-post-training-by-reintroducing-markov-states.md)
- **2026-03-19** [Total Recall QA: A Verifiable Evaluation Suite for Deep Research Agents](https://arxiv.org/abs/2603.18516v1) (End-to-End AI Scientists, Literature And Survey Agents, Research Infrastructure And Benchmarks) - card: [2603-18516v1-total-recall-qa-a-verifiable-evaluation-suite-for-deep-research-agents.md](archive/papers/2026-03-20/2603-18516v1-total-recall-qa-a-verifiable-evaluation-suite-for-deep-research-agents.md)
- **2026-03-18** [Toward Reliable, Safe, and Secure LLMs for Scientific Applications](https://arxiv.org/abs/2603.18235v1) (End-to-End AI Scientists) - card: [2603-18235v1-toward-reliable-safe-and-secure-llms-for-scientific-applications.md](archive/papers/2026-03-20/2603-18235v1-toward-reliable-safe-and-secure-llms-for-scientific-applications.md)
- **2026-03-18** [Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)](https://arxiv.org/abs/2603.17417v1) (Literature And Survey Agents) - card: [2603-17417v1-is-your-llm-as-a-recommender-agent-trustable-llms-recommendation-is-easily-hacked-by-biases-preferences.md](archive/papers/2026-03-20/2603-17417v1-is-your-llm-as-a-recommender-agent-trustable-llms-recommendation-is-easily-hacked-by-biases-preferences.md)
- **2026-03-17** [AI Scientist via Synthetic Task Scaling](https://arxiv.org/abs/2603.17216v1) (End-to-End AI Scientists) - card: [2603-17216v1-ai-scientist-via-synthetic-task-scaling.md](archive/papers/2026-03-19/2603-17216v1-ai-scientist-via-synthetic-task-scaling.md)
- **2026-03-17** [AI Scientist via Synthetic Task Scaling](https://huggingface.co/papers/2603.17216) (End-to-End AI Scientists) - card: [2603-17216-ai-scientist-via-synthetic-task-scaling.md](archive/papers/2026-03-19/2603-17216-ai-scientist-via-synthetic-task-scaling.md)
- **2026-03-17** [MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild](https://huggingface.co/papers/2603.17187) (Autoresearch Loops) - card: [2603-17187-metaclaw-just-talk-an-agent-that-meta-learns-and-evolves-in-the-wild.md](archive/papers/2026-03-19/2603-17187-metaclaw-just-talk-an-agent-that-meta-learns-and-evolves-in-the-wild.md)
- **2026-03-17** [Machine Learning Reconstruction of High-Dimensional Electronic Structure from Angle-Resolved Photoemission Spectroscopy](https://arxiv.org/abs/2603.16725v1) (Autonomous Discovery) - card: [2603-16725v1-machine-learning-reconstruction-of-high-dimensional-electronic-structure-from-angle-resolved-photoemission-spectroscopy.md](archive/papers/2026-03-20/2603-16725v1-machine-learning-reconstruction-of-high-dimensional-electronic-structure-from-angle-resolved-photoemission-spectroscopy.md)
- **2026-03-17** [VisBrowse-Bench: Benchmarking Visual-Native Search for Multimodal Browsing Agents](https://arxiv.org/abs/2603.16289v1) (Literature And Survey Agents) - card: [2603-16289v1-visbrowse-bench-benchmarking-visual-native-search-for-multimodal-browsing-agents.md](archive/papers/2026-03-18/2603-16289v1-visbrowse-bench-benchmarking-visual-native-search-for-multimodal-browsing-agents.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [Pitfalls in Evaluating Interpretability Agents](https://arxiv.org/abs/2603.20101v1): As AI models grow in complexity, understanding their inner workings becomes critical for trust, safety, and innovation. Automated interpretability agents promise to scale this understanding, but evaluating their effectiveness is fraught with challenges. This research identifies key pitfalls and proposes new evaluation methods, paving the way for more reliable and transparent AI systems.
- [Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States](https://arxiv.org/abs/2603.19987v1): This research addresses a critical limitation in how Large Language Models are refined post-training, offering a pathway to unlock genuinely novel reasoning and discovery capabilities. By revisiting classical RL principles like Markov states, it challenges the status quo of relying on extensive action histories, potentially enabling more efficient and innovative AI systems that can tackle complex, open-ended problems.
- [Total Recall QA: A Verifiable Evaluation Suite for Deep Research Agents](https://arxiv.org/abs/2603.18516v1): As large language models (LLMs) increasingly power deep research agents, ensuring their ability to accurately synthesize and reason over complex, multi-source information is critical. TRQA provides a robust, verifiable framework to evaluate these systems, addressing gaps in existing benchmarks and enabling more reliable advancements in AI-driven research capabilities.
- [Toward Reliable, Safe, and Secure LLMs for Scientific Applications](https://arxiv.org/abs/2603.18235v1): As LLMs increasingly contribute to scientific discovery, ensuring their reliability, safety, and security is critical to prevent harm and misuse while unlocking their transformative potential. This research addresses gaps in current evaluation methods and proposes robust frameworks to safeguard scientific applications of AI, fostering trust and innovation in the field.
- [Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)](https://arxiv.org/abs/2603.17417v1): As LLMs become integral to decision-making in critical domains like research, hiring, and e-commerce, their susceptibility to biases poses significant risks to fairness, reliability, and trustworthiness. Addressing these vulnerabilities is essential to ensure ethical and effective deployment of AI systems in real-world applications.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[Pitfalls in Evaluating Interpretability Agents](https://arxiv.org/abs/2603.20101v1) is the latest archived addition. Themes: End-to-End AI Scientists. Why it matters: As AI models grow in complexity, understanding their inner workings becomes critical for trust, safety, and innovation. Automated interpretability agents promise to scale this understanding, but evaluating their effectiveness is fraught with challenges. This research identifies key pitfalls and proposes new evaluation methods, paving the way for more reliable and transparent AI systems.
<!-- END: latest-entry -->

## License

MIT
