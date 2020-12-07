sudo apt-get update

sudo snap install chromium # takes a lot of time approx 15-20 min

sudo apt-get install chromium-chromedriver python3-pip python3-venv -y

python3 -m venv env

. env/bin/activate

pip3 install locust selenium

