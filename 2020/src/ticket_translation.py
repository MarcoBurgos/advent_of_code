import re
from utils import read_and_load_input

def ticket_translation_1():
    input = read_and_load_input("DAY16")
    valid_seq = set()
    rules = True
    nearby = False
    solution = 0

    for line in input:
        if rules:
            seq = re.findall('\d+', line )
            round = 0
            while round < 3 and len(seq) > 0:
                for _ in range(int(seq[round]),int(seq[round +1]) + 1):
                    valid_seq.add(_)

                round += 2
            sorted(valid_seq)
        elif nearby:
            numbers = line.split(",")
            for number in numbers:
                if int(number) not in valid_seq:
                    solution += int(number)

        if len(line) == 0:
            rules = False

        if line.startswith("nearby"):
            nearby = True
    return solution



def ticket_translation_2(data):
    rules, my_ticket, nearby_tickets = data
    possible_fields = [set() for _ in my_ticket]
    for ticket in nearby_tickets:
        for ix, num in enumerate(ticket):
            fields = set()
            for name, ranges in rules.items():
                for from_num, to_num in ranges:
                    if from_num <= num <= to_num:
                        fields.add(name)

            if fields:
                possible_fields[ix] = possible_fields[ix].intersection(fields) if possible_fields[ix] else fields

    sorted_possible_fields = [
        [len(fields), ix, fields]
        for ix, fields in enumerate(possible_fields)
    ]
    sorted_possible_fields.sort()

    visited = set()
    ans = 1
    for ix, data in enumerate(sorted_possible_fields):
        length, index, fields = data

        field_name = list(fields - visited)[0]
        if 'departure' in field_name:
            ans *= my_ticket[index]
        visited = visited.union(fields)

    return ans


def extract_data(lines):
    ix = 0
    rules = {}
    while lines[ix]:
        name, ranges = lines[ix].split(':')
        ranges = map(str.strip, ranges.split('or'))
        int_ranges = []
        for r in ranges:
            from_num, to_num = r.split('-')
            int_ranges.append((int(from_num), int(to_num)))
        rules[name] = int_ranges
        ix += 1

    ix += 2
    my_ticket = list(map(int, lines[ix].split(',')))


    ix += 2
    nearby_tickets = []
    for line in lines[ix+1:]:
        nearby_tickets.append(list(map(int, line.split(','))))

    return rules, my_ticket, nearby_tickets



if __name__ == '__main__':
    print(ticket_translation_1())
    #input = read_and_load_input("DAY16")
    #print(ticket_translation_2(extract_data(input)))
