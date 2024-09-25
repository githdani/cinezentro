# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class cinezentro(models.Model):
#     _name = 'cinezentro.cinezentro'
#     _description = 'cinezentro.cinezentro'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class Pelicula(models.Model):
    _name = 'cinezentro.pelicula'
    
    name = fields.Char(string = "Título", required= True)
    genero = fields.Selection([("1","Acción"),("2","Comedia"),("3","Drama"),("4","Terror"),
                               ("5","Ciencia Ficción"),("6","Aventura")],string="Género")
    duracion = fields.Integer(string="Duración (min)")
    fecha_estreno= fields.Date(string = "Fecha de estreno")
    sinopsis = fields.Text(string="Sinopsis")
    puntuacion= fields.Float(string = "Puntuacion IMDB", compute="puntuacion_total")
    
    funciones_ids = fields.One2many('cinezentro.funciones', 'pelicula', string='Funciones')
    opiniones_ids = fields.One2many('cinezentro.opinion', 'pelicula_id', string='Opiniones')
    
    @api.depends('opiniones_ids.puntuacion_opi')
    def puntuacion_total(self):
        for pelicula in self:
            if pelicula.opiniones_ids:
                puntuaciones = pelicula.opiniones_ids.mapped('puntuacion_opi')
                if puntuaciones:
                    pelicula.puntuacion = sum(puntuaciones) / len(puntuaciones)
                else:
                    pelicula.puntuacion = 0.0
            else:
                pelicula.puntuacion = 0.0
    
    
class Sala(models.Model):
    _name= 'cinezentro.sala'
    
    name= fields.Char(string = "Sala")
    capacidad = fields.Integer(string = "Capacidad")
    ubicacion = fields.Char(string = "Ubicación")
    
    funciones_ids = fields.One2many('cinezentro.funciones', 'sala_id', string='Funciones')
   
    
    
    
class Funciones(models.Model):
    _name= 'cinezentro.funciones'
    
    name = fields.Char(string= "Nombre función")
    fecha_hora = fields.Datetime(string='Fecha y hora de la función')
    precio_entrada = fields.Float(string='Precio de entrada')
    
    pelicula = fields.Many2one('cinezentro.pelicula', string='Película')
    sala_id = fields.Many2one('cinezentro.sala', string='Sala')
    
    boletos_ids = fields.One2many('cinezentro.boletos', 'funcion_id', string='Boletos')




class Boletos(models.Model):
    _name = 'cinezentro.boletos'
    
    numero_asiento = fields.Integer(string='Número de asientos')
    precio_pagado = fields.Float(string='Precio total', compute='precio_total')
    
    funcion_id = fields.Many2one('cinezentro.funciones', string='Función')
    cliente_id = fields.Many2one('res.partner', string='Cliente')
    
    @api.depends('numero_asiento', 'funcion_id')
    def precio_total(self):
        for boleto in self:
            if boleto.numero_asiento and boleto.funcion_id:
                boleto.precio_pagado = boleto.numero_asiento * boleto.funcion_id.precio_entrada
            else:
                boleto.precio_pagado = 0.0
    
    


class Opinion(models.Model):
    _name = 'cinezentro.opinion'
    
    comentario = fields.Text(string ="Comentario")
    puntuacion_opi = fields.Float(string = "Puntuacion")
    
    pelicula_id = fields.Many2one('cinezentro.pelicula', string='Película')
    cliente_id = fields.Many2one('res.partner', string='Cliente')