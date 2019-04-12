# -*- coding: utf-8 -*-


# IPython log file
# print('PyDev console: using IPython 7.2.0\n')

# import sys; print('Python %s on %s' % (sys.version, sys.platform))
# sys.path.extend(['C:\\Users\\clee\\code\\mne_learn', 'C:/Users/clee/code/mne_learn'])
# import sys
# sys.__file__
# import os
# os.__file__
# import json
# get_ipython().run_line_magic('pinfo', 'json.load')
# fp = open('c:/Users/clee/code/bects-connectivity/47238654/FA27312R_1-1+-annot.json')
# anns = json.load(fp)
# anns
# anns.keys()
# anns['type_names']
# anns['sfreq']
# anns['channels']
# anns.keys()
# anns['time']
# labeltime = list(zip(anns['label'], anns['time']))
# labeltime[:5]
# event_list = [[int(393.5*200), 0, 1],
#               [int(399.5*200), 1, 2],
#               [int(410*200), 2, 1]]
# event_list
# sfreq = anns['sfreq']
# labeltime[5:10]
# Lspike_asleep = [ (xx[1][0]*sfreq, 0, 0) for xx in labeltime if xx[0] == 'L-spike-asleep']
# Lspike_asleep
# Lspike_asleep[:5]
# Lspike_asleep_event_list
# Lspike_asleep_event_list = Lspike_asleep
# tbefore = 0.2; tafter=0.2

# help(mne.Epochs)
# Lspike_asleep_event_list
# get_ipython().run_line_magic('logstart', '')

import json
import mne


class AnnotationsConverter:
    """
    convert he annotations from the LVIS eeg_annotator
    into event lists or epoch

    c = AnnotationsConverter()
    c.load_json('annotations.json')
    events = c.to_event_list()

    TODO: add to_epoch()
    """
    def __init__(self):
        pass

    def load_json(self, file_name):
        with open(file_name) as fp:
            self.annotations = json.load(fp)
        self.sfreq = self.annotations["sfreq"]
        anns = self.annotations
        self.labeltime = list(zip(anns["label"], anns["time"]))
        # creates a list of tuples with the format: ('<label>', [<start_time_sec>,duration_sec])
        # example
        # [('spindle', [354.038, 1.0]),
        #  ('spindle', [397.962, 0.8040000000000305]),
        #  ('spindle', [435.368, 1.391999999999996]),
        #  ('L-spike-asleep', [452.098, 0.0]),
        #  ('bilat-spike-asleep', [450.488, 1.136000000000024]),
        #  ('L-spike-asleep', [461.158, 0.0]),... ]
        self.labels = list(set(self.annotations["label"]))  # not so efficient
        self.labels.sort()  # just so it is consistent
        self.label2num = {xx[1]: xx[0] for xx in enumerate(self.labels)}

    def labels_types(self):
        return self.labels

    def to_event_list(self, labelchoices=None):
        """just create an event list based on a signal label
        this has the form of a list of tuples
        [(<sample_number>, 0, <event_id>),
         (<sample_number>, 0, <event_id>),...
         ]

        @labelchoices is an optional list or tuple of labels (strings) you want in the event list
        """
        l2n = self.label2num
        sfreq = self.sfreq
        if labelchoices:
            events = [
                (int(xx[1][0] * sfreq), 0, l2n[xx[0]])
                for xx in self.labeltime
                if xx[0] in labelchoices
            ]
        else:
            events = [(int(xx[1][0] * sfreq), 0, l2n[xx[0]]) for xx in self.labeltime]

        return events
