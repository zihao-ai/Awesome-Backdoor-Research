# Curation and coverage — October 23, 2026

This is a dated editorial snapshot of the first full migration and topic-by-topic expansion. It is not an exhaustive bibliography of all published backdoor research.

## Batch accounting

| Source | Unique papers |
| :--- | ---: |
| Migrated from the original catalog | 212 |
| Previously reviewed examples outside that catalog | 4 |
| Initial abstract-reviewed additions | 90 |
| Subsequent 2025–2026 expansion | 146 |
| **Total** | **452** |

The old README contains 222 year-table rows and four additional toolbox-associated paper rows. All 226 rows are accounted for: 212 migrated works, seven repeated rows merged into their canonical records, and seven scope exclusions. The fifth toolbox-only row had no paper and remains a software resource. The [original catalog](https://github.com/zihao-ai/Awesome-Backdoor-Research/blob/4be174fceda6034a8b7856a56a848e5b10adc097/README.md) and retired parser are available in Git history; redundant working-tree copies have been removed.

## Coverage by subcategory

Counts below are table appearances, not unique-paper counts. Cross-listed papers are stored once. The initial expansion covered every subcategory; the subsequent pass prioritizes 2025–2026 work, particularly modern language/multimodal models, agents, embodied systems, and generation.

| Area | Subcategory | Current papers | Initial additions | Recent additions |
| :--- | :--- | ---: | ---: | ---: |
| Surveys | [General Surveys](../README.md#topic-general-surveys) | 7 | 1 | 1 |
| Surveys | [Topic-Specific Surveys](../README.md#topic-surveys-specific) | 7 | 3 | 3 |
| Computer Vision | [Image Classification & Recognition](../README.md#topic-image-classification) | 134 | 3 | 1 |
| Computer Vision | [Object Detection, Segmentation & Tracking](../README.md#topic-detection-segmentation-tracking) | 17 | 3 | 10 |
| Computer Vision | [Video Understanding](../README.md#topic-video-understanding) | 3 | 2 | 0 |
| Computer Vision | [3D Vision & Point Clouds](../README.md#topic-3d-vision) | 9 | 2 | 4 |
| Computer Vision | [Visual Representation Learning](../README.md#topic-visual-representation) | 11 | 1 | 4 |
| Computer Vision | [Image Restoration & Compression](../README.md#topic-image-restoration-compression) | 5 | 1 | 2 |
| Computer Vision | [Visual Regression & Counting](../README.md#topic-visual-regression-counting) | 5 | 1 | 3 |
| NLP & Language Models | [Text Classification & Sequence Labeling](../README.md#topic-text-classification) | 19 | 2 | 0 |
| NLP & Language Models | [Language Representation & Embedding Models](../README.md#topic-language-representation) | 10 | 2 | 1 |
| NLP & Language Models | [Sequence Generation & Translation](../README.md#topic-sequence-generation-translation) | 3 | 1 | 0 |
| NLP & Language Models | [Large Language Models & Instruction Following](../README.md#topic-llms) | 38 | 5 | 28 |
| NLP & Language Models | [Code Language Models](../README.md#topic-code-models) | 16 | 6 | 10 |
| NLP & Language Models | [Retrieval-Augmented Generation](../README.md#topic-rag) | 7 | 3 | 4 |
| Multimodal Learning | [Vision–Language Representation & Retrieval](../README.md#topic-vision-language-representation) | 13 | 2 | 7 |
| Multimodal Learning | [Vision–Language Understanding & MLLMs](../README.md#topic-mllms) | 23 | 3 | 17 |
| Multimodal Learning | [Audio–Language & Other Multimodal Models](../README.md#topic-audio-language) | 4 | 3 | 0 |
| Generative Models | [Image Generation & Editing](../README.md#topic-image-generation) | 21 | 3 | 14 |
| Generative Models | [Video Generation](../README.md#topic-video-generation) | 2 | 2 | 0 |
| Generative Models | [Audio, Speech & Music Generation](../README.md#topic-audio-generation) | 1 | 1 | 0 |
| Generative Models | [3D Content & Motion Generation](../README.md#topic-3d-generation) | 3 | 2 | 1 |
| AI Agents | [Planning & Reasoning](../README.md#topic-agent-planning) | 5 | 3 | 2 |
| AI Agents | [Memory & Knowledge](../README.md#topic-agent-memory) | 4 | 2 | 1 |
| AI Agents | [Tools & Skills](../README.md#topic-agent-tools) | 19 | 6 | 13 |
| AI Agents | [Multi-Agent Systems](../README.md#topic-multi-agent-systems) | 5 | 2 | 3 |
| Embodied AI | [Vision–Language–Action Models](../README.md#topic-vla-models) | 6 | 2 | 3 |
| Embodied AI | [Robotic Manipulation & Control](../README.md#topic-robotic-control) | 3 | 1 | 2 |
| Embodied AI | [Navigation & Autonomous Driving](../README.md#topic-navigation-driving) | 5 | 3 | 2 |
| Embodied AI | [Embodied Planning & Interaction](../README.md#topic-embodied-planning) | 6 | 2 | 4 |
| Graph Learning | [Graph & Node Classification](../README.md#topic-graph-node-classification) | 10 | 4 | 1 |
| Graph Learning | [Link Prediction & Graph Representation Learning](../README.md#topic-graph-representation) | 5 | 2 | 3 |
| Speech & Audio | [Speech & Speaker Recognition](../README.md#topic-speech-recognition) | 10 | 5 | 3 |
| Speech & Audio | [Audio Classification & Representation Learning](../README.md#topic-audio-representation) | 2 | 2 | 0 |
| Reinforcement Learning | [Single-Agent Reinforcement Learning](../README.md#topic-single-agent-rl) | 11 | 3 | 7 |
| Reinforcement Learning | [Multi-Agent Reinforcement Learning](../README.md#topic-multi-agent-rl) | 7 | 2 | 2 |
| Federated Learning | [Horizontal Federated Learning](../README.md#topic-horizontal-fl) | 21 | 2 | 6 |
| Federated Learning | [Vertical Federated Learning](../README.md#topic-vertical-fl) | 5 | 3 | 2 |
| Foundations & Theory | [Learning Theory & Formal Guarantees](../README.md#topic-learning-theory) | 13 | 5 | 1 |

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
- [Topic search log](../data/curation/searches.json): queries and retrieval methods for every leaf topic in the initial expansion.
- [Recent expansion log](../data/curation/recent-expansion.json): 2025–2026 retrieval parameters, counts, exclusions, and version/alias decisions.

Read abstracts and publication metadata, without downloading PDFs or reviewing full papers. Sources include arXiv, publisher/proceedings abstracts, OpenReview, ACL Anthology, and author/institution publication pages. Some abstracts were visible in web-indexed author papers; this did not involve downloading the PDFs. Full abstracts and raw retrieval responses are not copied into the public catalog.

The initial pass used up to 12 arXiv results for each of the original 35 topic queries, a separate recent-title query with 350 results, and targeted follow-ups for sparse areas and missing older abstracts. Four additional subcategories were identified during migration and covered through screened recent results and targeted follow-ups. Query hits were screened by abstract rather than assigned automatically. These retrieval limits leave room for additional relevant work, especially papers absent from arXiv or with uncommon terminology.

Publication venue/year follow explicit proceedings metadata or author-reported publication metadata where available. Otherwise entries use arXiv and first-submission year. Legacy venue/year metadata is retained unless a correction was established; this pass is not a comprehensive bibliographic audit. Code links are retained from the original collection or explicitly supplied in source metadata; their implementations were not executed.

Two abstracts require an explicit source caveat: BadTTS was read through a mirrored abstract after publisher/OpenReview access was challenged, with DOI/title/year checked against publisher-supplied Crossref metadata; One-to-N & N-to-One was read from an author-posted ResearchGate abstract. These sources are identified in the ledgers rather than presented as primary-page confirmations.

Papers can make overlapping contributions. Classification is an editorial interpretation of the abstract and does not independently validate reported success rates, guarantees, or reproducibility. Later full-text review may refine some placements.


## Subsequent 2025–2026 expansion

The additional pass reviewed 152 abstracts and added **146 independent papers**, taking the catalog from 306 to **452**. By displayed publication year, 75 additions are from 2026 and 71 from 2025. By first arXiv submission year, the same additions comprise 58 from 2026 and 88 from 2025. This distinction avoids presenting every newly uploaded manuscript as a new publication.

The title query `(ti:backdoor OR ti:trojan) AND submittedDate:[202501010000 TO 202610232359]` returned 767 of 767 reported records in one bounded request, sorted by submission date. Metadata and prior-catalog filtering produced 699 candidates. This is retrieval reconciliation for that query, not a claim to have abstract-screened all 767 records or found every relevant paper. The 152 selected abstracts were read individually; 146 were accepted and six were held out. Exact identifiers, normalized titles, and possible near-title aliases were checked against the current catalog, and accepted records were also compared with each other.

Each accepted entry has a primary arXiv abstract source, reviewed version, review date, and individual classification rationale in the expansion ledger. A `batch_id` distinguishes this pass from the original 90 additions. Venue/year use explicit author-supplied publication statements where available; entries without established publication details remain marked arXiv. Author-reported acceptance is not an independent publisher confirmation. No PDFs were downloaded and no full papers were read.

| Held-out item | Reason |
| :--- | :--- |
| Natural Backdoor Attacks on Speech Recognition Models | Uploaded in 2026, but source metadata identifies publication in 2023 |
| SpeechGuard | Uploaded in 2026, but published at IJCNN 2024 |
| MBTSAD | Uploaded in 2025, but source identifies ICTAI 2024 |
| AnywhereDoor, arXiv:2503.06529 | Author explicitly identifies a mistaken duplicate submission and withdrawal; canonical record is arXiv:2411.14243 |
| DUP | Abstract alone does not establish the evaluated model family/tasks sufficiently for a confident PLM-versus-generative-LLM placement |
| SSD for UAV route planning | Abstract establishes state-triggered GNSS spoofing but does not establish an implanted learning-model backdoor |

Additional classification checks prevent misleading placements: BadEngram targets parameterized memory inside an LLM rather than an agent's external memory; FreqDoor attacks captioning/VQA models rather than CLIP embeddings; SPBA uses an SLLM to attack speech classifiers; SRD uses RL as a defense tool for a captioning model; and retrieval-augmented diffusion belongs in image generation rather than language RAG. Topology-Conditioned Backdoors is listed under code/language models because its abstract explicitly says live multi-agent activation remains untested.

The retrieval/parser workflow used the `paper-lookup` procedure from Scientific Agent Skills: Timothy Kassis, Vinayak Agarwal, Yuhuan He, Darshil Patel, and Aubrey M. Brueckner (2026), [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://arxiv.org/abs/2609.00065). The procedure supports retrieval and provenance; editorial classification remains based on the paper abstracts.
