using System.Collections.Generic;
using System.Threading.Tasks;

namespace University.BL.Repositories
{
    public interface IGenericRepository<TEntity> where TEntity : class
    {
        Task<IEnumerable<TEntity>> GetAll();
        Task<TEntity> GetById(int id);
        Task<List<TEntity>> Insert(List<TEntity> entity);
        Task<TEntity> Update(TEntity entity);
        Task Delete(int id);
    }
}
