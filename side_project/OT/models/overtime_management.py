from odoo import fields, models

class overtime_management(models.Model):
    _name = "overtime_management"
    _description = "Phiếu làm thêm"
    _rec_name = 'department'


    department = fields.Many2one(comodel_name='hr.department', string='Phòng ban',required=True)
    date = fields.Date(string='Ngày làm thêm',required=True)
    ot_rate = fields.Float("Tỷ lệ làm thêm",required=True)
    ot_sum = fields.Float("Tổng thời gian làm thêm")
    reason = fields.Char(string='Lý do làm thêm', size=100,required=True)
    detail = fields.One2many(comodel_name='overtime_detail', inverse_name='management', string="Chi tiết làm thêm")
    status = fields.Selection(string="Trạng thái",selection=[('draft', 'Nháp'),
                                                             ('done', 'Đã phê duyệt'),
                                                             ('reject', 'Bị từ chối')])