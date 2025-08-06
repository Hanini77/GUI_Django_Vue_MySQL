<template>
  <div class="p-4" style="background: linear-gradient(to right, #dbeafe, #fce7f3); min-height: 100vh;">
    <h1 style="color: #6b21a8; text-align: center; font-size: 2rem; font-weight: bold;">Usuarios Synapsia UNAM</h1>
    <table style="width: 100%; background: white; border-radius: 10px; margin-top: 1rem; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
      <thead>
        <tr style="background: #c084fc; color: white;">
          <th style="padding: 10px; border: 1px solid #ccc;">Nombre</th>
          <th style="padding: 10px; border: 1px solid #ccc;">Apellidos</th>
          <th style="padding: 10px; border: 1px solid #ccc;">Edad</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="usuario in usuarios" :key="usuario.id" style="text-align: center;" :style="{ background: index % 2 === 0 ? '#f3e8ff' : '#fff' }">
          <td style="padding: 10px; border: 1px solid #ccc;">{{ usuario.nombre }}</td>
          <td style="padding: 10px; border: 1px solid #ccc;">{{ usuario.apellidos }}</td>
          <td style="padding: 10px; border: 1px solid #ccc;">{{ usuario.edad }}</td>
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
    };
  },
  mounted() {
    fetch("http://localhost:8000/api/usuarios/")
      .then(res => res.json())
      .then(data => {
        console.log("Datos recibidos:", data);
        this.usuarios = data;
      })
      .catch(err => console.error("Error al cargar usuarios:", err));
      }
};
</script>
