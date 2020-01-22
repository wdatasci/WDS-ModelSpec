#pragma once

// The WDS::Comp::MatrixXLL class extends WDS::Comp::Matrix with a few xll12 methods.
// See WDS::Comp::Matrix for further details.


// This class is specific to windows Excel XLLs using xll12.
//
#include "WDS\Comp\Matrix.h"

#include "windows.h"
#include "AddIn-xll12.h"
#include "xlcall.h"

namespace WDS::Comp::Matrix {

	
	using namespace arma;

	template <class T> struct _MatrixXLLDecorator : public T {

		using T::Mat;
		using T::Mat::operator=;
		using T::Mat::operator%=;
		using T::Mat::operator();
		using T::Mat::operator*=;
		using T::Mat::operator++;
		using T::Mat::operator+=;
		using T::Mat::operator--;
		using T::Mat::operator-=;
		using T::Mat::operator/=;
		using T::Mat::operator<<;
		using T::Mat::operator[];
		
		double &operator[](mDoubleIndex arg0) { return (*this)(arg0.i, arg0.j); }
		double &operator[](mIndex arg0) { return (*this)(arg0.value); }

		size_t nrows() { return (size_t) ((T*) this)->n_rows; }
		size_t ncols() { return (size_t) ((T*) this)->n_cols; }

		static _MatrixDecorator<T> eye(int arg0, int arg1) { return arma::eye<mat>(arg0, arg1); }
		static _MatrixDecorator<T> zeros(int arg0, int arg1) { return arma::zeros<mat>(arg0, arg1); }

	};

	typedef _MatrixXLLDecorator<mat> dMatrixXLL;
	typedef _MatrixXLLDecorator<imat> iMatrixXLL;

	class dMatrixAlt : public mat {
	public:
		//exposing inherited stuff
		using mat::Mat;
		//without the "using" line above, constructors would have to be replicated:
		//dMatrix(size_t nrows, size_t ncols) : arma::mat(nrows, ncols) { this->zeros();  };
		//dMatrix(const dMatrix& arg0) : arma::mat(arg0) {};

		using mat::Mat::operator%=;
		using mat::Mat::operator();
		using mat::Mat::operator*=;
		using mat::Mat::operator++;
		using mat::Mat::operator+=;
		using mat::Mat::operator--;
		using mat::Mat::operator-=;
		using mat::Mat::operator/=;
		using mat::Mat::operator<<;
		using mat::Mat::operator=;
		using mat::Mat::operator[];
		/*
		using mat::Mat::clear;
		using mat::Mat::diag;
		using mat::Mat::empty;
		using mat::Mat::has_inf;
		using mat::Mat::has_nan;
		using mat::Mat::is_col;
		using mat::Mat::is_colvec;
		using mat::Mat::is_empty;
		using mat::Mat::is_finite;
		using mat::Mat::is_row;
		using mat::Mat::is_rowvec;
		using mat::Mat::is_sorted;
		using mat::Mat::is_square;
		using mat::Mat::is_symmetric;
		using mat::Mat::is_vec;
		using mat::Mat::load;
		using mat::Mat::fill;
		using mat::Mat::min;
		using mat::Mat::max;
		using mat::Mat::n_cols;
		using mat::Mat::n_elem;
		using mat::Mat::n_rows;
		using mat::Mat::randn;
		using mat::Mat::randu;
		using mat::Mat::row;
		using mat::Mat::rows;
		using mat::Mat::save;
		using mat::Mat::size;
		using mat::Mat::transform;
		using mat::Mat::vec_state;
		using mat::Mat::zeros;
		*/

		
		double &operator[](mDoubleIndex arg0) { return (*this)(arg0.i, arg0.j); }
		double &operator[](mIndex arg0) { return (*this)(arg0.value); }

		size_t nrows() { return (size_t) ((mat*) this)->n_rows; }
		size_t ncols() { return (size_t) ((mat*) this)->n_cols; }

		~dMatrixAlt(){};
	};


}
