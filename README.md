# ⚔🛡 Awesome Backdoor Attacks and Defenses

This repository contains a collection of papers and resources  on **backdoor attacks** and **backdoor defense** in deep learning.

# Table of contents
- [📃Survey](#survey)
- [⚔Backdoor Attacks](#backdoor-attacks)
  - [Supervised learning (Image classification)](#supervised-learning-image-classification)
  - [Semi-supervised learning](#semi-supervised-learning)
  - [Self-supervised learning](#self-supervised-learning)
  - [Federated learning](#federated-learning)
  - [Reinforcement Learning](#reinforcement-learning)
  - [Other CV tasks (Object detection, segmentation, point cloud)](#other-cv-tasks-object-detection-segmentation-point-cloud)
  - [Multimodal models (Visual and Language)](#multimodal-models-visual-and-language)
  - [Diffusion model](#diffusion-model)
  - [Large language model \& other NLP tasks](#large-language-model--other-nlp-tasks)
  - [Graph Neural Networks](#graph-neural-networks)
  - [Theoretical analysis](#theoretical-analysis)
- [🛡Backdoor Defenses](#backdoor-defenses)
  - [Defense for supervised learning (Image classification)](#defense-for-supervised-learning-image-classification)
    - [Before-training (Preprocessing) stage](#before-training-preprocessing-stage)
    - [In-training stage](#in-training-stage)
    - [Post-training stage](#post-training-stage)
    - [Inference stage](#inference-stage)
  - [Defense for semi-supervised learning](#defense-for-semi-supervised-learning)
  - [Defense for self-supervised learning](#defense-for-self-supervised-learning)
  - [Defense for reinforcement learning](#defense-for-reinforcement-learning)
  - [Defense for federated learning](#defense-for-federated-learning)
  - [Defense for other CV tasks (Object detection, segmentation)](#defense-for-other-cv-tasks-object-detection-segmentation)
  - [Defense for multimodal models (Visual and Language)](#defense-for-multimodal-models-visual-and-language)
  - [Defense for Large Language model \& other NLP tasks](#defense-for-large-language-model--other-nlp-tasks)
  - [Defense for diffusion models](#defense-for-diffusion-models)
  - [Defense for Graph Neural Networks](#defense-for-graph-neural-networks)
- [Backdoor for social good](#backdoor-for-social-good)
  - [Watermarking](#watermarking)
  - [Explainable AI](#explainable-ai)
- [⚙Benchmark and toolboxes](#benchmark-and-toolboxes)



# 📃Survey
| Year | Publication                  | Paper                                                        |
| ---- | ---------------------------- | ------------------------------------------------------------ |
| 2023 | arXiv                        | [Adversarial Machine Learning: A Systematic Survey of Backdoor Attack, Weight Attack and Adversarial Example](https://arxiv.org/pdf/2012.10544.pdf) |
| 2022 | TPAMI                        | [Data Security for Machine Learning: Data Poisoning, Backdoor Attacks, and Defenses](https://arxiv.org/pdf/2012.10544.pdf) |
| 2022 | TNNLS                        | [Backdoor Learning: A Survey](https://www.researchgate.net/publication/343006441_Backdoor_Learning_A_Survey) |
| 2022 | IEEE Wireless Communications | [Backdoor Attacks and Defenses in Federated Learning: State-of-the-art, Taxonomy, and Future Directions](https://ieeexplore.ieee.org/abstract/document/9806416) |
| 2021 | Neurocomputing               | [Defense against Neural Trojan Attacks: A Survey](https://www.sciencedirect.com/science/article/pii/S0925231220316350) |
| 2020 | ISQED                        | [A Survey on Neural Trojans](https://eprint.iacr.org/2020/201.pdf) |

# Tutorial & Workshop

| Venue        | Title                                                        |
| ------------ | ------------------------------------------------------------ |
| ICCV 2023    | [Backdoor Learning: Recent Advances and Future Trends](https://backdoor-learning-tutorial.github.io/) |
| NeurIPS 2023 | [Backdoors in Deep Learning](https://neurips2023-bugs.github.io/) |

# ⚔Backdoor Attacks

## Supervised learning (Image classification)
| Year | Publication  | Paper                                                        | Code                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2024 | arXiv        | [Unlearn to Relearn Backdoors: Deferred Backdoor Functionality Attacks on Deep Learning Models](https://arxiv.org/abs/2411.14449) |                                                              |
| 2023 | NeurIPS 2023 | [Label Poisoning is All You Need](https://neurips.cc/virtual/2023/poster/70392) |  |
| 2023 | ICCV 2023 | [Computation and Data Efficient Backdoor Attacks](https://openaccess.thecvf.com/content/ICCV2023/html/Wu_Computation_and_Data_Efficient_Backdoor_Attacks_ICCV_2023_paper.html) |  |
| 2023 | arXiv | [Boosting backdoor attack with a learnable poisoning sample selection strategy](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=lBSoR4IAAAAJ&citation_for_view=lBSoR4IAAAAJ:KlAtU1dfN6UC) | |
| 2023 | arXiv | [Robust Backdoor Attack with Visible, Semantic, Sample-Specific, and Compatible Triggers](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=lBSoR4IAAAAJ&citation_for_view=lBSoR4IAAAAJ:kNdYIx-mwKoC) | |
| 2023 | CVPR 2023    | [Architectural Backdoors in Neural Networks](https://arxiv.org/abs/2206.07840) | |
| 2023 | CVPR 2023    | [Color Backdoor: A Robust Poisoning Attack in Color Space](https://openaccess.thecvf.com/content/CVPR2023/papers/Jiang_Color_Backdoor_A_Robust_Poisoning_Attack_in_Color_Space_CVPR_2023_paper.pdf) | |
| 2023 | CVPR 2023    | [You Are Catching My Attention: Are Vision Transformers Bad Learners Under Backdoor Attacks?](https://openreview.net/forum?id=7P_yIFi6zaA) | |
| 2023 | CVPR 2023    | [The Dark Side of Dynamic Routing Neural Networks: Towards Efficiency Backdoor Injection](https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_The_Dark_Side_of_Dynamic_Routing_Neural_Networks_Towards_Efficiency_CVPR_2023_paper.pdf) | [:octocat:](https://github.com/SeekingDream/CVPR23_EfficFrog) |
| 2023 | CVPR 2023    | [Backdoor Attacks Against Deep Image Compression via Adaptive Frequency Trigger](https://arxiv.org/abs/2302.14677) ||
| 2023 | ICLR 2023    | [Revisiting the Assumption of Latent Separability for Backdoor Defenses](https://openreview.net/forum?id=_wSHsgrVali) | [:octocat:](https://github.com/Unispac/Circumventing-Backdoor-Defenses)  |
| 2023 | ICLR 2023    | [Few-shot Backdoor Attacks via Neural Tangent Kernels](https://openreview.net/forum?id=a70lGJ-rwy) |   |
| 2023 | ICLR 2023    | [The Dark Side of AutoML: Towards Architectural Backdoor Search](https://openreview.net/forum?id=bsZULlDGXe) | [:octocat:](https://github.com/ain-soph/nas_backdoor)  |
| 2023 | ICLR 2023    | [Clean-image Backdoor: Attacking Multi-label Models with Poisoned Labels Only](https://openreview.net/forum?id=rFQfjDC9Mt) | |
| 2022 | AAAI 2022    | [Backdoor Attacks on the DNN Interpretation System](https://ojs.aaai.org/index.php/AAAI/article/view/19935) ||
| 2022 | AAAI 2022    | [Faster Algorithms for Weak Backdoors](https://ojs.aaai.org/index.php/AAAI/article/view/20288) ||
| 2022 | AAAI 2022    | [Finding Backdoors to Integer Programs: A Monte Carlo Tree Search Framework](https://ojs.aaai.org/index.php/AAAI/article/view/20293) |                                                              |
| 2022 | AAAI 2022    | [Hibernated Backdoor: A Mutual Information Empowered Backdoor Attack to Deep Neural Networks](https://ojs.aaai.org/index.php/AAAI/article/view/21272) |                                                              |
| 2022 | AAAI 2022    | [On Probabilistic Generalization of Backdoors in Boolean Satisfiability](https://ojs.aaai.org/index.php/AAAI/article/view/21277) |                                                              |
| 2022 | CCS 2022     | [Backdoor Attacks on Spiking NNs and Neuromorphic Datasets](https://doi.org/10.1145/3548606.3563532) | [:octocat:](https://github.com/GorkaAbad/NeuromorphicBackdoors) |
| 2022 | CCS 2022     | [LoneNeuron: A Highly-Effective Feature-Domain Neural Trojan Using Invisible and Polymorphic Watermarks](https://doi.org/10.1145/3548606.3560678) |                                                              |
| 2022 | CVPR 2022    | [BppAttack: Stealthy and Efficient Trojan Attacks against Deep Neural Networks via Image Quantization and Contrastive Adversarial Learning](https://doi.org/10.1109/CVPR52688.2022.01465) |                                                              |
| 2022 | CVPR 2022    | [DEFEAT: Deep Hidden Feature Backdoor Attacks by Imperceptible Perturbation and Latent Representation Constraints](https://doi.org/10.1109/CVPR52688.2022.01478) ||
| 2022 | CVPR 2022    | [FIBA: Frequency-Injection based Backdoor Attack in Medical Image Analysis](https://doi.org/10.1109/CVPR52688.2022.02021) | [:octocat:](https://github.com/HazardFY/FIBA)                |
| 2022 | CVPR 2022    | [Towards Practical Deployment-Stage Backdoor Attack on Deep Neural Networks.](https://doi.org/10.1109/CVPR52688.2022.01299) |                                                              |
| 2022 | ECCV 2022    | [An Invisible Black-Box Backdoor Attack Through Frequency Domain](https://doi.org/10.1007/978-3-031-19778-9_23) | [:octocat:](https://github.com/SoftWiser-group/FTrojan)      |
| 2022 | ECCV 2022    | [RIBAC: Towards Robust and Imperceptible Backdoor Attack against Compact DNN](https://doi.org/10.1007/978-3-031-19772-7_41) | [:octocat:](https://github.com/huyvnphan/ECCV2022-RIBAC)     |
| 2022 | EUROSP 2022  | [Dynamic Backdoor Attacks Against Machine Learning Models](https://doi.org/10.1109/EuroSP53844.2022.00049) |                                                              |
| 2022 | ICASSP 2022 | [Invisible and Efficient Backdoor Attacks for Compressed Deep Neural Networks](https://doi.org/10.1109/ICASSP43922.2022.9747582) |                                                              |
| 2022 | ICASSP 2022  | [Stealthy Backdoor Attack with Adversarial Training](https://doi.org/10.1109/ICASSP43922.2022.9746008) |                                                              |
| 2022 | ICASSP 2022  | [When Does Backdoor Attack Succeed in Image Reconstruction? A Study of Heuristics vs. Bi-Level Solution](https://doi.org/10.1109/ICASSP43922.2022.9746433) |                                                              |
| 2022 | ICLR 2022    | [How to Inject Backdoors with Better Consistency: Logit Anchoring on Clean Data](https://openreview.net/forum?id=Bn09TnDngN) |                                                              |
| 2022 | IJCAI 2022   | [Data-Efficient Backdoor Attacks](https://doi.org/10.24963/ijcai.2022/554) | [:octocat:](https://github.com/xpf/Data-Efficient-Backdoor-Attacks) |
| 2022 | IJCAI 2022   | [Imperceptible Backdoor Attack: From Input Space to Feature Representation](https://doi.org/10.24963/ijcai.2022/242) | [:octocat:](https://github.com/Ekko-zn/IJCAI2022-Backdoor)   |
| 2022 | MM 2022      | [BadHash: Invisible Backdoor Attacks against Deep Hashing with Clean Label](https://doi.org/10.1145/3503161.3548272) |                                                              |
| 2022 | NeurIPS 2022 | [Marksman Backdoor: Backdoor Attacks with Arbitrary Target Class](https://openreview.net/pdf/db491ee3cff9f8c9a87b1206e94fda5d277c7b32.pdf) |                                                              |
| 2022 | NeurIPS 2022 | [Handcrafted Backdoors in Deep Neural Networks](https://openreview.net/forum?id=6yuil2_tn9a) |                                                              |
| 2022 | NeurIPS 2022 | [Sleeper Agent: Scalable Hidden Trigger Backdoors for Neural Networks Trained from Scratch](https://openreview.net/pdf/d9cc18a9db99b77f760aec0f53633607a0d43f44.pdf) | [:octocat:](https://github.com/hsouri/Sleeper-Agent)         |
| 2022 | TDSC 2022    | [One-to-N & N-to-One: Two Advanced Backdoor Attacks Against Deep Learning Models](https://doi.org/10.1109/TDSC.2020.3028448) |                                                              |
| 2022 | TIFS 2022    | [Dispersed Pixel Perturbation-Based Imperceptible Backdoor Trigger for Image Classifier Models](https://doi.org/10.1109/TIFS.2022.3202687) |                                                              |
| 2022 | TIFS 2022    | [Stealthy Backdoors as Compression Artifacts](https://doi.org/10.1109/TIFS.2022.3160359) | [:octocat:](https://github.com/yulongtzzz/Stealthy-Backdoors-as-Compression-Artifacts) |
| 2022 | TIP 2022     | [Poison Ink: Robust and Invisible Backdoor Attack](https://doi.org/10.1109/TIP.2022.3201472) |                                                              |
| 2021 | AAAI 2021    | [Backdoor Decomposable Monotone Circuits and Propagation Complete Encodings](https://ojs.aaai.org/index.php/AAAI/article/view/16501) |                                                              |
| 2021 | AAAI 2021    | [Deep Feature Space Trojan Attack of Neural Networks by Controlled Detoxification](https://ojs.aaai.org/index.php/AAAI/article/view/16201) | [:octocat:](https://github.com/Megum1/DFST)                  |
| 2021 | CVPR 2021    | [Backdoor Attacks Against Deep Learning Systems in the Physical World](https://openaccess.thecvf.com/content/CVPR2021/html/Wenger_Backdoor_Attacks_Against_Deep_Learning_Systems_in_the_Physical_World_CVPR_2021_paper.html) |                                                              |
| 2021 | ICCV 2021    | [CLEAR: Clean-up Sample-Targeted Backdoor in Neural Networks](https://doi.org/10.1109/ICCV48922.2021.01614) |                                                              |
| 2021 | ICCV 2021    | [Invisible Backdoor Attack with Sample-Specific Triggers](https://doi.org/10.1109/ICCV48922.2021.01615) | [:octocat:](https://github.com/yuezunli/ISSBA)               |
| 2021 | ICCV 2021    | [LIRA: Learnable, Imperceptible and Robust Backdoor Attacks](https://doi.org/10.1109/ICCV48922.2021.01175) | [:octocat:](https://github.com/sunbelbd/invisible_backdoor_attacks) |
| 2021 | ICCV 2021    | [Rethinking the Backdoor Attacks' Triggers: A Frequency Perspective](https://doi.org/10.1109/ICCV48922.2021.01616) | [:octocat:](https://github.com/YiZeng623/frequency-backdoor) |
| 2021 | ICLR 2021    | [WaNet - Imperceptible Warping-based Backdoor Attack](https://openreview.net/forum?id=eEn8KTtJOx) | [:octocat:](https://github.com/VinAIResearch/Warping-based_Backdoor_Attack-release) |
| 2021 | ICML 2021    | [Just How Toxic is Data Poisoning? A Unified Benchmark for Backdoor and Data Poisoning Attacks](http://proceedings.mlr.press/v139/schwarzschild21a.html) | [:octocat:](https://github.com/aks2203/poisoning-benchmark)  |
| 2021 | IJCAI 2021   | [Backdoor DNFs](https://doi.org/10.24963/ijcai.2021/194)     |                                                              |
| 2021 | NeurIPS 2021 | [Backdoor Attack with Imperceptible Input and Latent Modification](https://proceedings.neurips.cc/paper/2021/hash/9d99197e2ebf03fc388d09f1e94af89b-Abstract.html) |                                                              |
| 2021 | NeurIPS 2021 | [Excess Capacity and Backdoor Poisoning](https://proceedings.neurips.cc/paper/2021/hash/aaebdb8bb6b0e73f6c3c54a0ab0c6415-Abstract.html) | [:octocat:](https://github.com/narenmanoj/mnist-adv-training) |
| 2021 | TDSC 2021    | [Invisible Backdoor Attacks on Deep Neural Networks Via Steganography and Regularization](https://doi.org/10.1109/TDSC.2020.3021407) |                                                              |
| 2021 | USS 2021     | [Blind Backdoors in Deep Learning Models](https://www.usenix.org/conference/usenixsecurity21/presentation/bagdasaryan) | [:octocat:](https://github.com/ebagdasa/backdoors101)        |
| 2020 | AAAI 2020    | [Hidden Trigger Backdoor Attacks](https://ojs.aaai.org/index.php/AAAI/article/view/6871) | [:octocat:](https://github.com/UMBCvision/Hidden-Trigger-Backdoor-Attacks) |
| 2020 | CCS 2020     | [Composite Backdoor Attack for Deep Neural Network by Mixing Existing Benign Features](https://doi.org/10.1145/3372297.3423362) |                                                              |
| 2020 | CIKM 2020    | [Can Adversarial Weight Perturbations Inject Neural Backdoors](https://doi.org/10.1145/3340531.3412130) | [:octocat:](https://github.com/goel96vibhor/AdvWeightPerturbations) |
| 2020 | CVPR 2020    | [Clean-Label Backdoor Attacks on Video Recognition Models](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhao_Clean-Label_Backdoor_Attacks_on_Video_Recognition_Models_CVPR_2020_paper.html) | [:octocat:](https://github.com/ShihaoZhaoZSH/Video-Backdoor-Attack) |
| 2020 | ECCV 2020    | [Reflection Backdoor: A Natural Backdoor Attack on Deep Neural Networks](https://doi.org/10.1007/978-3-030-58607-2_11) | [:octocat:](https://github.com/DreamtaleCore/Refool)         |
| 2020 | KDD 2020     | [An Embarrassingly Simple Approach for Trojan Attack in Deep Neural Networks](https://doi.org/10.1145/3394486.3403064) | [:octocat:](https://github.com/trx14/TrojanNet)              |
| 2020 | MM 2020      | [GangSweep: Sweep out Neural Backdoors by GAN](https://doi.org/10.1145/3394171.3413546) |                                                              |
| 2020 | NeurIPS 2020 | [Input-Aware Dynamic Backdoor Attack](https://proceedings.neurips.cc/paper/2020/hash/234e691320c0ad5b45ee3c96d0d7b8f8-Abstract.html) | [:octocat:](https://github.com/VinAIResearch/input-aware-backdoor-attack-release) |
| 2020 | NeurIPS 2020 | [On the Trade-off between Adversarial and Backdoor Robustness](https://proceedings.neurips.cc/paper/2020/hash/8b4066554730ddfaa0266346bdc1b202-Abstract.html) | [:octocat:](https://github.com/nthu-datalab/On.the.Trade-off.between.Adversarial.and.Backdoor.Robustness) |
| 2019 | CCS 2019     | [Latent Backdoor Attacks on Deep Neural Networks](https://doi.org/10.1145/3319535.3354209) | [:octocat:](https://github.com/Huiying-Li/Latent-Backdoor)   |
| 2018 | NDSS 2018    | [Trojaning Attack on Neural Networks](http://wp.internetsociety.org/ndss/wp-content/uploads/sites/25/2018/02/ndss2018_03A-5_Liu_paper.pdf) | [:octocat:](https://github.com/PurduePAML/TrojanNN)          |


## Semi-supervised learning

| Year | Publication | Paper                                                        | Code |
| ---- | ----------- | ------------------------------------------------------------ | ---- |
| 2023 | ICCV 2023   | [The Perils of Learning From Unlabeled Data: Backdoor Attacks on Semi-supervised Learning](https://openaccess.thecvf.com/content/ICCV2023/html/Shejwalkar_The_Perils_of_Learning_From_Unlabeled_Data_Backdoor_Attacks_on_ICCV_2023_paper.html) |      |
| 2023 | ICML 2023   | [Chameleon: Adapting to Peer Images for Planting Durable Backdoors in Federated Learning](https://arxiv.org/abs/2304.12961) |      |
| 2021 | AAAI 2021   | [DeHiB: Deep Hidden Backdoor Attack on Semi-supervised Learning via Adversarial Perturbation](https://ojs.aaai.org/index.php/AAAI/article/view/17266) |      |
| 2021 | TIFS 2021   | [Deep Neural Backdoor in Semi-Supervised Learning: Threats and Countermeasures](https://doi.org/10.1109/TIFS.2021.3116431) |      |

## Self-supervised learning

| Year | Publication | Paper                                                        | Code                                                    |
| ---- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------- |
| 2023 | ICCV 2023   | [An Embarrassingly Simple Backdoor Attack on Self-supervised Learning](https://openaccess.thecvf.com/content/ICCV2023/html/Li_An_Embarrassingly_Simple_Backdoor_Attack_on_Self-supervised_Learning_ICCV_2023_paper.html) | [:octocat:](https://github.com/meet-cjli/CTRL)          |
| 2022 | CVPR2022    | [Backdoor Attacks on Self-Supervised Learning](https://doi.org/10.1109/CVPR52688.2022.01298) | [:octocat:](https://github.com/UMBCvision/SSL-Backdoor) |

## Federated learning

| Year | Publication  | Paper                                                        | Code                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2023 | NeurIPS 2023 | [IBA: Towards Irreversible Backdoor Attacks in Federated Learning](https://neurips.cc/virtual/2023/poster/71079) |                                                              |
| 2023 | NeurIPS 2023 | [A3FL: Adversarially Adaptive Backdoor Attacks to Federated Learning](https://neurips.cc/virtual/2023/poster/71628) |                                                              |
| 2023 | SIGIR 2023   | [Manipulating Federated Recommender Systems: Poisoning with Synthetic Users and Its Countermeasures](https://arxiv.org/abs/2304.03054) |                                                              |
| 2022 | ICML2022     | [Neurotoxin: Durable Backdoors in Federated Learning](https://proceedings.mlr.press/v162/zhang22w.html) |                                                              |
| 2020 | AISTATS 2020 | [How To Backdoor Federated Learning](http://proceedings.mlr.press/v108/bagdasaryan20a.html) | [:octocat:](https://github.com/ebagdasa/backdoor_federated_learning) |
| 2020 | ICLR 2020    | [DBA: Distributed Backdoor Attacks against Federated Learning](https://openreview.net/forum?id=rkgyS0VFvr) | [:octocat:](https://github.com/AI-secure/DBA)                |
| 2020 | NeurIPS 2020 | [Attack of the Tails: Yes, You Really Can Backdoor Federated Learning](https://proceedings.neurips.cc/paper/2020/hash/b8ffa41d4e492f0fad2f13e29e1762eb-Abstract.html) | [:octocat:](https://github.com/pps-lab/fl-analysis)          |
| 2022 | USS 2022     | [FLAME: Taming Backdoors in Federated Learning](https://www.usenix.org/conference/usenixsecurity22/presentation/nguyen) |                                                              |

## Reinforcement Learning

| Year | Publication | Paper                                                        | Code |
| ---- | ----------- | ------------------------------------------------------------ | ---- |
| 2021 | IJCAI 2021  | [BACKDOORL: Backdoor Attack against Competitive Reinforcement Learning](https://doi.org/10.24963/ijcai.2021/509) |      |

## Other CV tasks (Object detection, segmentation, point cloud)

| Year | Publication  | Paper                                                        | Code                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2024 | ICIP 2024    | [Mask-based Invisible Backdoor Attacks on Object Detection](https://ieeexplore.ieee.org/document/10647450/) | [:octocat:](https://github.com/jeongjin0/invisible-backdoor-object-detection) |
| 2023 | NeurIPS 2023 | [BadTrack: A Poison-Only Backdoor Attack on Visual Object Tracking](https://neurips.cc/virtual/2023/poster/71420) |                                                              |
| 2022 | ICLR 2022    | [Few-Shot Backdoor Attacks on Visual Object Tracking](https://openreview.net/forum?id=qSV5CuSaK_a) | [:octocat:](https://github.com/HXZhong1997/FSBA)             |
| 2022 | MM 2022      | [Backdoor Attacks on Crowd Counting](https://doi.org/10.1145/3503161.3548296) | [:octocat:](https://github.com/Nathangitlab/Backdoor-Attacks-on-Crowd-Counting) |
| 2021 | ICCV 2021    | [A Backdoor Attack against 3D Point Cloud Classifiers](https://doi.org/10.1109/ICCV48922.2021.00750) | [:octocat:](https://github.com/zhenxianglance/PCBA)          |
| 2021 | ICCV 2021    | [PointBA: Towards Backdoor Attacks in 3D Point Cloud](https://doi.org/10.1109/ICCV48922.2021.01618) | [:octocat:](https://github.com/zhenxianglance/PCBA)          |

## Multimodal models (Visual and Language)

| Year | Publication | Paper                                                        | Code                                                         |
| ---- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2024 | IEEE SP     | [Backdooring Multimodal Learning](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a031/1RjEa7rmaxW) |                                                              |
| 2022 | CVPR2022    | [Dual-Key Multimodal Backdoors for Visual Question Answering](https://doi.org/10.1109/CVPR52688.2022.01494) | [:octocat:](https://github.com/SRI-CSL/TrinityMultimodalTrojAI) |
| 2022 | ICASSP 2022 | [Object-Oriented Backdoor Attack Against Image Captioning](https://doi.org/10.1109/ICASSP43922.2022.9746440) |                                                              |
| 2022 | ICLR 2022   | [Poisoning and Backdooring Contrastive Learning](https://openreview.net/forum?id=iC4UHbQ01Mp) |                                                              |

## Diffusion model

| Year | Publication  | Paper                                                        | Code                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2023 | NeurIPS 2023 | [VillanDiffusion: A Unified Backdoor Attack Framework for Diffusion Models](https://neurips.cc/virtual/2023/poster/70045) |                                                              |
| 2023 | ICCV 2023    | [Rickrolling the Artist: Injecting Backdoors into Text Encoders for Text-to-Image Synthesis](https://openaccess.thecvf.com/content/ICCV2023/html/Struppek_Rickrolling_the_Artist_Injecting_Backdoors_into_Text_Encoders_for_Text-to-Image_ICCV_2023_paper.html) | [:octocat:](https://github.com/LukasStruppek/Rickrolling-the-Artist) |
| 2023 | CVPR 2023    | [How to Backdoor Diffusion Models?](https://arxiv.org/abs/2206.07840) | [:octocat:](https://github.com/IBM/BadDiffusion)             |
| 2023 | CVPR 2023    | [TrojDiff: Trojan Attacks on Diffusion Models with Diverse Targets](https://chenweixin107.github.io/assets/pdf/TrojDiff_camera_ready_main_ieee.pdf) | [:octocat:](https://github.com/chenweixin107/TrojDiff)       |

## Large language model & other NLP tasks

| Year | Publication | Paper                                                                                                                                                        | Code                                                                                         |
| ---- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| 2023 | NeurIPS 2023 | [TrojPrompt: A Black-box Trojan Attack on Pre-trained Language Models](https://neurips.cc/virtual/2023/poster/71224) |  |
| 2023 | ICML 2023 | [Poisoning Language Models During Instruction Tuning](https://arxiv.org/abs/2305.00944) | [:octocat:](https://github.com/AlexWan0/Poisoning-Instruction-Tuned-Models) |
| 2023 | ICLR 2023 | [TrojText: Test-time Invisible Textual Trojan Insertion](https://openreview.net/forum?id=ja4Lpp5mqc2) | [:octocat:](https://github.com/UCF-ML-Research/TrojText) |
| 2023 | NDSS 2023 | [BadGPT: Exploring Security Vulnerabilities of ChatGPT via Backdoor Attacks to InstructGPT ](https://arxiv.org/abs/2304.12298) |  |
| 2022 | ICLR 2022    | [BadPre: Task-agnostic Backdoor Attacks to Pre-trained NLP Foundation Models](https://openreview.net/forum?id=Mng8CQ9eBW)                                    | [:octocat:](https://github.com/kangjie-chen/BadPre)                                          |
| 2022 | IJCAI 2022   | [PPT: Backdoor Attacks on Pre-trained Models via Poisoned Prompt Tuning](https://doi.org/10.24963/ijcai.2022/96)                                             |                                                                                              |
| 2022 | MM 2022      | [Opportunistic Backdoor Attacks: Exploring Human-imperceptible Vulnerabilities on Speech Recognition Systems](https://doi.org/10.1145/3503161.3548261)       |                                                                                              |
| 2022 | NeurIPS 2022 | [BadPrompt: Backdoor Attacks on Continuous Prompts](https://openreview.net/pdf/5c4cf5b33c7da305a496573c8b6b363f56143e32.pdf)                                 | [:octocat:](https://github.com/papersPapers/BadPrompt)                                       |
| 2022 | USS 2022     | [Hidden Trigger Backdoor Attack on NLP Models via Linguistic Style Manipulation](https://www.usenix.org/conference/usenixsecurity22/presentation/pan-hidden) |                                                                                              |
| 2021 | ACL 2021     | [Hidden Killer: Invisible Textual Backdoor Attacks with Syntactic Trigger](https://doi.org/10.18653/v1/2021.acl-long.37)                                     | [:octocat:](https://github.com/thunlp/HiddenKiller)                                          |
| 2021 | ACL 2021     | [Rethinking Stealthiness of Backdoor Attack against NLP Models](https://doi.org/10.18653/v1/2021.acl-long.431)                                               | [:octocat:](https://github.com/lancopku/SOS)                                                 |
| 2021 | ACL 2021     | [Turn the Combination Lock: Learnable Textual Backdoor Attacks via Word Substitution](https://doi.org/10.18653/v1/2021.acl-long.377)                         | [:octocat:](https://github.com/thunlp/BkdAtk-LWS)                                            |
| 2021 | CCS 2021     | [Backdoor Pre-trained Models Can Transfer to All](https://doi.org/10.1145/3460120.3485370)                                                                   | [:octocat:](https://github.com/thunlp/OpenBackdoor)                                          |
| 2021 | CCS 2021     | [Hidden Backdoors in Human-Centric Language Models](https://doi.org/10.1145/3460120.3484576)                                                                 | [:octocat:](https://github.com/lishaofeng/NLP_Backdoor)                                      |
| 2021 | EMNLP 2021   | [Backdoor Attacks on Pre-trained Models by Layerwise Weight Poisoning](https://doi.org/10.18653/v1/2021.emnlp-main.241)                                      |                                                                                              |
| 2021 | EMNLP 2021   | [Mind the Style of Text! Adversarial and Backdoor Attacks Based on Text Style Transfer](https://doi.org/10.18653/v1/2021.emnlp-main.374)                     | [:octocat:](https://paperswithcode.com/paper/?acl=2021.emnlp-main.374)                       |
| 2021 | EUROSP 2021  | [Trojaning Language Models for Fun and Profit](https://doi.org/10.1109/EuroSP51992.2021.00022)                                                               | [:octocat:](https://github.com/alps-lab/trojan-lm)                                           |
| 2021 | ICASSP 2021  | [Backdoor Attack Against Speaker Verification](https://doi.org/10.1109/ICASSP39728.2021.9413468)                                                             | [:octocat:](https://github.com/zhaitongqing233/Backdoor-attack-against-speaker-verification) |

## Graph Neural Networks

| Year | Publication | Paper                                                        | Code                                                         |
| ---- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2022 | CCS 2022    | [Clean-label Backdoor Attack on Graph Neural Networks](https://doi.org/10.1145/3548606.3563531) |                                                              |
| 2022 | ICMR 2022   | [Camouflaged Poisoning Attack on Graph Neural Networks](https://dl.acm.org/doi/abs/10.1145/3512527.3531373) | [:octocat:](https://github.com/chao92/GAFNC)                 |
| 2022 | RAID 2022   | [Transferable Graph Backdoor Attack](https://dl.acm.org/doi/10.1145/3545948.3545976) |                                                              |
| 2021 | SACMAT 2021 | [Backdoor Attacks to Graph Neural Networks](https://dl.acm.org/doi/10.1145/3450569.3463560) | [:octocat:](https://github.com/zaixizhang/graphbackdoor)     |
| 2021 | USS 2021    | [Graph Backdoor](https://www.usenix.org/conference/usenixsecurity21/presentation/xi) | [:octocat:](https://github.com/HarrialX/GraphBackdoor)       |
| 2021 | WiseML 2021 | [Explainability-based Backdoor Attacks Against Graph Neural Network](https://dl.acm.org/doi/abs/10.1145/3468218.3469046) | [:octocat:](https://github.com/xujing1994/Explanability_bkd_gnn) |

## Theoretical analysis

| Year | Publication  | Paper                                                        | Code                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2020 | NeurIPS 2020 | [On the Trade-off between Adversarial and Backdoor Robustness](https://proceedings.neurips.cc/paper/2020/hash/8b4066554730ddfaa0266346bdc1b202-Abstract.html) | [:octocat:](https://github.com/nthu-datalab/On.the.Trade-off.between.Adversarial.and.Backdoor.Robustness) |

# 🛡Backdoor Defenses

## Defense for supervised learning (Image classification)

### Before-training (Preprocessing) stage

| Year | Publication          | Paper                                                        | Code                                                         |
| ---- | -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2023 | ICCV 2023            | [Beating Backdoor Attack at Its Own Game](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Beating_Backdoor_Attack_at_Its_Own_Game_ICCV_2023_paper.html) | [:octocat:](https://github.com/damianliumin/non-adversarial) |
| 2023 | USENIX Security 2023 | [Towards A Proactive ML Approach for Detecting Backdoor Poison Samples](https://arxiv.org/abs/2205.13616) |                                                              |
| 2023 | USENIX Security 2023 | [ASSET: Robust Backdoor Data Detection Across a Multiplicity of Deep Learning Paradigms](https://www.usenix.org/system/files/usenixsecurity23-pan.pdf) | [:octocat:](https://github.com/ruoxi-jia-group/ASSET)        |
| 2023 | USENIX Security 2023 | [How to Sift Out a Clean Data Subset in the Presence of Data Poisoning? ](http://arxiv.org/abs/2210.06516) | [:octocat:](https://github.com/ruoxi-jia-group/Meta-Sift)    |
| 2023 | ICLR 2023            | [Towards Robustness Certification Against Universal Perturbations](https://openreview.net/forum?id=7GEvPKxjtt) | [:octocat:](https://github.com/KaiyuanZh/FLIP)               |
| 2021 | ICML 2021            | [SPECTRE: Defending Against Backdoor Attacks Using Robust Statistics](https://proceedings.mlr.press/v139/hayase21a.html) | [:octocat:](https://github.com/SewoongLab/spectre-defense)   |
| 2021 | USENIX Security 2021 | [Demon in the Variant: Statistical Analysis of DNNs for Robust Backdoor Contamination Detection](https://www.usenix.org/conference/usenixsecurity21/presentation/tang-di) | [:octocat:](https://github.com/TDteach/Demon-in-the-Variant) |
| 2020 | ICLR 2020            | [Robust anomaly detection and backdoor attack detection via differential privacy](https://arxiv.org/abs/1911.07116) |                                                              |
| 2019 | IEEE SP              | [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](https://cs.ucsb.edu/~bolunwang/assets/docs/backdoor-sp19.pdf) | [:octocat:](https://github.com/bolunwang/backdoor)           |
| 2018 |                      | [Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering](https://arxiv.org/pdf/1811.03728.pdf) |                                                              |
| 2018 | NeurIPS 2018         | [Spectral Signatures in Backdoor Attacks](https://proceedings.neurips.cc/paper_files/paper/2018/file/280cf18baf4311c92aa5a042336587d3-Paper.pdf) | [:octocat:](https://github.com/MadryLab/backdoor_data_poisoning) |

### In-training stage

| Year | Publication          | Paper                                                        | Code                                                         |
| ---- | -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2023 | CVPR 2023    | [Backdoor Defense via Adaptively Splitting Poisoned Dataset](https://arxiv.org/abs/2303.12993) | [:octocat:](https://github.com/KuofengGao/ASD) |
| 2023 | CVPR 2023    | [Backdoor Defense via Deconfounded Representation Learning](https://arxiv.org/abs/2303.06818) | [:octocat:](https://github.com/zaixizhang/CBD) |
| 2023 | IEEE SP | [RAB: Provable Robustness Against Backdoor Attacks](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a640/1OXH36wfd3a) | [:octocat:](https://github.com/AI-secure/Robustness-Against-Backdoor-Attacks/blob/master/README.md) |
| 2023 | ICLR 2023 | [Towards Robustness Certification Against Universal Perturbations](https://openreview.net/forum?id=7GEvPKxjtt) | [:octocat:](https://github.com/KaiyuanZh/FLIP) |
| 2022 | ICLR 2022 | [Backdoor defense via decoupling the training process](https://openreview.net/pdf?id=TySnJ-0RdKI) | [:octocat:](https://github.com/SCLBD/DBD) |
| 2022 | NeurIPS 2022 | [Effective Backdoor Defense by Exploiting Sensitivity of Poisoned Samples](https://openreview.net/pdf?id=AsH-Tx2U0Ug) | [:octocat:](https://github.com/SCLBD/Effective_backdoor_defense) |
| 2022 | AAAI 2022 | [Certified Robustness of Nearest Neighbors against Data Poisoning and Backdoor Attacks](https://arxiv.org/abs/2012.03765) |  |
| 2021 | NeurIPS 2021 | [Anti-Backdoor Learning: Training Clean Models on Poisoned Data](https://proceedings.neurips.cc/paper/2021/file/7d38b1e9bd793d3f45e0e212a729a93c-Paper.pdf) | [:octocat:](https://github.com/bboylyg/ABL) |
| 2021 | AAAI 2021 | [Intrinsic Certified Robustness of Bagging against Data Poisoning Attacks](https://arxiv.org/abs/2008.04495) | [:octocat:](https://github.com/jinyuan-jia/BaggingCertifyDataPoisoning) |
| 2022 | NeurIPS 2022 | [BagFlip: A Certified Defense against Data Poisoning](https://arxiv.org/abs/2205.13634) | [:octocat:](https://github.com/foreverzyh/defend_framework) |

### Post-training stage

| Year | Publication  | Paper                                                        | Category             | Code                                                         |
| ---- | ------------ | ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ |
| 2024 | IEEE SP      | [MM-BD: Post-Training Detection of Backdoor Attacks with Arbitrary Backdoor Pattern Types Using a Maximum Margin Statistic](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a015/1RjE9SU7Kz6) | Detection            |                                                              |
| 2023 | NeurIPS 2023 | [Neural Polarizer: A Lightweight and Effective Backdoor Defense via Purifying Poisoned Features](https://neurips.cc/virtual/2023/poster/71467) | Mitigation           |                                                              |
| 2023 | NeurIPS 2023 | [Shared Adversarial Unlearning: Backdoor Mitigation by Unlearning Shared Adversarial Examples](https://neurips.cc/virtual/2023/poster/69874) | Mitigation           |                                                              |
| 2023 | NeurIPS 2023 | [Stable Backdoor Purification with Feature Shift Tuning](https://neurips.cc/virtual/2023/poster/72630) | Mitigation           | [:octocat:](https://github.com/AISafety-HKUST/stable_backdoor_purification) |
| 2023 | NeurIPS 2023 | [CBD: A Certified Backdoor Detector Based on Local Dominant Probability](https://neurips.cc/virtual/2023/poster/72180) |                      |                                                              |
| 2023 | ICCV 2023    | [Enhancing Fine-Tuning Based Backdoor Defense with Sharpness-Aware Minimization](https://openaccess.thecvf.com/content/ICCV2023/html/Zhu_Enhancing_Fine-Tuning_Based_Backdoor_Defense_with_Sharpness-Aware_Minimization_ICCV_2023_paper.html) | Mitigation           |                                                              |
| 2023 | CVPR 2023    | [Backdoor Cleansing with Unlabeled Data](https://arxiv.org/abs/2211.12044) | Mitigation           | [:octocat:](https://github.com/luluppang/BCU)                |
| 2023 | CVPR 2023    | [MEDIC: Remove Model Backdoors via Importance Driven Cloning](https://openreview.net/forum?id=qHcR93949op) | Mitigation           |                                                              |
| 2023 | CVPR 2023    | [Progressive Backdoor Erasing via connecting Backdoor and Adversarial Attacks](https://openaccess.thecvf.com/content/CVPR2023/papers/Mu_Progressive_Backdoor_Erasing_via_Connecting_Backdoor_and_Adversarial_Attacks_CVPR_2023_paper.pdf) | Mitigation           |                                                              |
| 2023 | CVPR 2023    | [Single Image Backdoor Inversion via Robust Smoothed Classifiers](https://arxiv.org/abs/2304.01482) | Inversion            | [:octocat:](https://github.com/locuslab/smoothinv)           |
| 2023 | ICLR 2023    | [UNICORN: A Unified Backdoor Trigger Inversion Framework](https://openreview.net/forum?id=Mj7K4lglGyj) | Inversion            | [:octocat:](https://github.com/RU-System-Software-and-Security/UNICORN) |
| 2023 | ICLR 2023    | [Incompatibility Clustering as a Defense Against Backdoor Poisoning Attacks](https://openreview.net/forum?id=mkJm5Uy4HrQ) | Mitigation           |                                                              |
| 2023 | ICASSP 2023  | [Backdoor Defense via Suppressing Model Shortcuts](https://arxiv.org/pdf/2211.05631.pdf) | Mitigation           | [:octocat:](https://github.com/20000yshust/Backdoor-Defense-Via-Suppressing-Model-Shortcuts) |
| 2022 | ICLR 2022    | [Adversarial Unlearning of Backdoors via Implicit Hypergradient](https://arxiv.org/abs/2110.03735) | Mitigation           | [:octocat:](https://github.com/YiZeng623/I-BAU)              |
| 2022 | ICLR 2022    | [Trigger Hunting with a Topological Prior for Trojan Detection](https://arxiv.org/pdf/2110.08335.pdf) | Detection            | [:octocat:](Trigger Hunting with a Topological Prior for Trojan Detection) |
| 2022 | ICLR 2022    | [AEVA: Black-box Backdoor Detection Using Adversarial Extreme Value Analysis]() | Detection            | [:octocat:](https://github.com/JunfengGo/AEVA-Blackbox-Backdoor-Detection-main) |
| 2022 | ICLR 2022    | [Post-Training Detection of Backdoor Attacks for Two-Class and Multi-Attack Scenarios](https://arxiv.org/abs/2201.08474) | Detection            | [:octocat:](https://github.com/zhenxianglance/2ClassBADetection) |
| 2022 | NeruIPS 2022 | [Pre-activation Distributions Expose Backdoor Neurons](https://proceedings.neurips.cc/paper_files/paper/2022/hash/76917808731dae9e6d62c2a7a6afb542-Abstract-Conference.html#:~:text=In%20this%20work%2C%20we%20demonstrate,to%20efficiently%20locate%20backdoor%20neurons.) | Mitigation           | [:octocat:](https://github.com/RJ-T/NIPS2022_EP_BNP)         |
| 2022 | NeruIPS 2022 | [One-shot Neural Backdoor Erasing via Adversarial Weight Masking](https://proceedings.neurips.cc/paper_files/paper/2022/file/8c0f7107ab85892ccf51f0a814957af1-Paper-Conference.pdf) | Mitigation           | [:octocat:](https://github.com/jinghuichen/AWM)              |
| 2022 | NeruIPS 2022 | [Randomized channel shuffling: Minimal-overhead backdoor attack detection without clean datasets](https://proceedings.neurips.cc/paper_files/paper/2022/file/db1d5c63576587fc1d40d33a75190c71-Paper-Conference.pdf) | Detection            | [:octocat:](https://github.com/VITA-Group/Random-Shuffling-BackdoorDetect) |
| 2022 | MM 2022      | [Purifier: Plug-and-play Backdoor Mitigation for Pre-trained Models Via Anomaly Activation Suppression](https://dl.acm.org/doi/pdf/10.1145/3503161.3548065) | Mitigation           | [:octocat:](https://github.com/clustering-effect/Purifier)   |
| 2022 | IJCAI 2022   | [Eliminating Backdoor Triggers for Deep Neural Networks Using Attention Relation Graph Distillation](https://doi.org/10.24963/ijcai.2022/206) | Mitigation           |                                                              |
| 2022 | ECCV 2022    | [Data-free backdoor removal based on channel lipschitzness](https://arxiv.org/abs/2208.03111) | Mitigation           | [:octocat:](https://github.com/rkteddy/channel-Lipschitzness-based-pruning) |
| 2022 | CVPR 2022    | [Few-Shot Backdoor Defense Using Shapley Estimation](https://openaccess.thecvf.com/content/CVPR2022/papers/Guan_Few-Shot_Backdoor_Defense_Using_Shapley_Estimation_CVPR_2022_paper.pdf) | Mitigation           |                                                              |
| 2022 | CVPR 2022    | [Better Trigger Inversion Optimization in Backdoor Scanning](https://openaccess.thecvf.com/content/CVPR2022/papers/Tao_Better_Trigger_Inversion_Optimization_in_Backdoor_Scanning_CVPR_2022_paper.pdf) | Inversion            | [:octocat:](https://github.com/Gwinhen/PixelBackdoor)        |
| 2022 | CVPR 2022    | [Complex Backdoor Detection by Symmetric Feature Differencing](https://openaccess.thecvf.com/content/CVPR2022/papers/Liu_Complex_Backdoor_Detection_by_Symmetric_Feature_Differencing_CVPR_2022_paper.pdf) | Detection            | [:octocat:](https://github.com/PurduePAML/Exray)             |
| 2022 | INFOCOM 2022 | [Backdoor Defense with Machine Unlearning](https://arxiv.org/abs/2201.09538) | Mitigation           | [:octocat:](https://github.com/fmy266/Pytorch-Backdoor-Unlearning) |
| 2022 | TNNLS 2022   | [Critical Path-Based Backdoor Detection for Deep Neural Networks](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9882007) | Detection            |                                                              |
| 2021 | IEEE SP      | [Detecting AI Trojans Using Meta Neural Analysis](https://arxiv.org/pdf/1910.03137.pdf) | Detection            | [:octocat:](https://github.com/AI-secure/Meta-Nerual-Trojan-Detection) |
| 2021 | NeurIPS 2021 | [Adversarial Neuron Pruning Purifies Backdoored Deep Models](https://proceedings.neurips.cc/paper/2021/file/8cbe9ce23f42628c98f80fa0fac8b19a-Paper.pdf) | Mitigation           | [:octocat:](https://github.com/csdongxian/ANP_backdoor)      |
| 2021 | NeurIPS 2021 | [Topological Detection of Trojaned Neural Networks](https://proceedings.neurips.cc/paper/2021/file/8fd7f981e10b41330b618129afcaab2d-Paper.pdf) | Detection            | [:octocat:](https://github.com/TopoXLab/TopoTrojDetection)   |
| 2021 | ICLR 2021    | [Neural Attention Distillation: Erasing Backdoor Triggers from Deep Neural Networks]() | Mitigation           | [:octocat:](https://github.com/bboylyg/NAD)                  |
| 2021 | TIFS         | [Odyssey: Creation, Analysis and Detection of Trojan Models](https://ieeexplore.ieee.org/document/9524677) | Detection            | [:octocat:](https://github.com/LCWN-Lab/Odyssey)             |
| 2020 | ICLR 2020    | [Bridging Mode Connectivity in Loss Landscapes and Adversarial Robustness](https://arxiv.org/pdf/2005.00060.pdf) | Mitigation           | [:octocat:](https://github.com/IBM/model-sanitization)       |
| 2020 | MM 2020      | [Gangsweep: Sweep out neural backdoors by gan](https://dl.acm.org/doi/10.1145/3394171.3413546) | Mitigation           | [:octocat:](https://github.com/nicholasbennet/neural-network-backdoor-removal) |
| 2020 | ICDM 2020    | [Towards Inspecting and Eliminating Trojan Backdoors in Deep Neural Networks]() | Mitigation           |                                                              |
| 2019 | NeurIPS 2019 | [Defending Neural Backdoors via Generative Distribution Modeling](https://proceedings.neurips.cc/paper_files/paper/2019/file/78211247db84d96acf4e00092a7fba80-Paper.pdf) | Mitigation           | [:octocat:](https://github.com/superrrpotato/Defending-Neural-Backdoors-via-Generative-Distribution-Modeling) |
| 2019 | CCS 2019     | [Abs: Scanning neural networks for backdoors by artificial brain stimulation](https://dl.acm.org/doi/10.1145/3319535.3363216) | Detection            | [:octocat:](https://github.com/naiyeleo/ABS)                 |
| 2019 | IEEE SP      | [Neural cleanse: Identifying and mitigating backdoor attacks in neural networks](https://ieeexplore.ieee.org/document/8835365) | Mitigation           | [:octocat:](https://github.com/bolunwang/backdoor)           |
| 2019 | IJCAI 2019   | [DeepInspect: A Black-box Trojan Detection and Mitigation Framework for Deep Neural Networks](https://aceslab.org/sites/default/files/DeepInspect.pdf) | Detection+Mitigation |                                                              |
| 2018 | RAID 2018    | [Fine-pruning: Defending against backdooring attacks on deep neural networks](https://link.springer.com/chapter/10.1007/978-3-030-00470-5_13) | Mitigation           | [:octocat:](https://github.com/kangliucn/Fine-pruning-defense) |

### Inference stage

| Year | Publication  | Paper                                                        | Code                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2024 | IEEE S&P 2024| [Robust Backdoor Detection for Deep Learning via Topological Evolution Dynamics](https://arxiv.org/pdf/2312.02673.pdf) | [:octocat:](https://github.com/tedbackdoordefense/ted)   
| 2023 | arXiv        | [VDC: Versatile Data Cleanser for Detecting Dirty Samples via Visual-Linguistic Inconsistency](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=lBSoR4IAAAAJ&citation_for_view=lBSoR4IAAAAJ:Zph67rFs4hoC) |                                                              |
| 2023 | NeurIPS 2023 | [Black-box Backdoor Defense via Zero-shot Image Purification](https://neurips.cc/virtual/2023/poster/71421) |                                                              |
| 2023 | NeurIPS 2023 | [A Unified Framework for Inference-Stage Backdoor Defenses](https://neurips.cc/virtual/2023/poster/72827) |                                                              |
| 2023 | ICLR 2023    | [SCALE-UP: An Efficient Black-box Input-level Backdoor Detection via Analyzing Scaled Prediction Consistency](https://openreview.net/forum?id=o0LFPcoFKnr) | [:octocat:](https://github.com/JunfengGo/SCALE-UP%7D)        |
| 2023 | CVPR 2023    | [Detecting Backdoors During the Inference Stage Based on Corruption Robustness Consistency](https://arxiv.org/abs/2303.18191) |                                                              |
| 2023 | CVPR 2023    | [Don’t FREAK Out: A Frequency-Inspired Approach to Detecting Backdoor Poisoned Samples in DNNs](https://openaccess.thecvf.com/content/CVPR2023W/AML/papers/Al_Kader_Hammoud_Dont_FREAK_Out_A_Frequency-Inspired_Approach_to_Detecting_Backdoor_Poisoned_CVPRW_2023_paper.pdf) |                                                              |
| 2023 | NDSS 2023    | [The “Beatrix” Resurrections: Robust Backdoor Detection via Gram Matrices](https://arxiv.org/abs/2209.11715) | [:octocat:](https://github.com/wanlunsec/Beatrix)            |
| 2023 | IJCAI 2023   | [Orion: Online Backdoor Sample Detection via Evolution Deviance](https://www.ijcai.org/proceedings/2023/96#:~:text=In%20this%20paper%2C%20we%20propose,outputs%20of%20the%20backdoor%20inputs.) |                                                              |
| 2021 | ICCV 2021    | [Rethinking the backdoor attacks’ triggers: A frequency perspective](https://arxiv.org/abs/2104.03413) | [:octocat:](https://github.com/YiZeng623/frequency-backdoor) |
| 2020 | IEEE SP      | [SentiNet: Detecting Localized Universal Attacks Against Deep Learning Systems](https://arxiv.org/abs/1812.00292) |                                                              |
| 2019 | ACSAC 2019   | [STRIP: A Defence Against Trojan Attacks on Deep Neural Networks](https://arxiv.org/abs/1902.06531) | [:octocat:](https://github.com/garrisongys/STRIP)            |

## Defense for semi-supervised learning

| Year | Publication | Paper | Code |
| ---- | ----------- | ----- | ---- |
|      |             |       |      |

## Defense for self-supervised learning

| Year | Publication | Paper                                                        | Code                                                  |
| ---- | ----------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| 2023 | CVPR 2023   | [Detecting Backdoors in Pre-trained Encoders](https://arxiv.org/abs/2303.15180) | [:octocat:](https://github.com/GiantSeaweed/DECREE)   |
| 2023 | CVPR 2023   | [Defending Against Patch-based Backdoor Attacks on Self-Supervised Learning](https://arxiv.org/abs/2304.01482) | [:octocat:](https://github.com/UCDvision/PatchSearch) |

## Defense for reinforcement learning

| Year | Publication  | Paper                                                        | Code |
| ---- | ------------ | ------------------------------------------------------------ | ---- |
| 2023 | NeurIPS 2023 | [BIRD: Generalizable Backdoor Detection and Removal for Deep Reinforcement Learning](https://neurips.cc/virtual/2023/poster/70618) |      |
| 2023 | ICCV 2023    | [PolicyCleanse: Backdoor Detection and Mitigation for Competitive Reinforcement Learning](https://openaccess.thecvf.com/content/ICCV2023/html/Guo_PolicyCleanse_Backdoor_Detection_and_Mitigation_for_Competitive_Reinforcement_Learning_ICCV_2023_paper.html) |      |

## Defense for federated learning

| Year | Publication  | Paper                                                        | Code                                           |
| ---- | ------------ | ------------------------------------------------------------ | ---------------------------------------------- |
| 2023 | NeurIPS 2023 | [Theoretically Modeling Client Data Divergence for Federated Natural Language Backdoor Defense](https://neurips.cc/virtual/2023/poster/70177) |                                                |
| 2023 | NeurIPS 2023 | [FedGame: A Game-Theoretic Defense against Backdoor Attacks in Federated Learning](https://neurips.cc/virtual/2023/poster/70499) |                                                |
| 2023 | NeurIPS 2023 | [Lockdown: Backdoor Defense for Federated Learning with Isolated Subspace Training](https://neurips.cc/virtual/2023/poster/71476) |                                                |
| 2023 | ICCV 2023    | [Multi-Metrics Adaptively Identifies Backdoors in Federated Learning](https://openaccess.thecvf.com/content/ICCV2023/html/Huang_Multi-Metrics_Adaptively_Identifies_Backdoors_in_Federated_Learning_ICCV_2023_paper.html) |                                                |
| 2023 | ICLR 2023    | [FLIP: A Provable Defense Framework for Backdoor Mitigation in Federated Learning](https://openreview.net/forum?id=Xo2E217_M4n) | [:octocat:](https://github.com/KaiyuanZh/FLIP) |

## Defense for other CV tasks (Object detection, segmentation)

| Year | Publication  | Paper                                                        | Code |
| ---- | ------------ | ------------------------------------------------------------ | ---- |
| 2023 | NeurIPS 2023 | [Django: Detecting Trojans in Object Detection Models via Gaussian Focus Calibration](https://neurips.cc/virtual/2023/poster/72584) |      |

## Defense for multimodal models (Visual and Language)

| Year | Publication  | Paper                                                        | Code                                                   |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------ |
| 2023 | NeurIPS 2023 | [Robust Contrastive Language-Image Pretraining against Data Poisoning and Backdoor Attacks](https://neurips.cc/virtual/2023/poster/71818) |                                                        |
| 2023 | ICCV 2023    | [CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning](https://openaccess.thecvf.com/content/ICCV2023/html/Bansal_CleanCLIP_Mitigating_Data_Poisoning_Attacks_in_Multimodal_Contrastive_Learning_ICCV_2023_paper.html) | [:octocat:](https://github.com/nishadsinghi/CleanCLIP) |
| 2023 | ICCV 2023    | [TIJO: Trigger Inversion with Joint Optimization for Defending Multimodal Backdoored Models](https://openaccess.thecvf.com/content/ICCV2023/html/Sur_TIJO_Trigger_Inversion_with_Joint_Optimization_for_Defending_Multimodal_Backdoored_ICCV_2023_paper.html) | [:octocat:](https://github.com/indranil-sri/TIJO)      |
| 2023 | CVPR 2023    | [Detecting Backdoors in Pre-trained Encoders](https://arxiv.org/abs/2303.15180) | [:octocat:](https://github.com/GiantSeaweed/DECREE)    |

## Defense for Large Language model & other NLP tasks

| Year | Publication  | Paper                                                        | Code |
| ---- | ------------ | ------------------------------------------------------------ | ---- |
| 2023 | NeurIPS 2023 | [Setting the Trap: Capturing and Defeating Backdoor Threats in PLMs through Honeypots](https://neurips.cc/virtual/2023/poster/72945) |      |
| 2023 | NeurIPS 2023 | [Defending Pre-trained Language Models as Few-shot Learners against Backdoor Attacks](https://neurips.cc/virtual/2023/poster/72193) |      |
| 2023 | NeurIPS 2023 | [Theoretically Modeling Client Data Divergence for Federated Natural Language Backdoor Defense](https://neurips.cc/virtual/2023/poster/70177) |      |
| 2023 | ACL 2023     | [Defending against Insertion-based Textual Backdoor Attacks via Attribution](https://arxiv.org/abs/2305.02394) |      |
| 2023 | ACL 2023     | [Diffusion Theory as a Scalpel: Detecting and Purifying Poisonous Dimensions in Pre-trained Language Models Caused by Backdoor or Bias](https://arxiv.org/abs/2305.04547) |      |

## Defense for diffusion models

| Year | Publication | Paper | Code |
| ---- | ----------- | ----- | ---- |
|      |             |       |      |

## Defense for Graph Neural Networks

| Year | Publication | Paper | Code |
| ---- | ----------- | ----- | ---- |
|      |             |       |      |

# Backdoor for social good

## Watermarking

| Year | Publication  | Paper                                                        | Code                                                         |
| ---- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2022 | IJCAI2022    | [Membership Inference via Backdooring](https://doi.org/10.24963/ijcai.2022/532) | [:octocat:](https://github.com/HongshengHu/membership-inference-via-backdooring) |
| 2022 | NeurIPS 2022 | [Untargeted Backdoor Watermark: Towards Harmless and Stealthy Dataset Copyright Protection](https://openreview.net/pdf/59189794e612834ea8d509a71f501144e4bf881d.pdf) | [:octocat:](https://github.com/THUYimingLi/Untargeted_Backdoor_Watermark) |
| 2018 | USS 2018     | [Turning Your Weakness Into a Strength: Watermarking Deep Neural Networks by Backdooring](https://www.usenix.org/conference/usenixsecurity18/presentation/adi) | [:octocat:](https://github.com/adiyoss/WatermarkNN)          |

## Explainable AI

| Year | Publication | Paper                                                        | Code |
| ---- | ----------- | ------------------------------------------------------------ | ---- |
| 2021 | KDD 2021    | [What Do You See?: Evaluation of Explainable Artificial Intelligence (XAI) Interpretability through Neural Backdoors](https://doi.org/10.1145/3447548.3467213) |      |

# ⚙Benchmark and toolboxes

| Name            | Publication  | Paper                                                        | Code                                                    |
| --------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------- |
| BackdoorBench   | NeurIPS 2022 | [BackdoorBench: A Comprehensive Benchmark of Backdoor Learning](https://arxiv.org/abs/2206.12654) | [:octocat:](https://github.com/SCLBD/backdoorbench)     |
| OpenBackdoor    | NeurIPS 2022 | [A Unified Evaluation of Textual Backdoor Learning: Frameworks and Benchmarks](https://arxiv.org/abs/2206.08514) | [:octocat:](https://github.com/thunlp/OpenBackdoor)     |
| TrojanZoo       | EuroS&P 2022 | [TrojanZoo: Towards Unified, Holistic, and Practical Evaluation of Neural Backdoors]() | [:octocat:](https://github.com/ain-soph/trojanzoo)      |
| BackdoorBox     |              | [BackdoorBox: An Open-sourced Python Toolbox for Backdoor Attacks and Defenses](https://arxiv.org/abs/2302.01762) | [:octocat:](https://github.com/THUYimingLi/BackdoorBox) |
| BackdoorToolbox |              |                                                              | [:octocat:](https://github.com/vtu81/backdoor-toolbox)  |
