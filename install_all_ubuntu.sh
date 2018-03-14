virtualenv cafe_env
source cafe_env/bin/activate
pip install opencafe
cafe-config init
ls cafe_env/.opencafe
cat cafe_env/.opencafe/engine.config
cafe-config plugins install http

git clone https://github.com/openstack/cloudcafe
git clone https://github.com/openstack/cloudroast
pip install cloudcafe/
pip install cloudroast/

# If working with Nova or Cinder, these system dependencies are necessary the SSH plugin. I have them installed, so this does nothing
sudo apt-get install -y git python-dev make build-essential
cafe-config plugins install ssh
cafe-config plugins install winrm