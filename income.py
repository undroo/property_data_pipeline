from typing import Dict, List, Tuple
import numpy as np

class Income:
    def __init__(self, df):
        """Initialize Income class with a dataframe containing exactly one row of data.
        
        Args:
            df (pd.DataFrame): DataFrame containing census data
            
        Raises:
            ValueError: If DataFrame is empty or contains more than one row
        """
        if df.empty:
            raise ValueError("DataFrame is empty")
        if len(df) > 1:
            raise ValueError("DataFrame contains more than one row")
        
        self.df = df
        
        # Define income bands and their midpoints for calculations
        self.income_bands = {
            "650_799": (650, 799),
            "800_999": (800, 999),
            "1000_1249": (1000, 1249),
            "1250_1499": (1250, 1499),
            "1500_1749": (1500, 1749),
            "1750_1999": (1750, 1999),
            "2000_2999": (2000, 2999),
            "3000_3499": (3000, 3499),
            "3500_more": (3500, 5000)  # Assuming $5000 as upper bound for calculation purposes
        }
        
        # Define age bands
        self.age_bands = [
            "15_19", "20_24", "25_34", "35_44", "45_54",
            "55_64", "65_74", "75_84", "85ov"
        ]

    def _get_value(self, column: str) -> float:
        """Helper method to safely extract a single value from a column.
        
        Args:
            column (str): Column name to extract value from
            
        Returns:
            float: The numeric value from the specified column
        """
        return float(self.df[column].iloc[0])

    def get_income_by_age(self, age_band: str) -> Dict[str, float]:
        """Get income distribution for a specific age band.
        
        Args:
            age_band (str): Age band to get income distribution for (e.g., '15_19', '25_34')
            
        Returns:
            Dict[str, float]: Dictionary containing income distribution for the age band
                Keys are income ranges, values are counts
        """
        if age_band not in self.age_bands:
            raise ValueError(f"Invalid age band. Must be one of {self.age_bands}")
        
        distribution = {}
        for income_band in self.income_bands.keys():
            # For 85+ age group, use special format
            if age_band == "85ov":
                column = f"P_{income_band}_85ov"
            else:
                column = f"P_{income_band}_{age_band}_yrs"
            distribution[income_band] = self._get_value(column)
            
        # Add not stated income
        if age_band == "85ov":
            ns_column = "P_PI_NS_ns_85_yrs_ovr"
        else:
            ns_column = f"P_PI_NS_ns_{age_band}_yrs"
        distribution["not_stated"] = self._get_value(ns_column)
        
        return distribution

    def get_income_distribution(self) -> Dict[str, Dict[str, float]]:
        """Get complete income distribution across all age bands.
        
        Returns:
            Dict[str, Dict[str, float]]: Dictionary containing income distribution
                First level keys are age bands
                Second level keys are income ranges
                Values are counts
        """
        distribution = {}
        for age_band in self.age_bands:
            distribution[age_band] = self.get_income_by_age(age_band)
        return distribution

    def calculate_average_income(self, age_band: str = None) -> Tuple[float, float]:
        """Calculate weighted average weekly income for overall population or specific age band.
        
        Args:
            age_band (str, optional): Age band to calculate average for. If None, calculates for all ages.
            
        Returns:
            Tuple[float, float]: (average_income, total_stated_count)
                average_income: Weighted average weekly income
                total_stated_count: Total number of people with stated income
        """
        total_weighted_sum = 0
        total_stated_count = 0
        
        if age_band:
            distribution = {age_band: self.get_income_by_age(age_band)}
        else:
            distribution = self.get_income_distribution()
        
        for age, income_data in distribution.items():
            for income_band, count in income_data.items():
                if income_band != "not_stated":
                    band_range = self.income_bands[income_band]
                    midpoint = (band_range[0] + band_range[1]) / 2
                    total_weighted_sum += midpoint * count
                    total_stated_count += count
        
        if total_stated_count == 0:
            return 0, 0
            
        average_income = total_weighted_sum / total_stated_count
        return average_income, total_stated_count

    def get_income_percentiles(self) -> Dict[str, float]:
        """Calculate income distribution percentiles.
        
        Returns:
            Dict[str, float]: Dictionary containing income percentiles
                Keys: 'median', 'p25', 'p75', 'p90'
                Values: Weekly income values
        """
        # Collect all income data points
        all_incomes = []
        for age_band in self.age_bands:
            distribution = self.get_income_by_age(age_band)
            for income_band, count in distribution.items():
                if income_band != "not_stated":
                    band_range = self.income_bands[income_band]
                    midpoint = (band_range[0] + band_range[1]) / 2
                    # Add this income midpoint to the list count times
                    all_incomes.extend([midpoint] * int(count))
        
        if not all_incomes:
            return {
                'p25': 0,
                'median': 0,
                'p75': 0,
                'p90': 0
            }
        
        # Calculate percentiles
        all_incomes = np.array(all_incomes)
        return {
            'p25': np.percentile(all_incomes, 25),
            'median': np.percentile(all_incomes, 50),
            'p75': np.percentile(all_incomes, 75),
            'p90': np.percentile(all_incomes, 90)
        }

    def get_income_summary(self) -> Dict[str, float]:
        """Get a comprehensive summary of income statistics.
        
        Returns:
            Dict[str, float]: Dictionary containing various income statistics
                Keys:
                - average_income: Overall weighted average weekly income
                - total_stated: Total number of people with stated income
                - total_not_stated: Total number of people with unstated income
                - percentiles: Dictionary of income percentiles
        """
        average_income, total_stated = self.calculate_average_income()
        
        # Calculate total not stated
        total_not_stated = 0
        for age_band in self.age_bands:
            distribution = self.get_income_by_age(age_band)
            total_not_stated += distribution["not_stated"]
        
        return {
            "average_income": average_income,
            "total_stated": total_stated,
            "total_not_stated": total_not_stated,
            "percentiles": self.get_income_percentiles()
        }

    def get_age_band_summary(self, age_band: str) -> Dict[str, float]:
        """Get income summary for a specific age band.
        
        Args:
            age_band (str): Age band to get summary for
            
        Returns:
            Dict[str, float]: Dictionary containing income statistics for the age band
                Keys:
                - average_income: Weighted average weekly income for the age band
                - total_stated: Total number of people with stated income in the age band
                - distribution: Income distribution for the age band
        """
        average_income, total_stated = self.calculate_average_income(age_band)
        distribution = self.get_income_by_age(age_band)
        
        return {
            "average_income": average_income,
            "total_stated": total_stated,
            "distribution": distribution
        }