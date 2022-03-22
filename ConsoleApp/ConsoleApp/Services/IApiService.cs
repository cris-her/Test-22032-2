using ConsoleApp.Models;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp.Services
{
    public interface IApiService
    {
        Task<Response> GetDataAsync(string urlBase, string servicePrefix, string controller, string tokenType, string accessToken);
        Task<Response> GetTokenAsync(string urlBase, string servicePrefix, string controller, TokenRequest request);
        Task<Response> PostDataAsync(string urlBase, string servicePrefix, string controller, DataTable model, string tokenType, string accessToken);

    }
}
