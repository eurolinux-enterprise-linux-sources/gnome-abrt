# TODO: https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering
#       rpmlint warns about private-shared-object-provides
#       can't use filter because the package doesn't met any of the required criteria
#         ! Noarch package       ... caused by libreport wrappers shared library
#         ! no binaries in $PATH ... caused by gnome-abrt python script in /usr/bin

Name:       gnome-abrt
Version:    0.3.4
Release:    8%{?dist}
Summary:    A utility for viewing problems that have occurred with the system

Group:      User Interface/Desktops
License:    GPLv2+
URL:        https://fedorahosted.org/abrt/
Source0:    https://fedorahosted.org/released/abrt/%{name}-%{version}.tar.gz

# Remove with gnome-abrt > 0.3.4
Patch1:     0001-Do-not-crash-when-a-FileIcon-cant-be-loaded.patch
Patch2:     0002-Enable-multiple-problems-selection.patch
Patch3:     0003-Update-translations.patch
Patch4:     0004-Initialize-gnome_abrt-module-before-importing-its-su.patch
Patch5:     0005-Translation-updates.patch
Patch6:     0006-Pull-the-newest-rhel7-translations.patch
Patch7:     0007-Move-from-transifex-to-zanata.patch
Patch8:     0008-Add-gettext-mappings-to-the-zanata-config.patch
Patch9:     0009-translations-update-zanata-configuration.patch
Patch10:    0010-Test-availability-of-XServer-in-C-wrappers.patch
Patch11:    0011-Do-not-crash-in-case-of-a-DBus-timeout.patch
Patch12:    0012-Mark-Search-place-holder-text-for-translations.patch
Patch13:    0013-Translation-updates.patch
Patch14:    0014-Translation-updates.patch

# Downstream patches
Patch1000:  gnome-abrt-0.3.4_dont_suggest_reporting_to_bugzilla.patch

BuildRequires: intltool
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: python2-devel
BuildRequires: desktop-file-utils
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: pygobject3-devel
BuildRequires: libreport-gtk-devel >= 2.0.20
BuildRequires: abrt-gui-devel >= 2.1.7
BuildRequires: gtk3-devel
%if 0%{?fedora}
BuildRequires: pylint
BuildRequires: python-inotify
BuildRequires: pygobject3
BuildRequires: dbus-python
%else
%define checkoption --with-nopylint
%endif

Requires:   python-inotify
Requires:   pygobject3
Requires:   dbus-python
Requires:   xdg-utils

%description
A GNOME application allows users to browse through detected problems and
provides them with convenient way for managing these problems.


%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

# Downstream patches
%patch1000 -p1


%build
autoreconf -f
%configure %checkoption
make


%install
make install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}
%find_lang %{name}

# remove all .la and .a files
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f

desktop-file-install \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    --delete-original \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop


%check
make check


%post
# update icon cache
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc COPYING
%{python_sitearch}/gnome_abrt
%{_datadir}/%{name}
%{_datadir}/%{name}/ui
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/appdata/*
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/status/*


%changelog
* Mon Jun 20 2016 Matej Habrnal <mhabrnal@redhat.com> - 0.3.4-8
- Translation updates
- Resolves: #1272961

* Mon May 2 2016 Jakub Filak <jfilak@redhat.com> - 0.3.4-7
- Translation updates
- Do not crash in case of a DBus timeout
- Do not crash when testing availability of XServer
- Resolves: #1178712, #1175662

* Thu Jan 30 2014 Jakub Filak <jfilak@redhat.com> - 0.3.4-6
- Properly initialize gettext for glade files
- Resolves: #1030335

* Thu Jan 30 2014 Jakub Filak <jfilak@redhat.com> - 0.3.4-5
- Translation updates
- Resolves: #1047476

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.3.4-4
- Mass rebuild 2014-01-24

* Mon Jan 20 2014 Jakub Filak <jfilak@redhat.com> - 0.3.4-3
- Select multiple records to delete in gnome-abrt
- Do not crash when a FileIcon can't be loaded
- Resolves: #1048120, #1054089

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.3.4-2
- Mass rebuild 2013-12-27

* Thu Dec 19 2013 Jakub Filak <jfilak@redhat.com> 0.3.4-1
- Do not use deprecated GObject API
- Make gnome-abrt compatible with Python GObject < 3.7.2
- Do not fail if there is no Problem D-Bus service
- Make all labels selectable
- Run xdg-open for problem directory nonblocking
- Fix translations (rhbz#1044241)
- Make problem list resizable
- Make info about Reported state of problem more clear
- Remove message about missing Bugzilla ticket
- Fix a bug in SIGCHLD handler causing 100% CPU usage
- Show "yes" in Reported field only if no URL is available
- Load only the most recent reported to value
- Check if Application has valid name in filter fn
- Fix issues found by new pylint
- Related: #1044241
- Resolves: #1044569

* Fri Dec 06 2013 Jakub Filak <jfilak@redhat.com> 0.3.1-2
- Update translations
- Resolves: #1030335

* Thu Sep 12 2013 Jakub Filak <jfilak@redhat.com> 0.3.1-1
- Improve user experience
- Make About dialog transient for the main window
- Add AppData file
- Ship the 256x256 icon in the right place
- Recover from fork errors
- Add ABRT configure application menu
- Use absolute path in python shebang
- Recover from invalid time stamp values
- Use wrapped text for the bug report link
- Resolves: #994749, #995337, #995868, #1005472

* Fri Jul 26 2013 Jakub Filak <jfilak@redhat.com> 0.3.0-1
- Do not include url files twice
- Get rid of Stock Items usage
- Do not remove invalid problems while sorting the list
- Check if X display can be opened
- Fix a condition in the source changed notification handler
- Update Translations
- Skip inotify events for sub folders in dump location watcher
- Use GLib.io_add_watch() instead of IOChanell.add_watch()
- Fix a typo in macro name
- Remove shebang from non-executable scripts
- Remember missing elements and load them only once
- Download more problem elements in a single D-Bus call
- Improve data caching
- Display two sets of problems (My/System)
- Fix typo in dbus error message
- Don't crash if a new directory problem is invalid
- Resolves: #956912, #973125, #967499

* Mon May 06 2013 Jakub Filak <jfilak@redhat.com> 0.2.12-3
- Disable downloading of HTML titles

* Mon May 06 2013 Jakub Filak <jfilak@redhat.com> 0.2.12-2
- Fix a wrong path in contoller.py

* Fri May 03 2013 Jakub Filak <jfilak@redhat.com> 0.2.12-1
- Use 'N/A' instead of ??
- Use package name is neither component nor executable items are available
- Don't try to select a problem if the list is empty
- Catch InvalidProblem exception in sort function
- Handle DBus initialization errors gracefully
- Show HTML titles of URLs from reported_to element
- Updated translation
- Continue in handling of SIGCHLD after the first one is handled
- Fix two comma splices
- Fix wrong dialog flag names
- Resolves: #958974

* Mon Apr 22 2013 Jakub Filak <jfilak@redhat.com> 0.2.11-1
- Enable pylint check only on Fedora
- Fix bogus dates in chagelog
- Introduce expert mode and show 'Analyze' button in that mode
- Use last occurrence item for problems sorting
- Fix broken keyboard shortcuts
- Fix missing space typo - Martin Milata <mmilata@redhat.com>
- Compare all DesktopEntry.*() return values to None
- Display 'component' name instead of 'executable' if desktop file is missing
- Do not show scrollbar for long links
- Allow to disable pylint check in configure.ac
- Move manpage to volume 1 - Chris Lockfort <clockfort@csh.rit.edu>
- Move gnome_abrt module check to module's Makefile
- Disable 'Interface not implemented' pylint warning
- Configure pylint to produce parseable output
- Resolves: #919838

* Tue Apr  9 2013 Jakub Filak <jfilak@redhat.com> 0.2.10-2
- Make check only on fedora

* Wed Mar 27 2013 Jakub Filak <jfilak@redhat.com> 0.2.10-1
- Add the report dialog to the menu
- Add 'Report problem with ABRT' dialog
- Add VERSION and PACKAGE attributes to gnome_abrt module
- Rename attribute in errors.InvalidProblem
- Use IOChannel approach in order to make signal handling synchronous
- Add all python Requires to BuildRequires because of pylint
- Replace GNU style make pattern rules by implicit rules
- Remove left-over RELEASE varible from configure.ac
- Recover from DBus errors while sending command line
- Catch more exceptions and handle them correctly
- Add pylint check and fix problems uncoverend by pylint
- Filter out empyt strings from splitted cmdline
- Fix sytanx error
- Change the label "No oopses" to "No problems detected"
- Get rid of scrollbar around the text on the bottom of window in default size
- Fix appearance of scrolled widgets to no longer have white background
- Remove leftover shebang from non-executable script
- Resolves: #926010, #926011

* Mon Mar 18 2013 Jakub Filak <jfilak@redhat.com> 0.2.9-1
- Truncate long texts with ellipsis instead of auto-adjusting of window width
- Add a popopup menu for list of problems
- Use executable's basename as an application name instead of the full path
- Remove invalid problems from GUI tree view list
- Remove invalid problems from the dbus cache
- Robustize the processing of newly occurred problems
- Remove a left-over usage of the window member in OopsApplication
- Handle reaching inotify max watches better
- Update translation
- Don't allow reporting if the problem is not reportable
- Suggest reporting a bug if it wasn't reported yet
- Simplify the glade file and add a widget for messages
- Refactorize the function rendering a problem data
- A workaround for the bug in remote GtkApplications
- Allow only a single instance of gnome-abrt
- Fix bugs in main window in handler of configuration updates
- Resolves: #922653, #922655, #922647

* Mon Feb 25 2013 Jakub Filak <jfilak@redhat.com> 0.2.8-1
- Try harder when looking for icon and don't cache weak results
- Make controller more robust against invalid arguments
- Check return value of the get selection function
- Require correct version of libreport
- Return an empty list instead of None from OopsWindow.get_selected()
- Return an empty list instead of None from get_problems() in case of DBus error
- Get rid of unnecessary variable from the directory source
- Add a cmd line argument for selected problem id

* Fri Feb 08 2013 Jakub Filak <jfilak@redhat.com> - 0.2.7-1
- Fix failure in processing of dump directories from user's home
- Resolves: #908712

* Tue Jan 08 2013 Jakub Filak <jfilak@redhat.com> - 0.2.6-1
- Require libreport version 2.0.20 and greater
- Use DD api correctly
- Reflect changes in libreport
- Resolves: #890357

* Wed Nov 28 2012 Jakub Filak <jfilak@redhat.com> - 0.2.5-1
- Add licenses to all files
- Refresh view's source if InvalidProblem exception is caught during GUI update
- Properly handle removal of the first and the last problem from the list
- Use right tree model in searching for problems
- Use theme backround color as background for the link buttons
- Make the links to servers less moving
- Keep user's selection even if a source has changed
- Destroy abrt-handle-event zombies

* Mon Nov 12 2012 Jakub Filak <jfilak@redhat.com> - 0.2.4-1
- Fix label fields size
- Assure ownership of reported problem
- Remove unnecessary GtkEventBox
- Fix appearance of link button widget to no longer have a white background
- Update translations

* Fri Oct 05 2012 Jakub Filak <jfilak@redhat.com> - 0.2.3-1
- Generate version
- Add GNOME3 application menu
- Use correct D-Bus path to listen on for Crash signal
- Make path to abrt-handle-event configurable
- Fix a bug in running of subprocesses
- Refactorize directory problems implementation
- Don't print weired debug message
- Don't show the 'reconnecting to dbus' warning
- Don't show new root's crashes by default
- Fix indentation

* Fri Sep 21 2012 Jakub Filak <jfilak@redhat.com> - 0.2.2-1
- Lazy initialization of directory source
- Don't utilize CPU for 99%
- Code refactorization
- Add translation from the ABRT project
- Properly log exceptions
- Delete directory problems marked as invalid after refresh in inotify handler
- Declare directory problems deleted if its directory doesn't exist
- Fix indentation bug in icon look up algorithm
- Add --verbose command line argument
- Add directory name to error messages

* Mon Sep 17 2012 Jakub Filak <jfilak@redhat.com> - 0.2.1-4
- Fix a problem with desktop items without icons
- A bit better handling of uncaght exceptions

* Mon Sep 17 2012 Jakub Filak <jfilak@redhat.com> - 0.2.1-3
- Add cs and et translations

* Fri Sep 14 2012 Jakub Filak <jfilak@redhat.com> - 0.2.1-2
- Fixed problem with selection of problem after start up
- Corrected application icon look up algorithm
- Fixed problem with missing problems directory

* Fri Sep 14 2012 Jakub Filak <jfilak@redhat.com> - 0.2.1-1
- Detail button replaced by list of reported_to links
- Improved look (margins, icons, wider window by default)
- Implemented multiple delete
- Changed window tiple
- Double click and keyboard shortcuts

* Thu Sep 06 2012 Jakub Filak <jfilak@redhat.com> - 0.2-9
- Remove noarch because of binary wrappers
- Added support for adjusting libreport preferences

* Tue Aug 28 2012 Jakub Filak <jfilak@redhat.com> - 0.2-8
- Take ownership of all installed directories
- Correct paths to translated files

* Mon Aug 27 2012 Jakub Filak <jfilak@redhat.com> - 0.2-7
- Dropped versions from requires
- Simplified spec
- Removed pylint check from configure.ac
- Whitespace cleanup (rmarko@redhat.com)

* Fri Aug 24 2012 Jakub Filak <jfilak@redhat.com> - 0.2-6
- Use own icons set

* Fri Aug 24 2012 Jakub Filak <jfilak@redhat.com> - 0.2-5
- Reorganize source files
- Get rid of all rpmlint complaints

* Thu Aug 23 2012 Jakub Filak <jfilak@redhat.com> - 0.2-4
- Update GUI on various signals (new problem, problem changed, etc.)
- Sort problems by time in descending order
- Correct internationalization in date string generator

* Wed Aug 15 2012 Jakub Filak <jfilak@redhat.com> - 0.2-3
- Reconnect to DBus bus
- Default values for missing items
- Correct field for 'is_reported' flag

* Wed Aug 15 2012 Jakub Filak <jfilak@redhat.com> - 0.2-2
- Add missing files

* Wed Aug 15 2012 Jakub Filak <jfilak@redhat.com> - 0.2-1
- Problems filtering
- Errors handling
- Localization support

* Mon Aug 13 2012 Jakub Filak <jfilak@redhat.com> - 0.1-1
- Initial version
