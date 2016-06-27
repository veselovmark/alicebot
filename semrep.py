import os
import subprocess
import tempfile

#f_in='/home/sda/data/src/tmp/test.txt'

#sentences=['Treatment with bendamustine was associated with the development of immune hemolytc anemia in patients with chronic lymphocytic leukemia.','History of fludarabine-related hemolysis acts as risk factor in these patients']

def metamap_output(sentences):
    
    metamap_filename='/home/sda/data/src/nlm.nih.gov/public_semrep/bin/semrep.v1.7'

    #f_in='/home/sda/data/src/tmp/test.txt'

    #sentences=['Treatment with bendamustine was associated with the development of immune hemolytic anemia in patients with chronic lymphocytic leukemia.',
               #'History of fludarabine-related hemolysis acts as risk factor in these patients']

    input_file = None
    if sentences is not None:
        input_file = tempfile.NamedTemporaryFile(delete=False)
    else:
        input_file = open(filename, 'r')
    #output_file = tempfile.NamedTemporaryFile(delete=False)
    error = None
    try:
        if sentences is not None:
            for sentence in sentences:
                input_file.write('%r\n' % sentence)
            #input_file.write(sentences)
            input_file.flush()


        #f_out='/home/sda/data/src/tmp/test_out_1.txt'
        output_file = tempfile.NamedTemporaryFile(delete=False)

        command=[metamap_filename, '-F',input_file.name,output_file.name]
        #for com in command:
            #print command
        print 'hi'

        metamap_process = subprocess.Popen(command, stdout=subprocess.PIPE)
        while metamap_process.poll() is None:
            stdout = metamap_process.stdout.readline()
            if 'ERROR' in stdout:
                metamap_process.terminate()
                error = stdout.rstrip()               
        output = output_file.read()
        #return output

    finally:       
        if sentences is not None:
            os.remove(input_file.name)
        else:
            input_file.close()
        os.remove(output_file.name)

    concepts = output.splitlines()
    return (concepts, error)