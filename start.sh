if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/AyushSharma64047/postfilter /postfilter 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /postfilter
fi
cd /postfilter 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 bot.py
