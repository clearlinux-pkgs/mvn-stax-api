#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-stax-api
Version  : 1.0.1
Release  : 4
URL      : https://repo1.maven.org/maven2/stax/stax-api/1.0.1/stax-api-1.0.1.jar
Source0  : https://repo1.maven.org/maven2/stax/stax-api/1.0.1/stax-api-1.0.1.jar
Source1  : https://repo1.maven.org/maven2/javax/xml/stream/stax-api/1.0-2/stax-api-1.0-2.jar
Source2  : https://repo1.maven.org/maven2/javax/xml/stream/stax-api/1.0-2/stax-api-1.0-2.pom
Source3  : https://repo1.maven.org/maven2/stax/stax-api/1.0.1/stax-api-1.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-stax-api-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-stax-api package.
Group: Data

%description data
data components for the mvn-stax-api package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/stax/stax-api/1.0.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/stax/stax-api/1.0.1/stax-api-1.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/xml/stream/stax-api/1.0-2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/javax/xml/stream/stax-api/1.0-2/stax-api-1.0-2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/xml/stream/stax-api/1.0-2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/javax/xml/stream/stax-api/1.0-2/stax-api-1.0-2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/stax/stax-api/1.0.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/stax/stax-api/1.0.1/stax-api-1.0.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/javax/xml/stream/stax-api/1.0-2/stax-api-1.0-2.jar
/usr/share/java/.m2/repository/javax/xml/stream/stax-api/1.0-2/stax-api-1.0-2.pom
/usr/share/java/.m2/repository/stax/stax-api/1.0.1/stax-api-1.0.1.jar
/usr/share/java/.m2/repository/stax/stax-api/1.0.1/stax-api-1.0.1.pom
