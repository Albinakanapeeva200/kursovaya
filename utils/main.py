import os.path
from all_funct import (get_executed_operations, sort_operations_by_date, get_last_operations, get_valid_operation_obj,
                       load_operations)

file_dict = os.path.join('operations.json')

sort_operations_state = get_executed_operations(load_operations(file_dict))
sort_operations = sort_operations_by_date(sort_operations_state)
last_operations = get_last_operations(sort_operations)
get_valid_operation_obj(last_operations)
