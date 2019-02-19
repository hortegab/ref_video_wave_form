#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lab Total
# Generated: Tue Feb 19 03:25:56 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_Canal_AWGN_ff import b_Canal_AWGN_ff  # grc-generated hier_block
from b_Eye_Diagram import b_Eye_Diagram  # grc-generated hier_block
from b_sampler import b_sampler  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import E3TRadio
import cmath
import math
import numpy
import random
import sip


class Lab_total(gr.top_block, Qt.QWidget):

    def __init__(self, ntaps=128, rolloff=0.5):
        gr.top_block.__init__(self, "Lab Total")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lab Total")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.ntaps = ntaps
        self.rolloff = rolloff

        ##################################################
        # Variables
        ##################################################
        self.m = m = 9
        self.samp_rate_usrp = samp_rate_usrp = 100000000
        self.Kd = Kd = math.pow(2,m)
        self.Constelacion = Constelacion = [1.+0.j,    -1.+0.j ]
        self.samp_rate = samp_rate = int(samp_rate_usrp/Kd)
        self.Sps = Sps = 16
        self.M = M = len(Constelacion)
        self.Rs = Rs = samp_rate/Sps
        self.Bps = Bps = int(math.log(M,2))
        self.run_stop = run_stop = True
        self.Tmax_scope = Tmax_scope = 32./Rs
        self.TimingDelay = TimingDelay = 0
        self.Rb = Rb = Rs*Bps
        self.NodB = NodB = -65
        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((Constelacion), (), 4, 1).base()
        self.Fc = Fc = 80e6
        self.Delay_osc_tx = Delay_osc_tx = 38
        self.BW = BW = samp_rate/2.

        ##################################################
        # Blocks
        ##################################################
        self.canal = Qt.QTabWidget()
        self.canal_widget_0 = Qt.QWidget()
        self.canal_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_0)
        self.canal_grid_layout_0 = Qt.QGridLayout()
        self.canal_layout_0.addLayout(self.canal_grid_layout_0)
        self.canal.addTab(self.canal_widget_0, "Diagrama de Ojo")
        self.canal_widget_1 = Qt.QWidget()
        self.canal_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_1)
        self.canal_grid_layout_1 = Qt.QGridLayout()
        self.canal_layout_1.addLayout(self.canal_grid_layout_1)
        self.canal.addTab(self.canal_widget_1, "Constelaciones")
        self.canal_widget_2 = Qt.QWidget()
        self.canal_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_2)
        self.canal_grid_layout_2 = Qt.QGridLayout()
        self.canal_layout_2.addLayout(self.canal_grid_layout_2)
        self.canal.addTab(self.canal_widget_2, "Osciloscopio")
        self.canal_widget_3 = Qt.QWidget()
        self.canal_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_3)
        self.canal_grid_layout_3 = Qt.QGridLayout()
        self.canal_layout_3.addLayout(self.canal_grid_layout_3)
        self.canal.addTab(self.canal_widget_3, "PSD Spectrum")
        self.top_grid_layout.addWidget(self.canal, 1,0,1,4)
        self._TimingDelay_range = Range(0, Sps-1, 1, 0, 200)
        self._TimingDelay_win = RangeWidget(self._TimingDelay_range, self.set_TimingDelay, "Timing", "counter_slider", int)
        self.top_grid_layout.addWidget(self._TimingDelay_win, 0,3,1,1)
        self._NodB_range = Range(-140., 0., 1., -65, 200)
        self._NodB_win = RangeWidget(self._NodB_range, self.set_NodB, "No (in dB for white noise)", "counter_slider", float)
        self.top_grid_layout.addWidget(self._NodB_win, 0,1,1,1)
        self._Delay_osc_tx_range = Range(0, 1000*Sps, 1, 38, 200)
        self._Delay_osc_tx_win = RangeWidget(self._Delay_osc_tx_range, self.set_Delay_osc_tx, "Delay_osc_tx", "counter_slider", int)
        self.canal_grid_layout_2.addWidget(self._Delay_osc_tx_win, 0,0,1,1)
        self._BW_range = Range(0., samp_rate/2., (samp_rate/2)/128., samp_rate/2., 200)
        self._BW_win = RangeWidget(self._BW_range, self.set_BW, "Ch BW (Hz)", "counter_slider", float)
        self.top_grid_layout.addWidget(self._BW_win, 0,2,1,1)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0,1,1)
        self.qtgui_time_sink_x_0_2_0_0 = qtgui.time_sink_f(
        	int(Tmax_scope*Rb), #size
        	Rb, #samp_rate
        	"bits transmitidos versus regenerados", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_2_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2_0_0.set_y_axis(-2, 2)
        
        self.qtgui_time_sink_x_0_2_0_0.set_y_label("", "")
        
        self.qtgui_time_sink_x_0_2_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_2_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_2_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_2_0_0.disable_legend()
        
        labels = ["Tx. Bits transmitidos", "Rx. Bits regenerados", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_2_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_2_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2_0_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_2_0_0_win, 2,0,1,1)
        self.qtgui_time_sink_x_0_2_0 = qtgui.time_sink_f(
        	int(Tmax_scope*Rs), #size
        	Rs, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2_0.set_y_axis(-2, 2)
        
        self.qtgui_time_sink_x_0_2_0.set_y_label("", "")
        
        self.qtgui_time_sink_x_0_2_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2_0.enable_grid(False)
        self.qtgui_time_sink_x_0_2_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_2_0.disable_legend()
        
        labels = ["Re", "Im", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_2_0_win, 1,0,1,1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	int(Tmax_scope*samp_rate), #size
        	samp_rate, #samp_rate
        	"Entrada y salida del canal", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-3, 3)
        
        self.qtgui_time_sink_x_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()
        
        labels = ["Tx", "Rx", "Re.Rx", "Im.Rx", "Re.Rx.Muestreo          .",
                  "Im.Rx.Muestreo", "", "", "", ""]
        widths = [6, 6, 6, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "red",
                  "red", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, 0,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_1_win, 1,0,1,2)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"PSD", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-60, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["Tx.Entrada al canal", "Rx.Salida del canal", "", "", "",
                  "", "", "", "", ""]
        widths = [4, 4, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_3.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, int(Delay_osc_tx/Sps)+1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Delay_osc_tx)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.b_sampler_0 = b_sampler(
            DelayDiez=TimingDelay,
            Sps=Sps,
        )
        self.b_Eye_Diagram_0 = b_Eye_Diagram(
            AlphaLineas=0.5,
            GrosorLineas=20,
            N_eyes=2,
            Samprate=samp_rate,
            Sps=Sps,
            Title="Rx.Canal",
            Ymax=2,
            Ymin=-2,
            Delay_i=0,
        )
        self.canal_grid_layout_0.addWidget(self.b_Eye_Diagram_0, 0,0,1,1)
        self.b_Canal_AWGN_ff_0 = b_Canal_AWGN_ff(
            BW=BW,
            Ch_NodB=NodB,
            Ch_Toffset=0,
            samp_rate=samp_rate,
        )
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 1000)), True)
        self.E3TRadio_Zero_Order_Hold_0 = E3TRadio.Zero_Order_Hold(Sps)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.b_Canal_AWGN_ff_0, 0))    
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_char_to_float_1, 0))    
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.b_Eye_Diagram_0, 0))    
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.b_sampler_0, 0))    
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.qtgui_time_sink_x_0_1, 1))    
        self.connect((self.b_sampler_0, 1), (self.b_Eye_Diagram_0, 1))    
        self.connect((self.b_sampler_0, 1), (self.blocks_null_sink_0, 0))    
        self.connect((self.b_sampler_0, 0), (self.blocks_null_sink_0_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.blocks_char_to_float_1, 0), (self.E3TRadio_Zero_Order_Hold_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0_1, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0_2_0_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.qtgui_time_sink_x_0_2_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff

    def get_m(self):
        return self.m

    def set_m(self, m):
        self.m = m
        self.set_Kd(math.pow(2,self.m))

    def get_samp_rate_usrp(self):
        return self.samp_rate_usrp

    def set_samp_rate_usrp(self, samp_rate_usrp):
        self.samp_rate_usrp = samp_rate_usrp
        self.set_samp_rate(int(self.samp_rate_usrp/self.Kd))

    def get_Kd(self):
        return self.Kd

    def set_Kd(self, Kd):
        self.Kd = Kd
        self.set_samp_rate(int(self.samp_rate_usrp/self.Kd))

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Rs(self.samp_rate/self.Sps)
        self.b_Canal_AWGN_ff_0.set_samp_rate(self.samp_rate)
        self.b_Eye_Diagram_0.set_Samprate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.set_BW(self.samp_rate/2.)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Rs(self.samp_rate/self.Sps)
        self.E3TRadio_Zero_Order_Hold_0.set_retardo(self.Sps)
        self.b_Eye_Diagram_0.set_Sps(self.Sps)
        self.b_sampler_0.set_Sps(self.Sps)
        self.blocks_delay_0_0.set_dly(int(self.Delay_osc_tx/self.Sps)+1)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Rb(self.Rs*self.Bps)
        self.set_Tmax_scope(32./self.Rs)
        self.qtgui_time_sink_x_0_2_0.set_samp_rate(self.Rs)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rb(self.Rs*self.Bps)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_TimingDelay(self):
        return self.TimingDelay

    def set_TimingDelay(self, TimingDelay):
        self.TimingDelay = TimingDelay
        self.b_sampler_0.set_DelayDiez(self.TimingDelay)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.qtgui_time_sink_x_0_2_0_0.set_samp_rate(self.Rb)

    def get_NodB(self):
        return self.NodB

    def set_NodB(self, NodB):
        self.NodB = NodB
        self.b_Canal_AWGN_ff_0.set_Ch_NodB(self.NodB)

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc

    def get_Delay_osc_tx(self):
        return self.Delay_osc_tx

    def set_Delay_osc_tx(self, Delay_osc_tx):
        self.Delay_osc_tx = Delay_osc_tx
        self.blocks_delay_0.set_dly(self.Delay_osc_tx)
        self.blocks_delay_0_0.set_dly(int(self.Delay_osc_tx/self.Sps)+1)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.b_Canal_AWGN_ff_0.set_BW(self.BW)


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--ntaps", dest="ntaps", type="intx", default=128,
        help="Set ntaps [default=%default]")
    parser.add_option(
        "", "--rolloff", dest="rolloff", type="eng_float", default=eng_notation.num_to_str(0.5),
        help="Set rolloff [default=%default]")
    return parser


def main(top_block_cls=Lab_total, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(ntaps=options.ntaps, rolloff=options.rolloff)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
