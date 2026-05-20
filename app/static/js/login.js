 async function verificar_token() {

    const token = sessionStorage.getItem('token');

    // sem token
    if (!token) {
        return;
    }

    try {

        const res = await fetch('http://127.0.0.1:8000/perfil', {

            method: 'POST',

            headers: {
                'Authorization': `Bearer ${token}`
            }

        });

        const dados = await res.json();


        if(token) {
            setTimeout(() => {
                window.location.href ="/";
            }, 0)
        }



    } catch (erro) {

        console.log(erro);

        sessionStorage.removeItem('token');

    }

}

verificar_token();




//=========== aviso modal ==========================


function showForm(id) {

    const titles = {
        login: 'Acessar Conta',
        register: 'Criar Conta',
        forgot: 'Recuperar Senha'
    };

    // remove active
    document.querySelectorAll('.form').forEach(form => {

        form.classList.remove('active');

        // anima saída
        form.classList.remove('form-enter');

    });

    // pega form atual
    const currentForm = document.getElementById(id);

    // pequena animação
    setTimeout(() => {

        currentForm.classList.add('active');
        currentForm.classList.add('form-enter');

    }, 100);

}

// TOAST

function showToast(message, type = 'success') {

    const toast = document.getElementById('toast');
    const msg = document.getElementById('toast-msg');
    const icon = toast.querySelector('i');

    msg.textContent = message;

    // limpa classes antigas
    toast.className = 'toast';

    // ícones
    if(type === 'success'){
        icon.className = 'bi bi-check-circle-fill';
    }

    if(type === 'error'){
        icon.className = 'bi bi-x-circle-fill';
    }

    if(type === 'aviso'){
        icon.className = 'bi bi-exclamation-triangle-fill';
    }

    // ativa
    toast.classList.add('show', type);

    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

//=========== aviso modal ==========================


const u = document.getElementById("usuario");
const p = document.getElementById("senha");


document.getElementById("register").addEventListener("submit", async (e) => {

    console.log("clicou")
    e.preventDefault();

    const reg_user = document.getElementById("reg_user").value;
    const reg_email = document.getElementById("reg_email").value;
    const reg_pass = document.getElementById("reg_pass").value;


    
    const res = await fetch("http://127.0.0.1:8000/register", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            reg_user,
            reg_email,
            reg_pass
        })
    })
    
    const dados = await res.json();

    if(dados.status == "accept") {
        showToast('Registro realizado com sucesso','success');
        u.value = reg_email;
        p.value = reg_pass;
        
    setTimeout(() => {

        document.getElementById('toast')
            .classList.remove('show');

        showForm("login");

    }, 1200);

    } else if (dados.status == "aviso") {
        showToast(String(dados.mensagem), String(dados.status));
    }

})


// fetch login

document.getElementById('login').addEventListener('submit', async (e) => {

        console.log('clicou');

        
    e.preventDefault();

    const user = u.value;
    const pass2 = p.value;


    const res = await fetch('http://127.0.0.1:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user,
            pass2
        })
    })

    const dados = await res.json();

    if (dados.status == 'accept') {
           // salva token
        sessionStorage.setItem('token', dados.token);

        showToast('Login realizado com sucesso', 'success');

        // espera um pouco e redireciona
        setTimeout(() => {
            window.location.href = '/';
        }, 1000);

    } else if (dados.status == "error") {
         sessionStorage.removeItem('token');
        showToast(String(dados.mensagem), 'error');
        
    }    
});


