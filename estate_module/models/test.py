from odoo import fields, models
from dateutil.relativedelta import relativedelta
from datetime import datetime

class TestModel(models.Model):
    _name = "test.model"  # el . el ORM lo convierte en _
    _description = "Test Model"
    
    name = fields.Char(string='Nombre', required = True, default="uknown")
    description = fields.Text(string='Descripcion')
    postcode = fields.Char(string='Codigo Postals')
    date_availability = fields.Date(string='Fecha Disponible')
    # default = lambda self: fields.DateTime.today()
    expected_price = fields.Float(string='Precio Esperado', digits=(6, 2))
    selling_price = fields.Float(string='Precio Venta', digits=(6, 2), readonly=True)
    bedrooms = fields.Integer(string='Cantidad Cuartos', default=2)
    living_area = fields.Integer(string='Area de la vivienda')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Tiene garage')
    garden = fields.Boolean(string='Tiene Jardin')
    garden_area = fields.Integer(string='Area del Jardin')
    garden_orientation = fields.Selection([
        ('North', 'Norte'),
        ('South', 'Sur'),
        ('East', 'Este'),
        ('West', 'Oeste')
    ], string='Posicion del Jardin')
    state = fields.Selection([
        ('new', 'Nuevo'),
        ('offer_received', 'Oferta Recibida'),
        ('offer_accepted', 'Oferta Aceptada'),
        ('sold', 'Vendida'),
        ('cancelled', 'Cancelada')
    ], string='estado', active = True, default = 'new')
    
    
    def default_get(self, fields):
        print(' default_get '*100)
        res = super(TestModel,self).default_get(fields)
        res.update({
            'date_availability': datetime.now()+relativedelta(months=3)
        })
        
        return res