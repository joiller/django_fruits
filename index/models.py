from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    pwd = models.CharField(max_length=30)

    class Meta:
        db_table = 'user'
        verbose_name = 'user'


class GoodType(models.Model):
    type = models.CharField(max_length=30, verbose_name='类型')
    picture = models.ImageField(upload_to='static/upload/goodtype', null=True, verbose_name='图片')
    description = models.TextField(verbose_name='描述')

    def __str__(self):
        return self.type

    def to_dict(self):
        return {
            'type': self.type,
            'picture': self.picture.__str__(),
            'desc': self.description
        }

    class Meta:
        db_table = 'goodtype'
        verbose_name = 'goodtype'


class Good(models.Model):
    name = models.CharField(max_length=30, verbose_name='商品名称')
    price = models.DecimalField(decimal_places=2, verbose_name='商品价格', max_digits=7)
    special = models.CharField(max_length=30, verbose_name='商品规格')
    picture = models.ImageField(upload_to='static/upload/good')
    type = models.ForeignKey('GoodType', verbose_name='商品类型', on_delete=models.SET_NULL, null=True)
    isActive = models.BooleanField(verbose_name='是否上架', default=True)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price.__str__(),
            'special': self.special,
            'picture': self.picture.__str__(),
            'isActive': self.isActive
        }

    class Meta:
        db_table = 'good'
        verbose_name = 'good'


class Cart(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    good = models.ForeignKey('Good', on_delete=models.CASCADE)
    num = models.IntegerField()

    def to_dict(self):
        dic = {
            'num': self.num,
            'name': self.good.name,
            'picture': self.good.picture.__str__(),
            'price': self.good.price.__str__(),
            'gid': self.good.id
        }
        return dic

    class Meta:
        db_table = 'cart'
