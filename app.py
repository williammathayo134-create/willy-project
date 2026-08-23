import datetime
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>WILLY-PROJECT SYSTEM</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f9; }
        .card { background: white; padding: 20px; border-radius: 8px; max-width: 400px; margin: auto; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h2 { color: #0056b3; text-align: center; }
        select, input, button { width: 100%; padding: 10px; margin: 8px 0; box-sizing: border-box; }
        button { background: #ff6600; color: white; border: none; font-weight: bold; cursor: pointer; }
        .receipt { background: #eef; padding: 15px; border-left: 4px solid #0056b3; font-family: monospace; }
    </style>
</head>
<body>
    <div class="card">
        <h2>WILLY-PROJECT</h2>
        <form method="POST">
            <label>Jina la Mteja:</label>
            <input type="text" name="jina" required placeholder="Ingiza jina kamili">

            <label>Chagua Huduma:</label>
            <select name="huduma">
                <option value="Vyeti vya Kuzaliwa">Vyeti vya Kuzaliwa - TZS 15,000</option>
                <option value="Kutengeneza Logo">Kutengeneza Logo - TZS 30,000</option>
                <option value="Website Development">Website Development - TZS 150,000</option>
                <option value="Automatic Systems">Automatic Systems - TZS 100,000</option>
            </select>

            <button type="submit">Tengeneza Risiti</button>
        </form>

        {% if risiti %}
        <div class="receipt">
            <h3>RISITI YA ODA</h3>
            <p><b>Tarehe:</b> {{ risiti.tarehe }}</p>
            <p><b>Mteja:</b> {{ risiti.jina }}</p>
            <p><b>Huduma:</b> {{ risiti.huduma }}</p>
            <p><b>Hali:</b> IMELIPWA (PAID)</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    risiti = None
    if request.method == 'POST':
        jina = request.form.get('jina')
        huduma = request.form.get('huduma')
        tarehe = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        risiti = {'jina': jina, 'huduma': huduma, 'tarehe': tarehe}
    return render_template_string(HTML_TEMPLATE, risiti=risiti)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
