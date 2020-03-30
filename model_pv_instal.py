from odoo import models, fields

class PV_instal(models.Model):
    _name = "pv_instal.pv_instal"
    nom_projet = fields.Many2one('projet.projet',string='Projet',required=True)
    code_pv = fields.Char(string='Code PV',required=True)
    type_instal = fields.Selection([('Logiciel','Logiciel'),('Matériel','Matériel')],string='Type de l\'installation',required=True)
	traite = fields.Boolean(string='Traité',required=True)
    valide = fields.Boolean(string='Validé',required=True)
    observation = fields.Text(string='Observation',required=False)