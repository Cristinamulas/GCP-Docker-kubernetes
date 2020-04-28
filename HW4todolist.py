from flask import Flask, render_template, redirect, g, request, url_for, jsonify, json
import requests
from requests.utils import requote_uri


app = Flask(__name__)
my_url = "http://localhost:5001/api/items"


@app.route("/")
def show_list():
    response = requests.get(my_url)
    if response.status_code == 200:
        response = response.json()
        return render_template('index.html', todolist=response)
    else: 
        return'unauthorized'

@app.route("/add", methods=['POST'])
def add_entry():
    data = {"what_to_do": 'hw_4', "due_date" :'05/12/2020'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(my_url ,data=json.dumps(data), headers=headers)
    return redirect(url_for('show_list'))

@app.route("/delete/<item>")
def delete_entry(item):
    item = requote_uri(item)
    requests.delete(my_url+item)
    return redirect(url_for('show_list'))

@app.route("/mark/<item>")
def mark_as_done(item):
    item = requote_uri(item)
    requests.put(my_url+item)
    return redirect(url_for('show_list'))


if __name__ == "__main__":
    app.run("0.0.0.0")
