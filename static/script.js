document.getElementById('reservaForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const nome   = document.getElementById('nome').value.trim();
  const tipo   = parseInt(document.getElementById('tipo').value);
  const pessoas = parseInt(document.getElementById('pessoas').value);
  const dias   = parseInt(document.getElementById('dias').value);

  if (!nome || !pessoas || !dias) {
    mostrarResultado('Preencha todos os campos.', 'erro');
    return;
  }

  fetch('/api/reservas/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome, tipo, pessoas, dias })
  })
  .then(res => {
    if (!res.ok) throw new Error('Erro na resposta do servidor');
    return res.json();
  })
  .then(data => {
    const msg = `
      ✅ Reserva confirmada!<br>
      <strong>Responsável:</strong> ${data.nome}<br>
      <strong>Apartamento:</strong> Tipo ${data.tipo}<br>
      <strong>Pessoas:</strong> ${data.pessoas}<br>
      <strong>Dias:</strong> ${data.dias}<br>
      <strong>Total:</strong> R$ ${parseFloat(data.total).toFixed(2).replace('.', ',')}
    `;
    mostrarResultado(msg, 'sucesso');
  })
  .catch(() => {
    mostrarResultado('❌ Erro de conexão com a API. Verifique se o servidor está rodando.', 'erro');
  });
});

function mostrarResultado(msg, tipo) {
  const div = document.getElementById('resultado');
  div.innerHTML = msg;
  div.className = 'resultado ' + tipo;
}