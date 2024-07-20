from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        choice = request.form.get("choice")
        message = request.form.get("message")
        shift = int(request.form.get("shift"))
        
        if choice == "encrypt":
            result = caesar_cipher_encrypt(message, shift)
        elif choice == "decrypt":
            result = caesar_cipher_decrypt(message, shift)
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
