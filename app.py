from flask import Flask, render_template, jsonify
app=Flask(__name__)

JOBS=[
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Bengaluru, India',
        'salary' : 'Rs. 100000'
    },
    {
        'id' : 2,
        'title' : 'Data Scientist',
        'location' : 'Pune, India',
        'salary' : 'Rs. 700000'
    },
    {
        'id' : 3,
        'title' : 'Frontend Engineer',
        'location' : 'Delhi, India'
    },
    {
        'id' : 4,
        'title' : 'Backend Engineer',
        'location' : 'London, UK',
        'salary' : '$. 1000000'
    }
]

@app.route('/')
def helloworld():
    return render_template('home.html', jobs = JOBS)

@app.route('/jobs')
def hello_jovian():
    return jsonify(JOBS)

if __name__=='__main__':
    app.run(debug=True)