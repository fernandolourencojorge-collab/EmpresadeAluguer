using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EmpresadeAluguer
{
    public class veiculo
    {
      
        private string matricula;
        private string marca;
        private string modelo;
        private int anoFabricacao;
        private double quilometragem;

      
        public veiculo()
        {
            matricula = "";
            marca = "";
            modelo = "";
            anoFabricacao = 0;
            quilometragem = 0;
        }

        
        public veiculo(string matricula, string marca, string modelo, int anoFabricacao, double quilometragem)
        {
            this.matricula = matricula;
            this.marca = marca;
            this.modelo = modelo;
            this.anoFabricacao = anoFabricacao;
            this.quilometragem = quilometragem;
        }

        public string Matricula
        {
            get { return matricula; }
            set { matricula = value; }
        }

        public string Marca
        {
            get { return marca; }
            set { marca = value; }
        }

        public string Modelo
        {
            get { return modelo; }
            set { modelo = value; }
        }

        public int AnoFabricacao
        {
            get { return anoFabricacao; }
            set { anoFabricacao = value; }
        }

        public double Quilometragem
        {
            get { return quilometragem; }
            set { quilometragem = value; }
        }

        public void AtualizarQuilometragem(double kmPercorridos)
        {
            quilometragem += kmPercorridos;
        }

        public void ApresentarDados()
        {
            Console.WriteLine("Matrícula: " + matricula);
            Console.WriteLine("Marca: " + marca);
            Console.WriteLine("Modelo: " + modelo);
            Console.WriteLine("Ano de Fabricação: " + anoFabricacao);
            Console.WriteLine("Quilometragem: " + quilometragem + " km");
            Console.WriteLine("----------------------------");
        }
    }
}
    

