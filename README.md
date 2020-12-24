# web3_matic_python
## install solc using the command (solidity compiler for python)
```
from solc import install_solc
install_solc("v0.4.25")
```
## copy the solc binary using the command
```
sudo cp $HOME/.py-solc/solc-v0.4.25/bin/solc /usr/local/bin
```
## if there is permission error then 
```
cd /usr/local/bin
sudo chown -R $USER solc

```
- to verify permissions
```
cd /usr/local/bin
ls -la
```
