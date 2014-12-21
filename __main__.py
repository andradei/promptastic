from promptastic import Prompt

prompt = Prompt()

# First line left (order: left to right).
prompt.first_line_left.append(sysinfo.UserAtHost())
prompt.first_line_left.append(basics.Divider())
prompt.first_line_left.append(network.Ssh())
prompt.first_line_left.append(basics.Divider())
prompt.first_line_left.append(filesystem.CurrentDir(prompt.cwd))
prompt.first_line_left.append(basics.Divider())
prompt.first_line_left.append(filesystem.ReadOnly(prompt.cwd))
prompt.first_line_left.append(basics.Divider())
prompt.first_line_left.append(basics.ExitCode())
prompt.first_line_left.append(basics.Divider())

# First line right (order: left to right).
prompt.first_line_right.append(basics.Divider())
prompt.first_line_right.append(git.Git())
prompt.first_line_right.append(basics.Divider())
prompt.first_line_right.append(filesystem.Venv())
prompt.first_line_right.append(basics.Divider())
prompt.first_line_right.append(sysinfo.Jobs())
prompt.first_line_right.append(basics.Divider())
prompt.first_line_right.append(sysinfo.Time())

# Last line.
prompt.last_line.append(basics.Root())

if hasattr(sys.stdout, 'buffer'):
    sys.stdout.buffer.write(prompt.render().encode('utf-8'))
else:
    sys.stdout.write(prompt.render())