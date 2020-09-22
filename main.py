from flask import Flask,jsonify, request
app = Flask(__name__)

@app.route('/')
def entryPoint():
    return jsonify("This is my fetchrewards solution. Please hit endpoint /fetchrewards/string1/string2/ where string1 and string2 are parameters to check my solution")

@app.route('/fetchrewards', strict_slashes = False)
def fetchrewards(string1=None, string2=None):
    query_params = request.args.to_dict()
    print(query_params)
    if not 'string1' in query_params or not 'string2' in query_params:
        this_error = "ERROR: Please either pass arguments into request as {string1:valueOfString1, string2:valueOfString2} or into url as fetchrewards/?string1=valueOfString1&string2=valueOfString2"
        print("ERROR")
        return jsonify(this_error)

    string1 = query_params["string1"]
    string2 = query_params["string2"]

    if string1 == None or string2 == None:
        this_error = "ERROR: Please enter string parameters into the url /fetchrewards/string1/string2"
        return this_error

    v1 = string1
    v2 = string2

    v1_split = v1.split(".")
    v2_split = v2.split(".")

    if len(v1) == 1:
        v1_split = []
        v1_split.append(v1)
    
    if len(v2) == 1:
        v2_split = []
        v2_split.append(v2)

    print(v1_split,v2_split)

    while len(v1_split) < len(v2_split):
        v1_split.append("0")

    while len(v2_split) < len(v1_split):
        v2_split.append("0")

    v1_full = ""
    v2_full = ""
    for i in range(len(v1_split)):
        v1_full += v1_split[i]
        v2_full += v2_split[i]

    print(int(v1_full), int(v2_full))

    if int(v1_full) == int(v2_full):
        return_string = v1 + " is equal to " + v2

    else:
        if int(v1_full) < int(v2_full):
            return_string = v1 + " is before " + v2

        else:
            return_string = v1 + " is after " + v2
            
    return jsonify(return_string)





    

