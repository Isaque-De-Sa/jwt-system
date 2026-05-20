


async function carregarUsuario() {

    const token = sessionStorage.getItem('token');

    const userArea = document.getElementById('userArea');

    // sem token
    if (!token) {

        userArea.innerHTML = `
            <a href="login">Login</a>
        `;

        return;
    }

    try {

        const res = await fetch('http://127.0.0.1:8000/perfil', {

            method: 'POST',

            headers: {
                'Authorization': `Bearer ${token}`
            }

        });

        // token inválido
        if (!res.ok) {

            sessionStorage.removeItem('token');

            userArea.innerHTML = `
                <a href="login">Login</a>
            `;

            return;
        }

        const dados = await res.json();

        userArea.innerHTML = `

            <div class="user-box">

                <span class="user-name">
                    <i class="bi bi-person-circle"></i>
                    ${dados.usuario.sub}
                </span>

                <button class="logout-btn" onclick="logout()">
                    <i class="bi bi-box-arrow-right"></i>
                    Sair
                </button>

            </div>

        `;

    } catch (erro) {

        console.log(erro);

        sessionStorage.removeItem('token');

    }

}

function logout() {

    sessionStorage.removeItem('token');

    window.location.href = 'login';

}

carregarUsuario();
