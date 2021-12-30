# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/cli/cli
%global goipath         github.com/cli/cli
Version:                2.4.0

%gometa

%global goname gh

%global common_description %{expand:
GitHub’s official command line tool.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        GitHub’s official command line tool

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  git
BuildRequires:  go-rpm-macros

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
export LDFLAGS="-X github.com/cli/cli/v2/internal/build.Version=2.4.0-Fedora  \
                -X github.com/cli/cli/v2/internal/build.Date=2021-12-30"

%gobuild -o %{gobuilddir}/cmd/%{name} %{goipath}/cmd/%{name}

%{gobuilddir}/cmd/%{name} completion bash > %{name}.bash
%{gobuilddir}/cmd/%{name} completion fish > %{name}.fish
%{gobuilddir}/cmd/%{name} completion zsh  > %{name}.zsh


%install
%gopkginstall
install -m 0755 -vd                           %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/cmd/%{name} %{buildroot}%{_bindir}/

install -Dp %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dp %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dp %{name}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}


%if %{with check}
%check
# pkg/liveshare fails with golang-1.18
%gocheck -d pkg/liveshare
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%gopkgfiles

%changelog
%autochangelog
