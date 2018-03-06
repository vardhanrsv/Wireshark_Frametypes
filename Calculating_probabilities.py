import csv
import numpy 
## read the file now identifying the things we want 3 different csv files are captured 
## 1) data 2) control 3) management

reader_1 = csv.reader(open("lib_data_ref.csv","rb"), delimiter=",")
x_1 = list(reader_1)
result_1 = numpy.array(x_1)


reader_2 = csv.reader(open("lib_control_ref.csv","rb"), delimiter=",")
x_2 = list(reader_2)
result_2 = numpy.array(x_2)


reader_3 = csv.reader(open("lib_managment_ref.csv","rb"), delimiter=",")
x_3 = list(reader_3)
result_3 = numpy.array(x_3)

num_data_packets    = float(len(result_1))
num_control_packets = float(len(result_2))
num_manag_packets   = float(len(result_3))
total_number_frames = num_data_packets + num_control_packets + num_manag_packets

probability_data =  num_data_packets / total_number_frames
probability_control =  num_control_packets / total_number_frames
probability_mana =  num_manag_packets / total_number_frames

probability_frame = [probability_data, probability_control, probability_mana]

i=0
count_Data = float(0)
count_QoS_Data = float(0)

# counting data packets and QoS Data packets
while i < num_data_packets:
	temp = result_1[i][2]
	if temp.startswith("Data"):
		count_Data = count_Data+1
	if temp.startswith("QoS"):
		count_QoS_Data = count_QoS_Data+1
	i = i+1
print count_Data
print count_QoS_Data
probability_dataP =  count_Data / num_data_packets
probability_dataQ =  count_QoS_Data / num_data_packets

toplot_1 = [probability_dataP, probability_dataQ]

print toplot_1

count_Poll=float(0)
count_Rts=float(0)
count_Cts=float(0)
count_Ack=float(0)

j=0
while j < num_control_packets:
	temp=result_2[j][2]
	if temp.startswith("Ack"):
		count_Ack = count_Ack+1
	if temp.startswith("Req"):
		count_Rts = count_Rts+1	
	if temp.startswith("Clear"):
		count_Cts = count_Cts+1	
	if temp.endswith("Poll"):
		count_Poll = count_Poll+1	

	j=j+1	

probability_Ack =  count_Ack / num_control_packets
probability_Rts =  count_Rts / num_control_packets
probability_Cts =  count_Cts / num_control_packets
probability_Poll =  count_Poll / num_control_packets

toplot_2 = [probability_Ack, probability_Rts, probability_Cts, probability_Poll]
print toplot_2

count_Beacon=float(0)
count_Diss=float(0)
count_Deact=float(0)
count_Auth=float(0)
count_Ass_request=float(0)
count_Ass_response=float(0)
count_probe_request=float(0)
count_probe_response=float(0)
count_Reass_request=float(0)
count_Reass_response=float(0)


k=0 
temp=0
while k < num_manag_packets-1:
	temp=result_3[k][2]
	if temp.startswith("Bea"):
		count_Beacon = count_Beacon + 1
	if temp.startswith("Dis"):
		count_Diss = count_Diss+1	
	if temp.startswith("Dea"):
		count_Deact = count_Deact+1
	if temp.startswith("Aut"):
		count_Auth = count_Auth+1		
	if temp == "Association Request":
		count_Ass_request = count_Ass_request+1	
	if temp == "Association Response":
		count_Ass_response = count_Ass_response+1		
	if temp == "Probe Request":
		count_probe_request = count_probe_request+1	
	if temp == "Probe Response":
		count_probe_response = count_probe_response+1
	if temp == "Reassociation Request":
		count_Reass_request = count_Reass_request+1	
	if temp == "Reassociation Response":
		count_Reass_response = count_Reass_response+1			

	k=k+1	

probability_Beacon =  count_Beacon / num_manag_packets
probability_Diss =  count_Diss / num_manag_packets
probability_Deact =  count_Deact / num_manag_packets
probability_Auth =  count_Auth / num_manag_packets
probability_Ass_request =  count_Ass_request / num_manag_packets
probability_Ass_response =  count_Ass_response / num_manag_packets
probability_probe_request =  count_probe_request / num_manag_packets
probability_probe_response =  count_probe_response / num_manag_packets
probability_Reass_request =  count_Reass_request / num_manag_packets
probability_Reass_response =  count_Reass_response / num_manag_packets

toplot_3 = [probability_Beacon,
probability_Diss,
probability_Deact,
probability_Auth,
probability_Ass_request,
probability_Ass_response,
probability_probe_request,
probability_probe_response,
probability_Reass_request,
probability_Reass_response]


print toplot_3