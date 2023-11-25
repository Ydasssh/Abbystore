from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    correo = StringField('correo', validators=[DataRequired()])
    contraseña = PasswordField('contraseña', validators=[DataRequired()])

    def imprimir_datos(self):
        print("----------------DATOS----------------")
        print("CORREO: ", self.correo.data)
        print("CONTRASEÑA: ", self.contraseña.data)

    submit = SubmitField('Login')

class FormularioRegistro(FlaskForm):
    nombres = StringField('Nombres', validators=[DataRequired()])
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    direccion = StringField('Direccion', validators=[DataRequired()])

    # Campos de selección para departamento y ciudad
    departamento = SelectField('Departamento', choices=[], validators=[DataRequired()])
    ciudad = SelectField('Ciudad', choices=[], validators=[DataRequired()])
    
    

    nombre_usuario = StringField('Nombre de Usuario', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    confirmar_contraseña = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('contraseña')])
    submit = SubmitField('Registrar')
    
class Buscador(FlaskForm):
    busqueda = StringField('Buscador')
    filtro = SelectField('filtro', choices=[])
    buscar = SubmitField('buscar')