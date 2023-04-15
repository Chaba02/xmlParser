#functions

def convertToSeconds(s,m, h):
    m = m*60
    h = h*3600

    #returns the duration in seconds
    return s+m+h

def parse(xml):

    print("Analyzing the file...")

    #scan the file
    s_sec = ""
    s_min = ""
    s_hour = ""

    s_buffer = ""

    sec = 0
    min = 0
    hours = 0

    #check the format
    if xml[0] == "-":
        print("Error")
    else:
        print("Correct Format")

    i = 2
    while i < len(xml):
        if xml[i] == "-":
            print("Error")
            break
        if xml[i] != "S" and xml[i] != "M" and xml[i] != "H":
            s_buffer += xml[i]
        else:
            if xml[i] == "S":
                s_sec = s_buffer
            if xml[i] == "M":
                s_min = s_buffer
            if xml[i] == "H":
                s_hour = s_buffer


            s_buffer = ""

        i=i+1

    if s_sec != "":
        sec = float(s_sec)
    if s_min != "":
        min = float(s_min)
    if s_hour != "":
        hours = float(s_hour)

    duration = convertToSeconds(sec,min, hours)
    print(duration, "seconds")


xmlf = "PT1M1.2S"

parse(xmlf)
