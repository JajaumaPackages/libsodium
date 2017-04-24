Name:           libsodium
Version:        1.0.12
Release:        1%{?dist}
Summary:        The Sodium crypto library

License:        ISC license
URL:            http://doc.libsodium.org/
Source0:        http://download.libsodium.org/libsodium/releases/libsodium-%{version}.tar.gz


%description
Sodium is a modern, easy-to-use software library for encryption, decryption,
signatures, password hashing and more.


%package        devel
Summary:        Development files and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig


%description    devel
Headers and libraries for developing applications that use %{name}
functionality.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags} V=1


%check
make check


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog LICENSE README* THANKS
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libsodium.pc


%changelog
* Mon Apr 24 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0.12-1
- Update to latest upstream release

* Wed Aug 10 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.0.11-1
- Public release
