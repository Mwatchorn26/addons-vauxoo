# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2010 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: Luis Torres (luis_t@vauxoo.com)
############################################################################
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
##############################################################################
from osv import osv, fields
import netsvc
from tools.translate import _

class stock_picking(osv.osv):
    _inherit = 'stock.picking'
    
    def action_cancel_draft(self, cr, uid, ids, *args):
        if not len(ids):
            return False
        move_obj = self.pool.get('stock.move')
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for p_id in ids:
            moves = move_obj.search(cr,uid,[('picking_id','=',p_id)])
            move_obj.write(cr,uid,moves,{'state':'draft'})
            # Deleting the existing instance of workflow for PO
            wf_service.trg_delete(uid, 'stock.picking', p_id, cr)
            wf_service.trg_create(uid, 'stock.picking', p_id, cr)
        for (id,name) in self.name_get(cr, uid, ids):
            message = _("Picking '%s' has been set in draft state.") % name
            self.log(cr, uid, id, message)
        return True
stock_picking()