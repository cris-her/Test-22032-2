using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Configuration;

namespace WindowsService
{
    public partial class FormWinService : Form
    {
        #region 
        private System.Windows.Forms.Timer timer;
        #endregion
        public FormWinService()
        {
            InitializeComponent();
        }

        #region MetodosPrivados
        private void InicioServicio(object sender, EventArgs e)
        {
            try
            {
                timer = new System.Windows.Forms.Timer();
                timer.Interval = Convert.ToInt32(ConfigurationManager.AppSettings["intervaloEjecucion"]);
                timer.Enabled = true;
                this.timer.Tick += new EventHandler(EventoTemporizador)
            }
            catch 
            {
                throw;
            }
        }

        private void EventoTemporizador(object sender, EventArgs e)
        {
            try
            {

            }
            catch
            {

            }
        }
        #endregion
    }
}
