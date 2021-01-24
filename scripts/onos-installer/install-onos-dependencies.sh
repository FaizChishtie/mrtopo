sudo adduser sdn --system --group

for JavaCommand in java jar java2groovy javac javadoc javafxpackager javah javap javapackager javaws
do
    sudo update-alternatives --install /usr/bin/$JavaCommand $JavaCommand /your_path_extracted_jdk/bin/$JavaCommand 1
done

sudo apt install openjdk-11-jdk

sudo apt-get install curl