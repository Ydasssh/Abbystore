from flask import Flask, render_template, redirect, url_for, flash, session, request
from config import config
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from controller.func import *
from controller.validators import is_valid_email
from model.users import User
from model.forms import *


app = Flask(__name__)
app.secret_key = 'Pussyss2003*'
app.config['JWT_SECRET_KEY'] = 'Pussyss2003*'  
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']
app.config['SESSION_COOKIE_SECURE'] = True 
jwt = JWTManager(app)


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return "Redireccion sin token"


@app.route('/', methods=['GET'])
def presentacion():

    return render_template('pages/index.html')


@app.route('/registro', methods=['GET', 'POST'])
def registrar():
    form = FormularioRegistro()
    # print("form---------", form.data)
    
    
    if request.method == 'POST':
    
        id_dpto = int(form.data['departamento'])
        departamentos = obtener_opciones_departamentos()
        # print("Arreglo dpt------------------",departamentos)
        ciudades = obtener_opciones_ciudades(id_dpto)

        form.ciudad.choices = [(ciudad, ciudad) for ciudad in ciudades]
        form.departamento.choices = [(dep, dep) for dep in departamentos]
        
        # print("Opciones de Departamento:", form.departamento.choices)
        # print("Opciones de Ciudad:", form.ciudad.choices)
        
        # print("Valor seleccionado para Departamento:", form.data['departamento'])
        # print("Valor seleccionado para Ciudad:", form.data['ciudad'])
        
        ciudad = form.data['ciudad']
        departamento = form.data['departamento']
        
        print(form.validate_on_submit())

        if form.validate():
            
            print("Form validate on submit")
            
            codigo = generar_codigo_usuario().upper()
            
            print("codigo",codigo)

            usuario = User(
            codigo=codigo,
            nombres=form.nombres.data,
            apellidos=form.apellidos.data,
            telefono=form.telefono.data,
            direccion=form.direccion.data,
            id_departamento=form.departamento.data,
            id_ciudad=ciudad,
            nombre_usuario=departamento,
            correo=form.correo.data,
            contraseña=form.contraseña.data,
            rol="user"
            )
            
            print("codigo -------------------",usuario.codigo)


            if not is_valid_email(usuario.correo):
                print("Email invalido")
                flash('Ingrese un correo válido', 'error')
                return render_template('pages/registro.html', form=form)

            contraseña_hasheada = hashear_contraseña(usuario.contraseña)
            print("Hasea contraseña")

            usuario.contraseña = contraseña_hasheada
            print("Define hash contraseña")
            
            
            
            if User.registrar_usuario(usuario):
                print("TODO CORRECTO")
                response = flash('Registro exitoso. ¡Ahora puedes iniciar sesión!', 'success')
                response = redirect(url_for('registrar'))
                return response
            
        else:
            print(form.errors)

    return render_template('pages/registro.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            correo = form.correo.data
            contraseña = form.contraseña.data
    
            if not is_valid_email(correo):
                flash('Ingrese un correo válido', 'error')
                return render_template('pages/login.html', form=form)
    
    
            user = is_valid_login(correo, contraseña)
            
            print("USER ROL------------------", user['rol'])
    
            if user:
                access_token = create_access_token(identity=correo,additional_claims={'rol':user['rol']})
                response = redirect(url_for('inicio'))
                response.set_cookie('access_token_cookie', access_token, 10 ,secure=True, httponly=True)
                flash(f'Bienvenido usuario', 'success')
                return response
            else:
                flash('Credenciales invalidas', 'error')
                
                
    return render_template('pages/login.html', form=form)


@app.route('/inicio')
@jwt_required()
def inicio():
    
    # print("IDENTITY_____________________________",get_jwt_identity())  # Verifica qué información está disponible en el token
    # rol = get_jwt_identity().get('rol')
    # print(f'Rol del usuario: {rol}')
    
    
    # if rol == 'user':
    #     return "ROL: Usuario"
    # elif rol == 'admin':
    #     return "ROL: Admin"
    
    
    
    # current_user = get_jwt_identity()
    # print(f'Usuario actual: {current_user}')
    

    # print("Session: ", session)
    
    return render_template('pages/inicio-users.html')

@app.route('/admin')
def dashboard():
    
    return render_template('pages/dashboard.html')

@app.route('/usuarios')
def gestion_usuarios():
    
    return render_template('pages/gestion-usuario.html.html')

# @app.route('/prueba')
# def prueba():
#     # Verifica si el token está presente en la cookie
#     access_token = request.cookies.get('access_token')
#     if not access_token:
#         flash('La sesión ha expirado', 'error')
#         return redirect(url_for('login'))  # Redirige al usuario al login si no hay token

#     # Aquí puedes verificar el token JWT si es necesario
#     # Puedes usar funciones como `decode_token` de Flask-JWT-Extended para verificar la validez del token

#     # Renderiza la plantilla protegida
#     return render_template("pages/prueba.html")



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(port=3000)

