from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)
Caesar = CaesarCipher()
Vigenere = VigenereCipher()

#router
@app.route("/")
def home():
    return render_template('index.html')

#router routes CAESAR
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template('caesar.html', encrypted_text=encrypted_text, inputPlainText=text, inputKeyPlain=key)
    
@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = Caesar.decrypt_text(text, key)
    return render_template('caesar.html', decrypted_text=decrypted_text, inputCipherText=text, inputKeyCipher=key)



#router routes VIGENERE
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypted_text = Vigenere.encrypt_text(text, key)
    return render_template('vigenere.html', encrypted_text=encrypted_text, inputPlainText=text, inputKeyPlain=key)
    
@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = Vigenere.decrypt_text(text, key)
    return render_template('vigenere.html', decrypted_text=decrypted_text, inputCipherText=text, inputKeyCipher=key)
    
#main_funtion
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)