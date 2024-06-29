using Microsoft.EntityFrameworkCore;
using ST.Hotel.Entities;
using System.Net.Sockets;
using Microsoft.Extensions.Configuration;
using System;
namespace ST.Hotel
{
    public class HotelDbContext : DbContext
    {
        private IConfiguration _configuration { get; }

        public DbSet<Room> Rooms { get; set; }

        public DbSet<Reservation> Reservations { get; set; }

       

        public HotelDbContext(IConfiguration configuration)
          : base()
        {
            _configuration = configuration;
        }

        protected override void OnConfiguring(DbContextOptionsBuilder options)
        {
            options.UseSqlServer(@"server = 10.200.2.28; Database = cinema-dev-w68264; User Id = stud; Password =wsiz; ",
                       //options.UseSqlServer(@"server=(localdb)\MSSQLLocalDB;database=cinema-dev1;trusted_connection=true;",
                       //  options.UseSqlServer("",
                       x => x.MigrationsHistoryTable("__EFMigrationsHistory", "Cinema"));
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
        }


    }
}
