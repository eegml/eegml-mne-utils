# -*- coding: utf-8 -*-

import mne

DB_LABELS = [
    'Fp1-F7', 'F7-T3', 'T3-T5', 'T5-O1', 'Fp2-F8', 'F8-T4', 'T4-T6', 'T6-O2',
    'Fp1-F3', 'F3-C3', 'C3-P3', 'P3-O1', 'Fp2-F4', 'F4-C4', 'C4-P4', 'P4-O2',
    'Fz-Cz', 'Cz-Pz'
]

TCP_LABELS = [
    'Fp1-F7', 'F7-T3', 'T3-T5', 'T5-O1', 'Fp2-F8', 'F8-T4', 'T4-T6', 'T6-O2',
    'A1-T3', 'T3-C3', 'C3-Cz', 'Cz-C4', 'C4-T4', 'T4-A2', 'Fp1-F3', 'F3-C3',
    'C3-P3', 'Fp2-F4', 'F4-C4', 'C4-P4'
]

LAPLACIAN_LABELS = [
    'F7-aF7', 'T3-aT3', 'T5-aT5', "O1-aO1",
    'F3-aF3', 'C3-aC3', 'P3-aP3',
    'Cz-aCz',
    'F4-aF4', 'C4-aC4', 'P4-aP4',
    'F8-aF8', 'T4-aT4', 'T6-aT6', 'O2-aO2'
]


def raw_bipolar_montage_maker(raw, ch_labels):
    """@raw object
    @ch_labels - list of strings describing bipolar channel
               - example: Fp1-F7
               - names must match names in the raw

    usage:
    raw = mne.read_raw_fif('filename_raw.fif') # a 10-20 channel file
    anodes, caths, label_order_list = raw_bipolar_montage_maker(raw, DB_LABELS)
    
    """
    an_cat_tuples = [label.split('-') for label in DB_LABELS]
    
    anodes, caths = zip(*an_cat_tuples)
    # or
    # anodes = [xx[0] for xx in an_cat_tuples]
    # caths  = [xx[1] for xx in an_cat_tuples]

    # now find mapping between channel number and ch_names
    ch_name2num = {name:num for num, name in enumerate(raw.ch_names)}
    label_order_list = [ch_name2num[label] for label in ch_labels]

    return anodes, caths, label_order_list
