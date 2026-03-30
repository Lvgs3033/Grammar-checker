from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# ----------- TEXT CORRECTION -----------
def correct_text(text):
    try:
        url = "https://api.languagetool.org/v2/check"
        data = {
            'text': text,
            'language': 'en-US'
        }

        response = requests.post(url, data=data)
        result = response.json()

        corrected_text = text

        for match in reversed(result.get('matches', [])):
            if match.get('replacements'):
                start = match['offset']
                end = start + match['length']
                replacement = match['replacements'][0]['value']

                corrected_text = (
                    corrected_text[:start] +
                    replacement +
                    corrected_text[end:]
                )

        return corrected_text

    except Exception as e:
        return f"Error: {str(e)}"


# ----------- PARAPHRASING -----------
def paraphrase_text(text):
    try:
        replacements = {
            "went": "visited",
            "bought": "purchased",
            "very": "extremely",
            "hot": "warm",
            "enjoyed": "had a great time",
            "friend": "companion",
            "came": "joined",
            "ate": "had",
            "lunch": "a meal",
            "restaurant": "dining place"
        }

        words = text.split()
        new_words = []

        for w in words:
            key = w.lower().strip('.,')
            if key in replacements:
                new_word = replacements[key]
                if w[0].isupper():
                    new_word = new_word.capitalize()
                new_words.append(new_word)
            else:
                new_words.append(w)

        return " ".join(new_words)

    except Exception as e:
        return f"Error: {str(e)}"


# ----------- ROUTES -----------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        text = data.get('text', '')

        if not text.strip():
            return jsonify({
                "corrected": "Please enter text",
                "paraphrased": ""
            })

        corrected = correct_text(text)
        paraphrased = paraphrase_text(corrected)

        return jsonify({
            "corrected": corrected,
            "paraphrased": paraphrased
        })

    except Exception as e:
        return jsonify({
            "corrected": "Error",
            "paraphrased": str(e)
        })


if __name__ == '__main__':
    app.run(debug=True)