import React from 'react';
import Button from '@material-ui/core/Button';
import Icon from '@material-ui/core/Icon';

export default function AddButton(props) {

  return (
    <Button onClick={props.onClick} ><Icon color="primary">add_circle</Icon></Button>
  );
}
