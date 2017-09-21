#!/usr/bin/bash

#Derived from :  
# http://www.techrepublic.com/article/sample-directory-structure-helps-manage-project-documentation/

#from project root

mkdir "ProjectDeliverables"
cd "ProjectDeliverables"
mkdir Final
mkdir Draft
mkdir "WorkInProgress"
ls -al
cd ..

mkdir "ProjectManagementDeliverables"
cd "ProjectManagementDeliverables"
mkdir "Project Definition"
mkdir Communications
mkdir Presentations
mkdir "FinancialInformation"
mkdir Logs
mkdir Miscellaneous
mkdir Workplans
mkdir Status
mkdir "MeetingMinutes"
mkdir Reports
ls -al
cd ..

mkdir Reference
cd Reference
mkdir Tutorials
mkdir Templates
mkdir "OtherReferenceMaterial"
ls -al
cd ..

mkdir Workarea
cd Workarea
mkdir User1
mkdir User2
ls -al
cd ..
