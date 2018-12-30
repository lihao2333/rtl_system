from rtlsdr import RtlSdr

class MySdr():
    def __init__():
        self.sdr = RtlSdr()
    def set_paras(paras):
        self.sdr.sample_rate = paras.setdefault("sample_rate","")
        self.sdr.center_freq = paras.setdefault("center_freq","")
        self.sdr.freq_correction = paras.setdefault("freq_correction","")
        self.sdr.gain = paras.setdefault("gain","")
        self.sample_num = paras.setdefault("sample_num",0)
    def sample_data():
        self.sdr.read_samples(self.sample_num)

'''
sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 70e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

print(sdr.read_samples(512))
'''
