# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2015 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
##############################################################################

{
    "name": "Deltatech Stock Reports",
    "version": "1.0",
    "author": "Terrabit, Dorin Hongu",
    "website" : "www.terrabit.ro",
    "description": """
    
Functionalitati:
    Raport cu pozitii din liste de ridicare
    """,

    "category": "Generic Modules",
    "depends": ["base", "stock","stock_account"],


    "license": "AGPL-3",

    "data": [ 'security/ir.model.access.csv',
              "report/stock_picking_report.xml"],
    "active": False,
    "installable": True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
