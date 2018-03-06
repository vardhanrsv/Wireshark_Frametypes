# Wireshark_Frametypes

# identifying different frames
  we can capture the frames by using wireshark and we can filter out the frame types using filters.
  there are 3 type of frames
  1) data frames       : wlan.fc.type eq 0
  2) control frames    : wlan.fc.typr eq 1
  3) management frames : wlan.fc.type eq 2
  
  We also found a way to live capture the data we are uploading that file too Livecapture.py
  we can change the filters according to our applications.
  
  captured data can easily be converted to a csv file using ¨sudo python file_name.py > output.csv¨
  
  we captured data at library, myroom, jumbo, citycentre
  
  all files captured are uploaded each type is saved into a seperate  csv  file.
  
  plug in the filename into the calculating_prob.py it will give you the probability of each type and subtype frames.
  
  As the capturing time at each spot is varied we thought probabilities will give a better comparision.
  we plotted the probabilities of each type and subtype for comparision.
  
# References

http://www.itcertnotes.com/2011/05/ieee-80211-frame-types.html

http://www.bitforestinfo.com/2017/07/how-to-create-ap-finder-using-python-and-pyshark-module-airodump-ng-clone-using-python.html
