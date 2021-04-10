from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        nama = request.form.get('nama')
        nim  = request.form.get('nim')
        programStudi  = request.form.get('programStudi')
        jenisKelamin = request.form.get('jenisKelamin')
        tempatLahir  = request.form.get('tempatLahir')
        tanggalLahir  = request.form.get('tanggalLahir')
        alamat  = request.form.get('alamat')
        return render_template("output.html",
        namamhs = nama,
        nimmhs  = nim,
        prodi = programStudi,
        jnskelamin = jenisKelamin,
        tmplahir = tempatLahir,
        tgllahir = tanggalLahir,
        alamat = alamat)



if __name__ == "__main__":
    app.run()