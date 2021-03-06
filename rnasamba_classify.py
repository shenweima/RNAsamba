#!/usr/bin/env python

import argparse
import sys

from rnasamba import RNAsambaClassificationModel


def main(output_file, fasta_file, weights, protein_fasta, verbose):
    """Classify sequences from a input FASTA file."""
    classification = RNAsambaClassificationModel(fasta_file, weights, verbose=verbose)
    classification.write_classification_output(output_file)
    if protein_fasta:
        classification.output_protein_fasta(protein_fasta)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classify sequences from a input FASTA file.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('output_file',
                        help='output TSV file containing the results of the classification.')
    parser.add_argument('fasta_file',
                        help='input FASTA file containing transcript sequences.')
    parser.add_argument('weights',
                        nargs='+', help='input HDF5 file(s) containing weights of a trained RNAsamba network (if more than a file is provided, an ensembling of the models will be performed).')
    parser.add_argument('-p', '--protein_fasta',
                        help='output FASTA file containing translated sequences for the predicted coding ORFs.')
    parser.add_argument('-v', '--verbose',
                        default=0, type=int, choices=[0, 1],
                        help='print the progress of the classification. 0 = silent, 1 = current step.')
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    main(**vars(args))
