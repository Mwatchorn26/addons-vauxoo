# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) Vauxoo (<http://vauxoo.com>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Luis Escobar                <luis@vauxoo.com>
#              María Gabriela Quilarque    <gabriela@vauxoo.com>
#    Planified by: Nhomar Hernandez        <nhomar@vauxoo.com>
#    Finance by: Helados Gilda, C.A. http://heladosgilda.com.ve
#    Audited by: María Gabriela Quilarque  <gabriela@vauxoo.com>
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
###
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
{
    "name": "CRM Cost Issue", 
    "version": "0.2", 
    "author": "Vauxoo", 
    "category": "Generic Modules/Accounting", 
    "description": """
        Este modulo agrega el costo de una incidencia segun las horas estimadas.

        Para definir el costo de la Hora, hay que crear un producto de tipo servicio y asociarlo al usuario para que asi pueda generar el costo.

    """, 
    "website": "http://vauxoo.com", 
    "license": "", 
    "depends": [
        "base", 
        "crm", 
        "project", 
        "project_issue", 
        "product"
    ], 
    "demo": [], 
    "data": [
        "view/project_task_view.xml"
    ], 
    "test": [], 
    "js": [], 
    "css": [], 
    "qweb": [], 
    "installable": True, 
    "auto_install": False, 
    "active": False
}