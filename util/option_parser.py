from optparse import OptionParser

  
parser = OptionParser(usage="usage:%prog [optinos] filepath")  
parser.add_option("-a", "--api",  
                action = "store",  
                type = 'str',  
                dest = "api",  
                default = None,  
                help="Specify annalysis execution time limit"  
                )  
parser.add_option("-u", "--url",  
                action = "store_true",  
                dest = "url",  
                default = False,  
                help = "Specify if the target is an URL"  
                )  
(options, args) = parser.parse_args()  
  
# if options.url:  
#     print(args[0])  
# print options.api 