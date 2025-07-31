public class Player
{
    public int RollDie() {
        var die = new Random();
        return die.Next(1, 19);
    }

    public double GenerateSpellStrength()
    {
        var spellstrength = new Random();
        return (Double)spellstrength.Next(100);
    }
}
