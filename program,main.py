using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EmpresadeAluguer
{
    public class Program
    {
        static void Main(string[] args)
        {
            veiculo v1 = new veiculo("LD-122-ao", "Toyota", "starlet", 2023, 60000);
            veiculo v2 = new veiculo("LA-226-bg", "Hyundai", "i20", 2020, 40000);
            veiculo v3 = new veiculo("LU-339-cc", "Kia", "Sportage", 2024, 25000);

            Console.WriteLine("== DADOS INICIAIS ==");
            v1.ApresentarDados();
            v2.ApresentarDados();
            v3.ApresentarDados();


            Console.WriteLine("Atualizando quilometragem...\n");

            v1.AtualizarQuilometragem(200);
            v2.AtualizarQuilometragem(150);
            v3.AtualizarQuilometragem(300);

            Console.WriteLine("== DADOS ATUALIZADOS ==");
            v1.ApresentarDados();
            v2.ApresentarDados();
            v3.ApresentarDados();
        }
    }
}
        
    

