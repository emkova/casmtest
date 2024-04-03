import os, sqlite3

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get(".env"),
)

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        reflection = request.form["reflection"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {"role": "system","content": "You are a virtual assistant here to help your users cultivate their online presence. Your responsibilities include brainstorming ideas, answering questions, and helping with organizing/scheduling project timelines. Your goal is to act as a collaborative team member, supporting your human counterparts in their creative process"},
                {"role": "user", "content": reflection}
            ]
        )
        msg = response.choices[0].message.content
        conn = get_db_connection()
        conn.execute("INSERT INTO prompts (reflection, msg) VALUES (?, ?)",
                     (reflection, msg))
        conn.commit()
        conn.close()
        return redirect(url_for("index", result=msg))

    result = request.args.get("result")
    return render_template("index.html", result=result)