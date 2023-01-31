# gen-bucketname.py 
Generate a bucket name from a provided noun. 

## requirements
Python3+ 

## usage

```console 
./gen-bucketname.py noun
noun2023-01-31-10-24-45

./gen-bucketname.py -h  
usage: gen-bucketname.py [-h] noun

positional arguments:
  noun        noun to generate a unique bucket name from

optional arguments:
  -h, --help  show this help message and exit

```

## installation

```console
git clone https://github.com/TWolfis/gen-bucketname.git
sudo cp gen-bucketname/src/gen-bucketname.py /usr/local/bin/gen-bucketname
```