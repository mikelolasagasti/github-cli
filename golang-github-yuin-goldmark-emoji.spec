# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/yuin/goldmark-emoji
%global goipath         github.com/yuin/goldmark-emoji
Version:                1.0.1

%gometa

%global common_description %{expand:
An emoji extension for the goldmark markdown parser.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        An emoji extension for the goldmark markdown parser

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/yuin/goldmark)
BuildRequires:  golang(github.com/yuin/goldmark/ast)
BuildRequires:  golang(github.com/yuin/goldmark/parser)
BuildRequires:  golang(github.com/yuin/goldmark/renderer)
BuildRequires:  golang(github.com/yuin/goldmark/renderer/html)
BuildRequires:  golang(github.com/yuin/goldmark/text)
BuildRequires:  golang(github.com/yuin/goldmark/util)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/yuin/goldmark/testutil)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep


%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md

%gopkgfiles

%changelog
* Sun Sep 26 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0.1-1
- Initial package

