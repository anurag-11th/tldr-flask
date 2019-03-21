from flask import Flask, render_template, url_for, redirect, url_for, request, flash, session
from summary import summarize

app = Flask(__name__)
app.secret_key = "bubblysnowmeninjeanschicago"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def get_text():
    summ = []
    if request.method == 'POST':
        text = request.form.get('text')
        # print(text)
        summ = summarize(text)
        summ = [str(s) for s in summ]
        # summ = " ".join(summ)
        summaries = []
        for s in summ:
            # temp_str = "%r"%s
            # raw_str = temp_str[1:-1]
            # print(raw_str)
            # print(type(raw_str))
            # summaries.append(raw_str)
            print(s)
            print("________________")

    return render_template("result.html", summaries=summ)

if __name__ == "__main__":
    app.run(debug=True)