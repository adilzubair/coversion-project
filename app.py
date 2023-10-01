from flask import Flask, request, jsonify
import PyPDF2

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_text():
    try:
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            pdf = PyPDF2.PdfFileReader(uploaded_file)
            text = ''
            for page_num in range(pdf.getNumPages()):
                page = pdf.getPage(page_num)
                text += page.extractText()

            return jsonify({'text': text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
