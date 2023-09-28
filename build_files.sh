echo "BUILD START"
py -m pip install -r requirements.txt
py -m manage collectstatic --noinput --clear
echo "BUILD END"