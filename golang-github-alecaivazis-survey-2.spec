%global debug_package %{nil}

# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/AlecAivazis/survey
%global goipath         github.com/AlecAivazis/survey/v2
Version:                2.3.2

%gometa

%global common_description %{expand:
A golang library for building interactive and accessible prompts with full
support for windows and posix terminals.}

%global golicenses      LICENSE terminal/LICENSE.txt
%global godocs          CONTRIBUTING.md README.md terminal/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A golang library for building interactive and accessible prompts

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  go-rpm-macros

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d .
%endif

%gopkgfiles

%changelog
%autochangelog
