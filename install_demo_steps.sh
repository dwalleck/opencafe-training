virtualenv cafe_env
source cafe_env/bin/activate
pip install opencafe
cafe-config init
ls cafe_env/.opencafe
cat cafe_env/.opencafe/engine.config
cafe-plugins install http

# If working with CloudRoast

# These system dependencies are necessary for pycrypto
apt-get install -y git python-pip python-dev make build-essential
cafe-plugins install ssh
cafe-plugins install winrm

git clone https://github.com/openstack/cloudcafe
git clone https://github.com/openstack/cloudroast
pip install cloudcafe/
pip install cloudroast/