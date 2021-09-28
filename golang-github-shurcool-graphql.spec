# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/shurcooL/graphql
%global goipath         github.com/shurcooL/graphql
%global commit          18c5c3165e3af7c70ca625593f8066462ad684cc

%gometa

%global common_description %{expand:
Package graphql provides a GraphQL client implementation.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.8%{?dist}
Summary:        Package graphql provides a GraphQL client implementation

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Patches from GitHub fork
Patch0001:      https://github.com/cli/shurcooL-graphql/commit/a4a48d3af0f4d1e937f58787378e657fd3bff388.patch
Patch0002:      https://github.com/cli/shurcooL-graphql/commit/53d29f0eb7f5f1838b5f4f137b215e19bb10a5c9.patch

BuildRequires:  golang(github.com/graph-gophers/graphql-go)
# Examples are not packaged
# BuildRequires:  golang(github.com/graph-gophers/graphql-go/example/starwars)
BuildRequires:  golang(github.com/graph-gophers/graphql-go/relay)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0001 -p1
%patch0002 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Sep 28 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0-0.8
- Version bump and patches

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 16:35:56 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20210113git18c5c31
- Bump to commit 18c5c3165e3af7c70ca625593f8066462ad684cc

* Fri Sep 04 13:31:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200904gitd48a9a7
- Bump to commit d48a9a75455f6af30244670bc0c9d0e38e7392b5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git3d276b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git3d276b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180419git3d276b9
- First package for Fedora

