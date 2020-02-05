from app import app
from flask import render_template, request, send_from_directory
from .process import *
import uuid


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("home.html")


@app.route("/combinations", methods=['GET', 'POST'])
def generate():
    sample_size = int(request.form.get('sample_size'))
    choice = request.form.get('choice')
    report = pd.DataFrame(compile_final_results(sample_size, choice))
    report_name = choice+str(sample_size)+str(uuid.uuid4()) + '.tsv'
    report.to_csv(os.path.join(path+'/app/results/', report_name), sep='\t', index=False)
    return send_from_directory(os.path.join(path+'/app/results'), report_name, as_attachment=True)
