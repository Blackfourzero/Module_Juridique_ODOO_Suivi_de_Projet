from odoo import models, fields

class Projet(models.Model):
    _name = "projet.projet"
    nom_projet = fields.Char(string='Nom du projet',required=True)
    description = fields.Text('Description du projet',required=True)
    code_contrat = fields.Char(string='Code contrat',required=True)
    date_debut = fields.Date(string='Date début',required=True)
    date_fin = fields.Date(string='Date fin',required=True)
    etat_projet = fields.Selection([('En cours','En cours'),('Terminé','Terminé'),('En litige','En litige')],string='Etat du projet',required=True)