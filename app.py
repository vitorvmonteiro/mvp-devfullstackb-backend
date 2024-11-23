from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa o CORS
from database.incidentes import Incidente
from database import db, init_app

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Inicializa o banco de dados
init_app(app)

# Rota para criar um incidente
@app.route('/api/incidentes', methods=['POST'])
def criar_incidente():
    try:
        dados = request.get_json()
        novo_incidente = Incidente(
            ambiente=dados['ambiente'],
            cluster=dados['cluster'],
            servico=dados['servico'],
            criticidade=dados['criticidade'],
            descricao=dados['descricao'],
            data_hora=dados['data_hora']
        )
        db.session.add(novo_incidente)
        db.session.commit()
        return jsonify({"message": "Incidente criado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

# Rota para listar os incidentes
@app.route('/api/incidentes', methods=['GET'])
def listar_incidentes():
    try:
        incidentes = Incidente.query.all()
        resposta = [{
            "id": i.id,
            "ambiente": i.ambiente,
            "cluster": i.cluster,
            "servico": i.servico,
            "criticidade": i.criticidade,
            "descricao": i.descricao,
            "data_hora": i.data_hora
        } for i in incidentes]
        return jsonify(resposta), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

# Rota para deletar um incidente
@app.route('/api/incidentes/<int:id>', methods=['DELETE'])
def deletar_incidente(id):
    try:
        incidente = Incidente.query.get_or_404(id)
        db.session.delete(incidente)
        db.session.commit()
        return jsonify({"message": "Incidente tratado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
