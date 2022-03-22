﻿using AutoMapper;
using System.Collections.Generic;
using University.BL.Models;

namespace University.BL.DTOs
{
    public class MapperConfig
    {
        public static MapperConfiguration MapperConfiguration()
        {
            return new MapperConfiguration(cfg =>
            {
                cfg.CreateMap<Course, CourseDTO>(); // GET
                cfg.CreateMap<CourseDTO, Course>(); // POST-PUT

                cfg.CreateMap<Student, StudentDTO>();
                cfg.CreateMap<StudentDTO, Student>();

                cfg.CreateMap<Enrollment, EnrollmentDTO>();
                cfg.CreateMap<EnrollmentDTO, Enrollment>();

                //cfg.CreateMap<List<Course>, List<CourseDTO>>(); // GET
                //cfg.CreateMap<List<CourseDTO>, List<Course>>(); // POST-PUT
            });
        }
    }
}
