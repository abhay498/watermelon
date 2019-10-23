import textfsm
import tempfile

output = '''RP/0/RP0/CPU0:Router1#show event manager environment 
Wed Jun 26 12:10:21.773 UTC
No. Name                          Value                                             
1   _period                       60                                                
2   show_command                  show event manager policy available               
3   _cron_entry                   0-59/2 0-23/1 * * 0-7                             
4   _email_to                     xyz@cisco.com                                     
5   _process                      ltrace_server                                     
RP/0/RP0/CPU0:Router1#
'''

parser = r"""Value variable_name (\S+)
Value variable_value (([$&+,:;=?@#|'<>.^*()%!-|\w+|\d+](\s??))+)

Start
  ^\d+\s+${variable_name}\s+${variable_value}\s\s -> Record

EOF
"""


def parse_textfsm(template, output):
# Define the text processing template for output.

    # Create temp file to hold template.
    tmp = tempfile.NamedTemporaryFile(delete=False)

    # Write template to file for textfsm.
    with open(tmp.name, 'w') as f:
        f.write(template)

    # Get read handle for textfsm.
    with open(tmp.name, 'r') as f:
        # Instantiate a new TextFSM wrapper.
        fsm = textfsm.TextFSM(f)
        # Parse the output text according to template rules.
        fsm_results = fsm.ParseText(output)
        # Convert to list of dictionaries since TextFSM may return multiple
        # 'row' results.
        parsed = [dict(zip(fsm.header, row)) for row in fsm_results]

    # Return the parsed data.
    return parsed

# Parse the output.
parsed = parse_textfsm(template=parser, output=output)

# Print
print ("command output\n", output)
print ("textfsm\n", parser)
print ("parsed output")
for i in parsed:
    print(i)
