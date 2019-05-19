using System;
using System.Collections.Generic;
using System.Text;
using Sys = Cosmos.System;
using System.IO;

namespace SalmonKernel1
{
    public class Kernel : Sys.Kernel
    {
        protected override void BeforeRun()
        {
            Console.WriteLine("Salmon booted successfully. Version 0.1.0 Coho");

        }

        protected override void Run()
        {
            void setup()
            {
                var fs = new Sys.FileSystem.CosmosVFS();
                Sys.FileSystem.VFS.VFSManager.RegisterVFS(fs);
                //List<string> commands = new List<string>();
                //commands.Add("Help");
            }


            Console.Write("User@Salmon ^");
            var input = Console.ReadLine();
            switch (input)
            {
                case "help":
                    {
                        //Console.Write(commands);
                        Console.Write("Help, Shutdown, Reboot \n");
                        break;
                    }
            }
        }
    }
}
