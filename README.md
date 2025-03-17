

# HRRPGraphNet :satellite: 
**Accepted to IET Electronics Letters 2024** :tada::tada::tada:

HRRPGraphNet revolutionizes HRRP data processing through graph neural networks, achieving efficient radar target recognition :zap:.

---

> High Resolution Range Profiles (HRRPs) have become a key area of focus in the domain of Radar Automatic Target Recognition (RATR). Despite the success of deep learning based HRRP recognition, these methods need a large amount of training samples to generate good performance, which could be a severe challenge under non-cooperative circumstances. Currently, deep learning-based models treat HRRPs as sequences, which may lead to ignorance of the internal relationship of range cells. This letter proposes HRRPGraphNet, a novel graph-theoretic approach, whose primary innovation is the use of the graph-theory of HRRP which models the spatial relationships among range cells through a range cell amplitude-based node vector and a range-relative adjacency matrix, enabling efficient extraction of both local and global features in noneuclidean space. Experiments on the aircraft electromagnetic simulation dataset confirmed HRRPGraphNet's superior accuracy and robustness compared with existing methods, particularly in limited training sample condition. This underscores the potential of graph-driven innovations in enhancing HRRP-based RATR, offering a significant advancement over sequence-based methods.
><p align="center">
  > <img src="./architecture.jpg" width="40%">
</p>

---

## Platform :computer: 
Developed and tested on PyCharm with Conda environment. Recommended OS: Linux (Ubuntu 20.04/22.04 LTS).

---

## Getting Started :rocket:
```bash
git clone https://github.com/your-repo/HRRPGraphNet.git
cd HRRPGraphNet
conda create -n hrrpgn python=3.8
conda activate hrrpgn
pip install -r requirements.txt
```

---

## Dataset Structure :file_folder: 
Prepare HRRP data in the following structure:
```
data/
├── train/
│   ├── class1/
│   └── class2/
└── test/
    ├── classA/
    └── classB/
```

## Citation :blue_book:
If HRRPGraphNet inspires your research, please cite:
```bibtex
@article{chen2024hrrpgraphnet,
  title={HRRPGraphNet: Make HRRPs to be Graphs for Efficient Target Recognition},
  author={Chen, Lingfeng and Sun, Xiao and Pan, Zhiliang and Liu, Qi and Wang, Zehao and Su, Xiaolong and Liu, Zhen and Hu, Panhe},
  journal={Electronics Letters},
  volume={60},
  number={22},
  pages={e70088},
  year={2024},
  publisher={IET}
}
```

---

## License :scroll:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact :e-mail:
**Lingfeng Chen**  
:office: National University of Defense Technology  
:email: [chenlingfeng@nudt.edu.cn](mailto:chenlingfeng@nudt.edu.cn)  
:globe_with_meridians: [Personal Homepage](http://lingfengchen.cn/)  
