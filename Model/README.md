# EnPy - English to Python Translation Model

![CoNaLa Logo](https://conala-corpus.github.io/conala-logo.png "CoNaLa Logo")

This repository contains our submission for the [CoNaLa Challenge competition](https://competitions.codalab.org/competitions/19175).

## Table of contents

  * [Architecture Diagram](#architecture-diagram)
  * [Setup Prerequisites](#setup-prerequisites)
      * [Setup A Cluster Account](#cluster-account)
  * [Model Setup On Linux](#model-setup-on-linux)
  * [Running Jobs](#running-jobs)
  * [More Infomation](#more-information)


## Setup Prerequisites

Before setting up our project we'd like to make sure you have some prerequisite installations and setups.

### Cluster Account


**Note:** Since training the model takes a long time we highly recommend using a computer cluster.

### Step 1: Python Setup
 * If you are using the cluster run the following command to enable **Python 3.7 with CUDA**: `module load cuda/9.2  anaconda3/5.0.1-cuda92`
 
* If you are not using the cluster, install **Python 3.7** from [*Anaconda*](https://www.anaconda.com/download/).

 **Note:** You need to run ``module load...`` on the cluster every time you login because the default python version is 2.7.
 
 **Optional:** To make *Python 3.7 w/ CUDA* the default Python run the following command ``echo 'module load cuda/9.2  anaconda3/5.0.1-cuda92' >> ~/.bashrc``
 ### Step 2: Dependencies Setup
 * Install *Dynet* using the command ``pip install --user dynet``  
   * You can also run the following to install dynet with GPU ``BACKEND=cuda pip install --user  git+https://github.com/clab/dynet#egg=dynet``

 * Install [xnmt](https://github.com/neulab/xnmt) using the following commands:
   * ``wget https://github.com/neulab/xnmt/archive/0.1.0.tar.gz``
   * ``pip install --user 0.1.0.tar.gz``
   * ``rm 0.1.0.tar.gz``
   * **Note** - To make sure xnmt and dynet are installed properly run ``python`` then type ``import xnmt``
 * Navigate to the xnmt directory using ``cd xnmt`` and run the following command ``pip install -r requirements.txt``
 *  Install additional dependencies for xnmt using pip:
   * ``pip install --user librosa``
   * ``pip install --user Sphinx``
   * ``pip install --user sphinxcontrib-napoleon``
   * ``pip install --user docopt``
   * ``pip install --user graphviz``
   * ``pip install --user sentencepiece>=0.0.6``
   * ``pip install --user tensorflow``
   * ``pip install --user tensorboardX unidecode pylru``
   * ``python -m ntlk.downloader``
   
   
 ### Step 3: EnPy Model Setup
* cd to a directory of your choosing, outside of xnmt.
* Run the following command in terminal/command prompt ``git clone https://github.com/HIJaXAnonymous/HIJaX``
* Run the following command: ``echo "alias watchme='watch -n 10 qstat -u $USER'" >> ~/.bashrc; source ~/.bashrc``
  * This enables you to run type the command ``watchme`` to view the status CoNaLa's jobs on the cluster.
* cd to `conala-baseline`
* Run ``pip install --user -r requirements.txt``
* Run ``cd ..``
* To extract and pre-process the dataset run the following in the home directory: ``bash conala-baseline/test_split.sh``
  * **Note** - it will take a few minutes to complete.
* Create a folder in your home directory using the following command `mkdir ~/results_archive/`
### Step 4: Test Run
Run ``bash ultraLaunch.bash`` for a test run. It will take around 30 minutes. The results should be stored in a folder inside results_archive with a timestamp.

### Running Jobs
* To submit a job to the cluster run the following command:
``qsub -q copperhead -l walltime=36:00:00 -d $(pwd) -l nodes=1:ppn=16 -l mem="8GB" ./ultraLaunch.bash``
* Feel free to exit the terminal and leave it, the job will keep running until it's done.
## More Information
For more information on what each file and folder contains, please visit this **TO BE ADDED**.

