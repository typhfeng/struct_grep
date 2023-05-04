#start_str = "nic400"
end_str = "references"
#input_file = "/Users/ellawang/work/chip/hier_area/s5_syn_hierarchy.rpt"
#output_file = "./nic_out.rpt"
line_str = ""

def grep_nic_per(input_file, output_file, start_str):
    with open(input_file, "r") as f_input, open(output_file, "w") as f_output:
        write = False
        for line in f_input:
            if "Design" in line and start_str in line:
                write = True
                line_str = line
                f_output.write(line)
            if end_str in line and write is True:
                sub_char = line.split()
                last_num = sub_char[-1]
                last_str = last_num.split(".")
                if int(last_str[0]) > 1: #10000:
                    f_output.write(line_str)
                    f_output.write(line)
                write = False
            if write is True:
                f_output.write(line)

