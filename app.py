from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  


productos = []

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        
        id_producto = request.form['id']
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        fecha_vencimiento = request.form['fecha_vencimiento']
        categoria = request.form['categoria']
        
       
        productos.append({
            'id': id_producto,
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio,
            'fecha_vencimiento': fecha_vencimiento,
            'categoria': categoria
        })
        
        flash('Producto agregado exitosamente!')
        return redirect(url_for('index'))
    
    return render_template('agregar.html')

@app.route('/eliminar/<id_producto>')
def eliminar(id_producto):
    global productos
    productos = [p for p in productos if p['id'] != id_producto]
    flash('Producto eliminado exitosamente!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)