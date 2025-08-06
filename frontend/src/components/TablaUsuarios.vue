<template>
  <div style="padding: 20px; background-color: #f0f4ff; min-height: 100vh;">
    <h1 style="text-align: center; color: #4b0082; font-size: 24px; margin-bottom: 20px;">
      Usuarios Synapsia UNAM
    </h1>
    <table border="1" cellpadding="10" cellspacing="0" style="width: 100%; background-color: white;">
      <thead style="background-color: #d8b4fe; color: white;">
        <tr>
          <th>Nombre</th>
          <th>Apellidos</th>
          <th>Edad</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="usuario in usuarios" :key="usuario.id" style="text-align: center;">
          <td>{{ usuario.nombre }}</td>
          <td>{{ usuario.apellidos }}</td>
          <td>{{ usuario.edad }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      usuarios: []
    }
  },
  mounted() {
    fetch('http://localhost:8000/api/usuarios/')
      .then(response => response.json())
      .then(data => {
        this.usuarios = data
      })
      .catch(error => {
        console.error('Error al obtener usuarios:', error)
      })
  }
}
</script>
