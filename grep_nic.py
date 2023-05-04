start_str0 = "Design"
start_str1 = "nic400"
end_str = "references"
#input_file = "/Users/ellawang/work/chip/hier_area/s5_syn_hierarchy.rpt"
#output_file = "./nic_out.rpt"
line_str = ""

def grep_nic(input_file, output_file):
    with open(input_file, "r") as f_input, open(output_file, "w") as f_output:
        write = False
        for line in f_input:
            if start_str0 in line and start_str1 in line:
                write = True
                line_str = line
                #f_output.write(line)
            if end_str in line and write is True:
                sub_char = line.split()
                last_num = sub_char[-1]
                last_str = last_num.split(".")
                if int(last_str[0]) > 10000:
                    f_output.write(line_str)
                    f_output.write(line)
                write = False
