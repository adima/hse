# -*- mode: ruby -*-
# vi: set ft=ruby :


ipythonPort = 8888
ipythonHost = 4545
sparkUIPort = 4040


$script = <<SCRIPT
# APT-GET
sudo apt-get update
sudo apt-get upgrade

# PIP
apt-get -y install python-pip

# ANACONDA
#anaconda=Anaconda-2.3.0-Linux-x86_64.sh
anaconda=Anaconda2-2.5.0-Linux-x86_64.sh
if [[ ! -f $anaconda ]]; then
	wget --quiet https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/$anaconda
	#wget --quiet https://repo.continuum.io/archive/$anaconda
fi
chmod +x $anaconda
./$anaconda -b -p /home/vagrant/anaconda
cat >> /home/vagrant/.bashrc << END
export PATH=/home/vagrant/anaconda/bin:$PATH
END
rm $anaconda

# JAVA
apt-get -y install openjdk-7-jdk 

# Vowpal Wabbit
sudo apt-get -y install vowpal-wabbit

#Seaborn 
/home/vagrant/anaconda/bin/conda install seaborn

# XGBOOST
sudo apt-get -y install git
sudo apt-get -y install  make
sudo apt-get -y install g++
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost; ./build.sh
cd python-package; sudo /home/vagrant/anaconda/bin/python setup.py install; cd ../..

# Hyperopt
sudo /home/vagrant/anaconda/bin/pip install pymongo hyperopt 

# Watermark
sudo /home/vagrant/anaconda/bin/pip install watermark 

# APACHE SPARK
#spark=spark-1.4.1-bin-hadoop2.6.tgz
spark=spark-1.6.2-bin-hadoop2.6.tgz
if [[ ! -f $spark ]]; then
	wget --quiet http://d3kbcqa49mib13.cloudfront.net/$spark
fi
tar xvf $spark
rm $spark
#mv spark-1.4.1-bin-hadoop2.6 spark
mv spark-1.6.2-bin-hadoop2.6 spark

# Install findspark & py4j
/home/vagrant/anaconda/bin/pip install findspark py4j

echo 'SPARK_HOME=/home/vagrant/spark' >> /etc/environment
echo 'PYSPARK_PYTHON=/home/vagrant/anaconda/bin/python' >> /etc/environment
echo 'PYTHONPATH=/home/vagrant/spark/python/'  >> /etc/environment

mkdir -p /home/vagrant/.ipython/profile_default/startup/
echo "import findspark\nfindspark.init()\nimport pyspark\nsc = pyspark.SparkContext()" > /home/vagrant/.ipython/profile_default/startup/00-pyspark-setup.py

# Start ipython notebook
sed -i "17i su vagrant -c 'cd /home/vagrant && /home/vagrant/anaconda/bin/ipython notebook --ip=\\"*\\"'" /etc/rc.local

SCRIPT


Vagrant.configure(2) do |config|
  config.vm.box = "hashicorp/precise64"

  config.vm.network "forwarded_port", guest: ipythonPort, host: ipythonHost,
    auto_correct: true

  config.vm.network "forwarded_port", guest: sparkUIPort, host: sparkUIPort,
    auto_correct: true

  config.vm.provider :virtualbox do |v|
  	v.memory = 1024
  	v.cpus = 2
  end
  
  config.vm.provision :shell, inline: $script
  config.vm.synced_folder ".", "/home/vagrant/ML_DM_HSE"

end
