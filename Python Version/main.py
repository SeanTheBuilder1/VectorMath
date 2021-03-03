import vectorOp

def main():
    while True:
        try:
            mode = int(input("Press 1 to use distance formula\nPress 2 to use midpoint formmula\n"))
            if mode == 1:
                vectorOp.calcDistance()
            elif mode == 2:
                vectorOp.calcMidpoint()
            else:
                raise(ValueError)
        except:
            print("Invalid Character")


if __name__ == "__main__":
	main()