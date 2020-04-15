# ClimberingLadderSafe?

## from detecto import core, utils, visualize

   1. model = core.Model.load('mm.pth',['Ladder','Hand','Feet'])

   2. pred = model.predict(image) 
    
   ### image's shape should be (224,224,3)
    
   3. labels, boxes, scores = pred
  
   4. visualize.show_labeled_image(image, boxes, labels)
  
      or 
   
      visualize.detect_video(model, mp4, output)