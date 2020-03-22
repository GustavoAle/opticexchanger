#include <at89x52.h>
#include <stdio.h>

/** Macros de controle de envio e recepção*/
#define GET_IN(x) 	P2_0 = !(x) //Output enable (74hc595)
#define LOAD()		P2_1 = 0   //SH_LD em 0 (74hc165)
#define SHIFT()		P2_1 = 1   //SH_LD em 1 (74hc165)

char regLido;

int putchar (int c)
{
    //espera a serial estar disponivel
   while (!TI);

   TI = 0;
   SBUF = (char)c;
   return c;
}

int getchar (void)
{
    //espera a serial estar disponivel
   while (!RI);

   RI = 0;

   return SBUF;
}


/** Enviar pela fibra*/
void enviar(char _byte){
   // desabilita o output do 74hc595
   GET_IN(0);
   // coloca o byte na porta 1
   P1 = _byte; 
   LOAD(); //carrega no registrador 165
   SHIFT(); //envia
}

/** Recebe pela fibra*/
void interruptINT0(void) __interrupt(IE0_VECTOR){
   //habilita o output do 74hc595
   GET_IN(1);
   //obtem o byte na porta 1
   regLido = P1;
   GET_IN(0);
   //mostra no terminal tty a saida
   printf("Recebido: %c (%x)\r\n",regLido,regLido);
}

/** Interrupção da serial*/
void interruptSI0(void) __interrupt(SI0_VECTOR){
   if(TI && !RI){
      return;
   }else{
      RI = 0;
      //envia o que foi recebido pela serial
      enviar(SBUF | 0x80);
   }
}

void main(void)
{
    /** Inicia a Serial*/
    SCON  = 0xDA;        // SCON: 8n1
    TMOD |= 0x20;        
    TH1   = 0xFD;        // TH1:  1200 baud @ 12MHz
    TR1   = 1;           // TR1:  executa timer 1
    TI    = 1;           // TI:   habilita o timer*/

    char buf;

    /** Habilita as interrupcoes*/
    IT0 = 1; //int0 - externo
    EX0 = 1;
    EA = 1;
    ES = 1; //interrupcao serial


    printf("Transceiver Iniciado\r\n");

    regLido = 0;
    //envia byte de teste
    enviar(0x9B);

    // Write your code here
    while (1);
}
