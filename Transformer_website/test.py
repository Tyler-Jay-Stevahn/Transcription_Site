import os
import re
import time
import subprocess


def transcriber(file_path):
    # This folder should only have the mp4 files you wish to transcribe. NO OTHER FILES
    directory = os.path.dirname(file_path)
    minutes = 60
    input_dir = '/tmp/'

    # iterate over files in that directory
    count = 0
    for filename in os.listdir(directory):
        name_before = filename
        # print(filename)
        name_before = re.sub(" ", "_", name_before)
        # print(filename, "renamed to", name_before)
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f) and filename.endswith(".mp3") or filename.endswith(".MP3"):
            count += 1
            file_path = os.path.join(directory, filename)
            #print(file_path)
            #print('started ', filename, 'finished ', (count - 1))
            filepath_name = "whisper "
            filepath_name = str(filepath_name)
            filepath_name = filepath_name + f
            ###########################################################################################################
            options = "--language en --model large --device cuda --task transcribe --output_dir "
            options = str(options + directory)
            ###########################################################################################################
            options = str(options)
            command = str(filepath_name + ' ' +  options)

            # Add the exit command at the end of the command
            # command += " & exit"

            # print(command)

            # Run the command and store the exit code
            # print(command)
            start = time.time()
            exit_code = subprocess.run(command, shell=True)
            print("----------------------------------------------------------")
            print("----------------------------------------------------------")
            end = time.time()
            total_time = end-start

            # Print a message to indicate that the command was successful
            if total_time < 60:
                print("Transcription took", str(total_time)[:5], "Seconds")

            else:
                print("Transcription took", str(total_time/60)[:5], "Minutes")
            location = os.getcwd()
            # Set the input and output directories
            '''
            classname = input("What is the subject? (Biology)")
            classname = channelname.replace(" ", "_")
            classnumber = input("What is the number for the class? (MATH 1593, BIO 1224 Lecture/Lab, HUM 2113)")
            classnumber = foldername.replace(" ", "_")
            '''
            input_dir = '/tmp/'
            output_dir = file_path

            # Create the output directories if they don't already exist
            # os.makedirs(output_dir, exist_ok=True)
            # Iterate through the input directory
            break
        for file_name in os.listdir(input_dir):
            #print(file_name)
            # Check if the file is a text file
            if file_name.endswith(".txt"):
            # Open the file and read its contents
                with open(os.path.join(input_dir, file_name), "r") as input_file:
                    text = input_file.read()
                #print(file_name, "is finished")
                command2 = 'rm -rf ' + directory
                exit_code = subprocess.run(command2, shell=True)
                return text
            

file_path = '/tmp/230120_001_testing.mp3'
transcriber(file_path)