UART1_Println("ENVIO A PLATAFORMA");
        UART3_Print("1TC2,Madurador,");
        UART1_Print("1TC2,Madurador,ZGTU0015");
        sprintf(sms, ",%0.2f", fTempSP);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSupply1);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSupply2);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fReturn);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fEvaporator);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fCondenser);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fCompresor);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fCompresor2);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fAmbient);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fUsda1);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fUsda2);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fUsda3);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fCargo);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", iHumidity);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", iAvl);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuction);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fDischarge);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", iVoltage);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", iFrecuencia);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fCurrentph1);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fCurrentph2);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fCurrentph3);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fCo2);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fO2);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", iEvapFanSpeed);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", iCondenserFanSpeed);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fBatteryData);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fPowerMeterReading);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", iPowerMeterTrip);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", (int)fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", (int)fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", iPowerstate); //control mode
        UART3_Print(sms);
        
        sprintf(sms, ",%d", (int)fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", (int)fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", (int)fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%0.2f", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", fSuplyShow);
        UART3_Print(sms);
        
        sprintf(sms, ",%d", fSuplyShow);
        UART3_Print(sms);
        
        UART3_Print(",0.00");
         UART3_Print(",0.00");
        UART3_Print(",0.00");
        UART3_Print(",THERMOKING,0.00,0.00");
        sprintf(sms, ",%d,%d,%d", fSuplyShow, fSuplyShow, fSuplyShow);
        UART3_Print(sms);
        UART3_Write(0x1A);
        UART1_Println(" ");
        SIM_Wait = 10;
        SIM_CHECK_ERROR();