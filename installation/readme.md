


# conda
Check the lastest version of Anaconda at 
https://repo.anaconda.com/archive/ 

```
cd ~/Downloads
wget https://repo.anaconda.com/archive/Anaconda2-5.3.0-Linux-x86_64.sh #617.8M 	2018-11-19 13:37:31
md5sum Anaconda2*.sh
bash Anaconda2*.sh 
	#Licence
	#ENTER/yes/yes/no

	#Anaconda2 will now be installed into this location:
	#/home/tree/anaconda2
	# - Press ENTER to confirm the location

	#Do you wish the installer to initialize Anaconda2
	#in your /home/tree/.bashrc ? [yes|no]

	#Do you wish to proceed with the installation of Microsoft VSCode? [yes|no]
	#>>> no

source ~/.bashrc
#rm Anaconda3*.sh #don't delete in case of reinstallation
```


* verify installation 
```
conda info
conda --version
```


# Brian 2



```
conda create -n brain python=3.6 pip 
conda activate brain


pip install nose
pip install matplotlib


conda install -c conda-forge brian2
conda config --add channels conda-forge
conda install brian2


conda deactivate
```



```
conda remove -n brain --all
```


# test

conda activate brain
python

```
import brian2
brian2.test() # it takes 20-30 mins
```

conda deactivate


