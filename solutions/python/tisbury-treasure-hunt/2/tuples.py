"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple[str]) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate: str) -> tuple[str]:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record: tuple[str], rui_record: tuple[str]) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    return convert_coordinate(get_coordinate(azara_record)) == rui_record[1]


def create_record(azara_record: tuple[str], rui_record: tuple[str]) -> tuple[str]|str:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return 'not a match'


def clean_up(combined_record_group: tuple[tuple[str]]) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.
    """

    result = '('
    for pos, record in enumerate(combined_record_group):
        for index, item in enumerate(record):
            if index == 1:
                continue
            if index == 3:
                result += f'{str(item)}, '
                continue
            if index == (len(record) - 1):
                result += f"'{item}')\n"
                continue
            result += f"'{item}', "
        if pos != (len(combined_record_group) - 1):
            result += '('
    return result
