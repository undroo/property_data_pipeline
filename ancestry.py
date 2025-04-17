from typing import Dict, List

ancestry_prefix_list = [
    "Aust_",
    "Aust_Abor_",
    "Chinese_",
    "Croatian_",
    "Dutch_",
    "English_",
    "Filipino_",
    "French_",
    "German_",
    "Greek_",
    "Hungarian_",
    "Indian_",
    "Irish_",
    "Italian_",
    "Korean_",
    "Lebanese_",
    "Maltese_",
    "Maori_",
    "Macedonian_",
    "NZ_",
    "Other_",
    "Polish_",
    "Russian_",
    "Samoan_",
    "Scottish_",
    "Serbian_",
    "Sth_African_",
    "Spanish_",
    "Sri_Lankan_",
    "Vietnamese_",
    "Welsh_",
    "Other_",
]

class Ancestry:
    def __init__(self, df):
        """Initialize Ancestry class with a dataframe containing exactly one row of data.
        
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

    def _get_value(self, column: str) -> float:
        """Helper method to safely extract a single value from a column.
        
        Args:
            column (str): Column name to extract value from
            
        Returns:
            float: The numeric value from the specified column
        """
        return float(self.df[column].iloc[0])

    def get_ancestry_summary(self, ancestry: str) -> Dict[str, float]:
        """Get a summary of birthplace statistics for a specific ancestry.
        
        Args:
            ancestry (str): The ancestry to get statistics for (e.g., 'Chinese', 'Italian', etc.)
            
        Returns:
            Dict[str, float]: Dictionary containing birthplace statistics for the specified ancestry
                Keys:
                - both_overseas: Both parents born overseas
                - father_overseas: Father only born overseas
                - mother_overseas: Mother only born overseas
                - both_australia: Both parents born in Australia
                - not_stated: Parents' birthplace not stated
                - total: Total responses for this ancestry
        """
        prefix = f"{ancestry}_"
        if ancestry == "New Zealand":
            prefix = "NZ_"
        elif ancestry == "South African":
            prefix = "Sth_African_"
        
        return {
            "both_overseas": self._get_value(f"{prefix}BP_B_OS"),
            "father_overseas": self._get_value(f"{prefix}FO_B_OS"),
            "mother_overseas": self._get_value(f"{prefix}MO_B_OS"),
            "both_australia": self._get_value(f"{prefix}BP_B_Aus"),
            "not_stated": self._get_value(f"{prefix}BP_NS"),
            "total": self._get_value(f"{prefix}Tot_resp")
        }

    def get_total_population_summary(self) -> Dict[str, float]:
        """Get a summary of birthplace statistics for the total population.
        
        Returns:
            Dict[str, float]: Dictionary containing birthplace statistics for the total population
                Keys:
                - both_overseas: Both parents born overseas
                - father_overseas: Father only born overseas
                - mother_overseas: Mother only born overseas
                - both_australia: Both parents born in Australia
                - not_stated: Parents' birthplace not stated
                - total: Total responses
        """
        return {
            "both_overseas": self._get_value("Tot_P_BP_B_OS"),
            "father_overseas": self._get_value("Tot_P_FO_B_OS"),
            "mother_overseas": self._get_value("Tot_P_MO_B_OS"),
            "both_australia": self._get_value("Tot_P_BP_B_Aus"),
            "not_stated": self._get_value("Tot_P_BP_NS"),
            "total": self._get_value("Tot_P_Tot_resp")
        }

    def get_australian_summary(self) -> Dict[str, Dict[str, float]]:
        """Get a summary of birthplace statistics for both general Australian and Aboriginal Australian ancestries.
        
        Returns:
            Dict[str, Dict[str, float]]: Dictionary containing birthplace statistics for both Australian categories
                Keys:
                - general: Statistics for general Australian ancestry
                - aboriginal: Statistics for Aboriginal Australian ancestry
                Each sub-dictionary contains:
                - both_overseas: Both parents born overseas
                - father_overseas: Father only born overseas
                - mother_overseas: Mother only born overseas
                - both_australia: Both parents born in Australia
                - not_stated: Parents' birthplace not stated
                - total: Total responses
        """
        general = {
            "both_overseas": self._get_value("Aust_BP_B_OS"),
            "father_overseas": self._get_value("Aust_FO_B_OS"),
            "mother_overseas": self._get_value("Aust_MO_B_OS"),
            "both_australia": self._get_value("Aust_Both_parents_born_Aust"),
            "not_stated": self._get_value("Aust_Birthplace_not_stated"),
            "total": self._get_value("Aust_Tot_resp")
        }
        
        aboriginal = {
            "both_overseas": self._get_value("Aust_Abor_BP_B_OS"),
            "father_overseas": self._get_value("Aust_Abor_FO_B_OS"),
            "mother_overseas": self._get_value("Aust_Abor_MO_B_OS"),
            "both_australia": self._get_value("Aust_Abor_BP_B_Aus"),
            "not_stated": self._get_value("Aust_Abor_BP_NS"),
            "total": self._get_value("Aust_Abor_Tot_resp")
        }
        
        return {
            "general": general,
            "aboriginal": aboriginal
        }

    def get_not_stated_summary(self) -> Dict[str, float]:
        """Get a summary of birthplace statistics for cases where ancestry is not stated.
        
        Returns:
            Dict[str, float]: Dictionary containing birthplace statistics for not stated ancestry
                Keys:
                - both_overseas: Both parents born overseas
                - father_overseas: Father only born overseas
                - mother_overseas: Mother only born overseas
                - both_australia: Both parents born in Australia
                - not_stated: Parents' birthplace not stated
                - total: Total responses
        """
        return {
            "both_overseas": self._get_value("Ancestry_NS_BP_B_OS"),
            "father_overseas": self._get_value("Ancestry_NS_FO_B_OS"),
            "mother_overseas": self._get_value("Ancestry_NS_MO_B_OS"),
            "both_australia": self._get_value("Ancestry_NS_BP_B_Aus"),
            "not_stated": self._get_value("Ancestry_NS_BP_NS"),
            "total": self._get_value("Ancestry_NS_Tot_resp")
        }

    def get_other_ancestry_summary(self) -> Dict[str, float]:
        """Get a summary of birthplace statistics for other ancestries not specifically categorized.
        
        Returns:
            Dict[str, float]: Dictionary containing birthplace statistics for other ancestries
                Keys:
                - both_overseas: Both parents born overseas
                - father_overseas: Father only born overseas
                - mother_overseas: Mother only born overseas
                - both_australia: Both parents born in Australia
                - not_stated: Parents' birthplace not stated
                - total: Total responses
        """
        return {
            "both_overseas": self._get_value("Other_BP_B_OS"),
            "father_overseas": self._get_value("Other_FO_B_OS"),
            "mother_overseas": self._get_value("Other_MO_B_OS"),
            "both_australia": self._get_value("Other_BP_B_Aus"),
            "not_stated": self._get_value("Other_BP_NS"),
            "total": self._get_value("Other_Tot_resp")
        }

    def get_ancestry_ranking(self) -> Dict[str, float]:
        """Get a dictionary of total population for each ancestry, sorted from highest to lowest.
        
        Returns:
            Dict[str, float]: Dictionary containing total population for each ancestry,
                sorted from highest to lowest population.
        """
        ancestry_totals = {}
        
        for prefix in ancestry_prefix_list:
            # Clean up the prefix name for display
            display_name = prefix.replace('_', ' ').strip()
            if display_name.endswith(' '):
                display_name = display_name[:-1]
            
            # Get the total responses for this ancestry
            try:
                total = self._get_value(f"{prefix}Tot_resp")
                if total > 0:  # Only include ancestries with responses
                    ancestry_totals[display_name] = total
            except:
                continue
        
        # Sort the dictionary by values (population) in descending order
        sorted_ancestry = dict(sorted(ancestry_totals.items(), 
                                    key=lambda item: item[1], 
                                    reverse=True))
        
        return sorted_ancestry

    def get_available_ancestries(self) -> List[str]:
        """Get a list of all available specific ancestries that can be queried.
        
        Returns:
            List[str]: List of ancestry names that can be used with get_ancestry_summary()
        """
        return [
            "Chinese", "Croatian", "Dutch", "English", "Filipino",
            "French", "German", "Greek", "Hungarian", "Indian",
            "Irish", "Italian", "Korean", "Lebanese", "Macedonian",
            "Maltese", "Maori", "New Zealand", "Polish", "Russian",
            "Samoan", "Scottish", "Serbian", "South African", "Spanish",
            "Sri Lankan", "Vietnamese", "Welsh"
        ]

    def calculate_percentage(self, value: float, total: float) -> float:
        """Calculate percentage, handling division by zero.
        
        Args:
            value (float): The value to calculate percentage for
            total (float): The total value to divide by
            
        Returns:
            float: The calculated percentage, or 0 if total is 0
        """
        return (value / total * 100) if total != 0 else 0

    def get_ancestry_percentages(self, ancestry: str) -> Dict[str, float]:
        """Get percentages for each birthplace category for a specific ancestry.
        
        Args:
            ancestry (str): The ancestry to get percentages for
            
        Returns:
            Dict[str, float]: Dictionary containing percentage statistics
                Keys are the same as get_ancestry_summary() but values are percentages
        """
        summary = self.get_ancestry_summary(ancestry)
        total = summary["total"]
        
        return {
            key: self.calculate_percentage(value, total)
            for key, value in summary.items()
            if key != "total"
        }

    def plot_top_ancestries_horizontal(self, title="Top 10 Ancestries Distribution"):
        """Create a stacked horizontal bar chart of the top 10 ancestries (with others combined) using Plotly.
        
        Args:
            title (str, optional): Title for the plot. Defaults to "Top 10 Ancestries Distribution".
            
        Returns:
            plotly.graph_objects.Figure: Interactive Plotly figure object
        """
        import plotly.graph_objects as go
        
        # Get ancestry rankings and calculate total population
        rankings = self.get_ancestry_ranking()
        total_population = sum(rankings.values())
        
        # Get top 5 ancestries and their percentages
        top_n_items = list(rankings.items())[:10]
        other_value = sum(list(rankings.values())[10:])
        
        # Calculate percentages
        percentages = [value / total_population * 100 for _, value in top_n_items]
        other_percentage = other_value / total_population * 100
        
        # Prepare data for plotting
        labels = [name for name, _ in top_n_items] + ['All other']
        values = percentages + [other_percentage]
        
        # Create color palette
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC', '#A0A0A0', '#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC']
        
        # Create the stacked horizontal bar
        fig = go.Figure()
        
        # Add bars in sequence to create stacked effect
        for i, (value, label, color) in enumerate(zip(values, labels, colors)):
            fig.add_trace(go.Bar(
                name=f'{label} ({value:.1f}%)',
                y=['Ancestry Distribution'],
                x=[value],
                orientation='h',
                marker_color=color,
                text=f'{label}: {value:.1f}%',
                textposition='auto',
                hovertemplate=f'{label}<br>Percentage: {value:.1f}%<extra></extra>'
            ))
        
        # Update layout for stacked bars and styling
        fig.update_layout(
            barmode='stack',
            title=dict(
                text=title,
                x=0.5,
                xanchor='center'
            ),
            showlegend=True,
            xaxis_title="Percentage (%)",
            xaxis=dict(range=[0, 100]),
            yaxis=dict(showticklabels=False),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(l=20, r=20, t=120, b=20),
            height=300
        )
        
        return fig