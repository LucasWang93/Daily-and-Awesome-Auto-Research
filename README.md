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
- **2026-05-11** [RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](https://arxiv.org/abs/2605.10899v1) (End-to-End AI Scientists, Literature And Survey Agents, Research Infrastructure And Benchmarks) - card: [2605-10899v1-rubricem-meta-rl-with-rubric-guided-policy-decomposition-beyond-verifiable-rewards.md](archive/papers/2026-05-12/2605-10899v1-rubricem-meta-rl-with-rubric-guided-policy-decomposition-beyond-verifiable-rewards.md)
- **2026-05-11** [Hypothesis-Driven Deep Research with Large Language Models: A Structured Methodology for Automated Knowledge Discovery](https://arxiv.org/abs/2605.10224v1) (Literature And Survey Agents) - card: [2605-10224v1-hypothesis-driven-deep-research-with-large-language-models-a-structured-methodology-for-automated-knowledge-discovery.md](archive/papers/2026-05-12/2605-10224v1-hypothesis-driven-deep-research-with-large-language-models-a-structured-methodology-for-automated-knowledge-discovery.md)
- **2026-05-11** [SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems](https://arxiv.org/abs/2605.10246v1) (End-to-End AI Scientists) - card: [2605-10246v1-sciintegrity-bench-a-benchmark-for-evaluating-academic-integrity-in-ai-scientist-systems.md](archive/papers/2026-05-12/2605-10246v1-sciintegrity-bench-a-benchmark-for-evaluating-academic-integrity-in-ai-scientist-systems.md)
- **2026-05-11** [Personalized Deep Research: A User-Centric Framework, Dataset, and Hybrid Evaluation for Knowledge Discovery](https://arxiv.org/abs/2605.10530v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2605-10530v1-personalized-deep-research-a-user-centric-framework-dataset-and-hybrid-evaluation-for-knowledge-discovery.md](archive/papers/2026-05-12/2605-10530v1-personalized-deep-research-a-user-centric-framework-dataset-and-hybrid-evaluation-for-knowledge-discovery.md)
- **2026-05-10** [LEVI: Stronger Search Architectures Can Substitute for Larger LLMs in Evolutionary Search](https://arxiv.org/abs/2605.09764v1) (Research Infrastructure And Benchmarks) - card: [2605-09764v1-levi-stronger-search-architectures-can-substitute-for-larger-llms-in-evolutionary-search.md](archive/papers/2026-05-12/2605-09764v1-levi-stronger-search-architectures-can-substitute-for-larger-llms-in-evolutionary-search.md)
- **2026-05-09** [Agentic MIP Research: Accelerated Constraint Handler Generation](https://arxiv.org/abs/2605.09186v1) (Autoresearch Loops) - card: [2605-09186v1-agentic-mip-research-accelerated-constraint-handler-generation.md](archive/papers/2026-05-12/2605-09186v1-agentic-mip-research-accelerated-constraint-handler-generation.md)
- **2026-04-29** [HalluCiteChecker: A Lightweight Toolkit for Hallucinated Citation Detection and Verification in the Era of AI Scientists](https://arxiv.org/abs/2604.26835v1) (End-to-End AI Scientists) - card: [2604-26835v1-hallucitechecker-a-lightweight-toolkit-for-hallucinated-citation-detection-and-verification-in-the-era-of-ai-scientists.md](archive/papers/2026-04-30/2604-26835v1-hallucitechecker-a-lightweight-toolkit-for-hallucinated-citation-detection-and-verification-in-the-era-of-ai-scientists.md)
- **2026-04-29** [From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets](https://arxiv.org/abs/2604.26747v1) (Autonomous Discovery) - card: [2604-26747v1-from-hypotheses-to-factors-constrained-llm-agents-in-cryptocurrency-markets.md](archive/papers/2026-04-30/2604-26747v1-from-hypotheses-to-factors-constrained-llm-agents-in-cryptocurrency-markets.md)
- **2026-04-28** [AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery](https://arxiv.org/abs/2604.25256v1) (Autoresearch Loops, Literature And Survey Agents) - card: [2604-25256v1-autoresearchbench-benchmarking-ai-agents-on-complex-scientific-literature-discovery.md](archive/papers/2026-04-30/2604-25256v1-autoresearchbench-benchmarking-ai-agents-on-complex-scientific-literature-discovery.md)
- **2026-04-28** [AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery](https://huggingface.co/papers/2604.25256) (Autoresearch Loops, Literature And Survey Agents) - card: [2604-25256-autoresearchbench-benchmarking-ai-agents-on-complex-scientific-literature-discovery.md](archive/papers/2026-04-29/2604-25256-autoresearchbench-benchmarking-ai-agents-on-complex-scientific-literature-discovery.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](https://arxiv.org/abs/2605.10899v1): RubricEM addresses the challenge of training AI systems for complex, long-horizon research tasks where traditional verifiable rewards are insufficient. By leveraging rubrics as a central structuring mechanism, it enables more effective planning, feedback, and learning, pushing the boundaries of AI's ability to perform autonomous research and synthesis. This has implications for advancing AI-driven scientific discovery and knowledge generation.
- [Hypothesis-Driven Deep Research with Large Language Models: A Structured Methodology for Automated Knowledge Discovery](https://arxiv.org/abs/2605.10224v1): HDRI shifts the paradigm of AI-powered research from passive information retrieval to an active, hypothesis-driven process, enabling more structured, accurate, and iterative knowledge discovery. This approach has the potential to revolutionize how researchers across diverse fields generate, validate, and refine scientific insights, making it a cornerstone for future advancements in automated research systems.
- [LEVI: Stronger Search Architectures Can Substitute for Larger LLMs in Evolutionary Search](https://arxiv.org/abs/2605.09764v1): LEVI demonstrates that smarter search architectures can significantly reduce the computational and financial costs of evolutionary search, making advanced AI-driven discovery more accessible and sustainable. This could democratize research in fields like algorithmic discovery, systems optimization, and prompt engineering, where resource constraints often limit participation.
- [Agentic MIP Research: Accelerated Constraint Handler Generation](https://arxiv.org/abs/2605.09186v1): Mixed-integer programming is a cornerstone of optimization, with applications spanning logistics, finance, and engineering. By embedding LLM agents into the research process, this framework significantly reduces the time and effort required to test and implement algorithmic innovations. This not only accelerates solver development but also opens the door to discovering novel optimization strategies, potentially transforming how complex problems are solved in practice.
- [HalluCiteChecker: A Lightweight Toolkit for Hallucinated Citation Detection and Verification in the Era of AI Scientists](https://arxiv.org/abs/2604.26835v1): As AI tools increasingly assist in academic writing, the risk of hallucinated citations—references to non-existent works—has grown, threatening the integrity of scientific literature. HalluCiteChecker provides a practical solution to detect and verify citations, ensuring credibility and reducing the workload for reviewers and publishers in an era of AI-driven research workflows.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](https://arxiv.org/abs/2605.10899v1) is the latest archived addition. Themes: End-to-End AI Scientists, Literature And Survey Agents, Research Infrastructure And Benchmarks. Why it matters: RubricEM addresses the challenge of training AI systems for complex, long-horizon research tasks where traditional verifiable rewards are insufficient. By leveraging rubrics as a central structuring mechanism, it enables more effective planning, feedback, and learning, pushing the boundaries of AI's ability to perform autonomous research and synthesis. This has implications for advancing AI-driven scientific discovery and knowledge generation.
<!-- END: latest-entry -->

## License

MIT
