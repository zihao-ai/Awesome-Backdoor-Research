# Classification guide

The catalog is organized for researchers looking for papers and code in a particular direction. Its public structure is **resource section → paper area → subcategory → compact table**. The complete ordered hierarchy and stable IDs live in [data/taxonomy.json](../data/taxonomy.json); browse it in the [README](../README.md#papers).

## Resource sections

| Section | Contents |
| :--- | :--- |
| Papers | Research papers, including surveys and benchmark/dataset papers |
| Tutorials & Courses | Teaching materials, tutorials, courses, and lecture collections |
| Workshops | Workshop websites and their programs, proceedings, and recordings |
| Toolboxes | Reusable software frameworks and libraries |

A resource's format and a paper's research area answer different questions. Toolboxes are independent resources; individual implementations belong beside their papers. Benchmark and dataset are paper types, not top-level resource sections.

## Paper areas and boundaries

| Area | Include | Boundary to consider |
| :--- | :--- | :--- |
| **Surveys** | General backdoor surveys and surveys of particular directions | Always collect survey papers here, even when focused on vision, LLMs, or agents |
| **Computer Vision** | Image recognition, detection/segmentation/tracking, video understanding, 3D vision, visual representations, restoration/compression, regression/counting | Synthesis/editing belongs in Generative Models; explicitly cross-modal representation belongs in Multimodal Learning |
| **NLP & Language Models** | Text tasks, embeddings, LLM instruction following, code models, RAG | RAG is a language-system subcategory; acting through tools/memory/planning may instead make the agent the central research object |
| **Multimodal Learning** | Cross-modal representations/retrieval, MLLM understanding, audio–language and other multimodal models | Organize by the attacked or defended model/task, not merely by how many modalities appear in the inputs |
| **Generative Models** | Image, video, audio/music, and 3D/motion synthesis | Language generation stays under language models; image-conditioned robot actions belong in Embodied AI |
| **AI Agents** | Agent planning/reasoning, memory/knowledge, tools/skills, and multi-agent systems | Requires an agent-level mechanism, behavior, or evaluation; an LLM with a prompt alone is not automatically an agent paper |
| **Embodied AI** | VLA models, robotic control/manipulation, navigation/driving, embodied interaction | Physical or simulated sensor–action interaction is central; generic policy-learning research can belong in RL |
| **Graph Learning** | Graph/node classification, link prediction, and graph representations | A graph merely used to describe an agent workflow does not make it graph-learning research |
| **Speech & Audio** | Speech/speaker recognition and audio classification/representations | Synthesis belongs in Generative Models; joint audio–language modeling belongs in Multimodal Learning |
| **Reinforcement Learning** | Single-agent and multi-agent RL backdoors in policies or learning processes | Multi-agent RL belongs here; LLM agent coordination belongs in AI Agents |
| **Federated Learning** | Horizontal and vertical federated learning | Use when client participation, model aggregation, or the federated training process is central to the work |
| **Foundations & Theory** | Learning-theoretic limits, formal guarantees, and cryptographic backdoors | Structural backdoors in SAT, causal backdoor paths, and integer-programming shortcuts are different concepts and outside the catalog |

These areas intentionally combine model/task families with widely used research settings such as federated learning. They are discovery routes, not a claim that every paper fits exactly one mutually exclusive box.

## Assigning subcategories

1. Identify the primary research object: the model, task, agent component, or training setting that is actually attacked, defended, or evaluated.
2. Choose the closest existing leaf topic in the taxonomy. Tables belong under these leaf topics; there are no direct area-level paper tables.
3. Add a second topic only when the paper makes a substantive contribution in that setting. Reuse the same record and ID.
4. Assign paper types separately. An evaluation paper can be `Analysis`, a reusable evaluation suite can be `Benchmark`, and a work can carry more than one type.
5. For survey papers, choose `general-surveys` for broad overviews or `surveys-specific` for focused surveys. Keep them in the Surveys area rather than duplicating them across all covered directions.

Examples of boundary decisions:

- Backdooring an image classifier during federated aggregation primarily fits Horizontal Federated Learning. Add Image Classification only if the vision-specific mechanism is itself a substantial contribution.
- Poisoning a retrieval corpus for a question-answering model fits RAG. Poisoning an agent's persistent memory to influence future tool use fits Memory & Knowledge.
- A backdoor in a vision–language representation fits Multimodal Learning. A backdoor in a vision–language–action policy fits Embodied AI.
- A simulated multi-agent control-policy study fits Multi-Agent Reinforcement Learning. A study of cooperating tool-using language agents fits Multi-Agent Systems.
- A diffusion model used to make poisoned images does not make an image-classifier attack a generative-model paper. Likewise, TTS-generated poisons targeting speech recognition belong under recognition, not speech generation.
- `Application` identifies constructive backdoor uses, including ownership verification and watermarking, within their ordinary research areas.

## Adding or changing a category

Prefer an existing category when it clearly covers the research object. Add a subcategory when a distinct direction has a meaningful scope; add a top-level area when its organizing concept cannot be expressed clearly under an existing area. There is no Cross-Cutting Topics catch-all.

Give every new area a concise description and at least one subcategory. Keep labels readable and IDs stable. Update the taxonomy source, this guide when boundaries change, and relevant records together, then rebuild. Renaming an ID breaks README anchors and record references, so prefer changing only the display name.

All categories remain visible. Empty categories get a generated italic placeholder row. The absence of catalog entries is not a claim that no literature exists in that direction. Classification is based on abstracts, not independent reproduction of the papers' claims.
