## Alejandro Hernández Rodríguez Test for Data Engineer position at Wenea.

Please, first of all, read the [documentation](https://www.dropbox.com/s/23y3kfivao04bxn/TestWeneaDataEngineerDoc.pdf?dl=0) associated!  


## Data ingestion into a MongoDB  ##

The goal is create a systems with several components for ingest and store data. 


### How to run it? ###

You can use docker-compose for up the DB, MongoDB: (You need to have installed before [Docker](https://docs.docker.com/engine/install/) and [Docker-compose](https://docs.docker.com/compose/install/)):
```
docker-compose up -d
```

When database is up, you can run the ingestion proccess executing main.py, you need to have installed 
Python3.9 (this would be dockerized too, but for more simplify, I didn't it): 
```
python3.9 -m venv env
source ./env/bin/activate
export MONGO_ROOT_USERNAME=root
export MONGO_ROOT_PASSWORD=rootpassword
export DATABASE_NAME=local
export DATABASE_ADDRESS=127.0.0.1 
export DATABASE_PORT=27017
export MAX_BYTES_TO_PERSIST=16793598
pip3.9 install -r requirements.txt

python3.9 main.py
```

### How run tests? ###

There are some Unit Test in the project that you can execute using pytest. Go to 
the root of project and execute it:
```
pytest
```

If you get some problems related to unrecognized modules, maybe you need 
to export the python path, so go to the root of the project and: 
```
export PYTHONPATH=`pwd`
```

If you want to see the code coverage, you can get a report running: 
```
pytest --cov=./src tests/
```

There aren't integreation or regression tests. 


### Quality code tools ### 

I use a static typing in python, so for check possible errors and incoherences with types it neccesary 
to uses some tool like Mypy.
If you want to run it: 
```
mypy --config-file mypy.ini ./*.py
```


### How it works? ###

The program simulates an extraction and store process. For do it, in a first step data is fetched from an url (defined in constants). Data need to be in .json structure. The next, is to store the data. The function that do it, receive a raw data from request, convert a .json if is required and send to MongoDB.

The extraction and store process has been implemented for use asynchrounously. So, it's possible execute all of this in a concurrent way, simulating a process that extract data at the same time from differents sources.

If you run main.py, you execute concurrently the process for the [url](https://raw.githubusercontent.com/chargeprice/open-ev-data/master/data/ev-data.json) required and for this other [url](https://data.wa.gov/api/views/f6w7-q2d2/rows.json). 


