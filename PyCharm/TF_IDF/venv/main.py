# main map reduce module import
from map_reduce import MapReduce;

################# !_WORKFLOW ! #################
# MR is on four stages:                        #
# Map Stage 1 -> Reduce Stage 1 -> Map Stage 2 #
# Map Stage 2 -> Reduce Stage 2 -> Map Stage 3 #
# Map Stage 3 -> Reduce Stage 3 -> Map Stage 4 #
# Map Stage 4 -> Output result                 #
################################################

# Input file - source (currenty .txt only)
input = "E:\\1_DATA\\1_WORK\\AI.MGIMO\II\\01_BD\\TF_IDF\\sample_data\\input_tfidf.txt";

##############################################
# Init MR class as MR Engine                 #
MR_Engine = MapReduce(input);                #
# Init MR stage 1                            #
m1_res = MR_Engine.m_stage_1(None,   False); #
r1_res = MR_Engine.r_stage_1(m1_res, False); #
# Init MR stage 2                            #
m2_res = MR_Engine.m_stage_2(r1_res, False); #
r2_res = MR_Engine.r_stage_2(m2_res, False); #
# Init MR stage 3                            #
m3_res = MR_Engine.m_stage_3(r2_res, False)  #
r3_res = MR_Engine.r_stage_3(m3_res, False); #
# Init MR final stage as map stage 4         #
m4_res = MR_Engine.m_stage_4(r3_res, False); #
# Output final result                        #
MR_Engine.output_result();                   #
##############################################