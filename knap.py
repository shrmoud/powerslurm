#!/usr/bin/env python

from __future__ import print_function

import pyslurm
import sys

from time import gmtime, strftime, sleep

def display(job_dict):

    if job_dict:

        for key, value in sorted(job_dict.iteritems()):

            print("JobID {0} :".format(key))
            for part_key in sorted(value.iterkeys()):

                if part_key in time_fields:
                    print("\t{0:<20} : Infinite".format(part_key))
                    continue

                if part_key in date_fields:

                    if value[part_key] == 0:
                        print("\t{0:<20} : N/A".format(part_key))
                    else:
                        ddate = pyslurm.epoch2date(value[part_key])
                        print("\t{0:<20} : {1}".format(part_key, ddate))
                else:
                    print("\t{0:<20} : {1}".format(part_key, value[part_key]))

            print("-" * 80)




if __name__ == "__main__":

    try:
        a = pyslurm.job()
        jobs = a.get()

        if len(jobs) > 0:

            display(jobs)
			njobs = len(jobs)

            pending = a.find('job_state', 'PENDING')
            #print("Number of pending jobs - {0}".format(len(pending)))
            #print("JobIDs in Pending state - {0}".format(pending))
            #print()
        else:
            print("No jobs found !")
    except ValueError as e:
print("Job query failed - {0}".format(e.args[0]))
