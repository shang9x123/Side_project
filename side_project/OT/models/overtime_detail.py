from odoo import fields, models
from datetime import datetime

class overtime_detail(models.Model):
    _name = 'overtime_detail'
    _description = "Chi tiết làm thêm"
    _rec_name = 'employee'

    employee = fields.Many2one(comodel_name='hr.employee',string="Tên nhân viên", required=True)
    department = fields.Many2one(comodel_name='hr.department',string='Phòng ban', required=True)
    date = fields.Date(string='Ngày làm thêm',default=datetime.today(), required=True)
    ot_rate = fields.Float(string='Tỷ lệ làm thêm')
    ot_time = fields.Integer(string="Số giờ làm thêm", min='0.5',max='16',required=True)
    reason = fields.Char(string="Lý do làm thêm", size=100, required=True)
    status = fields.Selection(string='Trạng thái',selection=[('draft','Nháp'),
                                                             ('wait','Chờ phê duyệt'),
                                                             ('done','Đã phê duyệt'),
                                                             ('reject','Bị từ chối')])
    management = fields.Many2one(comodel_name='overtime_management',string='Phiếu làm thêm')