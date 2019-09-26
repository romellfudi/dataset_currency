#%%
import pre_binarize
import pre_blurring
import pre_corners
import pre_edges
import pre_enhance_contrast_gray
import pre_enhance_contrast
import pre_isolate_colors
import pre_kernel
import pre_remove_background
import pre_shi_tomasi_corner

#%%
if __name__ == '__main__':
    print ('Start preprocessing...')
    [f.main() for f in [pre_binarize,pre_blurring,corners, \
        pre_edges,pre_enhance_contrast,pre_enhance_contrast_gray, \
            pre_isolate_colors, pre_kernel, pre_remove_background,
             pre_shi_tomasi_corner]]

    print ('Has already finished preprocessing!!!')


    

#%%
