#!/usr/bin/env python3

import vcf

__author__ = 'Dominic Viehböck'


class Assignment2:
    
    def __init__(self, file_name="chr22_new.vcf"):
        self.filename = file_name
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        # Create reader object
        self.reader = self.get_reader()#vcf.Reader(open(self.filename), 'r')
        self.reads = self.get_reads(self.reader)

    def get_reads(self, reader):
        reads = []
        for record in reader:
            reads.append(record)
        return reads

    def get_reader(self):
        reader = vcf.Reader(open(self.filename), 'r')
        return reader

    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''    
        i = 0
        averageQ = 0

        for record in self.reads:
            i += 1
            averageQ += record.QUAL
        phred = averageQ / i

        print('The average PHRED quality of all variants is: ', str(phred))
        
        
    def get_total_number_of_variants_of_file(self, file_name="chr22_new.vcf"):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        reader = vcf.Reader(open(file_name),'r')
        i = 0
        for record in reader:
            i += 1
        print("Total number of variants ({}): ".format(file_name), i)
    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        vcaller = []
        for record in self.reads:
            vcaller = record.INFO['callsetnames']
        print("Variant caller name: ", vcaller[1])


    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        print("Genome reference version: hg38")

    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        i = 0
        for record in self.reads:
            if record.is_indel:
                i += 1
        print('Number of identified INDELs: ', i)
        

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        i = 0
        for record in self.reads:
            if record.is_snp:
                i += 1
        print('Number of SNVs: ', i)
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        i = 0
        for record in self.reads:
            if record.num_het:
                i += 1
        print('Number of heterozygous variants: ', i)
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        try:
            vcf_chr21 = vcf.Reader(open("chr21_new.vcf"), "r")
            vcf_chr22 = vcf.Reader(open("chr22_new.vcf"), "r")
            vcf_Writer = vcf.Writer(open("combined2.vcf", "w"), vcf_chr21)
            for record in vcf_chr21:
                vcf_Writer.write_record(record)
            for record in vcf_chr22:
                vcf_Writer.write_record(record)

            self.get_total_number_of_variants_of_file(file_name="combined2.vcf")
        except:
            filenames = ['chr22.vcf', 'chr21.vcf']
            with open('combined.vcf', 'w') as outfile:
                for fname in filenames:
                    with open(fname) as infile:
                        for line in infile:
                            outfile.write(line)
            self.get_total_number_of_variants_of_file(file_name="combined.vcf")

    
    def print_summary(self):
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
        self.merge_chrs_into_one_vcf()
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    print(__author__,"\n")
    main()
   
    



