# Curation and coverage — October 23, 2026

This is a dated editorial snapshot of the first full migration and topic-by-topic expansion. It is not an exhaustive bibliography of all published backdoor research.

## Batch accounting

| Source | Unique papers |
| :--- | ---: |
| Migrated from the original catalog | 212 |
| Previously reviewed examples outside that catalog | 4 |
| Newly added after abstract review | 90 |
| **Total** | **306** |

The old README contains 222 year-table rows and four additional toolbox-associated paper rows. All 226 rows are accounted for: 212 migrated works, seven repeated rows merged into their canonical records, and seven scope exclusions. The fifth toolbox-only row had no paper and remains a software resource. The [original catalog](https://github.com/zihao-ai/Awesome-Backdoor-in-Deep-Learning/blob/4be174fceda6034a8b7856a56a848e5b10adc097/README.md) and retired parser are available in Git history; redundant working-tree copies have been removed.

## Coverage by subcategory

Counts below are table appearances. A paper listed in two genuinely relevant subcategories is stored only once. Every one of the 39 subcategories received at least one new paper in this batch.

| Area | Subcategory | Papers | Newly added |
| :--- | :--- | ---: | ---: |
| Surveys | [General Surveys](../README.md#topic-general-surveys) | 6 | 1 |
| Surveys | [Topic-Specific Surveys](../README.md#topic-surveys-specific) | 4 | 3 |
| Computer Vision | [Image Classification & Recognition](../README.md#topic-image-classification) | 133 | 3 |
| Computer Vision | [Object Detection, Segmentation & Tracking](../README.md#topic-detection-segmentation-tracking) | 7 | 3 |
| Computer Vision | [Video Understanding](../README.md#topic-video-understanding) | 3 | 2 |
| Computer Vision | [3D Vision & Point Clouds](../README.md#topic-3d-vision) | 5 | 2 |
| Computer Vision | [Visual Representation Learning](../README.md#topic-visual-representation) | 7 | 1 |
| Computer Vision | [Image Restoration & Compression](../README.md#topic-image-restoration-compression) | 3 | 1 |
| Computer Vision | [Visual Regression & Counting](../README.md#topic-visual-regression-counting) | 2 | 1 |
| NLP & Language Models | [Text Classification & Sequence Labeling](../README.md#topic-text-classification) | 19 | 2 |
| NLP & Language Models | [Language Representation & Embedding Models](../README.md#topic-language-representation) | 9 | 2 |
| NLP & Language Models | [Sequence Generation & Translation](../README.md#topic-sequence-generation-translation) | 3 | 1 |
| NLP & Language Models | [Large Language Models & Instruction Following](../README.md#topic-llms) | 10 | 5 |
| NLP & Language Models | [Code Language Models](../README.md#topic-code-models) | 6 | 6 |
| NLP & Language Models | [Retrieval-Augmented Generation](../README.md#topic-rag) | 3 | 3 |
| Multimodal Learning | [Vision–Language Representation & Retrieval](../README.md#topic-vision-language-representation) | 6 | 2 |
| Multimodal Learning | [Vision–Language Understanding & MLLMs](../README.md#topic-mllms) | 6 | 3 |
| Multimodal Learning | [Audio–Language & Other Multimodal Models](../README.md#topic-audio-language) | 4 | 3 |
| Generative Models | [Image Generation & Editing](../README.md#topic-image-generation) | 7 | 3 |
| Generative Models | [Video Generation](../README.md#topic-video-generation) | 2 | 2 |
| Generative Models | [Audio, Speech & Music Generation](../README.md#topic-audio-generation) | 1 | 1 |
| Generative Models | [3D Content & Motion Generation](../README.md#topic-3d-generation) | 2 | 2 |
| AI Agents | [Planning & Reasoning](../README.md#topic-agent-planning) | 3 | 3 |
| AI Agents | [Memory & Knowledge](../README.md#topic-agent-memory) | 3 | 2 |
| AI Agents | [Tools & Skills](../README.md#topic-agent-tools) | 6 | 6 |
| AI Agents | [Multi-Agent Systems](../README.md#topic-multi-agent-systems) | 2 | 2 |
| Embodied AI | [Vision–Language–Action Models](../README.md#topic-vla-models) | 3 | 2 |
| Embodied AI | [Robotic Manipulation & Control](../README.md#topic-robotic-control) | 1 | 1 |
| Embodied AI | [Navigation & Autonomous Driving](../README.md#topic-navigation-driving) | 3 | 3 |
| Embodied AI | [Embodied Planning & Interaction](../README.md#topic-embodied-planning) | 2 | 2 |
| Graph Learning | [Graph & Node Classification](../README.md#topic-graph-node-classification) | 9 | 4 |
| Graph Learning | [Link Prediction & Graph Representation Learning](../README.md#topic-graph-representation) | 2 | 2 |
| Speech & Audio | [Speech & Speaker Recognition](../README.md#topic-speech-recognition) | 7 | 5 |
| Speech & Audio | [Audio Classification & Representation Learning](../README.md#topic-audio-representation) | 2 | 2 |
| Reinforcement Learning | [Single-Agent Reinforcement Learning](../README.md#topic-single-agent-rl) | 4 | 3 |
| Reinforcement Learning | [Multi-Agent Reinforcement Learning](../README.md#topic-multi-agent-rl) | 5 | 2 |
| Federated Learning | [Horizontal Federated Learning](../README.md#topic-horizontal-fl) | 15 | 2 |
| Federated Learning | [Vertical Federated Learning](../README.md#topic-vertical-fl) | 3 | 3 |
| Foundations & Theory | [Learning Theory & Formal Guarantees](../README.md#topic-learning-theory) | 12 | 5 |

## Scope exclusions

These entries remain in the historical Git snapshot and in the row-by-row migration ledger. They were not silently discarded.

| Original entry | Reason |
| :--- | :--- |
| Faster Algorithms for Weak Backdoors | Structural backdoors for SAT algorithms, not malicious model behavior. |
| Finding Backdoors to Integer Programs: A Monte Carlo Tree Search Framework | Integer-programming search backdoors, not malicious model behavior. |
| On Probabilistic Generalization of Backdoors in Boolean Satisfiability | Boolean satisfiability backdoors, not malicious model behavior. |
| Backdoor Decomposable Monotone Circuits and Propagation Complete Encodings | Circuit/CNF tractability backdoors, not malicious model behavior. |
| Backdoor DNFs | CNF/DNF tractability backdoors, not malicious model behavior. |
| Manipulating Federated Recommender Systems: Poisoning with Synthetic Users and Its Countermeasures | Federated recommendation poisoning without a conditional backdoor mechanism in the abstract. |
| Camouflaged Poisoning Attack on Graph Neural Networks | Fake-node graph poisoning without a conditional backdoor mechanism in the abstract. |

## Important classification and link corrections

| Work | Decision |
| :--- | :--- |
| CLEAR, GangSweep, FLAME | Defense, despite their placement in old attack tables |
| Chameleon | Horizontal federated learning, rather than semi-supervised learning |
| BACKDOORL, PolicyCleanse | Multi-agent reinforcement learning, rather than LLM agents |
| VDC | Image-classification defense; an MLLM is the cleaning tool, not the compromised target |
| SmoothInv | Correct CVPR landing page; the old arXiv link belonged to PatchSearch |
| Universal-perturbation certification | Foundations & Theory; removed unrelated FLIP implementation link |
| TrojPrompt / TrojLLM | One work; updated to the current arXiv title and LLM category |
| Image compression / reconstruction | Dedicated Computer Vision subcategory |
| Crowd counting / depth estimation | Visual regression, rather than image classification |
| Translation / summarization | Sequence Generation & Translation |
| Watermarking, ownership verification, XAI evaluation | Application and/or Analysis within the corresponding model area |
| Benchmark and dataset papers | Paper rows in the subject-specific tables, with resource types, rather than a separate benchmark category |

Foundations & Theory was added as an ordinary area for formal guarantees and cryptographic backdoors. It does not collect unrelated SAT or causal-inference uses of the word “backdoor.”

## Evidence and review method

- [Legacy migration ledger](../data/curation/legacy-migration.json): one disposition per original paper row, line in the Git-history source linked above, canonical paper ID, abstract source, and editorial note.
- [Expansion review ledger](../data/curation/expansion-reviews.json): one entry per new paper, source, reviewed arXiv version where available, date, and classification rationale.
- [Topic search log](../data/curation/searches.json): queries and retrieval methods for every leaf topic.

Read abstracts and publication metadata, without downloading PDFs or reviewing full papers. Sources include arXiv, publisher/proceedings abstracts, OpenReview, ACL Anthology, and author/institution publication pages. Some abstracts were visible in web-indexed author papers; this did not involve downloading the PDFs. Full abstracts and raw retrieval responses are not copied into the public catalog.

The initial pass used up to 12 arXiv results for each of the original 35 topic queries, a separate recent-title query with 350 results, and targeted follow-ups for sparse areas and missing older abstracts. Four additional subcategories were identified during migration and covered through screened recent results and targeted follow-ups. Query hits were screened by abstract rather than assigned automatically. These retrieval limits leave room for additional relevant work, especially papers absent from arXiv or with uncommon terminology.

Publication venue/year follow explicit proceedings metadata or author-reported publication metadata where available. Otherwise entries use arXiv and first-submission year. Legacy venue/year metadata is retained unless a correction was established; this pass is not a comprehensive bibliographic audit. Code links are retained from the original collection or explicitly supplied in source metadata; their implementations were not executed.

Two abstracts require an explicit source caveat: BadTTS was read through a mirrored abstract after publisher/OpenReview access was challenged, with DOI/title/year checked against publisher-supplied Crossref metadata; One-to-N & N-to-One was read from an author-posted ResearchGate abstract. These sources are identified in the ledgers rather than presented as primary-page confirmations.

Papers can make overlapping contributions. Classification is an editorial interpretation of the abstract and does not independently validate reported success rates, guarantees, or reproducibility. Later full-text review may refine some placements.
