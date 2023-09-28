echo "BUILD START"
python3 -m pip install virtualenv
python3 -m venv env
python3 -m env\scripts\activate
python3 -m pip install -r requirements.txt
python3 -m manage collectstatic --noinput --clear
echo "BUILD END"