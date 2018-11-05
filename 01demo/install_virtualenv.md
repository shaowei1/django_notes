# Step-by-step instructions

virtualenv is an absolute must if you develop with Python. In simple terms, virtualenv creates a folder that stores a private copy of python, pip, and other Python packages. You can then enable this private folder while working a project. By using the virtual environment, you can use different versions of Python and Python packages on a per project basis.

In this post we will step through setting up virtualenv and virtualenvwrapper on Ubuntu Linux.

## Step-by-step instructions

Open a terminal and install the following packages.

sudo apt-get install python-pip python-dev build-essential

sudo pip install virtualenv virtualenvwrapper

sudo pip install --upgrade pip


## Setup virtualenvwrapper in ~/.bashrc.

- Create a backup of your .bashrc file

cp ~/.bashrc ~/.bashrc-org

-  Be careful with this command

printf '\n%s\n%s\n%s' '# virtualenv' 'export WORKON_HOME=~/virtualenvs' \
'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc

add to .bashrc

export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3.6'


## Enable the virtual environment.

source ~/.bashrc

mkdir -p $WORKON_HOME

mkvirtualenv api

-  Exit the 'api' virtual environment
deactivate

## Tips on using virtualenv
To enable the api virtual environment, run the following command:

workon api

To deactivate the api virtual environment, run the following command:

deactivate

That’s it. You now have a virtual environment setup for your Python development.

# python environment
Not exactly sure what you are needing, but maybe this will help. It is a little verbose, but hopefully will answer your questions:

There are a number of things going on here.

First, /usr/local/bin/virtualenvwrapper.sh is a shell script. If you read the script, you will see the following code:

```commandline
# Locate the global Python where virtualenvwrapper is installed.
if [ "$VIRTUALENVWRAPPER_PYTHON" = "" ] 
then
    VIRTUALENVWRAPPER_PYTHON="$(command \which python)"
fi
```

What this means is that the virtualenvwrapper.sh script uses an environmental variable named VIRTUALENVWRAPPER_PYTHON to determine the python installation. This is important because:

Second, multiple versions of python can be installed on a system. (I currently have 3: 2.7, 3.5, and 3.6). And with Linux systems anyway,

/usr/bin/python
is symbolically linked to one of those versions. This is how it looks on my system Linux system:

lenovo:davidj ~ >  ls -l /usr/bin/python
lrwxrwxrwx 1 root root 24 Apr 28 23:36 /usr/bin/python -> 
/etc/alternatives/python
 lenovo:davidj ~ >  ls -l /etc/alternatives/python
lrwxrwxrwx 1 root root 18 Aug 31 14:56 /etc/alternatives/python -> 
/usr/bin/python3.6
So, following the chain of symbolic links, when I run

/usr/bin/python
I am running version 3.6. I can change those links at will to point to version 2.7, 3.5, or any other version I might install.

What all of this means is this: unless you have VIRTUALENVWRAPPER_PYTHON set to a specific python installation, /usr/local/bin/virtualenvwrapper.sh will default to /usr/bin/python to determine the default python version you are running.

In my case, in my .bashrc file I have

export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3.6'
This means that virtualenvwrapper will use python 3.6 because I am telling it to use that specific version.

In your case, the script is failing because virtualenvwrapper is not installed for that version of python that /usr/bin/python points to. To determine your version of python simply run:

python -V
and then install virtualenvwrapper for that version.

I hope this helps.