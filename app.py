from flask import  app,Flask,request,jsonify,render_template
import sys

app=Flask(__name__,static_url_path='')


sys.path.insert(0, './crud/')

import crud


@app.before_first_request
def load_keys_onstartup():
    """
    This endpoint triggers loading of keys from the csv file to 
    Trie datastructure.
    """
    crud.loadstrings()
    return 'Successfully completed'

@app.route('/')
def render_searchpage():
    return render_template('search.html')


@app.route('/api/search',methods=['GET'])
def returncandidatestatus():
    """
    This endpoint is used to return search results from the triedatastructure.
    To make use of this endpoint type in http(s)://ipaddress:portnumber/api/search?searchterm=<searchterm>
    Eg. http://127.0.0.1:5000/api/search?searchterm=bala
    """
    searchterm=request.args.get('searchterm')
    if searchterm!=None:
        if len(searchterm)>2:
            return crud.returnsearchresults(searchterm)
        else:
            return jsonify([])
    else:
        return 'Invalid parameter has been passed! please change the parameter.'


app.config['SECRET_KEY'] = 'AZXSDM11233108123A'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,threaded=True)