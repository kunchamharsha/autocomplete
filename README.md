#Autocompleteserver

A Flask server that serves http endpoint to return autocomplete data 
from a csv file using trie datastructure.

#Prerequisites

Operating system
>mac,

>linux


Languages Used
>Python,


Python packages used

>flask,

>pytrie,

>pandas

#Installation 
Create a virtualenv

>virtualenv venv

Activate virtualenv

>source venv/bin/activate

Install python packages using setup.py, run the following command

>python setup.py

Run the flask server 

>python app.py

This will run the server on port number 5000,open browser and search for http://localhost:5000/api/search?searchterm=bala

PS: The first request will take close to 180 seconds depending on the system configuration to load the keys from the csv into the Trie Datastructure. The rest of the search terms should take less than 8 ms on a localserver.

As for the ranking, the datastructure used only returns search terms that have a prefix match and the keys are sorted by their length in ascending order.


#Endpoints and descriptions

FUNCTIONS

Filename: app.py

load_keys_onstartup()
    This endpoint triggers loading of keys from the csv file to
    Trie datastructure.

returncandidatestatus()
    This endpoint is used to return search results from the triedatastructure.
    To make use of this endpoint type in http(s)://ipaddress:portnumber/api/search?searchterm=<searchterm>
    Eg. http://127.0.0.1:5000/api/search?searchterm=bala

Filename: crud.py
    loadstrings()
        Function to load a csv file, preprocess the data and load it into the Trie Datastructure

    returnsearchresults(searchterm)
        Function to return search results
        from the data repository based on the search term input by the users.


#contact details
For any further queries you can mail me on kunchamharsha@gmail.com,
you can also raise an issue and I will get back to you as soon as possible
