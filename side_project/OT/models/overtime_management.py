from odoo import fields, models , api

class overtime_management(models.Model):
    _name = "overtime_management"
    _description = "Phiếu làm thêm"
    _rec_name = 'subject'

    subject = fields.Char(string='Mô tả', required=True)
    department = fields.Many2one(comodel_name='hr.department', string='Phòng ban',required=True)
    date = fields.Date(string='Ngày làm thêm', required=True)
    ot_rate = fields.Float("Tỷ lệ làm thêm", required=True)
    ot_sum = fields.Float("Tổng thời gian làm thêm", compute='_sum_ot')
    reason = fields.Char(string='Lý do làm thêm', size=100, required=True)
    detail = fields.One2many(comodel_name='overtime_detail', inverse_name='management', string="Chi tiết làm thêm")
    status = fields.Selection(string="Trạng thái", selection=[('draft', 'Nháp'),
                                                             ('done', 'Đã phê duyệt'),
                                                             ('reject', 'Bị từ chối')], default='draft')

    def action_approved(self):
        for rec in self:
            for line in rec.detail:
                line.status = 'done'
        self.status = 'done'

    def action_reject(self):
        for rec in self:
            for line in rec.detail:
                line.status = 'reject'
        self.status = 'reject'

    def _sum_ot(self):
        sum = 0
        for rec in self.detail:
            sum += rec.ot_time
        self.ot_sum = sum
