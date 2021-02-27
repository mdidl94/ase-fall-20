from flakon import JsonBlueprint
from flask import Flask, request, jsonify
from myservice.calculator import calculator as c


calc = JsonBlueprint('calc',__name__)

@calc.route('/calc/sum', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.sum(m,n)

    return jsonify({'result':str(result)})

@calc.route('/calc/sub', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.substract(m,n)

    return jsonify({'result':str(result)})

@calc.route('/calc/mul', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.multiply(m,n)

    return jsonify({'result':str(result)})

@calc.route('/calc/div', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.divide(m,n)

    return jsonify({'result':str(result)})

