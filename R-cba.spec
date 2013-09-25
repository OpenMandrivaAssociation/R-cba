%global packname  cba
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.2.12
Release:          1
Summary:          Clustering for Business Analytics
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/cba_0.2-12.tar.gz
Requires:         R-grid R-proxy 
Requires:         R-Matrix 
Requires:         R-gclus R-colorspace 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-grid R-proxy
BuildRequires:    R-Matrix 
BuildRequires:    R-gclus R-colorspace 

%description
Implements clustering techniques such as Proximus and Rock, utility
functions for efficient computation of cross distances and data

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
