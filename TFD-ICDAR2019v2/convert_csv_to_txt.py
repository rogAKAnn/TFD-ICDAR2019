
import csv
csv_file = 'Train/math_gt/BAMS_1971_1974_2.csv'
txt_file = 'Train/math_txt/'
X=3601
Y=5700

def convert_box_to_yolo(line: list()):
    line[0] = float(line[0])/  X
    line[1] = float(line[1]) / Y
    line[2] = float(line[2]) / X
    line[3] = float(line[3]) / Y
    x_center = (line[0] + line[2]) /2
    y_center = (line[1] + line[3]) /2
    width= abs(line[0] - line[2])
    height=abs(line[1] - line[3])
    return [str(round(x_center,6)),str(round(y_center,6)),str(round(width,6)),str(round(height,6))]


with open(csv_file, "r") as my_input_file:
    num_pages= 0
    for i in csv.reader(my_input_file):
        num_pages = max(int(i[0]),num_pages)
    num_pages+=1
        
    print("NNNNN: " + str(num_pages))
    my_input_file.seek(0)


    for i in range(0, num_pages):
        with open(txt_file + str(i+1) + ".txt", "w") as my_out_put_file:
            for rows in csv.reader(my_input_file,delimiter=';'):

                line = rows[0].split(",")

                if line[0] == str(i):
                    my_out_put_file.write(" ".join(["0"] + convert_box_to_yolo(line[1:])))
                    my_out_put_file.write("\n")
        my_input_file.seek(0)
        my_out_put_file.close()

my_input_file.close()