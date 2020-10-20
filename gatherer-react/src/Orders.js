import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './component/Title';
import FormDialog from './component/dialogs/FormDialog';
import {from} from 'rxjs';
import {map} from 'rxjs/operators';
import axios, { AxiosPromise } from 'axios';


// Generate Order Data
function createData(id, date, name, shipTo, paymentMethod, amount) {
  return { id, date, name, shipTo, paymentMethod, amount };
}

const rows = [
  createData(0, '16 Mar, 2019', 'Elvis Presley', 'Tupelo, MS', 'VISA ⠀•••• 3719', 312.44),
  createData(1, '16 Mar, 2019', 'Paul McCartney', 'London, UK', 'VISA ⠀•••• 2574', 866.99),
  createData(2, '16 Mar, 2019', 'Tom Scholz', 'Boston, MA', 'MC ⠀•••• 1253', 100.81),
  createData(3, '16 Mar, 2019', 'Michael Jackson', 'Gary, IN', 'AMEX ⠀•••• 2000', 654.39),
  createData(4, '15 Mar, 2019', 'Bruce Springsteen', 'Long Branch, NJ', 'VISA ⠀•••• 5919', 212.79),
];

const dialogOkButtonText = "Add"
const dialogCancelButtonText = "Cancel"
const dialogContentText = "Please input a url to download a video."
const dialogInputLabel = "URL"

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
  absolute: {
    // position: 'left'
    // right: theme.spacing(3),
  },
}));


export default function Orders() {
  const classes = useStyles();

  const [openAddDialog, setOpenAddDialog] = React.useState(false);
  const [addText, setAddText] = React.useState("");

  const onInputChange = t => {
    console.log("onInputChange")
    console.log(t)
    setAddText(t)
  }

  const handleClickOpenAddDialog = () => {
    setOpenAddDialog(true);
  };

  const handleCloseAddDialog = () => {
    setOpenAddDialog(false);
  };

  const handleOk = () => {
    
    console.log("test handleOk1 " + addText); 
    const a = axios.get("https://httpbin.org/get");
    console.log("test handleOk2 " + a); 
    a.then((response) => {
      const user = response.data.data;
      console.log("aaaa" + response);
      console.log("bbbb" + response.data);
    });

    from(a).pipe(map(x => x.data)).subscribe(console.log)
  }

  return (
    <React.Fragment>
      <Title count={4} onAddButtonClick={handleClickOpenAddDialog}>Recent Orders</Title>
      <FormDialog
        open={openAddDialog}
        handleClose={handleCloseAddDialog}
        okButtonText={dialogOkButtonText}
        cancelButtonText={dialogCancelButtonText}
        contentText={dialogContentText}
        inputLabel={dialogInputLabel}
        onTextChange={onInputChange}
        handleOk={handleOk}></FormDialog>

      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Name</TableCell>
            <TableCell>Ship To</TableCell>
            <TableCell>Payment Method</TableCell>
            <TableCell align="right">Sale Amount</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.shipTo}</TableCell>
              <TableCell>{row.paymentMethod}</TableCell>
              <TableCell align="right">{row.amount}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <div className={classes.seeMore}>
        <Link color="primary" href="#" onClick={preventDefault}>
          See more orders
        </Link>
      </div>
    </React.Fragment>
  );
}