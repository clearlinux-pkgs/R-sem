#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sem
Version  : 3.1.15
Release  : 56
URL      : https://cran.r-project.org/src/contrib/sem_3.1-15.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sem_3.1-15.tar.gz
Summary  : Structural Equation Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-sem-lib = %{version}-%{release}
Requires: R-mi
BuildRequires : R-mi
BuildRequires : buildreq-R

%description
equation models (with observed and latent variables) using the RAM approach, 
    and for fitting structural equations in observed-variable models by two-stage least squares.

%package lib
Summary: lib components for the R-sem package.
Group: Libraries

%description lib
lib components for the R-sem package.


%prep
%setup -q -c -n sem
cd %{_builddir}/sem

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649692401

%install
export SOURCE_DATE_EPOCH=1649692401
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sem
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sem
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sem
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc sem || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sem/CHANGES
/usr/lib64/R/library/sem/DESCRIPTION
/usr/lib64/R/library/sem/INDEX
/usr/lib64/R/library/sem/Meta/Rd.rds
/usr/lib64/R/library/sem/Meta/data.rds
/usr/lib64/R/library/sem/Meta/features.rds
/usr/lib64/R/library/sem/Meta/hsearch.rds
/usr/lib64/R/library/sem/Meta/links.rds
/usr/lib64/R/library/sem/Meta/nsInfo.rds
/usr/lib64/R/library/sem/Meta/package.rds
/usr/lib64/R/library/sem/NAMESPACE
/usr/lib64/R/library/sem/NEWS
/usr/lib64/R/library/sem/R/sem
/usr/lib64/R/library/sem/R/sem.rdb
/usr/lib64/R/library/sem/R/sem.rdx
/usr/lib64/R/library/sem/data/Rdata.rdb
/usr/lib64/R/library/sem/data/Rdata.rds
/usr/lib64/R/library/sem/data/Rdata.rdx
/usr/lib64/R/library/sem/etc/GreekLetters.txt
/usr/lib64/R/library/sem/etc/M-McArdle.txt
/usr/lib64/R/library/sem/etc/R-Blau-Duncan.txt
/usr/lib64/R/library/sem/etc/R-DHP.txt
/usr/lib64/R/library/sem/etc/R-Kerchoff.txt
/usr/lib64/R/library/sem/etc/R-Thurstone.txt
/usr/lib64/R/library/sem/etc/S-Wheaton.txt
/usr/lib64/R/library/sem/etc/model-Blau-Duncan.txt
/usr/lib64/R/library/sem/etc/model-Bollen.txt
/usr/lib64/R/library/sem/etc/model-DHP.txt
/usr/lib64/R/library/sem/etc/model-HS.txt
/usr/lib64/R/library/sem/etc/model-Kerchoff.txt
/usr/lib64/R/library/sem/etc/model-McArdle.txt
/usr/lib64/R/library/sem/etc/model-Tests.txt
/usr/lib64/R/library/sem/etc/model-Thurstone.txt
/usr/lib64/R/library/sem/etc/model-Wheaton-1.txt
/usr/lib64/R/library/sem/etc/model-Wheaton-2.txt
/usr/lib64/R/library/sem/help/AnIndex
/usr/lib64/R/library/sem/help/aliases.rds
/usr/lib64/R/library/sem/help/paths.rds
/usr/lib64/R/library/sem/help/sem.rdb
/usr/lib64/R/library/sem/help/sem.rdx
/usr/lib64/R/library/sem/html/00Index.html
/usr/lib64/R/library/sem/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sem/libs/sem.so
/usr/lib64/R/library/sem/libs/sem.so.avx2
/usr/lib64/R/library/sem/libs/sem.so.avx512
