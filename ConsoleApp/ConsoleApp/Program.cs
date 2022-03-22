using ConsoleApp.Models;
using ConsoleApp.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using System.Data.SqlClient;
using System.Data;

namespace ConsoleApp
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("Obteniendo datos de la API ...");
            
            var url = "https://localhost:44360/";
            //var connection = await _apiService.CheckConnectionAsync(url);
            if (false) //!connection
            {
                //IsRunning = false;
                //await App.Current.MainPage.DisplayAlert("Error", "Check the internet connection.", "Accept");
                //return;
            }

            ApiService Api = new ApiService();

            TokenRequest request = new TokenRequest
            {
                Username = "crs",
                Password = "123456"
            };

            Response response = await Api.GetTokenAsync(url, "api", "/Account", request);
            
            if (!response.IsSuccess)
            {
                //IsRunning = false;
                //IsEnabled = true;
                //await App.Current.MainPage.DisplayAlert(Languages.Error, Languages.LoginError, Languages.Accept);
                //Password = string.Empty;
                //return;
            }

            string token = (string)response.Result; //(TokenResponse)

            Response response2 = await Api.GetDataAsync(url, "api", "/Courses", "Bearer", token);

            /*
            List<Course> coursesResponse = (List<Course>)response2.Result;

            foreach (var item in coursesResponse)
            {
                Console.WriteLine(item.Title);
            }*/
            DataTable dtResponse = (DataTable)response2.Result;

            Console.WriteLine("----------------");
            foreach (DataRow dataRow in dtResponse.Rows)
            {
                foreach (var item in dataRow.ItemArray)
                {
                    Console.WriteLine(item);
                }
                Console.WriteLine("----------------");
            }

            Console.WriteLine("Insertando registros en la base de datos ...");

            
            var connectionString = ConfigurationManager.ConnectionStrings["defaultConnection"].ConnectionString;

            //insert to db
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                using (SqlTransaction transaction = connection.BeginTransaction())
                {
                    using (SqlBulkCopy bulkCopy = new SqlBulkCopy(connection, SqlBulkCopyOptions.Default, transaction))
                    {
                        try
                        {
                            bulkCopy.DestinationTableName = "dbo.Course";
                            //bulkCopy.BulkCopyTimeout = 0; 'for big inserts or slow servers'
                            bulkCopy.WriteToServer(dtResponse);
                            transaction.Commit();
                            //inserted = true; 
                            Console.WriteLine("Los registros han sido insertados en la base de datos.");
                        }
                        catch (Exception e)
                        {
                            transaction.Rollback();
                            connection.Close();
                            Console.Write(e.Message);
                        }
                    }
                }
            }
            //return inserted...
            Console.WriteLine("Obteniendo registros de la base de datos ...");

            //var query = @"select * from dbo.NewCourse";

            DataTable dt = new DataTable();
            using (SqlConnection sql = new SqlConnection(connectionString))
            {
                using (SqlCommand cmd = new SqlCommand("sp_buscar_todos_los_datos", sql))
                {
                    cmd.CommandType = CommandType.StoredProcedure;//
                    SqlDataAdapter da = new SqlDataAdapter(cmd);
                    sql.Open();
                    da.Fill(dt);
                }
            }

            Console.WriteLine("----------------");
            foreach (DataRow dataRow in dt.Rows)
            {
                foreach (var item in dataRow.ItemArray)
                {
                    Console.WriteLine(item);
                }
                Console.WriteLine("----------------");
            }
            
            Console.WriteLine("Enviando datos a la API ...");

            //IsRunning = true;
            //IsEnabled = false;
            //string url = App.Current.Resources["UrlAPI"].ToString();
            //bool connection = await _apiService.CheckConnectionAsync(url);
            if (false )//!connection
            {
                //IsRunning = false;
                //IsEnabled = true;
                //await App.Current.MainPage.DisplayAlert(Languages.Error,Languages.ConnectionError,Languages.Accept);
                //return;
            }
            //UserResponse user = JsonConvert.DeserializeObject<UserResponse>(Settings.User);
            //TokenResponse token = JsonConvert.DeserializeObject<TokenResponse>(Settings.Token);

            /*TripRequest tripRequest = new TripRequest
            {
                Address = Source,
                Latitude = _geolocatorService.Latitude,
                Longitude = _geolocatorService.Longitude,
                Plaque = Plaque,
                UserId = new Guid(user.Id)
            };*/

            
            Response response3 = await Api.PostDataAsync(url, "/api", "/Courses", dt, "Bearer", token);
            if (!response.IsSuccess)
            {
                //IsRunning = false;
                //IsEnabled = true;
                //await App.Current.MainPage.DisplayAlert(Languages.Error,response.Message,Languages.Accept);
                //return;
            }
            
            List<Course> coursesResponse = (List<Course>)response3.Result;

            foreach (var item in coursesResponse)
            {
                Console.WriteLine($"{item.CourseID} {item.Title}");
            }


            //IsRunning = false;
            //IsEnabled = true;

            Console.WriteLine("Datos enviados.");
            Console.ReadLine();
        }
    }
}
