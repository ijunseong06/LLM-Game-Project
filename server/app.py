from flask import Flask

from src.llm.item_generater import *

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
async def set_data():
    return generate_item()


if __name__ == '__main__':
    app.run(debug=True, port=5000)