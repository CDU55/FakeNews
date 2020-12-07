from DataLayer.DatabaseOperations import get_all, delete_entry


def validate():
    entries = get_all()
    for entry in entries:
        delete_current_Entry = False
        if entry[1] < 0:
            delete_current_Entry = True
        if entry[2] != 0 and entry[2] != 1:
            delete_current_Entry = True
        if entry[3] < 0:
            delete_current_Entry = True
        if entry[4] < 0:
            delete_current_Entry = True
        if entry[5] < 0:
            delete_current_Entry = True
        if entry[6] < 0:
            delete_current_Entry = True
        if entry[7] < 0 or entry[7] > 1:
            delete_current_Entry = True
        if entry[8] < 0 or entry[8] > 100:
            delete_current_Entry = True
        if entry[9] < 0 or entry[9] > 100:
            delete_current_Entry = True
        if delete_entry:
            delete_entry(entry[0])
