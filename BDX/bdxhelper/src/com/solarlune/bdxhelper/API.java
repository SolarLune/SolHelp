package com.solarlune.bdxhelper;

/**
 * Created by SolarLune on 1/15/2015.
 */
public final class API {

    static public boolean atLeastBooleans(int reqNum, boolean... checks){

        int numGood = 0;

        for (boolean b : checks){

            if (b)
                numGood += 1;

        }

        return numGood >= reqNum;

    }

    static public boolean atLeastNotBooleans(int reqNum, boolean... checks){

        int numGood = 0;

        for (boolean b : checks){

            if (!b)
                numGood += 1;

        }

        return numGood >= reqNum;

    }

}
