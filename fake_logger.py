import sys
import time
from datetime import datetime
import random

def random_ipv4():
    return f"{str(random.randint(0, 255)).lstrip('0')}.{str(random.randint(0, 255)).lstrip('0')}.{str(random.randint(0, 255)).lstrip('0')}.{str(random.randint(0, 255)).lstrip('0')}"

generator_name = sys.argv[1]
generator_lines_file = sys.argv[2]
generator_output = sys.argv[3]
generator_eps = sys.argv[4]

log_lines = list()

with open(generator_lines_file, "r") as file:
    log_lines = file.readlines()


while True:

    if int(generator_eps) != 0:

        random_line = random.choice(log_lines)

        with open(generator_output, "a") as output_file:
            output_file.write(
                str(random_line) \
                    .replace("T_MONTH_WORD", str(datetime.now().strftime('%h'))) \
                    .replace("T_YEAR", str(datetime.now().strftime('%Y'))) \
                    .replace("T_DAY", str(datetime.now().strftime('%a'))) \
                    .replace("T_HOUR", str(datetime.now().strftime('%H'))) \
                    .replace("T_MIN", str(datetime.now().strftime('%M'))) \
                    .replace("T_SEC", str(datetime.now().strftime('%S'))) \
                    .replace("R_IPV4", random_ipv4()) \

            )
        
        time.sleep(1/float(generator_eps))
