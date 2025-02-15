import sys, getopt
from LZ77 import LZ77Compressor

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('compress.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('compress.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile, '"')
   print ('Output file is "', outputfile, '"')
   
   compressor = 0
   compressor = LZ77Compressor(compressor)

   compressor.compress(compressor, input_file_path=inputfile, output_file_path=outputfile, verbose=True)

   raw_input("\n\nPress the enter key to exit.")


if __name__ == "__main__":
   main(sys.argv[1:])




