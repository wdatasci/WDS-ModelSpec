#pragma once

//The WDSMatrix class is either an overload of armadillo, or a custom c++ class which will be based on the classic Stroustrup class.
//Armadillo is an Apache licensed package, which at its core has all of the core elements of the Stroustrup class and significant wrapping of BLAS and LAPACK routines.
//
//The core matrix classes are extended here, primarily to add syntactical sugar so that hard chunks of code are interchangeable between C++, C#, Java, and potentially others.

#include <armadillo>
using namespace std;

namespace WDS::Comp::Matrix {

	
	//WDS Note: CJW - the local armadillo distribution on windows contains customizations for MKL BLAS and LAPACK libraries.
	using namespace arma;


	//for C++ overloading to get syntactical sugar for A[i,j]
	//we need a class version of an index
	typedef ptrdiff_t _mI;
	struct mIndex  { 
		_mI value;
		mIndex(_mI arg0) :value(arg0) {}
		mIndex(size_t arg0) :value((_mI) arg0) {}
		mIndex(int arg0) :value((_mI) arg0) {}
		mIndex(long arg0) :value((_mI) arg0) {}

		_mI operator=(mIndex& arg0) { return arg0.value; }
		mIndex operator=(_mI& arg0) { value = arg0; return *this; }
		mIndex operator=(size_t arg0) { value = (_mI)arg0; return *this; }
		mIndex operator=(int arg0) { value = (_mI)arg0; return *this; }
		mIndex operator=(long arg0) { value = (_mI) arg0; return *this; }

		bool operator<(size_t arg0) { return (value < (_mI)arg0); }
		bool operator<=(size_t arg0) { return (value <= (_mI)arg0); }
		bool operator>(size_t arg0) { return (value > (_mI)arg0); }
		bool operator>=(size_t arg0) { return (value >= (_mI)arg0); }
		bool operator==(size_t arg0) { return (value == (_mI)arg0); }

		bool operator<(int arg0) { return (value < (_mI)arg0); }
		bool operator<=(int arg0) { return (value <= (_mI)arg0); }
		bool operator>(int arg0) { return (value > (_mI)arg0); }
		bool operator>=(int arg0) { return (value >= (_mI)arg0); }
		bool operator==(int arg0) { return (value == (_mI)arg0); }

		bool operator<(long value) { return (this->value < (ptrdiff_t)value); }
		bool operator<=(long value) { return (this->value <= (ptrdiff_t)value); }
		bool operator>(long value) { return (this->value > (ptrdiff_t)value); }
		bool operator>=(long value) { return (this->value >= (ptrdiff_t)value); }
		bool operator==(long value) { return (this->value == (ptrdiff_t)value); }

		//conversion
		int as_int() { return (int)value; }
		int as_size_t() { return (size_t)value; }
		int ast() { return (size_t)value; }
		operator size_t() { return (size_t) value; }
		operator int() { return (int) value; }
		operator long() { return (long) value; }
		operator float() { return (float) value; }
		operator double() { return (double) value; }

		//prefix
		_mI &operator++() { this->value++; return this->value; }
		//postfix
		_mI operator++(int value) { _mI rv = value; this->value++; return rv; }

		~mIndex() {};
	};

	struct mDoubleIndexA {
		_mI i;
		_mI j;
		mDoubleIndexA(_mI arg0, _mI arg1) { i = arg0; j = arg1; }
		mDoubleIndexA(mIndex arg0, _mI arg1) { i = arg0.value; j = arg1; }
		mDoubleIndexA(_mI arg0, mIndex arg1) { i = arg0; j = arg1.value; }
		mDoubleIndexA(mIndex arg0, mIndex arg1) { i = arg0.value; j = arg1.value; }
	};

	class mDoubleIndex {
		public:
		_mI i;
		_mI j;
		mDoubleIndex(_mI arg0, _mI arg1) { i = arg0; j = arg1; }
		mDoubleIndex(mIndex arg0, _mI arg1) { i = arg0.value; j = arg1; }
		mDoubleIndex(_mI arg0, mIndex arg1) { i = arg0; j = arg1.value; }
		mDoubleIndex(mIndex arg0, mIndex arg1) { i = arg0.value; j = arg1.value; }
		~mDoubleIndex() {};
	};

	inline mDoubleIndex &operator,(mIndex arg0, mIndex arg1) { mDoubleIndex rv(arg0, arg1); return rv; }
	inline mDoubleIndex &operator,(mIndex arg0, _mI arg1) { mDoubleIndex rv(arg0, arg1); return rv; }
	inline mDoubleIndex &operator,(_mI arg0, mIndex arg1) { mDoubleIndex rv(arg0, arg1); return rv;}
	
	typedef vec dColVector;
	typedef rowvec dRowVector;

	//WDS Note: CJW - This is a template decorator pattern and the simplest way I could find to add 
	//a few methods and the [i,j] accessing to an existing matrix class while exposing all of the 
	//underlying methods of the parent class without having to add "using" lines for every one.
	//There are multiple on-line references for "decorators", but most of them are just class inheritance.
	//This template technique seems to keep it simple enough.

	template <class T,class U> struct _MatrixDecorator : public T {

		using T::Mat;
		using T::Mat::submat;
		//using T::Mat::operator*;
		//using T::Mat::operator-;
		//using T::Mat::operator+;
		//using T::Mat::operator/;
		//using T::Mat::operator%;
		//using T::Mat::operator=;
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
		
		U &operator[](mDoubleIndex arg0) { return (*this)(arg0.i, arg0.j); }
		U &operator[](mIndex arg0) { return (*this)(arg0.value); }

		size_t nrows() { return (size_t) ((T*) this)->n_rows; }
		size_t ncols() { return (size_t) ((T*) this)->n_cols; }

		static _MatrixDecorator<T,U> eye(int arg0, int arg1) { return arma::eye<T>(arg0, arg1); }
		static _MatrixDecorator<T,U> zeros(int arg0, int arg1) { return arma::zeros<T>(arg0, arg1); }

	};

	typedef _MatrixDecorator<mat,double> dMatrix;
	typedef _MatrixDecorator<imat,s64> iMatrix;


	inline dMatrix operator*(dMatrix& A, dMatrix& B) {
		dMatrix oResult = A;
		oResult *= B;
		return oResult;
	}


	inline dMatrix operator+(dMatrix& A, dMatrix& B) {
		dMatrix oResult = A;
		oResult += B;
		return oResult;
	}

	template <class T> struct _FieldDecorator : public T {

		using T::field;
		using T::field::operator=;
		using T::field::operator%=;
		using T::field::operator();
		using T::field::operator*=;
		using T::field::operator++;
		using T::field::operator+=;
		using T::field::operator--;
		using T::field::operator-=;
		using T::field::operator/=;
		using T::field::operator<<;
		using T::field::operator[];
		
		double &operator[](mDoubleIndex arg0) { return (*this)(arg0.i, arg0.j); }
		double &operator[](mIndex arg0) { return (*this)(arg0.value); }

		size_t nrows() { return (size_t) ((T*) this)->n_rows; }
		size_t ncols() { return (size_t) ((T*) this)->n_cols; }

	};

    // matrix-like objects for strings or wstrings
	typedef _FieldDecorator<field<string>> sMatrix;
	typedef _FieldDecorator<field<wstring>> wMatrix;
	
    // "cMatrix" is short for something like XLW's CellMatrix, which can effectively be 
    // a matrix of variants. Here, it is an armadillo field of std::variant's for a
    // double, wstring, or status.

    class cMatrix_cell {
        private:
			enum cMatrix_type {
				cMatrix_typeError = -1
				, cMatrix_typeEmpty = 0
				, cMatrix_typeNum = 1
				, cMatrix_typeStr = 2
			};
            cMatrix_type cmtype;
            double ddata;
            wstring wdata;

        public:
            cMatrix_cell() {
                this->cmtype=cMatrix_typeEmpty;
                this->ddata=0.0;
                this->wdata=L"";
            }
            cMatrix_cell(double arg){
                this->cmtype=cMatrix_typeNum;
                this->ddata=arg;
                this->wdata=L"";
            }
            cMatrix_cell(wstring arg){
                this->cmtype=cMatrix_typeStr;
                this->ddata=0.0;
                this->wdata=arg;
            }
            cMatrix_cell(int arg){
                this->cmtype=(cMatrix_type)arg;
                this->ddata=0.0;
                this->wdata=arg;
            }


			~cMatrix_cell() {}
	};

	/* not ready for prime-time
    class cMatrix : public field<cMatrix_cell> {
        public:
            //exposing inherited stuff
            using field<cMatrix_cell>;
            //without the "using" line above, constructors would have to be replicated:
            //dMatrix(size_t nrows, size_t ncols) : arma::mat(nrows, ncols) { this->zeros();  };
            //dMatrix(const dMatrix& arg0) : arma::mat(arg0) {};

            using field<cMatrix_type,double,std::wstring>::Mat::operator%=;
            using field<cMatrix_type,double,std::wstring>::Mat::operator();
            using field<cMatrix_type,double,std::wstring>::Mat::operator*=;
            using field<cMatrix_type,double,std::wstring>::Mat::operator++;
            using field<cMatrix_type,double,std::wstring>::Mat::operator+=;
            using field<cMatrix_type,double,std::wstring>::Mat::operator--;
            using field<cMatrix_type,double,std::wstring>::Mat::operator-=;
            using field<cMatrix_type,double,std::wstring>::Mat::operator/=;
            using field<cMatrix_type,double,std::wstring>::Mat::operator<<;
            using field<cMatrix_type,double,std::wstring>::Mat::operator=;
            using field<cMatrix_type,double,std::wstring>::Mat::operator[];


            double &operator[](mDoubleIndex arg0) { return (*this)(arg0.i, arg0.j); }
            double &operator[](mIndex arg0) { return (*this)(arg0.value); }

            size_t nrows() { return (size_t) ((mat*) this)->n_rows; }
            size_t ncols() { return (size_t) ((mat*) this)->n_cols; }

            ~cMatrix(){};
    };
	*/


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

	dMatrix RowNorm(dMatrix& Input);
	void RowNormInPlace(dMatrix& Input);

}
