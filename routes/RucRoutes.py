from flask import Blueprint, jsonify, request
import traceback

# Services
from services.RucService import RucService
from utils.Security import Security

ruc = Blueprint('ruc_blueprint', __name__)

@ruc.route('/', methods=['GET'])
def get_dataruc():
  has_access = Security.verify_token(request.headers)
  ruc = request.args.get('ruc')

  if has_access == False:
    return jsonify({'message': 'Acceso denegado'}),401
  
  #Validaciones
  if not ruc:
      return jsonify({'message': 'RUC no enviado'}),400
  
  ruc = ruc.strip()
  if len(ruc) != 11:
      return jsonify({'message': 'RUC no valido'}),400

  if ruc[0] != '1' and ruc[0] != '2':
      return jsonify({'message': 'RUC no valido'}),400
  #-----------------
  try:
    dataruc = RucService.get_dataruc(ruc)
    if (len(dataruc) > 0):
        return jsonify({'fields': dataruc, 'message': "SUCCESS", 'success': True}),200
    else:
        return jsonify({'message': "NOTFOUND", 'success': True})
  except Exception as ex:
    print("error", str(ex))
    print("error", traceback.format_exc())
    return jsonify({'message': "ERROR", 'success': False}),500
