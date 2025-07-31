class Lasagna
{
    // We assume the Expected Time is 40
    public int ExpectedMinutesInOven()
    {
        return 40;
    }

    // We take the elapsed time and subtract it from the expected time
    public int RemainingMinutesInOven(int minutes)
    {
        return ExpectedMinutesInOven() - minutes;
    }

    // We assume each layer of lasagna takes 2 minutes to prepare
    public int PreparationTimeInMinutes(int layers)
    {
        return layers * 2;
    }

    /* We calculate the total elapsed time by considering the time to prepare
    each layer and adding the time so far in the oven */
    public int ElapsedTimeInMinutes(int layers, int minutes)
    {
        return PreparationTimeInMinutes(layers) + minutes;
    }
}
