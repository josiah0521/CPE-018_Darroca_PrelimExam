     # -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:57:40 2023

@author: Josiah Darroca
"""

###1 NUMBER 1

### 3 NUMBER 1

import cv2
import filters

from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
                self.mode = 0
                self._windowManager = WindowManager('Cameo', self.onKeypress)
                self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
                
                # Contour Detection
                self._contour_filter = filters.ContourDetectionFilter(min_area=-1, color=(0, 255, 0), thickness=2)
                
                # Canny Edge detection
                self._canny_filter = filters.CannyEdgeDetectionFilter(lower_threshold=100, upper_threshold=200)

                # Circle Detection
                self._circle_detection_filter = filters.CircleDetectionFilter()

                # Create instances of your filter classes
                self._blur_filter = filters.BlurFilter()
                self._sharpen_filter = filters.SharpenFilter()
                self._edges_filter = filters.FindEdgesFilter()
                self._emboss_filter = filters.EmbossFilter()
                self._cross_process_filter = filters.BGRCrossProcessCurveFilter()

    def run(self):
            """Run the main loop."""
            self._windowManager.createWindow()
            while self._windowManager.isWindowCreated:
                self._captureManager.enterFrame()
                frame = self._captureManager.frame

                # Apply the selected filter based on self.mode
                if self.mode == 0:
                    pass # No filter
                elif self.mode == 1: # Blur Filter
                    self._blur_filter.apply(frame, frame)
                    
                elif self.mode == 2: # Sharpen Filter
                    self._sharpen_filter.apply(frame, frame)
                    
                elif self.mode == 3: # Edges Filter
                    self._edges_filter.apply(frame, frame)
                    
                elif self.mode == 4: # Emboss Filter
                    self._emboss_filter.apply(frame, frame)
                    
                elif self.mode == 5: # Apply the Cross Process filter
                    self._cross_process_filter.apply(frame, frame)
                    
                # Canny Edge Detection
                elif self.mode == 6: # Apply the Canny Edge Detection filter
                    self._canny_filter.apply(frame, frame)
                    
                # Contour Detection
                elif self.mode == 7: # Apply the Contour Detection filter
                    self._contour_filter.apply(frame, frame)

                # Circle Detection
                elif self.mode == 8: # apply Circle Detection filter
                    self._circle_detection_filter.apply(frame, frame)

                self._captureManager.exitFrame()
                self._windowManager.processEvents()

    def onKeypress (self, keycode):
            """Handle a keypress.
            space> Take a screenshot.
            tab -> Start/stop recording a
            screencast. escape -> Quit."""

            if keycode == 32: # space
                self._captureManager.writeImage('screenshot.png')
            elif keycode == 9: # tab
                if not self._captureManager.isWritingVideo:
                    self._captureManager.startWritingVideo(
                        'screencast.avi')
                
                else:
                    self._captureManager.stopWritingVideo()
            elif keycode == 27: # escape
                self._windowManager.destroyWindow()

            elif keycode == 117: # u
                self.mode = 0

            elif keycode == 118: # v
                self.mode = 1

            elif keycode == 119: # w
                self.mode = 2

            elif keycode == 120: # x
                self.mode = 3

            elif keycode == 121: # y
                self.mode = 4

            elif keycode == 122: # z
                self.mode = 5

            elif keycode == 97: # a
                self.mode = 6
            
            elif keycode == 98: # b
                self.mode = 7
            
            elif keycode == 99: # c
                self.mode = 8




if __name__=="__main__":
    Cameo().run()