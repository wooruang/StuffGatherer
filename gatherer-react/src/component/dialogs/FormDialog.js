import React from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';



/**
 * 
 * * props.
 * - open 
 * - handleClose
 * - contentText
 * - inputLbael
 * - okButtonText
 * - cancelButtonText
 * - onTextChange
 * - handleOk
 * 
 */
export default function FormDialog(props) {

  const onInputChange = e => {
    props.onTextChange(e.target.value);
  }

  return (
      <Dialog open={props.open} onClose={props.handleClose} aria-labelledby="form-dialog-title">
        <DialogTitle id="form-dialog-title">Subscribe</DialogTitle>
        <DialogContent>
          <DialogContentText>
            {props.contentText}
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            id="name"
            label={props.inputLabel}
            onChange={onInputChange}
            fullWidth
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={props.handleClose} color="primary">
            {props.cancelButtonText}
          </Button>
          <Button onClick={props.handleOk} color="primary">
            {props.okButtonText}
          </Button>
        </DialogActions>
      </Dialog>
  );
}