# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Template', 'Product']


class Template:
    __metaclass__ = PoolMeta
    __name__ = 'product.template'

    supply_on_sale = fields.Boolean('Supply On Sale',
        states={
            'invisible': ~Eval('purchasable') | ~Eval('salable'),
            },
        depends=['purchasable', 'salable'])


class Product:
    __metaclass__ = PoolMeta
    __name__ = 'product.product'
