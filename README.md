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
- **2026-04-16** [Mind DeepResearch Technical Report](https://arxiv.org/abs/2604.14518v1) (Literature And Survey Agents) - card: [2604-14518v1-mind-deepresearch-technical-report.md](archive/papers/2026-04-17/2604-14518v1-mind-deepresearch-technical-report.md)
- **2026-04-16** [DR$^{3}$-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://arxiv.org/abs/2604.14683v1) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-14683v1-dr-3-eval-towards-realistic-and-reproducible-deep-research-evaluation.md](archive/papers/2026-04-17/2604-14683v1-dr-3-eval-towards-realistic-and-reproducible-deep-research-evaluation.md)
- **2026-04-16** [DR^{3}-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://huggingface.co/papers/2604.14683) (End-to-End AI Scientists, Literature And Survey Agents) - card: [2604-14683-dr-3-eval-towards-realistic-and-reproducible-deep-research-evaluation.md](archive/papers/2026-04-17/2604-14683-dr-3-eval-towards-realistic-and-reproducible-deep-research-evaluation.md)
- **2026-04-16** [An Axiomatic Benchmark for Evaluation of Scientific Novelty Metrics](https://arxiv.org/abs/2604.15145v1) (End-to-End AI Scientists) - card: [2604-15145v1-an-axiomatic-benchmark-for-evaluation-of-scientific-novelty-metrics.md](archive/papers/2026-04-18/2604-15145v1-an-axiomatic-benchmark-for-evaluation-of-scientific-novelty-metrics.md)
- **2026-04-15** [TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration](https://arxiv.org/abs/2604.14116v1) (End-to-End AI Scientists) - card: [2604-14116v1-trex-automating-llm-fine-tuning-via-agent-driven-tree-based-exploration.md](archive/papers/2026-04-16/2604-14116v1-trex-automating-llm-fine-tuning-via-agent-driven-tree-based-exploration.md)
- **2026-04-15** [TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration](https://huggingface.co/papers/2604.14116) (End-to-End AI Scientists) - card: [2604-14116-trex-automating-llm-fine-tuning-via-agent-driven-tree-based-exploration.md](archive/papers/2026-04-16/2604-14116-trex-automating-llm-fine-tuning-via-agent-driven-tree-based-exploration.md)
- **2026-04-15** [MERRIN: A Benchmark for Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments](https://arxiv.org/abs/2604.13418v1) (Literature And Survey Agents) - card: [2604-13418v1-merrin-a-benchmark-for-multimodal-evidence-retrieval-and-reasoning-in-noisy-web-environments.md](archive/papers/2026-04-16/2604-13418v1-merrin-a-benchmark-for-multimodal-evidence-retrieval-and-reasoning-in-noisy-web-environments.md)
- **2026-04-15** [MERRIN: A Benchmark for Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments](https://huggingface.co/papers/2604.13418) (Literature And Survey Agents) - card: [2604-13418-merrin-a-benchmark-for-multimodal-evidence-retrieval-and-reasoning-in-noisy-web-environments.md](archive/papers/2026-04-16/2604-13418-merrin-a-benchmark-for-multimodal-evidence-retrieval-and-reasoning-in-noisy-web-environments.md)
- **2026-04-14** [Towards grounded autonomous research: an end-to-end LLM mini research loop on published computational physics](https://arxiv.org/abs/2604.12198v1) (Autoresearch Loops) - card: [2604-12198v1-towards-grounded-autonomous-research-an-end-to-end-llm-mini-research-loop-on-published-computational-physics.md](archive/papers/2026-04-15/2604-12198v1-towards-grounded-autonomous-research-an-end-to-end-llm-mini-research-loop-on-published-computational-physics.md)
- **2026-04-14** [Agentic MR sequence development: leveraging LLMs with MR skills for automatic physics-informed sequence development](https://arxiv.org/abs/2604.13282v1) (Autoresearch Loops) - card: [2604-13282v1-agentic-mr-sequence-development-leveraging-llms-with-mr-skills-for-automatic-physics-informed-sequence-development.md](archive/papers/2026-04-16/2604-13282v1-agentic-mr-sequence-development-leveraging-llms-with-mr-skills-for-automatic-physics-informed-sequence-development.md)
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
- [Mind DeepResearch Technical Report](https://arxiv.org/abs/2604.14518v1): MindDR demonstrates that smaller-scale models (~30B parameters) can achieve competitive or superior performance compared to larger-scale systems through innovative architecture and training pipelines. This approach could democratize access to high-performing AI systems, reduce computational costs, and accelerate real-world adoption in industries like automotive and research automation.
- [DR$^{3}$-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://arxiv.org/abs/2604.14683v1): As AI systems increasingly tackle complex research tasks, robust evaluation frameworks like DR$^{3}$-Eval are essential to ensure their reliability, reproducibility, and alignment with human expectations. This benchmark not only highlights current limitations but also provides a pathway for improving AI-driven research agents, which could revolutionize fields like scientific discovery and knowledge synthesis.
- [An Axiomatic Benchmark for Evaluation of Scientific Novelty Metrics](https://arxiv.org/abs/2604.15145v1): As AI increasingly contributes to scientific discovery and paper writing, ensuring reliable and automated evaluation of novelty is critical to avoid wasting resources on redundant ideas. This benchmark provides a structured framework to assess and improve novelty metrics, fostering innovation and efficiency in scientific research evaluation.
- [TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration](https://arxiv.org/abs/2604.14116v1): TREX represents a significant step toward fully automating complex AI workflows, such as fine-tuning large language models. By leveraging multi-agent collaboration and tree-based exploration, it reduces the need for human intervention in iterative experimentation, making advanced AI research more accessible and scalable. This could accelerate innovation in AI applications across diverse domains, from healthcare to finance.
- [TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration](https://huggingface.co/papers/2604.14116): TREX represents a significant step toward automating complex AI workflows, such as fine-tuning large language models, which are traditionally resource-intensive and require expert intervention. By leveraging multi-agent collaboration and tree-based exploration, TREX not only accelerates the training process but also enhances reproducibility and efficiency in AI research. This innovation could democratize access to advanced AI capabilities and streamline the development of domain-specific applications.
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
[Mind DeepResearch Technical Report](https://arxiv.org/abs/2604.14518v1) is the latest archived addition. Themes: Literature And Survey Agents. Why it matters: MindDR demonstrates that smaller-scale models (~30B parameters) can achieve competitive or superior performance compared to larger-scale systems through innovative architecture and training pipelines. This approach could democratize access to high-performing AI systems, reduce computational costs, and accelerate real-world adoption in industries like automotive and research automation.
<!-- END: latest-entry -->

## License

MIT
