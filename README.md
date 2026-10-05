Projeto Flask para a disciplina de Desenvolvimento Web

Branches e como trocar:

Branches e como trocar: São ramificações para criar funcionalidades sem alterar o código principal. Troca-se de branch com git checkout <nome> ou git switch <nome>.

Share push: É o envio das suas alterações locais para o repositório remoto (ex: GitHub) usando o comando git push.

Reescrever commit: É a alteração do histórico. Usa-se git commit --amend para corrigir o último commit ou git rebase -i para modificar commits mais antigos.

Revert vs Merge: O revert desfaz um erro criando um novo commit de correção (sem apagar o histórico). O merge junta o código de duas branches diferentes numa só.

Stage (Staging area): É a "sala de espera". Os ficheiros ficam aqui (através do git add) antes de serem guardados definitivamente num commit.

Squash de commit: Junta vários commits pequenos num único commit maior para manter a linha do tempo do projeto mais limpa.

Reflog: É o registo de segurança do Git. Grava todas as ações e permite recuperar commits que tenham sido apagados por engano.

Reset vs Clean: O reset recua no histórico e desfaz commits. O clean apaga apenas ficheiros soltos e temporários que o Git não está a seguir (untracked).