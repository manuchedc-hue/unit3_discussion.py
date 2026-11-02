"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    """
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Performance & Memory Explanation:
    # Python lists are implemented as dynamic arrays backed by contiguous blocks of memory.
    # When an element is inserted at a specific index, all subsequent elements from that
    # index onward must be shifted one position to the right in memory to make room.
    #
    # Performance variation:
    # - Inserting at the END (e.g., using append or insert at len(lst)): Runs in O(1) amortized time
    #   because no elements need to be shifted (unless a memory reallocation is triggered).
    # - Inserting at the BEGINNING or MIDDLE: Runs in O(n) time because every element
    #   following the insertion point must be physically shifted in memory, scaling with the number
    #   of elements (n) shifted.

    # Ensure index is within valid bounds to prevent IndexError or unintended out-of-bounds appends
    if index < 0:
        index = 0
    elif index > len(lst):
        index = len(lst)

    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Why index validation and safe deletion are important:
    # In dynamic arrays, attempting to access or delete an index outside the current bounds
    # (0 to len(lst) - 1) raises an IndexError, which can crash the application.
    # Validating the index ensures robust program behavior, prevents unhandled exceptions,
    # and allows graceful error handling by returning None when an invalid operation is attempted.

    # Validate that the index exists within the current list boundaries
    if not lst or index < 0 or index >= len(lst):
        return None

    # Remove and return the value at the specified index
    # Note: Deleting from the beginning or middle also triggers an O(n) memory shift
    # as subsequent elements are moved left to fill the gap.
    removed_value = lst.pop(index)
    return removed_value


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Explanation of Linear Search and Sequential Scanning:
    # Because a standard Python list is unsorted in this context, there is no structural
    # shortcut (like binary search) to locate the element instantly. Therefore, the algorithm
    # must perform a linear search, scanning through elements one by one sequentially from index 0
    # to the end of the list.
    # Time Complexity: O(n) in the worst case (if the item is at the end or missing),
    # and O(1) in the best case (if the item is found at the very beginning).

    for i in range(len(lst)):
        if lst[i] == value:
            return i  # Return the index immediately upon finding the match

    return -1  # Return -1 if the value is not present in the list


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Step 1: Create an initial list of inventory item codes
    my_inventory = [102, 104, 105]
    print(f"Original list: {my_inventory}")

    # Step 2: Test insertion at the beginning (index 0)
    # This requires shifting all existing elements 1 position to the right -> O(n) operation
    insert_at(my_inventory, 0, 101)
    print(f"After inserting 101 at the beginning (index 0): {my_inventory}")

    # Step 3: Test insertion in the middle (index 2)
    # This requires shifting elements from index 2 onward to the right -> O(n) operation
    insert_at(my_inventory, 2, 103)
    print(f"After inserting 103 in the middle (index 2): {my_inventory}")

    # Step 4: Test insertion at the end (using len() as index)
    # Appending at the end requires no shifting of existing elements -> O(1) amortized operation
    insert_at(my_inventory, len(my_inventory), 106)
    print(f"After inserting 106 at the end: {my_inventory}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Step 1: Delete from the beginning (index 0)
    # Elements are shifted left to fill the vacated space -> O(n)
    removed_item = delete_at(my_inventory, 0)
    print(f"Removed item from beginning: {removed_item}")
    print(f"Updated list after deleting from beginning: {my_inventory}")

    # Step 2: Delete from the middle (index 2)
    middle_index = len(my_inventory) // 2
    removed_item = delete_at(my_inventory, middle_index)
    print(f"Removed item from middle (index {middle_index}): {removed_item}")
    print(f"Updated list after deleting from middle: {my_inventory}")

    # Step 3: Delete from the end (last index)
    # Removing from the end requires no shifting -> O(1)
    removed_item = delete_at(my_inventory, len(my_inventory) - 1)
    print(f"Removed item from the end: {removed_item}")
    print(f"Updated list after deleting from the end: {my_inventory}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Step 1: Search for a value that exists in the list (e.g., 104)
    target_value = 104
    search_result = search_value(my_inventory, target_value)
    if search_result != -1:
        print(f"Search Success: Value {target_value} found at index {search_result}.")
    else:
        print(f"Value {target_value} was not found.")

    # Step 2: Search for a value that does not exist in the list (e.g., 999)
    missing_value = 999
    search_result = search_value(my_inventory, missing_value)
    if search_result != -1:
        print(f"Search Success: Value {missing_value} found at index {search_result}.")
    else:
        print(f"Search Result: Value {missing_value} is missing from the list (returned {search_result}).")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Edge Case 1: Deleting from an empty list / using an out-of-bounds index
    empty_list = []
    invalid_delete = delete_at(empty_list, 5)
    print(f"Edge Case 1 - Deleting from empty/invalid index: returned {invalid_delete} (Safe handling prevents IndexError)")

    # Edge Case 2: Inserting into an empty list
    print(f"Empty list before insertion: {empty_list}")
    insert_at(empty_list, 0, 500)
    print(f"Edge Case 2 - Inserted into empty list at index 0: {empty_list}")



if __name__ == "__main__":
    main()


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    pass


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    pass


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")



if __name__ == "__main__":
    main()