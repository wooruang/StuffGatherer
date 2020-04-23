import React from 'react';
import Button from '@material-ui/core/Button';
import Icon from '@material-ui/core/Icon';

interface AddButtonProps {
    onClick: (event: React.MouseEvent<HTMLButtonElement>) => void
}

const AddButton: React.SFC<AddButtonProps> = (props) => {
  return (
    <Button onClick={props.onClick} ><Icon color="primary">add_circle</Icon></Button>
  );
}

export default AddButton;
