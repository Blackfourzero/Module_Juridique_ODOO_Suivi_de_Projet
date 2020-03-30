from odoo import models, fields

class Reunion(models.Model):
    _name = "reunion.reunion"
    nom_projet = fields.Many2one('projet.projet',string='Projet',required=True)
    objet_reunion = fields.Char(string='Objet de la réunion',required=True)
    date_reunion = fields.Date(string='Date',required=True)