from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>WILLY-PROJECT</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; }
        .container { max-width: 400px; background: white; padding: 20px; margin: auto; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h2 { text-align: center; color: #0056b3; }
        input, select, button { width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { background-color: #0056b3; color: white; border: none; cursor: pointer; font-weight: bold; }
        .receipt { background: #eef; padding: 15px; border-radius: 5px; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>WILLY-PROJECT</h2>
        <form method="POST">
            <label>Jina la Mteja:</label>
            <input type="text" name="jina" placeholder="Ingiza jina kamili" required>

            <label>Chagua Huduma:</label>
            <select name="huduma">
                <option value="Vyeti vya Kuzaliwa">Vyeti vya Kuzaliwa</option>
                <option value="Kutengeneza Logo">Kutengeneza Logo</option>
                <option value="Website Development">Website Development</option>
                <option value="Automatic Systems">Automatic Systems</option>
            </select>

            <button type="submit">Tengeneza Risiti</button>
        </form>

        {% if risiti %}
        <div class="receipt">
            <h3>RISITI YA ODA</h3>
            <p><strong>Mteja:</strong> {{ risiti.jina }}</p>
            <p><strong>Huduma:</strong> {{ risiti.huduma }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    risiti = None
    if request.method == 'POST':
        jina = request.form.get('jina')
        huduma = request.form.get('huduma')
        risiti = {'jina': jina, 'huduma': huduma}
    return render_template_string(HTML_TEMPLATE, risiti=risiti)

if __name__ == '__main__':
    app.run(debug=True)
