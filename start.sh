if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Sawansingh24 /Btmanjusms
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Btmanjusms
fi
cd /Btmanjusms
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
