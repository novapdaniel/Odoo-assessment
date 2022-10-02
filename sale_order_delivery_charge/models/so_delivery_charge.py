from odoo import fields, models, api




class SaleOrderDeliveryCharge(models.Model):
    _inherit = 'sale.order'

    delivery_charge = fields.Float(String="Delivery Charge")

    @api.model
    def create(self, vals_list):
        res = super(SaleOrderDeliveryCharge, self).create(vals_list)
        prd_id = self.env['product.product'].search([('name', '=', 'Delivery Charge')])
        if not prd_id:
            prd_id = self.env['product.product'].create({
                'name': 'Delivery Charge',
                'detailed_type': 'service',
                'invoice_policy': 'order',
            })
        if res.order_line.product_id:
            res.order_line.create({
                'product_id': prd_id.id,
                'name': 'Delivery Charge',
                'product_uom_qty': 1,
                'product_uom': 1,
                'price_unit': res.delivery_charge,
                'delivery_charge_check':True,
                'order_id': res.id,
                'tax_id': False,

            })
        return res

class SaleOrderLineDeliveryCharge(models.Model):
    _inherit = 'sale.order.line'

    delivery_charge_check = fields.Boolean(String="Delivery Charge Check")

class AccountMoveLineDeliveryCharge(models.Model):
    _inherit = 'account.move.line'

    is_account_move = fields.Boolean(String="Account Move")

    def create(self, vals_list):
        res = super(AccountMoveLineDeliveryCharge, self).create(vals_list)
        for rec in res:
            if rec.product_id.name == 'Delivery Charge':
                rec.is_account_move = True

        return res

