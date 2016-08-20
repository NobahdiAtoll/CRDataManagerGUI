using System;
using System.Runtime.InteropServices;

namespace DataManagerGUI
{
    public class DragHelper
    {
        [DllImport("comctl32.dll")]
        public static extern bool InitCommonControls();

        [DllImport("comctl32.dll", CharSet = CharSet.Auto)]
        public static extern bool ImageList_BeginDrag(
            IntPtr himlTrack, // Handler of the image list containing the image to drag
            int iTrack,       // Index of the image to drag 
            int dxHotspot,    // x-delta between mouse position and drag image
            int dyHotspot     // y-delta between mouse position and drag image
        );
        /// <summary>
        /// 
        /// </summary>
        /// <param name="x">X-coordinate (relative to the form, not the treeview) at which to display the drag image.</param>
        /// <param name="y">Y-coordinate (relative to the form not the treeview) at which to display the drag image.</param>
        /// <returns></returns>
        [DllImport("comctl32.dll", CharSet = CharSet.Auto)]
        public static extern bool ImageList_DragMove(int x, int y);

        [DllImport("comctl32.dll", CharSet = CharSet.Auto)]
        public static extern void ImageList_EndDrag();

        /// <summary>
        /// 
        /// </summary>
        /// <param name="hwndLock">Handle to the control that owns the drag image.</param>
        /// <param name="x">X-coordinate (relative to the treeview) at which to display the drag image.</param>
        /// <param name="y">Y-coordinate (relative to the treeview) at which to display the drag image.</param>
        /// <returns></returns>
        [DllImport("comctl32.dll", CharSet = CharSet.Auto)]
        public static extern bool ImageList_DragEnter(IntPtr hwndLock, int x, int y);

        /// <summary>
        /// 
        /// </summary>
        /// <param name="hwndLock">Handle to the control that owns the drag image.</param>
        /// <returns></returns>
        [DllImport("comctl32.dll", CharSet = CharSet.Auto)]
        public static extern bool ImageList_DragLeave(IntPtr hwndLock);

        /// <summary>
        /// 
        /// </summary>
        /// <param name="fShow">False to hide, true to show the image</param>
        /// <returns></returns>
        [DllImport("comctl32.dll", CharSet = CharSet.Auto)]
        public static extern bool ImageList_DragShowNolock(bool fShow);

        static DragHelper()
        {
            InitCommonControls();
        }
    }
}
