Name:           nordic-themes
Version:        2.2.0
Release:        1
Summary:        Nord-derived themes for GTK and others
License:        GPL-3.0-only
URL:            https://github.com/EliverLara/Nordic
Source0:        https://github.com/EliverLara/Nordic/releases/download/v%{version}/Nordic.tar.xz
Source1:        https://github.com/EliverLara/Nordic/releases/download/v%{version}/Nordic-standard-buttons.tar.xz
Source2:        https://github.com/EliverLara/Nordic/releases/download/v%{version}/Nordic-Polar-standard-buttons.tar.xz
Source3:        https://github.com/EliverLara/Nordic/releases/download/v%{version}/Nordic-darker.tar.xz
Source4:        https://github.com/EliverLara/Nordic/releases/download/v%{version}/Nordic-darker-standard-buttons.tar.xz
Source5:        https://github.com/EliverLara/Nordic/releases/download/v%{version}/Nordic-bluish-accent.tar.xz
Source6:        https://github.com/EliverLara/Nordic/releases/download/v%{version}/Nordic-bluish-accent-standard-buttons.tar.xz
BuildArch:      noarch

#--- Subpackages ---

%package nordic-theme
Summary: Nordic GTK theme

%description nordic-theme
Standard Nordic GTK theme.

%package nordic-standard-buttons-theme
Summary: Nordic GTK theme with standard buttons

%description nordic-standard-buttons-theme
Nordic GTK theme with standard buttons.

%package nordic-polar-standard-buttons-theme
Summary: Nordic Polar GTK theme with standard buttons

%description nordic-polar-standard-buttons-theme
Nordic Polar GTK theme with standard buttons.

%package nordic-darker-theme
Summary: Nordic Darker GTK theme

%description nordic-darker-theme
Nordic Darker GTK theme.

%package nordic-darker-standard-buttons-theme
Summary: Nordic Darker GTK theme with standard buttons

%description nordic-darker-standard-buttons-theme
Nordic Darker GTK theme with standard buttons.

%package nordic-bluish-accent-theme
Summary: Nordic Bluish Accent GTK theme

%description nordic-bluish-accent-theme
Nordic Bluish Accent GTK theme.

%package nordic-bluish-accent-standard-buttons-theme
Summary: Nordic Bluish Accent GTK theme with standard buttons

%description nordic-bluish-accent-standard-buttons-theme
Nordic Bluish Accent GTK theme with standard buttons.


#--- Prep ---

%prep
%setup -q -T -c
# Extract manually one by one
tar xf %{SOURCE0}
tar xf %{SOURCE1}
tar xf %{SOURCE2}
tar xf %{SOURCE3}
tar xf %{SOURCE4}
tar xf %{SOURCE5}
tar xf %{SOURCE6}


#--- Build ---

%build
# No build step required


#--- Install ---

%install
rm -rf %{buildroot}

install -d %{buildroot}/usr/share/themes/

cp -a Nordic %{buildroot}/usr/share/themes/Nordic
cp -a Nordic-standard-buttons %{buildroot}/usr/share/themes/Nordic-standard-buttons
cp -a Nordic-Polar-standard-buttons %{buildroot}/usr/share/themes/Nordic-Polar-standard-buttons
cp -a Nordic-darker %{buildroot}/usr/share/themes/Nordic-darker
cp -a Nordic-darker-standard-buttons %{buildroot}/usr/share/themes/Nordic-darker-standard-buttons
cp -a Nordic-bluish-accent %{buildroot}/usr/share/themes/Nordic-bluish-accent
cp -a nordic-bluish-accent-standard-buttons %{buildroot}/usr/share/themes/nordic-bluish-accent-standard-buttons


#--- File lists ---

%files nordic-theme
/usr/share/themes/Nordic

%files nordic-standard-buttons-theme
/usr/share/themes/Nordic-standard-buttons

%files nordic-polar-standard-buttons-theme
/usr/share/themes/Nordic-Polar-standard-buttons

%files nordic-darker-theme
/usr/share/themes/Nordic-darker

%files nordic-darker-standard-buttons-theme
/usr/share/themes/Nordic-darker-standard-buttons

%files nordic-bluish-accent-theme
/usr/share/themes/Nordic-bluish-accent

%files nordic-bluish-accent-standard-buttons-theme
/usr/share/themes/nordic-bluish-accent-standard-buttons

