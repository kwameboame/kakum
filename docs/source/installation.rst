Installation Guide
==================

You can get Kakum by cloning it in your local development environment. Make sure you have git installed and run the following command

``git clone https://bitbucket.org/penplusbytes/kakum``

Kakum runs on python 2.7 so if you don't have it, you need to get it. If you have 3.x and 2.7 installed, switch to 2.7 by giving it priority in your PATH settings in environment variables.

After switching to python 2.7, create a virtual environment by running:

``mkvirtual env envname``

'envname' should be replaced with your desired name.

Choose a secret key and export it to the environment:

``set SECRET_KEY=your_secret_key``

'your_secret_key' should be replaced with a key of your choice.

The next step is to install dependencies. Run this command:

``pip install -r requirements.txt``

Now, run the local server:

``python manage.py runserver``

You will see the app running at localhost:8000


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`