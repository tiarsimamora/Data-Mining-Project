from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', label=0)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    '''
    Predict the label based on user inputs
    and render the result to the html page
    '''
    features = ['jnspelsep', 'kdkc', 'typeppk', 'dati2', 'cmg', 'severitylevel', 'diagprimer', 'ClmProcedureCode_2']
    umur, jkpst, features = [x for x in request.form.values()]

    data = []

    data.append(int(umur))
    if jkpst == 'Laki-laki':
        data.extend([0, 1])
    else:
        data.extend([1, 0])

    if features == 'value':
        data.extend([0, 1])
    else:
        data.extend([1, 0])

    # if kdkc == 'value':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])
    
    # if typeppk == 'value':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])
    
    # if dati2 == 'Ya':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])
    
    # if cmg == 'value':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])
    
    # if severitylevel == 'va;ue':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])
    
    # if diagprimer == 'value':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])

    # if ClmProcedureCode_2 == 'value':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])


    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', label=output, umur=umur, jkpst=jkpst, features=features)


if __name__ == '__main__':
    app.run(debug=True)