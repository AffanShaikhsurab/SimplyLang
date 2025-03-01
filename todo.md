### **TODO List**

#### **Important**

1. **Binary Operations**
   - Enable binary operations to support `c[0]` or mapping values.
2. Add event handling
3. Memory Management ( ram / disk )
4. Payable ( msg.sender )
5. Require statement

---

#### **Less Important**

1. **Enhanced `show` Functionality**
   - Add the ability to directly print mappings and arrays.Here's the updated version with "Class Function Argument Passing" moved to the **Completed** section:

---

### **TODO List**

#### **Important**

1. **Binary Operations**

   - Enable binary operations to support `c[0]` or mapping values.
2. **Modifiers**

   - Add support for modifiers.

---

#### **Less Important**

1. **Enhanced `show` Functionality**
   - Add the ability to directly print mappings and arrays.

---

### **Completed**

1. **Array Enhancements**

   - Supported features:
     - Array indexing.
     - Array length.
     - Array sorting.
2. **Functionality for Functions**

   - Functions now support:
     - Parameters.
     - Returning values via `return` statements.
     - Bug fixed: Functions only return values from `return` statements.
     - Nested function calls.
3. **Mapping Feature**

   - Added support for mappings.
4. **Class Function Calls**

   - Fixed bug where functions inside classes couldn't be called without a class instance.
5. **Class Function Argument Passing**

   - Resolved the issue where arguments could not be passed to class functions (e.g., calling `class.bob(a, b)`).
6. **Improved `show` Statements**

   - Supported complex statements such as:
     `show("Inside calculateSum, sum of ", x, " and ", y, " is -> ", sum)`
