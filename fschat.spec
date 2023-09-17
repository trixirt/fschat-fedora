# Created by pyp2rpm-3.3.10
%global pypi_name fschat
%global pypi_version 0.2.28

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        An open platform for training, serving, and evaluating large language model based chatbots

License:        None
URL:            None
Source0:        %{pypi_name}-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(accelerate) >= 0.21
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(anthropic) >= 0.3
BuildRequires:  python3dist(black) = 23.3
BuildRequires:  python3dist(einops)
BuildRequires:  python3dist(fastapi)
BuildRequires:  python3dist(flash-attn) >= 2
BuildRequires:  python3dist(gradio)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(markdown2)
BuildRequires:  python3dist(nh3)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(openai)
BuildRequires:  python3dist(peft)
BuildRequires:  python3dist(prompt-toolkit) >= 3
BuildRequires:  (python3dist(pydantic) >= 1 with python3dist(pydantic) < 2~~)
BuildRequires:  python3dist(pylint) = 2.8.2
BuildRequires:  python3dist(ray)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(rich) >= 10
BuildRequires:  python3dist(sentencepiece)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(shortuuid)
BuildRequires:  python3dist(tiktoken)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(transformers) >= 4.31
BuildRequires:  python3dist(uvicorn)
BuildRequires:  python3dist(wandb)

%description
 FastChat | [**Demo**]( | [**Discord**]( | [**Twitter**]( |FastChat is an open
platform for training, serving, and evaluating large language model based
chatbots. The core features include: - The weights, training code, and
evaluation code for state-of-the-art models (e.g., Vicuna). - A distributed
multi-model serving system with web UI and OpenAI-compatible RESTful APIs. News
- [2023/08] 🔥 We...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(accelerate) >= 0.21
Requires:       python3dist(aiohttp)
Requires:       python3dist(anthropic) >= 0.3
Requires:       python3dist(einops)
Requires:       python3dist(fastapi)
Requires:       python3dist(flash-attn) >= 2
Requires:       python3dist(gradio)
Requires:       python3dist(httpx)
Requires:       python3dist(markdown2)
Requires:       python3dist(nh3)
Requires:       python3dist(numpy)
Requires:       python3dist(openai)
Requires:       python3dist(peft)
Requires:       python3dist(prompt-toolkit) >= 3
Requires:       (python3dist(pydantic) >= 1 with python3dist(pydantic) < 2~~)
Requires:       python3dist(ray)
Requires:       python3dist(requests)
Requires:       python3dist(rich) >= 10
Requires:       python3dist(sentencepiece)
Requires:       python3dist(shortuuid)
Requires:       python3dist(tiktoken)
Requires:       python3dist(torch)
Requires:       python3dist(transformers) >= 4.31
Requires:       python3dist(uvicorn)
Requires:       python3dist(wandb)
%description -n python3-%{pypi_name}
 FastChat | [**Demo**]( | [**Discord**]( | [**Twitter**]( |FastChat is an open
platform for training, serving, and evaluating large language model based
chatbots. The core features include: - The weights, training code, and
evaluation code for state-of-the-art models (e.g., Vicuna). - A distributed
multi-model serving system with web UI and OpenAI-compatible RESTful APIs. News
- [2023/08] 🔥 We...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/build
%{python3_sitelib}/fastchat
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Sun Sep 17 2023 Tom Rix <trix@redhat.com> - 0.2.28-1
- Initial package.
