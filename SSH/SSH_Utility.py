import datetime

def get_command_results(channel):
    ## http://joelinoff.com/blog/?p=905

    interval = 0.1
    maxseconds = 10
    maxcount = maxseconds / interval
    bufsize = 1024

    # Poll until completion or timeout
    # Note that we cannot directly use the stdout file descriptor
    # because it stalls at 64K bytes (65536).
    input_idx = 0
    timeout_flag = False
    start = datetime.datetime.now()
    start_secs = datetime.time.mktime(start.timetuple())
    output = ''
    channel.setblocking(0)
    while True:
        if channel.recv_ready():
            data = channel.recv(bufsize).decode('ascii')
            output += data

        if channel.exit_status_ready():
            break

        # Timeout check
        now = datetime.datetime.now()
        now_secs = datetime.time.mktime(now.timetuple())
        et_secs = now_secs - start_secs
        if et_secs > maxseconds:
            timeout_flag = True
            break

        rbuffer = output.rstrip(' ')
        if len(rbuffer) > 0 and (rbuffer[-1] == '#' or rbuffer[-1] == '>'): ## got a Cisco command prompt
            break

        time.sleep(0.200)

    if channel.recv_ready():
        data = session.recv(bufsize)
        output += data.decode('ascii')

    return output


def send_command_and_get_response(channel, cmd):
    if not cmd.endswith("\n"):
        cmd += "\n"
    channel.send(cmd)
    results = get_command_results(channel)
    return results
