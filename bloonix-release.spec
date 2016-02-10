Summary: Bloonix repository configuration
Name: bloonix-release
Version: 0.6
Release: 1%{dist}
License: distributable
Group: System Environment/Base
Distribution: RHEL/CentOS/Fedora/SuSE

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: https://download.bloonix.de/sources/%{name}-%{version}.tar.gz

%description
bloonix-release provides files for the bloonix repository configuration.

# RHEL/CentOS
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel} 
%define repodir %{_sysconfdir}/yum.repos.d
%define repofile Bloonix-CentOS.repo
%else
# SLES/SuSE
%define repodir %{_sysconfdir}/zypp/repos.d
%define repofile Bloonix-SuSE.repo
%endif

%define gpgdir %{_sysconfdir}/pki/rpm-gpg

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{gpgdir}
mkdir -p ${RPM_BUILD_ROOT}%{repodir}
install -c -m 0644 bloonix.gpg ${RPM_BUILD_ROOT}%{gpgdir}/RPM-GPG-KEY-Bloonix
install -c -m 0644 %{repofile} ${RPM_BUILD_ROOT}%{repodir}/Bloonix.repo

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if 0%{?fedora}
sed 's@\$releasever@7@' %{repodir}/Bloonix.repo > /tmp/bloonix.repo.$$ && mv /tmp/bloonix.repo.$$ /etc/yum.repos.d/Bloonix.repo
%endif

%files
%defattr(-,root,root,-)
%dir %{repodir}
%dir %{gpgdir}
%config(noreplace) %{repodir}/*
%{gpgdir}/*

%changelog
* Wed Feb 10 2016 Jonny Schulz <js@bloonix.de> - 0.6-1
- Repo path fixed for SuSE.
* Fri Dec 05 2014 Jonny Schulz <js@bloonix.de> - 0.5-1
- Update bloonix-release.spec for fedora.
* Sat Sep 20 2014 Jonny Schulz <js@bloonix.de> - 0.4-1
- New path to the repositories.
* Sat Mar 29 2014 Jonny Schulz <js@bloonix.de> - 0.3-1
- Protocol changed to https.
* Sat Dec 01 2012 Jonny Schulz <js@bloonix.de> - 0.2-1
- Domain changed.
* Tue Sep 18 2012 Jonny Schulz <js@bloonix.de> - 0.1-1
- First release.
