from DataLayer.DatabaseOperations import get_all, delete_entry


def validate():
    entries = get_all()
    for entry in entries:
        delete_current_Entry = False
        if entry[1] < 0 \
                or (entry[2] != 0 and entry[2] != 1) \
                or entry[3] < 0 \
                or entry[4] < 0 or entry[5] < 0 \
                or entry[6] < 0 \
                or (entry[7] < 0 or entry[7] > 1) \
                or (entry[8] < 0 or entry[8] > 100) \
                or entry[9] < 0 \
                or entry[9] > 100:
            delete_current_Entry = True
        if delete_current_Entry:
            delete_entry(entry[0])
