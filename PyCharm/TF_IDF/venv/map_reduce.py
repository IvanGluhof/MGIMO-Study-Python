# my libs
from data import *;

# imports
import sys;
import os;

from math import log10,\
                 sqrt;

from operator import itemgetter;

# TYPE: Class
# NAME: MapReduce
# DESC: Main MapReduce class
class MapReduce:
  # Class  data

  # MR data holder
  data = DataMR();
  # stopwords
  stopwords = data.get_stop_words();

  # input file
  input_file = "";
  input_file_name = "";

  # MR output result
  result_output = [];

  # __init__ function
  def __init__(self, file):
    print("MapReduce initiated");
    f = open(file, 'r')
    # Get file name only and read it's content
    self.input_file_name = os.path.basename(f.name);
    self.input_file = f.readlines();
    f.close();
  #end def __init__(self)

  def m_stage_1(self, file, if_print):
    # variables
    result = "";

    if( file != None ):
      f = open(file, 'r')
      # Get file name only and read it's content
      self.input_file_name = os.path.basename(f.name);
      self.input_file = f.readlines();
      f.close();

    # input file is a txt search source
    for ln in self.input_file:
      ln = ln.strip()    # remove leading and trailing whitespace
      words = ln.split() # split the line into words
      # write the results to variable
      # result will be the input for the next reduce stage
      # tab-delimited; the trivial word count is 1
      for word in words:
        word = word.lower(); # convert to lower case (good for analysis)
        word = word.strip('.,()\'\"..'); # remove special charaters
        if word not in self.stopwords:
          z = word + ' ' + self.input_file_name;
          result += '%s\t%s\n' % (z, 1);

    # Save result for output with optional printing
    self.save_result(result, if_print);

    # Return result as list to pass to the next stage
    return result.split('\n');
  #end def m_stage_1(self, file, if_print):

  def m_stage_2(self, input, if_print):
    # variables
    result = "";

    # input is a previous stage result
    for ln in input:
      if ln == "": continue; # Do not process empty lines
      ln = ln.strip()        # remove leading and trailing whitespace
      # split the line into words
      wordfilename, count = ln.split('\t', 1)
      word, filename = wordfilename.split(' ', 1)
      z = word + ' ' + count;
      result += ('%s\t%s\n' % (filename, z))
      # write the results to variable
      # result will be the input for the next reduce stage
      # tab-delimited; the trivial word count is 1

    # Save result for output with optional printing
    self.save_result(result, if_print);

    # Return result as list to pass to the next stage
    return result.split('\n');
  #end def m_stage_2(self, input, if_print):

  def m_stage_3(self, input, if_print):
    # variables
    result = "";

    # input is a previous stage result
    for ln in input:
      if ln == "": continue;  # Do not process empty lines
      ln = ln.strip()         # remove leading and trailing whitespace
      # split the line into words
      wf, nN = ln.split('\t', 1)
      w, f = wf.split(' ', 1)
      z = f + ' ' + nN + ' ' + str(1)
      result += ( '%s\t%s\n' % (w, z) )
      # write the results to variable
      # result will be the input for the next reduce stage
      # tab-delimited; the trivial word count is 1

    # Save result for output with optional printing
    self.save_result(result, if_print);

    # Return result as list to pass to the next stage
    return result.split('\n');
  #end def m_stage_3(self, input, if_print):

  def m_stage_4(self, input, if_print):
    # variables
    result = ""
    D = 10.0

    # input is a previous stage result
    for ln in input:
      if ln == "": continue;  # Do not process empty lines
      ln = ln.strip()         # remove leading and trailing whitespace
      # split the line into words
      wf, nNm = ln.split('\t', 1)
      n, N, m = nNm.split(' ', 2)
      n = float(n)
      N = float(N)
      m = float(m)
      tfidf = (n / N) * log10(D / m)
      result += ( '%s\t%s\n' % (wf, tfidf) )
      # write the results to variable
      # map reduce is the final stage

    # Save result for output with optional printing
    self.save_result(result, if_print);

    # Return result as list to pass to the next stage
    return result.split('\n');
  #end def m_stage_4(self, input, prinif_print:

  def r_stage_1(self, input, if_print):
    # variables
    curr_word  = None
    curr_count = 0
    word       = None
    result     = ""

    # sorting is required for correct work by key (here: word) before it is passed to the reducer
    input.sort();

    # input is the result of mapper result
    for ln in input:
      if ln == "": continue;          # Do not process empty lines
      ln = ln.strip()                 # remove leading and trailing whitespace
      word, count = ln.split('\t', 1) # parse the input
      # convert count to int
      try:
        count = int(count)
      except ValueError:
        # ignore exception (quite obsolete)
        continue

      if curr_word == word: curr_count += count
      else:
        if curr_word: result += ( '%s\t%s\n' % (curr_word, curr_count) ) # write result to STDOUT
        curr_count = count
        curr_word = word

    if curr_word in word: result += ( '%s\t%s\n' % (curr_word, curr_count) )

    # Save result for output with optional printing
    self.save_result(result, if_print);

    # Return result as list to pass to the next stage
    return result.split('\n');
  #end def r_stage_1(self, input, if_print):

  def r_stage_2(self, input, if_print):
    # variables
    result = ""
    current_word = None
    prev_filename = None
    current_count = 0
    word = None
    N = 0
    df = {}
    l1 = []

    # input is the result of mapper result
    for ln in input:
      if ln == "": continue;  # Do not process empty lines
      ln = ln.strip()
      l1.append(ln)
      filename, wordcount = ln.split('\t', 1)
      word, count = wordcount.split(' ', 1)
      count = int(count)
      if prev_filename == filename:
        N = N + count
      else:
        if prev_filename != None:
          df[prev_filename] = N
        N = 0
        prev_filename = filename
    df[prev_filename] = N

    for h in l1:
      filename, wordcount = h.split('\t', 1)
      word, count = wordcount.split(' ', 1)
      for k in df:
        if filename == k:
          wf = word + ' ' + filename
          nN = count + ' ' + str(df[k])
          result += ( '%s\t%s\n' % (wf, nN) )

    # Save result for output with optional printing
    self.save_result(result, if_print);

    # Return result as list to pass to the next stage
    return result.split('\n');
  #end def r_stage_2(self, input, if_print):

  def r_stage_3(self, input, if_print):
    # variables
    result = ""
    prev_word = None
    count = 1
    word = None
    df = {}
    l1 = []

    # input is the result of mapper result
    for ln in input:
      if ln == "": continue;  # Do not process empty lines
      ln = ln.strip()
      w, z = ln.split('\t', 1)
      f, nNc = z.split(' ', 1)
      n, Nc = nNc.split(' ', 1)
      N, c = Nc.split(' ', 1)
      if prev_word == w:
        count = count + int(c)
      else:
        if prev_word != None:
          q = n + ' ' + N + ' ' + str(count)
          df[prev_word] = q
          j = prev_word + ' ' + f
          l1.append(j)
        count = 1
        prev_word = w

    q = n + ' ' + N + ' ' + str(count)
    df[prev_word] = q
    j = prev_word + ' ' + f
    l1.append(j)

    for h in l1:
      w, f = h.split(' ', 1)
      for d in df:
        if w == d:
          result += ( '%s\t%s\n' % (h, df[d]) )

    # Save result for output with optional printing
    self.save_result(result, if_print);

    # Return result as list to pass to the next stage
    return result.split('\n');
  #end def r_stage_3(self, input, if_print):

  def output_result(self):
    for ln in self.result_output:
      print(ln);
  #end def output_result(self)

  def save_result(self, result, print):
    self.result_output = result.split('\n');
    if( print == True ): self.output_result();
  #end def save_result(self, result, print):
#end class MapReduce