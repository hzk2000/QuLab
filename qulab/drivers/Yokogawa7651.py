# -*- coding: utf-8 -*-
import numpy as np
import visa

from qulab import BaseDriver, QOption, QReal, QList, QInteger


class Driver(BaseDriver):
    support_models = ['Yokogawa']

    quants = [
        QReal('Voltage', unit='V',
            set_cmd='S%(value).2E ;E',
            get_cmd='OD'),

        QReal('Current', unit='A',
            set_cmd='S%(value).2E ;E',
            get_cmd='OD'),

        QInteger('Output',value=1,unit='',
			set_cmd='O%(value)d ;E',
			get_cmd=''),
    ]
    #mode 0:Voltage mode;else current mode
    def mode_select(self,mode=0):
        if mode==0:
            self.write('F1;E')
        else:
            self.write('F5;E')
