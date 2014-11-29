import platform
system = platform.system()

if system == 'Linux':
    import wave
    import ossaudiodev as oss
    sound = wave.open('success.wav','rb')
    (nc,sw,fr,nf,comptype, compname) = sound.getparams( )
    dsp = oss.open('/dev/dsp','w')
    try:
      from ossaudiodev import AFMT_S16_NE
    except ImportError:
      if byteorder == "little":
        AFMT_S16_NE = oss.AFMT_S16_LE
      else:
        AFMT_S16_NE = oss.AFMT_S16_BE
    dsp.setparameters(AFMT_S16_NE, nc, fr)
    data = sound.readframes(nf)
    sound.close()
    dsp.write(data)
    dsp.close()
