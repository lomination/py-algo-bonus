from time import time
from math import floor, ceil


class Test:

    def __init__(self, *, print_to_console: bool = True, raise_on_failure: bool = False):
        """Creates a test instance."""
        self._count: int = 0
        self._successes: int = 0
        self._failures: int = 0
        self._func = None
        self._print_to_console = print_to_console
        self._raise_on_failure = raise_on_failure
        current_time = Test._get_time()
        self._total_chrono = current_time
        self._chrono = current_time
        if self._print_to_console:
            print()

    def _get_time() -> int:
        """Returns the current time in miliseconds."""
        return round(time() * 1000)

    def _reset_chrono(self) -> None:
        """Stores the current time in miliseconds."""
        self._chrono = Test._get_time()

    def _test(self, actual, expected, value, source: str = "unknown") -> None:
        """Compares the expected value with the actual value."""
        value = str(value)
        value = (value if len(value) < 10 else value[0:9]+"...)")
        self._count += 1
        if (actual == expected):
            self._successes += 1
            if self._print_to_console:
                print(f"\033[92mSuccess\033[2m [{Test._get_time() - self._chrono}ms] {value}\033[0m \033[2m{{{source}}}\033[0m")
        else:
            self._failures += 1
            if self._print_to_console:
                print(f"\033[91mFailure\033[2m [{Test._get_time() - self._chrono}ms] {value} => {actual} instead of {expected}\033[0m \033[2m{{{source}}}\033[0m")
            if self._raise_on_failure:
                raise Exception(f"\033[91mFailure\033[2m [{Test._get_time() - self._chrono}ms] {value} => {actual} instead of {expected}\033[0m \033[2m{{{source}}}\033[0m")

    def set_func(self, func) -> None:
        """Sets the function to test to the given function."""
        self._func = func
        if self._print_to_console:
            print(f"\033[1m--==[{func.__name__}]==--\033[0m")

    def unit(self, expected, value: tuple) -> None:
        """Runs an unit test. It takes as parameters the expected value and the parameters to give to the function."""
        if self._func is None:
            raise Exception("Function func has not been initialized before.")
        else:
            self._reset_chrono()
            self._test(self._func(*value), expected, value, "unit")

    def multi(self, ref_func, values: list[tuple]) -> None:
        """Runs a multi test. It takes as parameters the reference function and a set of tuple representing the arguments to give to the function."""
        if self._func is None:
            raise Exception("Function func has not been initialized before.")
        else:
            for value in values:
                self._reset_chrono()
                self._test(self._func(*value), ref_func(*value), value, "multi")

    def end(self) -> tuple[int, int, int, int]:
        """Ends the test suite. Returns a tuple containings the number of tests, successes, failures and the amount of time spent since the start of the tests."""
        total_time = Test._get_time() - self._total_chrono
        if self._print_to_console:
            tests_msg = f"{self._count} tests"
            successes_msg = f"{self._successes} successes"
            failures_msg = f"{self._failures} failures"
            total_time_msg = f"{total_time}ms (total)"
            l = max(len(tests_msg), len(successes_msg), len(failures_msg), len(total_time_msg))
            print()
            print(f"+-----{"-" * l}-----+")
            print(f"|     \033[1m{" "*ceil((l-len(tests_msg))/2)}{tests_msg}{" "*floor((l-len(tests_msg))/2)}\033[0m     |")
            print(f"|     \033[92m{" "*ceil((l-len(successes_msg))/2)}{successes_msg}{" "*floor((l-len(successes_msg))/2)}\033[0m     |")
            print(f"|     \033[91m{" "*ceil((l-len(failures_msg))/2)}{failures_msg}{" "*floor((l-len(failures_msg))/2)}\033[0m     |")
            print(f"|     \033[2m{" "*ceil((l-len(total_time_msg))/2)}{total_time_msg}{" "*floor((l-len(total_time_msg))/2)}\033[0m     |")
            print(f"+-----{"-" * l}-----+")
        return (self._count, self._successes, self._failures, total_time)

    def speed_test(funcs: list, suite: list[tuple], times: int = 1) -> dict[str, int]:
        """Runs a speed test between various functions. It takes as parameters, the list of functions to test, the set of tests and the number of iterations."""
        d = dict()
        for f in funcs:
            TEST = Test(print_to_console=False, raise_on_failure=True)
            TEST.set_func(f)
            for _ in range(times):
                for test in suite:
                    TEST.unit(*test)
            d[f.__name__] = TEST.end()[3]
        l = list(d.items())
        l.sort(key=lambda kv: kv[1])
        for kv in l:
            print(kv[0], "->", kv[1])
        return d
