This repository provides a Python generator for the supply chain benchmark described in [Modelling and Analysis of Supply Chains using Product Time Petri Nets].


# SupplyChain

SupplyChain is a repository containing a python script and the end-of-line net.

## Usage

```bash
python3 genSupply.py
```

The script will ask for:
  * the number of suppliers, and
  * the upper bound of the manager net to be generated.

It generates several files:

* SupplierX.net: the .net file describing a supplier.
* Manager.net: the manager net managing all previously generated suppliers.
* BAZ.net: the factory net launching all supply orders.

For several managers, you need to manually add a token to the starting place in Manager.net. This can be done using a text editor or NetDrawner (ND) from the TINA toolbox.

The script also generates the file fuse.tpn, which describes step by step the synchronised product to be performed via TWINA.

The following command can be used to process the PTPN file with TWINA:

```bash
twina -aut fuse.tpn
```

The end-of-line net is already provided in this repository.

## Example configuration:

Suppliers = 3

Manager validation delay = 6 (for a [2,6] delay)
