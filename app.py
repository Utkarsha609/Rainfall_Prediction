from flask import render_template, Flask, request
import pickle

app = Flask(__name__, template_folder="templates")

# State = 'MADHYA MAHARASHTRA'

# def get_data(State):
#     data = {"MADHYA MAHARASHTRA", "MATATHWADA", "VIDARBHA",
#             "TAMIL NADU", "West Rajasthan", "EAST RAJASTHAN"}
#     return data.get(State, "Data is not found").strip()

@app.route('/')
def front():
    return render_template('Home_page.html')


@app.route('/predictionhome')
# @app.route('/')
def home():
    return render_template('Front_ Page.html')

@app.route('/analysis')
# @app.route('/')
def analysis():
    return render_template('analysisPage.html')

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    predict.State = request.form.get('State')
    print(str(predict.State))
    return render_template('index.html')

@app.route("/result/", methods=["GET", "POST"])
def result():
    State = predict.State
    if State == 'MARATHWADA':
        pickle_file = './model/MARATHWADA.pkl'
    elif State == 'MADHYA MAHARASHTRA':
        pickle_file = './model/MADHYA_MAHARASHTRA_model.pkl'
    elif State == 'VIDARBHA':
        pickle_file = './model/VIDARBHA.pkl'
    elif State == 'TAMIL NADU':
        pickle_file = './model/model.pkl'
    elif State == 'WEST RAJASTHAN':
        pickle_file = './model/raj_west_model.pkl'
    elif State == 'EAST RAJASTHAN':
        pickle_file = './model/raj_east_model.pkl'

    file = open(pickle_file, 'rb')
    random_Forest = pickle.load(file)
    file.close()

    myDict = request.form
    Month = int(myDict["Month"])
    Year = int(myDict["Year"])
    pred = [Year, Month]
    result = random_Forest.predict([pred])[0]
    print(str(result))
    res = round(result, 2)
    return render_template('result.html', Month=Month, Year=Year, res=res)

if __name__ == "__main__":
    app.run(debug=True)
