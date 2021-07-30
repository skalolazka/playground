#!/usr/bin/env python

import random
from flask import Flask, request, make_response, jsonify
from multiprocessing import Value

app = Flask(__name__)

@app.route("/main")
def main():
    counter = request.cookies.get('counter')
    counter = int(counter) if counter else 0
    counter += 1
    response = make_response()
    response.set_cookie('counter', str(counter))
    return '<h1>The counter is ' + str(counter) + '</h1>'

@app.route("/cnt")
def cnt():
    counter = Value('i', 0)
    with counter.get_lock():
        counter.value += 1
        # save the value ASAP rather than passing to jsonify
        # to keep lock time short
        unique_count = counter.value

    return jsonify(count=unique_count)

@app.route("/random")
def rand():
    return "<h1> New random number: " + str(random.randint(0,1000)) + "</h1>"