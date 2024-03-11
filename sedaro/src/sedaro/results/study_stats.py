
import pandas as pd
import matplotlib.pyplot as plt

from functools import lru_cache
from .utils import ENGINE_MAP, stats, histogram, scatter_matrix, compare_sims


class StudyStats:

    def study_stats(self, module:str=None, filter_string=None):
        study_df = self.study_dataframe(module,filter_string )
        return stats(study_df)


    def study_histogram(self, module:str=None, filter_string=None, output_html= False):
    
        study_df = self.study_dataframe(module=module,filter_string=filter_string )
        histogram(study_df, output_html)

    def study_scatter_matrix(self, module:str=None,  filter_string=None, size=10):

        study_df = self.study_dataframe(module=module,filter_string=filter_string)
        scatter_matrix(study_df, size)


    def compare_sims(self,  sim_id_1, sim_id_2, module:str=None, filter_string=None, output_html=None, sim_id_1_label=None, sim_id_2_label=None):
        if not sim_id_1_label:
            sim_id_1_label = sim_id_1
        if not sim_id_2_label:
            sim_id_2_label = sim_id_2
        sim_1_df = self._simid_to_results[sim_id_1].create_pandas_dataframe(module, filter_string)
        sim_2_df = self._simid_to_results[sim_id_2].create_pandas_dataframe(module, filter_string)
        compare_sims(sim_1_df, sim_2_df, output_html, sim_id_1_label, sim_id_2_label)

    def study_dataframe(self, module:str=None, filter_string=None):
        dfs = []
        for (sim_id, results) in self._simid_to_results.items():
            sim_df = results.create_pandas_dataframe(module, filter_string)
            sim_df.columns = [f"{sim_id}_{col}" for col in sim_df.columns]
            dfs.append(sim_df)
        return pd.concat(dfs)
    
    def study_subplots(self,  size=10, cols=1, ylabel= "", module:str=None, filter_string=None):
        thisDF = self.study_dataframe(module=module,filter_string=filter_string)
        rows = len(thisDF.columns)
        rows = rows // cols if rows % cols == 0 else rows // cols + 1
        
        fig = plt.figure(figsize=(size, size))
        gs = fig.add_gridspec(rows, cols) 
        plots = gs.subplots(sharex=True, sharey=True)
        fig.suptitle(f'Study ID: {self._study_id} - {self.name}')
        for row in range(rows):
            for col in range(cols):
                index = row*cols+col
                if index >= len(thisDF.columns):
                    break
                sim_id = thisDF.columns[index]
                this_plot = plots[row,col] if rows > 1 and cols > 1 else plots[index]      
                sim_id = thisDF.columns[index]
                this_plot.set_title(f'{sim_id}')
                this_plot.set_xlabel('Time (s)')
                this_plot.set_ylabel(ylabel)
                this_plot.grid(True)   
                this_plot.plot( thisDF[ sim_id ].values, label=sim_id,linestyle='', marker='D', markersize=2 )

        for ax in plots.flat:
            ax.label_outer()
        plt.show()
    
    def study_summarize(self):
        print("📊 Display all agent block variables statistics with .study_stats( module, filter_string ) ")
        print("📊 Display all agent block variables histograms with .study_histogram( module, output_html=False, filter_string=None )")
        print("📈📉 Display block variables scatter matrix plot  ")
        print("📉📈      with .study_scatter_matrix( module, filter_string=None )")
        print("⎌  To compare two simulations use .compare_sims(sim_id_1, sim_id_2, module=None, filter_string=None, output_html, sim_id_1_label=None, sim_id_2_label=None)")
        print("Note: Agents 🛰️ and Blocks ⎕ should use module and filter_string to reduce the number of variables to analyse.")