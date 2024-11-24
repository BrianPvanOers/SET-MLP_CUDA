# SET-MLP using CUDA
This code is adapted from Selima Curci's work on SET-MLP to work with CUDA. This is done to speed up the process.
* The current version of the code runs in about 75% - 80% of the time it takes on the CPU. This may vary depending on the machine it runs on, and there is no guarantee it will speed things up.
* I obtained this result on an i7-7700K with 4 cores. On a machine with a CPU with more cores it might actually run slower due to the overhead of copying the arrays to and from the GPU.


###### [Tutorial-SCADS-Summer-School-2020-Scalable-Deep-Learning](https://github.com/SelimaC/Tutorial-SCADS-Summer-School-2020-Scalable-Deep-Learning) 
* Code associated with 6th International (online) Summer school on AI and Big Data tutorial "Scalable Deep Learning Tutorial" and "Scalable deep learning: how far is one billion neurons?" tutorial at ECAI 2020. 
* The code is based on [Implementation 2](https://github.com/dcmocanu/sparse-evolutionary-artificial-neural-networks/tree/master/SET-MLP-Sparse-Python-Data-Structures) of SET-MLP to which Dropout is added.


######  Sparse Evolutionary Artificial Neural Networks
* Proof of concept implementations of various sparse artificial neural network models with adaptive sparse connectivity trained with the Sparse Evolutionary Training (SET) procedure.  
* The [SET implementations](https://github.com/dcmocanu/sparse-evolutionary-artificial-neural-networks) are distributed in the hope that they may be useful, but without any warranties; Their use is entirely at the user's own risk.


###### References

For an easy understanding of these implementations please read the following articles. Also, if you use parts of this code in your work, please cite the corresponding ones:

1. @article{Mocanu2018SET,
  author =        {Mocanu, Decebal Constantin and Mocanu, Elena and Stone, Peter and Nguyen, Phuong H. and Gibescu, Madeleine and Liotta, Antonio},
  journal =       {Nature Communications},
  title =         {Scalable Training of Artificial Neural Networks with Adaptive Sparse Connectivity inspired by Network Science},
  year =          {2018},
  doi =           {10.1038/s41467-018-04316-3},
  url =           {https://www.nature.com/articles/s41467-018-04316-3 }}

2. @article{Mocanu2016XBM,
author={Mocanu, Decebal Constantin and Mocanu, Elena and Nguyen, Phuong H. and Gibescu, Madeleine and Liotta, Antonio},
title={A topological insight into restricted Boltzmann machines},
journal={Machine Learning},
year={2016},
volume={104},
number={2},
pages={243--270},
doi={10.1007/s10994-016-5570-z},
url={https://doi.org/10.1007/s10994-016-5570-z }}

3. @phdthesis{Mocanu2017PhDthesis,
title = {Network computations in artificial intelligence},
author = {Mocanu, Decebal Constantin},
year = {2017},
isbn = {978-90-386-4305-2},
publisher = {Eindhoven University of Technology},
url={https://pure.tue.nl/ws/files/69949254/20170629_CO_Mocanu.pdf }
}

4. @article{Liu2019onemillion,
  author =        {Liu, Shiwei and Mocanu, Decebal Constantin and Mocanu and Ramapuram Matavalam, Amarsagar Reddy and Pei, Yulong Pei and Pechenizkiy, Mykola},
  journal =       {arXiv:1901.09181},
  title =         {Sparse evolutionary Deep Learning with over one million artificial neurons on commodity hardware},
  year =          {2019},
  url={https://arxiv.org/abs/1901.09181 }
}
