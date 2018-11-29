# -*- coding: utf-8 -*-
import numpy as np
import visa

from qulab import BaseDriver, QOption, QReal, QList, QInteger


class Driver(BaseDriver):
    support_models = ['DP832']

    quants = [
        QReal('CH1 Votage',unit='V',ch=1,set_cmd='INST CH%(ch)d;VOLT %(value).4E',get_cmd='MEAS? CH%(ch)d'),

        QOption('CH1 Output',ch=1,
            set_cmd='OUTP CH%(ch)d,%(option)s', options=[('OFF', 'OFF'), ('ON', 'ON')]),
    ]
