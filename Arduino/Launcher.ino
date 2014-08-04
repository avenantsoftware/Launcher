// htpc
byte htpc[] = {192,168,2,3};


void launch_htpc(char *prog)
{
  if (client.connect(htpc,4040))
  {
    client.print("GET /");
    client.print(prog);
    client.println();
    client.stop();
  }
  else
  {
    client.stop();
  }
}

// run these commands

launch_htpc("changebg");

launch_htpc("chrome");

launch_htpc("xbmc");

launch_htpc("taskmanager");

launch_htpc("router");

launch_htpc("terminal");

launch_htpc("gmail");

launch_htpc("nemo");

launch_htpc("wiki");

launch_htpc("imdb");

launch_htpc("youtube");

launch_htpc("killchrome");

launch_htpc("killxbmc");

launch_htpc("killtaskmanager");

launch_htpc("killterminal");

launch_htpc("killnemo");
