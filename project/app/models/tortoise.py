from tortoise import fields, models

class TextSumarry(models.Model):
    url = fields.TextField()
    sumarry = fields.TextField()
    created_at = fields.DatatimeField(auto_now_add = True)  

    def __str__(self):
        return self.url

