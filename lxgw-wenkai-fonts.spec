%global fontname lxgw-wenkai
%global fontconf 60-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.250
Release:        1%{?dist}
Summary:        LXGW WenKai fonts

License:        OFL
URL:            https://github.com/lxgw/LxgwWenKai
Source0:        https://github.com/lxgw/LxgwWenKai/releases/download/v%{version}/lxgw-wenkai-v%{version}.tar.gz
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib

Requires:       fontpackages-filesystem

%description
An open-source Chinese font derived from Fontworks' Klee One. 一款开源中文字体，基于 FONTWORKS 出品字体 Klee One 衍生。


%prep
%autosetup -n lxgw-wenkai-v1.245.1


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata file
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Wed Sep 28 2022 Young Xu <xuthus5@gmail.com> - 1.245.1
- release tag: https://github.com/lxgw/LxgwWenKai/releases/tag/v1.245.1
* Wed Sep 7 2022 Young Xu <xuthus5@gmail.com> - 1.240
- release tag: https://github.com/lxgw/LxgwWenKai/releases/tag/v1.240
