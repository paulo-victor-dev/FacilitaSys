import createCrud from "./crudFactory";

const supplierApi = createCrud("supplier/");

export const listSupplier = supplierApi.list;
export const getSupplier = supplierApi.get;
export const createSupplier = supplierApi.create;
export const updateSupplier = supplierApi.update;
export const deleteSupplier = supplierApi.delete;