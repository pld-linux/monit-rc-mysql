Summary:	monitrc file for monitoring MySQL database server
Summary(pl.UTF-8):	Plik monitrc do monitorowania serwera baz danych MySQL
Name:		monit-rc-mysql
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	mysql.monitrc
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	monit
Requires:	monit
Requires:	mysql >= 5.0.27-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitrc file for monitoring MySQL database server.

%description -l pl.UTF-8
Plik monitrc do monitorowania serwera baz danych MySQL.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/monit

install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/monit

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q monit restart

%postun
%service -q monit restart

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/monit/*.monitrc
