import PySimpleGUI as sg
import pandas as pd
import joblib

logistic_model = joblib.load('logistic_model_Heart_failure.pkl')

def get_dummy_variables(values):
    return {
        'age': float(values['age']),
        'creatinine_phosphokinase': float(values['creatinine_phosphokinase']),
        'ejection_fraction': float(values['ejection_fraction']),
        'platelets': float(values['platelets']),
        'serum_creatinine': float(values['serum_creatinine']),
        'serum_sodium': float(values['serum_sodium']),
        'time': float(values['time']),
        'anaemia_1': 1 if values['anaemia'] == 'Ya' else 0,
        'diabetes_1': 1 if values['diabetes'] == 'Ya' else 0,
        'high_blood_pressure_1': 1 if values['high_blood_pressure'] == 'Ya' else 0,
        'sex_1': 1 if values['sex'] == 'Laki-laki' else 0,
        'smoking_1': 1 if values['smoking'] == 'Merokok' else 0
    }

def predict(values):
    try:
        new_user_data = get_dummy_variables(values)

        new_user_df = pd.DataFrame([new_user_data])

        prediction = logistic_model.predict(new_user_df)

        if prediction[0] == 1:
            return "Hasil: Kemungkinan Kematian Jantung"
        else:
            return "Hasil: Tidak Kemungkinan Kematian Jantung"

    except Exception as e:
        return f"Error: {str(e)}. Periksa input Anda."

layout = [
    [sg.Text('Prediksi Kematian Jantung', font=('Helvetica', 16))],
    [sg.Text('Umur'), sg.InputText(key='age')],
    [sg.Text('Creatinine Phosphokinase (mcg/L)'), sg.InputText(key='creatinine_phosphokinase')],
    [sg.Text('Ejection Fraction (%)'), sg.InputText(key='ejection_fraction')],
    [sg.Text('Platelets (kiloplatelets/mL)'), sg.InputText(key='platelets')],
    [sg.Text('Serum Creatinine (mg/dL)'), sg.InputText(key='serum_creatinine')],
    [sg.Text('Serum Sodium (mEq/L)'), sg.InputText(key='serum_sodium')],
    [sg.Text('Waktu Tindak Lanjut (dalam hari)'), sg.InputText(key='time')],
    [sg.Text('Anemia'), sg.Combo(['Ya', 'Tidak'], key='anaemia')],
    [sg.Text('Diabetes'), sg.Combo(['Ya', 'Tidak'], key='diabetes')],
    [sg.Text('Hipertensi'), sg.Combo(['Ya', 'Tidak'], key='high_blood_pressure')],
    [sg.Text('Jenis Kelamin'), sg.Combo(['Laki-laki', 'Perempuan'], key='sex')],
    [sg.Text('Status Merokok'), sg.Combo(['Merokok', 'Tidak Merokok'], key='smoking')],
    [sg.Button('Prediksi'), sg.Button('Keluar')],
    [sg.Text('Hasil Prediksi:', size=(40, 1), key='result')]
]

window = sg.Window('Prediksi Kematian Jantung', layout, resizable=True, finalize=True)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Keluar'):
        break

    if event == 'Prediksi':
        result = predict(values)
        window['result'].update(result)

window.close()




