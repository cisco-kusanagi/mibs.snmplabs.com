#
# PySNMP MIB module VMWARE-VMKERNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-VMKERNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, ObjectIdentity, MibIdentifier, Counter64, Bits, Counter32, ModuleIdentity, IpAddress, Unsigned32, TimeTicks, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "ObjectIdentity", "MibIdentifier", "Counter64", "Bits", "Counter32", "ModuleIdentity", "IpAddress", "Unsigned32", "TimeTicks", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwESX, = mibBuilder.importSymbols("VMWARE-PRODUCTS-MIB", "vmwESX")
esxVMKernel = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 1, 1))
vmkLoaded = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmkLoaded.setStatus('mandatory')
mibBuilder.exportSymbols("VMWARE-VMKERNEL-MIB", esxVMKernel=esxVMKernel, vmkLoaded=vmkLoaded)
