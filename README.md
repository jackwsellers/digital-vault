NOTE: This repository is no longer actively maintained. Since it was only ever supposed to serve as a prototype, only testnet bitcoins can be used (as opposed to mainnet coins). This software will not function unless you have a full bitcoin node running and have made the necessary changes in this repository's source code to reflect that.

# Digital Vault
## A Bitcoin custody platform
### Dependencies:
- [Python 3](https://www.python.org/)
- [Pip](https://pypi.org/project/pip/)
- [Flask](http://flask.pocoo.org/)
- [Bitcoin Core](https://bitcoin.org/en/bitcoin-core/)
#### Installation:
```
git clone https://github.com/jackwsellers/digital-vault.git
cd digital-vault
pip3 install flask_sqlalchemy, flask_login, flask_migrate, flask_sslify, flask_excel, wtforms, flask_wtf
```
### Running the app without HTTPS:
```
export FLASK_APP=app.py FLASK_DEBUG=1
flask run --host=0.0.0.0
```

#### Running the app with HTTPS:
```
pip install pyopenssl
python3.5 myproject.py
https://digitalvault.ga:5000/
```

#### To create the key and certs for localhost(FYI..)
```
Go to https://ssl.indexnl.com/ and click "get me certificate" button.  (Free and Easy SSL certificates for Developers)
Put the certificates in the folder called as "certs" in the root directory of POC.
Go to https://ssl.indexnl.com/windows-root-ca/ and follow the instructions to install a CA Root Certificate.
```

#### To create the key and certs for AWS ec2 instance(FYI..)
```
The domain name is generated by following link (use freenom as server to generate domain name)
www.dot.tk/

following site is used to Create SSL certificate with let’s encrypt for EC2 Amazon linux AMI :
https://medium.com/@idevdebug/create-ssl-certificate-with-lets-encrypt-for-ec2-amazon-linux-ami-1ec31df59e1d

certificate lies in 
/etc/letsencrypt/live/digitalvault.ga/
but due to access issue we copy that in the digital vault folder.
```
