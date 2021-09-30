# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/charmbracelet/glamour
%global goipath         github.com/charmbracelet/glamour
Version:                0.3.0

%gometa

%global common_description %{expand:
Stylesheet-based markdown rendering for your CLI apps.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Stylesheet-based markdown rendering for your CLI apps

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# merged - change tests because of reflow v0.3.0
Patch0001:      https://github.com/charmbracelet/glamour/commit/ea285ca64f6ea5c179861581b01433902ecd1fd1.patch

BuildRequires:  golang(github.com/alecthomas/chroma)
BuildRequires:  golang(github.com/alecthomas/chroma/quick)
BuildRequires:  golang(github.com/alecthomas/chroma/styles)
BuildRequires:  golang(github.com/microcosm-cc/bluemonday)
BuildRequires:  golang(github.com/muesli/reflow/indent)
BuildRequires:  golang(github.com/muesli/reflow/padding)
BuildRequires:  golang(github.com/muesli/reflow/wordwrap)
BuildRequires:  golang(github.com/muesli/termenv)
BuildRequires:  golang(github.com/olekukonko/tablewriter)
BuildRequires:  golang(github.com/yuin/goldmark)
BuildRequires:  golang(github.com/yuin/goldmark-emoji)
BuildRequires:  golang(github.com/yuin/goldmark-emoji/ast)
BuildRequires:  golang(github.com/yuin/goldmark/ast)
BuildRequires:  golang(github.com/yuin/goldmark/extension)
BuildRequires:  golang(github.com/yuin/goldmark/extension/ast)
BuildRequires:  golang(github.com/yuin/goldmark/parser)
BuildRequires:  golang(github.com/yuin/goldmark/renderer)
BuildRequires:  golang(github.com/yuin/goldmark/util)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0001 -p1

%install
%gopkginstall

#disable temporary check, as doesn't work in copr, but does with mock
#%%if %%{with check}
#%%check
#%%gocheck
#%%endif

%gopkgfiles

%changelog
* Sun Sep 26 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.3.0-1
- Initial package

