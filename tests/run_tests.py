import argparse
import fen_tests
import solution_tests

parser = argparse.ArgumentParser(description="unit tests for chess-trainer")
parser.add_argument("--fen_to_piece_list", action="store_true", help="run fen to piece list unit tests")
parser.add_argument("--url_to_solution", action="store_true", help="run url to solution unit tests")
parser.add_argument("--all", action="store_true", help="run all unit tests")

args = parser.parse_args()

if args.all:
  fen_tests.test_all()
  solution_tests.test_all()
elif args.fen_to_piece_list:
  fen_tests.test_all()
elif args.url_to_solution:
  solution_tests.test_all()
