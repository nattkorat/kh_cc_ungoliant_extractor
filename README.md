# Kh_CC_Ungoliant_Extractor
1. Set up ungoliant
``````
$ curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
$ source "$HOME/.cargo/env"
``````
2. Download fasttext language detector model:

``````
wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
``````

3. Create directory to store the extracted data
``````
mkdir src/extracted_data
``````