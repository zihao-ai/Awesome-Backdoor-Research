# Resource curation — October 23, 2026

This pass adds 18 non-paper resources: two tutorials/lectures, four courses, five workshop editions, and seven reusable software frameworks. Together with the seven existing entries, `data/resources.json` now contains 25 resources: seven learning resources (three tutorials/lectures and four courses), six workshops, and twelve toolboxes. The paper catalog remains at 452 unique works.

Selection uses organizer pages, university/instructor syllabi, and official project documentation. An accessible catalog or syllabus is not a claim that every lecture, exercise, recording, or software dependency is publicly available. Toolboxes were inspected through their documentation, not installed or executed. No PDFs, datasets, or model weights were downloaded.

## Tutorials, lectures, and courses

| Resource ID | Evidence and scope |
| :--- | :--- |
| `backdoor-copyright-tutorial-2025` | The [speaker's page](https://liyiming.tech/talks/) lists a January 8, 2025 tutorial at Southwest Jiaotong University and links the slides; the focus is constructive backdoor applications. |
| `theory-guided-backdoor-lecture-2024` | The [speaker's page](https://liyiming.tech/talks/) identifies the August 7, 2024 invited lecture and provides slides and video. It is labeled a lecture rather than a conference tutorial. |
| `bu-cs787-2026` | The [university course listing](https://www.bu.edu/csmet/academic-programs/courses/cs787/) explicitly identifies Fall 2026 and backdoor injection/defense coverage. This is a course description, not a complete open courseware collection. |
| `tau-cryptography-ml-2026` | The [instructor's course site](https://www.alonrosen.net/cryptoml/) identifies Fall 2026–27 and provides notes and a scheduled backdoor unit. The unit is scheduled for November 17, after this review date; it is not represented as an already delivered recording. |
| `umbc-robust-ml-2024` | The [Fall 2024 course site](https://courses.cs.umbc.edu/graduate/691rml/) lists a backdoor unit, BadNets reading, and course materials. |
| `cispa-adversarial-ml-2023` | The [2023 seminar syllabus](https://trustml-cispa.gitlab.io/seminar_aml_ss23/syllabus/) explicitly includes backdoors and links a reading list. It is a research seminar, not a backdoor-only course. |

## Workshop editions

| Resource ID | Evidence and scope |
| :--- | :--- |
| `c4ai4c-ieee-cai-2026` | The [IEEE CAI organizer page](https://www.ieeesmc.org/cai-2026/w12-security/) identifies the 2026 edition and backdoor threats within its broader AI/cybersecurity scope. Inclusion is based on scope, not a claim that all accepted papers concern backdoors. |
| `real-life-ml-security-2025` | The [organizer's program](https://mlsecurity-workshop.github.io/) identifies the September 2025 event, a backdoor-focused keynote, physical-world backdoor work, and slide links. |
| `dlsp-ieee-sp-2025` | The [organizer's page](https://dlsp2025.ieee-security.org/) explicitly solicits backdoor/poisoning research. The heading and program identify 2025; a leftover 2024 workshop-date line in the CFP is not used. |
| `trust-llms-iclr-2025` | The [workshop site](https://building-trust-in-llms.github.io/iclr-workshop/) identifies the 2025 edition; the [poster program](https://building-trust-in-llms.github.io/iclr-workshop/poster_session_2.html) includes CleanGen. This is a broader trustworthy-LLM workshop. |
| `aisec-acm-ccs-2024` | The [accepted-paper list](https://aisec.cc/2024/) includes graph backdoors, anti-backdoor learning, and audio backdoors. The 2024 edition is retained on this specific evidence rather than assuming every edition has the same coverage. |

## Reusable software

| Resource ID | Official source and inclusion rationale |
| :--- | :--- |
| `backdoorllm` | [Repository](https://github.com/bboylyg/BackdoorLLM): shared LLM attack evaluation and a defense module. Follow-up projects mentioned as progressively released are not separately listed as available tools. |
| `backdoordm` | [Repository](https://github.com/linweiii/BackdoorDM): multiple diffusion-model attacks, defenses, evaluation, and analysis tools. |
| `backdoormbti` | [Repository](https://github.com/SJTUHaiyangYu/BackdoorMBTI) and [supported tasks](https://backdoormbti.readthedocs.io/en/latest/tutorials/tasks.html): common tooling for image, text, and audio classification. The description does not imply a joint vision-language model implementation. |
| `backfed` | [Repository](https://github.com/thinh-dao/BackFed): modular federated backdoor attack/defense evaluation with configuration and parallel training support. |
| `backdoors101` | [Repository](https://github.com/ebagdasa/backdoors101): configurable backdoor experiments across centralized and federated training. |
| `mithridates` | [Repository](https://github.com/ebagdasa/mithridates): pipeline resistance measurement and configuration-search examples. The root emphasizes an MNIST example and links the larger experimental implementation; no production-readiness claim is made. |
| `adversarial-robustness-toolbox` | [Repository](https://github.com/Trusted-AI/adversarial-robustness-toolbox) and [poisoning API](https://adversarial-robustness-toolbox.readthedocs.io/en/latest/modules/attacks/poisoning.html): a general security library with explicit backdoor implementations, including generative-model attacks. |

Benchmark software is listed here for its reusable implementation. Benchmark and dataset papers remain in the Papers section; this pass does not create a separate benchmark/dataset resource group or duplicate paper rows.

## Existing entries

The ICCV 2023 tutorial's slide target was confirmed against the [official tutorial page](https://backdoor-learning-tutorial.github.io/). The [BackdoorBench documentation](https://backdoorbench.github.io/docs/index.html) was added as an extra toolbox link: these undated software tutorials are not assigned an invented teaching year. The other pre-existing resources are carried forward; this pass is not an execution or maintenance audit of those projects.
