# test_case_runner.py
import inspect
import ast
import re
import time
import tracemalloc

# ANSI Color Codes for beautiful terminal styling
CLR_RESET = "\033[0m"
CLR_PASS  = "\033[32m"   # Green
CLR_FAIL  = "\033[31m"   # Red
CLR_WARN  = "\033[33m"   # Yellow
CLR_BOLD  = "\033[1m"
CLR_DIM   = "\033[2m"


def _parse_value(val_str):
    """Safely normalizes and converts a LeetCode value string into a Python literal."""
    val_str = (val_str.strip()
               .replace("true", "True")
               .replace("false", "False")
               .replace("null", "None"))
    try:
        return ast.literal_eval(val_str)
    except (ValueError, SyntaxError):
        return val_str


def _parse_test_cases(raw_text):
    """Split raw test case text into (inputs_list, expected) pairs."""
    blocks = re.split(r'Test Case \d+:', raw_text, flags=re.IGNORECASE)
    test_cases = []
    for block in blocks:
        if not block.strip():
            continue
        input_match = re.search(r'(?i)input:\s*(.*?)(?=\n\s*-{3,}|expected output:|$)', block, re.DOTALL)
        output_match = re.search(r'(?i)expected output:\s*(.*?)(?=\s*$)', block, re.DOTALL)
        if input_match:
            raw_inputs = input_match.group(1).strip().splitlines()
            inputs = [_parse_value(v) for v in raw_inputs if v.strip().strip('-').strip()]
            expected = _parse_value(output_match.group(1)) if output_match else None
            test_cases.append((inputs, expected))
    return test_cases


def run_tests(solution_instance, raw_test_cases_text: str):
    klass = solution_instance.__class__
    methods = [f for f in dir(klass) if callable(getattr(klass, f)) and not f.startswith("__")]
    if not methods:
        print(f"{CLR_FAIL}No valid solution method found.{CLR_RESET}")
        return

    target_method = getattr(solution_instance, methods[0])
    num_args = len(inspect.signature(target_method).parameters)
    test_cases = _parse_test_cases(raw_test_cases_text)

    print(f"\n{CLR_BOLD}{methods[0]}{CLR_RESET}  {CLR_DIM}({len(test_cases)} test cases){CLR_RESET}\n")

    pass_count = 0
    fail_count = 0

    for idx, (args, expected) in enumerate(test_cases):
        args = args[:num_args]
        input_display = args[0] if len(args) == 1 else args

        try:
            tracemalloc.start()
            t_start = time.perf_counter()
            result = target_method(*args)
            t_end = time.perf_counter()
            _, mem_peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            elapsed_ms = (t_end - t_start) * 1000
            mem_kb = mem_peak / 1024

            passed = (result == expected)

            if passed:
                clr = CLR_PASS
                icon = "✓"
                pass_count += 1
            else:
                clr = CLR_FAIL
                icon = "✗"
                fail_count += 1

            result_clr = CLR_PASS if passed else CLR_FAIL

            print(f"  {clr}{CLR_BOLD}{icon} Test {idx + 1}{CLR_RESET}  {CLR_DIM}{elapsed_ms:.3f} ms  {mem_kb:.1f} KB{CLR_RESET}")
            print(f"  {CLR_DIM}in {CLR_RESET} {input_display}")
            if expected is not None:
                print(f"  {CLR_DIM}exp{CLR_RESET} {result_clr}{expected}{CLR_RESET}")
            print(f"  {CLR_DIM}got{CLR_RESET} {result_clr}{result}{CLR_RESET}\n")

        except Exception as e:
            tracemalloc.stop()
            fail_count += 1
            print(f"  {CLR_WARN}{CLR_BOLD}⚠ Test {idx + 1}{CLR_RESET}")
            print(f"  {CLR_DIM}{e}{CLR_RESET}\n")

    total = pass_count + fail_count
    if fail_count == 0:
        print(f"  {CLR_PASS}{CLR_BOLD}{pass_count}/{total} passed{CLR_RESET}\n")
    else:
        print(f"  {CLR_FAIL}{CLR_BOLD}{fail_count}/{total} failed{CLR_RESET}  {CLR_DIM}({pass_count} passed){CLR_RESET}\n")
