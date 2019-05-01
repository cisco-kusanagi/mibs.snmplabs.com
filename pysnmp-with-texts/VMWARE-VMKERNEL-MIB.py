#
# PySNMP MIB module VMWARE-VMKERNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-VMKERNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, IpAddress, iso, ObjectIdentity, Unsigned32, Counter64, Bits, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "IpAddress", "iso", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwESX, = mibBuilder.importSymbols("VMWARE-PRODUCTS-MIB", "vmwESX")
esxVMKernel = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 1, 1))
vmkLoaded = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmkLoaded.setStatus('mandatory')
if mibBuilder.loadTexts: vmkLoaded.setDescription('Has the vmkernel been loaded? (yes/no)')
mibBuilder.exportSymbols("VMWARE-VMKERNEL-MIB", esxVMKernel=esxVMKernel, vmkLoaded=vmkLoaded)
