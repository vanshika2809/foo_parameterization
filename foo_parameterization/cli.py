
import argparse
from .core import calculate_volume

def main():
    parser = argparse.ArgumentParser(description="Calculate the volume of a sphere using Foo et al. parameterization.")
    parser.add_argument('radius', type=float, help='The radius of the sphere')
    args = parser.parse_args()
    
    try:
        volume = calculate_volume(args.radius)
        print(f"The volume of the sphere with radius {args.radius} is {volume}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
