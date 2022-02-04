## Yichun TAO ##

import Record as r
import Part1_AudioD as w
import Part3_CtoNP as part3
import Part45_onlyFormula as part45
import Part5_LinkLatex as part5
import os

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir);

# 录音
r.record("Audio.wav")

# 识别语音
api = w.RequestApi(appid="5f853927", secret_key="edbd3c830f077f4b0b55ede15adbce81", upload_file_path=r"Audio.wav")
api.all_api_request()

# part2
os.system('Part2_SpeechProcessing.exe')

# part3
part3.CtoNP()


# part4
os.system('Part4_AC.exe')

#part4.5
part45.onlyformula()

# part5
part5.lat()
