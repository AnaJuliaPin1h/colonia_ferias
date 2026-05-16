const PRECOS = {
  1: [20, 28, 35, 42, 48, 53],
  2: [25, 34, 42, 50, 57, 63],
};

// Pré-visualização do valor enquanto digita
function calcularPreview() {
  const tipo    = parseInt(document.getElementById('tipo').value);
  const pessoas = parseInt(document.getElementById('pessoas').value);
  const dias    = parseInt(document.getElementById('dias').value);

  if (pessoas >= 1 && pessoas <= 6 && dias >= 1 && dias <= 7) {
    const diaria = PRECOS[tipo][pessoas - 1];
    const total  = diaria * dias;
    document.getElementById('resultado').innerHTML =
      `<p class="preview">💰 Prévia: R$ ${total},00 (${dias} dia(s) × R$ ${diaria},00/dia)</p>`;
  }
}

['tipo', 'pessoas', 'dias'].forEach(id => {
  document.getElementById(id).addEventListener('input', calcularPreview);
});

// Submit — chama a API
document.getElementById('reservaForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const btn = document.getElementById('btnSubmit');
  btn.disabled    = true;
  btn.textContent = 'Aguarde...';

  const body = {
    nome:    document.getElementById('nome').value.trim(),
    tipo:    parseInt(document.getElementById('tipo').value),
    pessoas: parseInt(document.getElementById('pessoas').value),
    dias:    parseInt(document.getElementById('dias').value),
  };

  try {
    const res  = await fetch('/api/reservas/', {   // ✅ URL relativa
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(body),
    });

    const data = await res.json();

    if (res.ok) {
      document.getElementById('resultado').innerHTML = `
        <div class="sucesso">
          <h3>✅ Reserva confirmada!</h3>
          <p><strong>Nome:</strong> ${data.nome}</p>
          <p><strong>Tipo:</strong> Apartamento Tipo ${data.tipo}</p>
          <p><strong>Pessoas:</strong> ${data.pessoas}</p>
          <p><strong>Dias:</strong> ${data.dias}</p>
          <p><strong>Total:</strong> R$ ${parseFloat(data.valor_total).toFixed(2).replace('.', ',')}</p>
          <a href="/pdf/${data.id}/" target="_blank" class="btn-pdf">
            📄 Baixar Comprovante PDF
          </a>
        </div>
      `;
      document.getElementById('reservaForm').reset();
    } else {
      // Monta mensagem de erro legível
      const erros = Object.entries(data)
        .map(([campo, msgs]) => `<li><strong>${campo}:</strong> ${msgs}</li>`)
        .join('');
      document.getElementById('resultado').innerHTML =
        `<div class="erro"><ul>${erros}</ul></div>`;
    }

  } catch (err) {
    document.getElementById('resultado').innerHTML =
      `<div class="erro">❌ Erro de conexão com a API. Verifique se o servidor está rodando.</div>`;
  } finally {
    btn.disabled    = false;
    btn.textContent = 'Calcular Reserva';
  }
});