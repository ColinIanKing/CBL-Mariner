Summary:        Connects C/C++/Objective C to some high-level programming languages
Name:           swig
Version:        4.0.2
Release:        1%{?dist}
License:        GPLv3+ AND BSD
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://swig.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/swig/swig/swig-%{version}/swig-%{version}.tar.gz
BuildRequires:  pcre-devel
Requires:       pcre

%description
Simplified Wrapper and Interface Generator (SWIG) is a software
development tool for connecting C, C++ and Objective C programs with a
variety of high-level programming languages.  SWIG is primarily used
with Perl, Python and Tcl/TK, but it has also been extended to Java,
Eiffel and Guile. SWIG is normally used to create high-level
interpreted programming environments, systems integration, and as a
tool for building user interfaces

%prep
%setup -q -n swig-%{version}

%build
./autogen.sh

%configure \
	--without-ocaml \
 	--without-java \
 	--without-r \
 	--without-go

make %{?_smp_mflags}

%install

make DESTDIR=%{buildroot} install

# Enable ccache-swig by default, if ccache is installed.
mkdir -p %{buildroot}%{_libdir}/ccache
ln -fs ../../bin/ccache-swig %{buildroot}%{_libdir}/ccache/swig

%check
make %{?_smp_mflags} check

%files
%license LICENSE LICENSE-GPL LICENSE-UNIVERSITIES
%{_bindir}/*
%{_datadir}/swig
%{_libdir}/ccache

%changelog
* Mon Mar 15 2021 Henry Li <lihl@microsoft.com> - 4.0.2-1
- Upgrade to version 4.0.2. License Verified.
- Correct licensing.
- Remove sha1 define

* Sat May 09 00:21:36 PST 2020 Nick Samson <nisamson@microsoft.com> - 3.0.12-4
- Added %%license line automatically

*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 3.0.12-3
-   Initial CBL-Mariner import from Photon (license: Apache2).

*       Tue May 02 2017 Vinay Kulkarni <kulkarniv@vmware.com> 3.0.12-2
-       Correct the license.

*       Wed Apr 12 2017 Vinay Kulkarni <kulkarniv@vmware.com> 3.0.12-1
-       Update to version 3.0.12

*       Tue Oct 04 2016 ChangLee <changlee@vmware.com> 3.0.8-3
-       Modified %check

*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 3.0.8-2
-	GA - Bump release of all rpms

* 	Tue Feb 23 2016 Anish Swaminathan <anishs@vmware.com>  3.0.8-1
- 	Upgrade to 3.0.8

* 	Thu Feb 26 2015 Divya Thaluru <dthaluru@vmware.com> 3.0.5-1
- 	Initial version
