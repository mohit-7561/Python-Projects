from flask import Flask, jsonify
app = Flask(__name__) 
  
@app.route('/') 
def helloWorld(): 
    return "Hello, World!"

@app.route('/armstrong/<int:n>') 

def armstrong(n):
    sum = 0
    save_n = n
    order = len(str(n))
    while(n>0):
        digit = n%10
        sum += digit**order
        n = n//10
    if (sum == save_n):
        print(f"{save_n} is an armstrong number")
        result = {
            "Number": save_n,
            "Armstrong": True,
            "server ID": "12.2.3.5"
        }
    else:
        print(f"{save_n} is not an armstrong number")
        result = {  
            "Number": save_n,
            "Armstrong": False,
            "server ID": "12.2.3.5"
        }
    return jsonify(result)

  
if __name__ == '__main__': 
    app.run(debug= True) # Debug setting set to true 

