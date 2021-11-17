--A general project prototype

CJW-Notes:  Based on years of experience doing rapid analysis of private equity type deal investments, a particular pattern for a project
directory was useful.  Now, one might argue that for note-book type control, such as Jupyter notebooks.  However, on a deal by deal basis,
there likely has been an NDA signed for which, depending on the deal outcome, someone in the data receiving firm may be designated to find 
and delete data owned by the other party and destroy it.  

Without violating that NDA agreement, it is often helpful to organize a short term project so that the protected party's data can be found, 
isolated, and removed, while not removing any special sauce code not covered by the NDA.  

These types of PE deals are usually short-term and hopefully resolve favorably.  But, more often than one usually would prefer, the deal is lost to a
competitor and focus shifts to another deal.  For this reason, even in a high intensity PE investment environment, it is a good idea for a
practioner to do a deal post-mortem.  Quickly evaluate what was successful and incorporate non-private information types of code and
concepts into libraries and best practices.

Otherwise, without proper isolation, do not count on going back to an old project to "see what I did".  Someone might have deleted upon
receipt of a destroy-data-request, and you have no right to be upset at that person.

The process is simple from a command line:
-   Go to the parent directory for the target project
-   Use the command line PATH-TO-DIRECTORY-CONTAINING-THIS-README/project_script NAME-OF-NEW-PROJECT
-   The script will copy the structure from proto, change the file names where necessary, and edit internal words like "prototype" to
    NAME-OF-NEW-PROJECT.


--Files

- proto:  A directory tree and supporting files for a protoype project.  This is a template for a project and the files will be renamed and
edited to build the project directory

- project_script:  This simple script is called from a command line, usually with the full path to the script.

- project_script_rev:   A script to help prototype-ize files in the an existing project.  Be sure to remove anything project specific from
  any code brought back into your prototype.




