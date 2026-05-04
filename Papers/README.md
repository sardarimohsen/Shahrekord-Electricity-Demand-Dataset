
# Publications & Research Foundations

This directory contains the bibliographic information and research context for the studies that utilized the **Shahrekord Electricity Demand Dataset**. These papers provide the theoretical framework, architectural details, and benchmark results for the models implemented in this repository.

---

## 1. Primary Framework: ParDeeB
*   **Title:** ParDeeB: A Graph Framework for Load Forecasting Based on Parallel DeepNet Branches[cite: 2]
*   **Journal:** *Scientia Iranica*, 2021
*   **Authors:** Najmeh Neshat, Mohsen Sardari Zarchi, Hashem Mahlooji

### **Research Focus**
*   This paper introduces the **ParDeeB** (Parallel DeepNet Branches) architecture, a directed acyclic graph (DAG) model specifically designed for multimodal energy data.
*   It demonstrates how the 23 determinants in the Shahrekord dataset are processed through parallel LSTM, GRU, and Dense branches to capture distinct historical dependencies.
*   **Link:** [Read the full paper on Scientia Iranica](https://doi.org/10.24200/sci.2021.56343.4673)

---

## 2. Foundational Study: Residual Peak Load Forecasting
*   **Title:** Application of Deep Learning Models Based on Fully-Connected and Recurrent Neural Networks to Residual Peak Load Forecasting[cite: 2]
*   **Journal:** *Sharif Journal of Industrial Engineering & Management*, 2020]
*   **Authors:** N. Neshat, M. Sardari Zarchi, H. Mahlooji.

### **Research Focus**
*   This foundational work explores the efficacy of standard deep learning architectures, including Stacked Dense and Recurrent Neural Networks (RNNs)[cite: 2].
*   It establishes the baseline performance for forecasting residual peak loads using the provided dataset[cite: 2].
* **Link:** [ Read the full paper on Sharif Journal of Industrial Engineering & Management ](https://sjie.journals.sharif.edu/article_21898.html)

---

## 📄 How to Cite

If you use the dataset or the ParDeeB framework in your research, please cite the following publications[cite: 2]:
```bibtex
@article{neshat2021pardeeb,
  title={ParDeeB: A Graph Framework for Load Forecasting Based on Parallel DeepNet Branches},
  author={Neshat, Najmeh and Zarchi, Mohsen Sardari and Mahlooji, Hashem},
  journal={Scientia Iranica},
  volume={28},
  number={6},
  pages={3551--3567},
  year={2021},
  doi={10.24200/sci.2021.56343.4673}
}

@article{neshat2020application,
  title={Application of Deep Learning Models Based on Fully-Connected and Recurrent Neural Networks to Residual Peak Load Forecasting},
  author={Neshat, N. and Sardari Zarchi, M. and Mahlooji, H.},
  journal={Sharif Journal of Industrial Engineering \& Management},
  volume={36},
  number={1.2},
  pages={103--111},
  year={2020}
}
```

```
