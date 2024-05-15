from email import message
import email
from flask_wtf import FlaskForm
#Aquí importamos, campodetexto, validadoresdedatos, y el boton submit
from  wtforms import StringField, validators, SubmitField
#Aquí de los validadores importamos el dato obligatorio
from wtforms.validators import DataRequired, Email
import email_validator


     #Clase que hereda de FlaskForm 
    #para crear nuestro formulario personalizado
class miformulario(FlaskForm):   
    nombre = StringField('Nombre',validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = StringField('Mensaje')
    submit = SubmitField(label='Enviar')
