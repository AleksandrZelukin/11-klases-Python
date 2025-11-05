def bin_to_dec(binary_str):
        try:
                return int(binary_str, 2)
        except ValueError:
                raise ValueError(f"Invalid binary string: {binary_str}")

if __name__ == "__main__":
        # Example usage
        binaries = ['1011', '110', '10001']
        for b in binaries:
                try:
                        print(f"{b} -> {bin_to_dec(b)}")
                except ValueError as e:
                        print(e)