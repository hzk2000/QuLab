# -*- coding: utf-8 -*-
import numpy as np

from qulab import BaseDriver, QInteger, QOption, QReal, QString, QVector


class Driver(BaseDriver):
    support_models = ['DSG3060']

    quants = [
        QReal('Frequency', unit='Hz',
          set_cmd=':FREQ %(value).13e%(unit)s',
          get_cmd=':FREQ?'),

        QReal('Power', unit='dBm',
          set_cmd=':LEV %(value).8e%(unit)s',
          get_cmd=':LEV?'),

        QOption('Output',
          set_cmd=':OUTP %(option)s', options=[('OFF', 'OFF'), ('ON', 'ON')]),
    ]


    def performGetValue(self, quant, **kw):
        get_Quants = ['Frequency']
        if quant.name in get_Quants and quant.get_cmd is not '':
            cmd = quant._formatGetCmd(**kw)
            res = self.query(cmd).strip('\n')
            quant.value= res[0]
            return res[0]
        else:
            return super(Driver, self).performGetValue(quant, **kw)
