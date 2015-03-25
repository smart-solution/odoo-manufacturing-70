# -*- coding: utf-8 -*-
##############################################################################
#
#    Smart Solution bvba
#    Copyright (C) 2010-Today Smart Solution BVBA (<http://www.smartsolution.be>).
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
from openerp.tools.translate import _


class stock_move(osv.osv):

    _inherit = "stock.move"

    _columns = {
        'purchase_id': fields.many2one('purchase.order', 'Purchase Order'),
    }

class procurement_order(osv.osv):

    _inherit = "procurement.order"

    def create_procurement_purchase_order(self, cr, uid, procurement, po_vals, line_vals, context=None):
        move_obj = self.pool.get('stock.move')
        res = super(procurement_order, self).create_procurement_purchase_order(cr, uid, procurement, po_vals, line_vals, context=context)
        if procurement.move_id:
            move_obj.write(cr, uid, [procurement.move_id.id], {'purchase_id':res}) 
            if procurement.move_id.move_dest_id:
                move_obj.write(cr, uid, [procurement.move_id.move_dest_id.id], {'purchase_id':res}) 
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
