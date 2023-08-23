from flask import Blueprint, jsonify, request
import traceback

# Services
from services.RucService import RucService

ruc = Blueprint('ruc_blueprint', __name__)

@ruc.route('/', methods=['GET'])
def get_dataruc():
  ruc = request.args.get('ruc')
  try:
    dataruc = RucService.get_dataruc(ruc)
    if (len(dataruc) > 0):
        return jsonify({'fields': dataruc, 'message': "SUCCESS", 'success': True})
    else:
        return jsonify({'message': "NOTFOUND", 'success': True})
  except Exception as ex:
    print("error", str(ex))
    print("error", traceback.format_exc())

    return jsonify({'message': "ERROR", 'success': False})
