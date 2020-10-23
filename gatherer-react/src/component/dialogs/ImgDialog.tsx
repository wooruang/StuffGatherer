import React from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';


 interface ImgDialogProps {
   open: boolean,
   source: string,
   fileName: string,
   handleClose: () => void
 }

const ImgDialog: React.FC<ImgDialogProps> = (props) => {

  return (
      <Dialog open={props.open} onClose={props.handleClose} aria-labelledby="form-dialog-title">
        <DialogTitle id="form-dialog-title">Subscribe</DialogTitle>
        <DialogContent>
          <img src={props.source} alt={props.fileName}/>
        </DialogContent>
      </Dialog>
  );
}

export default ImgDialog;
