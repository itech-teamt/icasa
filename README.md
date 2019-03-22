# icasa
IMPORTANT!

*********************************************************************
*The default branch is yjhallauth. Please DO NOT switch to master!!!*
*********************************************************************

To deploy it on your local machine, follow the steps:

1. clone this repo
2. create a virtual environment
3. in your virtual environment, run the command:
****************************************************************
pip install -r requirements.txt
****************************************************************
4. Run the commands to initialize the program:
****************************************************************
python manage.py migrate
****************************************************************
python populate.py
****************************************************************
python manage.py createsuperuser
****************************************************************
python mamange.py runserver
****************************************************************
