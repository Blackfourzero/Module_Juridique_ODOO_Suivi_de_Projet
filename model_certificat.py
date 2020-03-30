from odoo import models, fields

class Certificat(models.Model):
    _name = "certificat.certificat"
    nom_projet = fields.Many2one('projet.projet',string='Projet',required=True)
    code_certificat = fields.Char(string='Code certificat',required=True)
    description = fields.Text('Description du service',required=True)
	traite = fields.Boolean(string='Traité',required=True)
    valide = fields.Boolean(string='Validé',required=True)
    observation = fields.Text(string='Observation',required=False)