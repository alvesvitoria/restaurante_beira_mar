class ValidaForm {
    constructor(q = 'form') {
        this.form = document.querySelector(q);
        if (this.form) {
            this.init()
        }
    }

    init() {
        this.errors = {};
        this.fields = this.form.querySelectorAll('.toValidate');

        this.fields.forEach(field => {
            // remove os atributos required que vem no form django
            field.removeAttribute('required');

            this.errors[field.name] = [];
        });

        this.handleEvent();
    }

    handleEvent() {
        this.form.addEventListener('change', e => {
            const field = e.target;
            this.validateField(field);

            this.clearMessagesDiv(field);
            if (this.hasError()) {
                this.showFieldErrors(field);
            }
        });

        this.form.addEventListener('submit', e => {
            // faz a validação completa do formulário
            this.validate();

            // limpa div de erros de todos os campos
            this.fields.forEach(field => this.clearMessagesDiv(field));

            // se existe algum erro, não envia o formulário
            if (this.hasError()) {
                e.preventDefault();
                this.showErrors();
            }
        });
    }

    /**
     * Dado um campo, limpa sua div de mensagens
     */
    clearMessagesDiv(field) {
        const messagesDiv = this.form.querySelector(`.${field.name}-messages`);
        messagesDiv.innerHTML = '';
    }

    /**
     * Faz a validação de todos os campos do formulário
     */
    validate() {
        this.fields.forEach(field => {
            this.validateField(field);
        });
    }

    /**
     * Retorna true se existir erro no formulário
     */
    hasError() {
        for (const error in this.errors) {
            if (this.errors[error].length > 0) {
                return true;
            }
        }
        return false;
    }

    /**
     * Mostra os erros de todos os campos
     */
    showErrors() {
        this.fields.forEach(field => {
            this.showFieldErrors(field);
        });
    }

    /**
     * Mostra os erros de um campo específico
     */
    showFieldErrors(field) {
        const messagesDiv = this.form.querySelector(`.${field.name}-messages`);
        for (const e of this.errors[field.name]) {
            const div = document.createElement('div');
            div.classList.add('alert');
            div.classList.add('alert-danger');
            div.innerText = e;

            messagesDiv.appendChild(div);
        }
    }

    validateField(field) {
        this.errors[field.name] = [];

        if (field.name === 'username' || field.name === 'email') {
            this.validateEmail(field);
        } else if (field.name === 'password') {
            this.validatePassword(field);
        } else if (field.name === 'first_name') {
            this.validateFirstName(field);
        } else if (field.name === 'last_name') {
            this.validateLastName(field);
        } else if (field.name === 'birth_date') {
            this.validateBirthDate(field);
        } else if (field.name === 'phone_number') {
            this.validatePhoneNumber(field);
        } else if (field.name === 'cpf') {
            this.validateCpf(field);
        } else if (field.name === 'password1' || field.name === 'password2') {
            this.validatePassword(field);
            this.validatePasswords(field);
        }
    }

    // Métodos para validação do formulário:
    // validateExemplo(field) {
    //     const value = field.value;
    //     addError(field, 'Mensagem');
    // }

    validateEmail(field) { }
    validatePassword(field) { }
    validateFirstName(field) { }
    validateLastName(field) { }
    validateBirthDate(field) { }
    validatePhoneNumber(field) { }
    validateCpf(field) { }
    validatePasswords(field) { }

    addError(field, msg) {
        this.errors[field.name].push(msg);
    }
}


new ValidaForm();
