from tinydb import TinyDB, Query
from script import add
import json
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

db = TinyDB('db.json')

add(1,2)

