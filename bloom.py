#!/usr/bin/python
import subprocess, sys, os

'''
This script will perform a series of headless web page console inspections while capturing and examining the STDOUT of those processes.
The script will then create JIRA issues for each error or warning given by based on the outputs of each of these subprocesses each time this script is run.

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--project',   required=True, help='JIRA project name')
parser.add_argument('-i', '--issueType', required=True, help='Jira IssueType')
parser.add_argument('-w', '--website',   required=True, help='Site to scrape' )
args = parser.parse_args()
'''

def fileParse():
        if not os.path.exists('prices.txt'):
            print "shit, prices doesn't exist"
        with open('prices.txt','r') as f:
            inputS = f.read()
        print inputS
        inputStr = inputS.splitlines()
        myList = [ ]
        for line in inputStr :
            myList.append(float(line))
        return myList

def runCommand(cmd):
    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE)
    return proc.communicate()[0]

def testCommand(company):
    consoleOut = runCommand( ["sudo", "node", "bloom.js", str(company) ] )
    return fileParse()
