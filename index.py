from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

doses = ["FANTA","COCA","GUARANA","VODKA"]

drinks = [
    {
      "id":1,
      "bt_id":1,
      "name":"FantosaCoquissima",
      "price":20,
      "dose_A":"Fanta",
      "dose_B":"Coca",
      "qty_A":2,
      "qty_B":2,
      "img_url":"",
      "description":"Muito oba oba"
    }
]
    
@app.route('/get_all_drinks', methods=['GET'])
def get_all_drinks():
    return jsonify(drinks)
   
    
@app.route('/get_all_by_bt_id', methods=['GET'])
def get_all_by_bt_id():
    bt_id = request.args.get('bt_id')
    
    if bt_id == '1':
        drinks_same_bt_id = [drink for drink in drinks if drink["bt_id"] == 1]
    elif bt_id == '2':
        drinks_same_bt_id = drinks
    else:
        return jsonify({"error": "bt_id inválido"}), 400
    
    if drinks_same_bt_id:
        drinks_info = [{"id": drink["id"], "name": drink["name"], "price": drink["price"], "img_url": drink["img_url"]} for drink in drinks_same_bt_id]
        return jsonify(drinks_info)
    else:
        return jsonify({"error": "Nenhuma bebida encontrada com o bt_id fornecido"}), 404    


@app.route('/get_detail_by_id', methods=['GET'])
def get_detail_by_id():
    id = request.args.get('id')
    drinks_same_id = [drink for drink in drinks if drink["id"] == int(id)]
    if drinks_same_id:
        drinks_info = [{key: value for key, value in drink.items() if key not in ["bt_id"]} for drink in drinks_same_id]
        return jsonify(drinks_info)
    else:
        return jsonify({"error": "Nenhuma bebida encontrada com o id fornecido"}), 404


@app.route('/create_bebida', methods=['POST'])
def create_bebida():
    data = request.get_json()
    new_drink = {
        "id": len(drinks) + 1,
        "bt_id": data["bt_id"],
        "name": data["name"],
        "price": data["price"],
        "dose_A":data["dose_A"],
        "dose_B":data["dose_B"],
        "qty_A":data["qty_A"],
        "qty_B":data["qty_B"],
        "img_url":data["img_url"],
        "description":data["description"]
        
    }
    drinks.append(new_drink)
    return jsonify({"message": "Bebida criada com sucesso"}), 201

@app.route('/verify_drink', methods=['GET'])
def verify_drink():
    id = request.args.get('id')
    drink = next((d for d in drinks if d["id"] == int(id)), None)
    if drink:
        if drink["dose_A"].upper() in doses and drink["dose_B"].upper() in doses:
            return jsonify({"result": True})
        else:
            return jsonify({"result": False})
    else:
        return jsonify({"error": "Nenhuma bebida encontrada com o id fornecido"}), 404

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)