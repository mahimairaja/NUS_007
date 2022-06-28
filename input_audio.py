import parselmouth
import glob
import numpy as np
import pandas as pd
from parselmouth.praat import call
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import io


##Generating voice report
def process(voiceID, f0min, f0max, unit):
    sound = parselmouth.Sound(voiceID) # read the sound
    pitch = call(sound, "To Pitch", 0.0, f0min, f0max) #create a praat pitch object
    pulses = call([sound, pitch], "To PointProcess (cc)")
    report = parselmouth.praat.call([sound, pitch, pulses], "Voice report", 0.0, 0.0, 75, 600, 1.3, 1.6, 0.03, 0.45)
    return report

##Preprocessing data
def preprocess(df):
  df2=df.iloc[1:,:]# removing first row
  row=df2.iloc[:,1]#getting all rows in col 1
  return row


##According to 26 features dataset

# col=[]
# r=[]
# columns=['Id','Pitch',
#  'Median pitch',
#  'Mean pitch',
#  'Standard deviation',
#  'Minimum pitch',
#  'Maximum pitch',
#  'Pulses',
#  'Number of pulses',
#  'Number of periods',
#  'Mean period',
#  'Standard deviation of period',
#  'Voicing',
#  'Fraction of locally unvoiced frames',
#  'Number of voice breaks',
#  'Degree of voice breaks',
#  'Jitter',
#  'Jitter (local)',
#  'Jitter (local, absolute)',
#  'Jitter (rap)',
#  'Jitter (ppq5)',
#  'Jitter (ddp)',
#  'Shimmer',
#  'Shimmer (local)',
#  'Shimmer (local, dB)',
#  'Shimmer (apq3)',
#  'Shimmer (apq5)',
#  'Shimmer (apq11)',
#  'Shimmer (dda)',
#  'Harmonicity of the voiced parts only',
#  'Mean autocorrelation',
#  'Mean noise-to-harmonics ratio',
#  'Mean harmonics-to-noise ratio']
# df3=pd.DataFrame(columns=columns)


##According to 754 features dataset
##Building dataframe

col=[]
r=[]
columns=['Id','Pitch',
 'Median pitch',
 'Mean pitch',
 'Standard deviation',
 'Minimum pitch',
 'Maximum pitch',
 'Pulses',
 'numPulses',
 'numPeriodsPulses',
 'meanPeriodPulses',
 'stdDevPeriodPulses',
 'Voicing',
 'Fraction of locally unvoiced frames',
 'Number of voice breaks',
 'Degree of voice breaks',
 'Jitter',
 'locPctJitter',
 'locAbsJitter',
 'rapJitter',
 'ppq5Jitter',
 'ddpJitter',
 'Shimmer',
 'locShimmer',
 'locDbShimmer',
 'apq3Shimmer',
 'apq5Shimmer',
 'apq11Shimmer',
 'ddaShimmer',
 'Harmonicity of the voiced parts only',
 'meanAutoCorrHarmonicity',
 'meanNoiseToHarmonicity',
 'meanHarmToNoiseHarmonicity']
df3=pd.DataFrame(columns=columns)
 
##Taking input voice sample
##Main function
k=0
li=[]
for wave_file in glob.glob("audio/*.wav"):
  sound = parselmouth.Sound(wave_file)
  report=process(sound, 75, 500, "Hertz")
  df = pd.read_csv(io.StringIO(report), sep=':',error_bad_lines=False,header=None)
  row=preprocess(df)
  r.append(k)
  for i in range(1,len(row)+1):
    r.append(row[i])
  li.append(r)
  r=[]
  k=k+1

##Drop null values
for j in range(len(li)):
  df3.loc[len(df3.index)] = li[j] #Add list to dataframe
df3=df3.dropna(axis=1)

##Remove extra characters from data
new=[]
for i in range(len(df3)):
 for d in df3.iloc[i,1:28]:
   new.append(d.split(" ")[1])
   i=i+1
new_v=[]
for d in new:
  new_v.append(d.split("%")[0])  

##Convert data into float
float_list = [float(i) for i in new_v]

##Final datafram generation
col=[
 'Median pitch',
 'Mean pitch',
 'Standard deviation',
 'Minimum pitch',
 'Maximum pitch',
 'numPulses',
 'numPeriodsPulses',
 'meanPeriodPulses',
 'stdDevPeriodPulses',
 'Fraction of locally unvoiced frames',
 'Number of voice breaks',
 'Degree of voice breaks',
 'locPctJitter',
 'locAbsJitter',
 'rapJitter',
 'ppq5Jitter',
 'ddpJitter',
 'locShimmer',
 'locDbShimmer',
 'apq3Shimmer',
 'apq5Shimmer',
 'apq11Shimmer',
 'ddaShimmer',
 'meanAutoCorrHarmonicity',
 'meanNoiseToHarmonicity',
 'meanHarmToNoiseHarmonicity']
final_df=pd.DataFrame(columns=col)
final_df.loc[len(final_df.index)] = float_list

final_df.to_csv("input.csv", index=False)